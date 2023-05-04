from flask import Flask, request, jsonify, send_from_directory
import vulnerability_detector
import os
import csv
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

app = Flask(__name__, static_url_path='', static_folder='./static/')

def perform_scan(url):
    try:
        response = requests.get(url, timeout=10)
        scan_results = f"URL: {url}\nStatus Code: {response.status_code}\nContent-Type: {response.headers.get('Content-Type', 'N/A')}"
    except requests.exceptions.RequestException as e:
        scan_results = f"An error occurred while scanning the URL:\n{str(e)}"
    return scan_results

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/submit_image', methods=['POST'])
def submit_image():
    image = request.form.get('image')
    vulnerability_detector.trivy_vs_osquery(image)
    with open('vulnerabilities.csv', 'r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
    return jsonify({'status': 'success', 'rows': rows})

@app.route('/get_vulnerabilities')
def get_vulnerabilities():
    if not os.path.exists('vulnerabilities.csv'):
        return jsonify({'status': 'not_ready'})
    vulnerabilities = []
    with open('vulnerabilities.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            vulnerabilities.append(row)

    df = pd.read_csv("vulnerabilities.csv")
    # Vulnerability Count by Severity
    severity_counts = df['Severity'].value_counts()
    severity_percentage = (severity_counts / severity_counts.sum()) * 100
    plt.figure(figsize=(8, 5))
    severity_percentage.plot(kind='bar')
    plt.xticks(range(len(severity_percentage.index)), severity_percentage.index, rotation=45)
    plt.xlabel('Severity')
    plt.ylabel('Percentage')
    plt.title('Vulnerability Percentage by Severity')
    for i, p in enumerate(severity_percentage):
       plt.text(i, p + 0.5, f'{p:.1f}%', ha='center')
    plt.savefig('static/png/1.png')

    # Top 10 Vulnerabilites Based on CVE-ID's
    vuln_counts = df['VulnerabilityID'].value_counts().head(10)
    plt.figure(figsize=(10, 5))
    vuln_counts.plot(kind='bar')
    plt.xlabel('VulnerabilityID')
    plt.ylabel('Count')
    plt.title('Top 10 Vulnerabilities')
    plt.savefig('static/png/2.png')

    # Convert date columns to datetime format
    df['PublishedDate'] = pd.to_datetime(df['PublishedDate'])
    df['LastModifiedDate'] = pd.to_datetime(df['LastModifiedDate'])
    vuln_count_by_year = df['PublishedDate'].groupby(df['PublishedDate'].dt.year).count()
    plt.figure(figsize=(10, 5))
    ax = vuln_count_by_year.plot(kind='bar')
    vuln_count_by_year.plot(kind='bar')
    plt.xlabel('Year')
    plt.ylabel('Vulnerability Count')
    plt.title('Vulnerability Count by Year')
    ax.set_xticklabels([int(year) for year in vuln_count_by_year.index], rotation=45)
    plt.savefig('static/png/3.png')

    # Top 10 Vulnerable Packages by Severity
    top_10_pkg = df['PkgName'].value_counts().head(10).index
    top_10_pkg_df = df[df['PkgName'].isin(top_10_pkg)]
    severity_by_pkg = top_10_pkg_df.groupby(['PkgName', 'Severity']).size().unstack(fill_value=0)
    severity_by_pkg.plot(kind='bar', stacked=True, figsize=(10, 5))
    plt.xlabel('Package Name')
    plt.ylabel('Vulnerability Count')
    plt.title('Top 10 Vulnerable Packages by Severity')
    plt.xticks(range(len(severity_by_pkg.index)), severity_by_pkg.index, rotation=45)
    plt.savefig('static/png/4.png')

    # Days to Fix Vulnerabilities
    df['VulnerableFrom'] = (df['LastModifiedDate'] - df['PublishedDate']).dt.days
    plt.figure(figsize=(10, 5))
    df['VulnerableFrom'].plot(kind='hist', bins=np.arange(0, df['VulnerableFrom'].max()+30, 30), edgecolor='black')
    plt.xlabel('Vulnerable From Days')
    plt.ylabel('Vulnerability Count')
    plt.title('Vulnerable From How Long')
    plt.savefig('static/png/5.png')

    # Pie Chart: Distribution of Vulnerabilities by Severity
    severity_counts = df['Severity'].value_counts()
    plt.figure(figsize=(8, 8))
    plt.pie(severity_counts, labels=severity_counts.index, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    plt.title('Distribution of Vulnerabilities by Severity')
    plt.savefig('static/png/7.png')

    df['PublishedDate'] = pd.to_datetime(df['PublishedDate'])
    # Group by month
    monthly_counts = df.resample('M', on='PublishedDate').count()['VulnerabilityID']
    # Line plot
    plt.figure(figsize=(10, 5))
    monthly_counts.plot(kind='line')
    plt.xlabel('Time (Monthly)')
    plt.ylabel('Number of Vulnerabilities')
    plt.title('Number of Vulnerabilities Published Over Time')
    plt.savefig('static/png/6.png')

    return jsonify({
        'status': 'ready',
        'vulnerabilities': vulnerabilities
    })
	

@app.route('/', methods=['GET', 'POST'])
def scan():
    scan_results = None
    if request.method == 'POST':
        url = request.form['url']
        scan_results = perform_scan(url)
    return render_template('scan.html', scan_results=scan_results)

if __name__ == '__main__':
    app.run(debug=True)

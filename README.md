<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="OnDemand_Docker_Image_Vulnerability_Scanning_0"></a>On-Demand Docker Image Vulnerability Scanning</h1>
<p class="has-line-data" data-line-start="1" data-line-end="2">This project provides a web-based interface for performing vulnerability scans on Docker images hosted on Docker Hub. The web application uses the Trivy vulnerability scanner to scan Docker images and displays the scan results on a web page.</p>
<h2 class="code-line" data-line-start=2 data-line-end=3 ><a id="Installation_2"></a>Installation</h2>
<p class="has-line-data" data-line-start="3" data-line-end="4">To run this web application on your local machine, follow these steps:</p>
<ul>
<li class="has-line-data" data-line-start="5" data-line-end="6">Clone this repository: git clone <a href="https://github.com/girikMET/web_application_development.git">https://github.com/girikMET/web_application_development.git</a></li>
<li class="has-line-data" data-line-start="6" data-line-end="9">Install the required dependencies:<br>
cd web_application_development<br>
pip install -r requirements.txt</li>
<li class="has-line-data" data-line-start="9" data-line-end="11">Start the web application:<br>
python3 <a href="http://app.py">app.py</a></li>
<li class="has-line-data" data-line-start="11" data-line-end="12">Open a web browser and go to <a href="http://localhost:5000">http://localhost:5000</a> to access the web application.</li>
</ul>
<h2 class="code-line" data-line-start=14 data-line-end=15 ><a id="Usage_14"></a>Usage</h2>
<p class="has-line-data" data-line-start="15" data-line-end="17">To scan a Docker image, enter the image name in the search box and click the “Scan” button. The web application will retrieve the image from Docker Hub, scan it for vulnerabilities using Trivy, and display the scan results on the page.<br>
You can also view the results of past scans by clicking the “Demo Results” button on the navigation bar. This will display a page with pre-loaded scan results for a set of Docker images.</p>
<h1 class="code-line" data-line-start=18 data-line-end=19 ><a id="Contributing_18"></a>Contributing</h1>
<p class="has-line-data" data-line-start="19" data-line-end="20">If you find a bug or have a feature request, please open an issue on the GitHub repository. Pull requests are also welcome.</p>
class Logger {
  constructor(prefix) {
    this.prefix = prefix;
  }

  log(message) {
    console.log(`[${this.prefix}] ${message}`);
  }
}

const logger = new Logger("main.js");

$.ajax({
  url: '/vulnerabilities',
  method: 'GET',
  dataType: 'json',
  success: function(data) {
    const rows = data.rows;
    let table = '<table class="table"><thead><tr>';
    Object.keys(rows[0]).forEach(function(key) {
      table += '<th scope="col">' + key + '</th>';
    });
    table += '</tr></thead><tbody>';
    rows.forEach(function(row) {
      table += '<tr>';
      Object.values(row).forEach(function(value) {
        table += '<td>' + value + '</td>';
      });
      table += '</tr>';
    });
    table += '</tbody></table>';
    $('#table-div').html(table);
    $('#vulnerabilities-table').show();
    $('#loading').hide();
    $('#image').val('');
    $('body, html').animate({
      scrollTop: $('#vulnerabilities-table').offset().top
    }, 800);
  },
  error: function(xhr, status, error) {
    console.error('Error fetching vulnerabilities:', error);
  }
});

$("button").on("click", function () {
  logger.log("Button clicked");
});

$("input").on("focus", function () {
  logger.log("Input focused");
});

$(window).on("resize", function () {
  logger.log("Window resized");
});

$("form").on("submit", function (e) {
  e.preventDefault();
  logger.log("Form submitted");
});

$(document).on("keydown", function (e) {
  logger.log(`Key ${e.key} pressed`);
});

$("select").on("change", function () {
  logger.log("Select option changed");
});

$("a").on("click", function (e) {
  e.preventDefault();
  logger.log("Link clicked");
});

$("img").on("load", function () {
  logger.log("Image loaded");
});

$("table").on("mouseover", "td", function () {
  logger.log("Mouseover on table cell");
});

$("table").on("mouseleave", "td", function () {
  logger.log("Mouseleave from table cell");
});

$("div").on("mouseenter", function () {
  logger.log("Mouseenter on div");
});

$("div").on("mouseleave", function () {
  logger.log("Mouseleave from div");
});

$("p").on("dblclick", function () {
  logger.log("Paragraph double-clicked");
});

$("button").on("contextmenu", function (e) {
  e.preventDefault();
  logger.log("Right-click on button");
});

$("input").on("keyup", function () {
  logger.log("Input key released");
});

$("input").on("paste", function () {
  logger.log("Text pasted into input");
});

$("textarea").on("input", function () {
  logger.log("Text entered into textarea");
});

$("form").on("reset", function () {
  logger.log("Form reset");
});

function fetchData() {
  $.ajax({
    url: "https://jsonplaceholder.typicode.com/todos/1",
    success: function (data) {
      logger.log("Data fetched successfully");
      $("#data-container").html(`<p>${data.title}</p>`);
    },
  });
}

export { fetchData };

const showAlert = function(message) {
  alert(message);
};

function capitalizeString(string) {
  return string.charAt(0).toUpperCase() + string.slice(1);
}

$('#my-button').on('click', function() {
  console.log('Button clicked!');
});

const multiply = (a, b) => a * b;
console.log(capitalizeString('Reloading the page'));
console.log(multiply(2, 3));


function fetchVulnerabilities() {
  $.ajax({
    url: '/vulnerabilities',
    method: 'GET',
    dataType: 'json',
    success: function(data) {
      console.log('Vulnerabilities:', data);
    },
    error: function(xhr, status, error) {
      console.error('Error fetching vulnerabilities:', error);
    }
  });
}

function fetchUserProfile() {
  $.ajax({
    url: '/profile',
    method: 'GET',
    dataType: 'json',
    success: function(data) {
      console.log('User profile:', data);
    },
    error: function(xhr, status, error) {
      console.error('Error fetching user profile:', error);
    }
  });
}

function submitNewUser() {
  const formData = {
    name: $('#name').val(),
    email: $('#email').val(),
    password: $('#password').val()
  };

  $.ajax({
    url: '/users',
    method: 'POST',
    dataType: 'json',
    data: formData,
    success: function(data) {
      console.log('New user created:', data);
    },
    error: function(xhr, status, error) {
      console.error('Error creating new user:', error);
    }
  });
}

function startTask() {
  $.ajax({
    url: '/task',
    method: 'POST',
    dataType: 'json',
    success: function(data) {
      console.log('Task started:', data);
    },
    error: function(xhr, status, error) {
      console.error('Error starting task:', error);
    }
  });
}

document.getElementById('on-demand-scan-btn').addEventListener('click', () => {
  window.location.href = 'scan.html';
});

document.getElementById('about').addEventListener('click', () => {
  window.location.href = 'index.html';
});

document.getElementById('demo').addEventListener('click', () => {
  window.location.href = 'demo.html';
});

//fetchVulnerabilities();
//fetchUserProfile();
//submitNewUser();
//startTask();

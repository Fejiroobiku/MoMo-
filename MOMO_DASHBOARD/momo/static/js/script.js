// toggle icon navbar

let menuIcon = document.querySelector("#menu-icon");
let navbar = document.querySelector(".navbar");

menuIcon.onclick = () => {
  menuIcon.classList.toggle("bx-x");
  navbar.classList.toggle("active");
};

//scroll sections
let sections = document.querySelectorAll("section");
let navLinks = document.querySelectorAll("header nav a");

window.onscroll = () => {
  sections.forEach((sec) => {
    let top = window.scrollY;
    let offset = sec.offsetTop - 100;
    let height = sec.offsetHeight;
    let id = sec.getAttribute("id");

    if (top >= offset && top < offset + height) {
      navLinks.forEach((links) => {
        links.classList.remove("active");
        document
          .querySelector("header nav a[href*=" + id + "]")
          .classList.add("active");
      });
      // active section for animation on scroll
      sec.classList.add("show-animate");
    }
  });
  // sticky header
  let header = document.querySelector("header");

  header.classList.toggle("sticky", window.scrollY > 100);

  /* remove toggle icon and navbar when click navbar links*/
  menuIcon.classList.remove("bx-x");
  navbar.classList.remove("active");

  /*animation footer on scroll*/
  let footer = document.querySelector("footer");

  footer.classList.toggle(
    "show-animate",
    this.innerHeight + this.scrollY >=
      document.scrollingElement.scrollHeight - 5
  );
};

// chart.js
document.addEventListener('DOMContentLoaded', function() {
  // Adding chart js
  const script = document.createElement('script');
  script.src = 'https://cdn.jsdelivr.net/npm/chart.js';
  document.head.appendChild(script);

  script.onload = function() {
      // defaulting Chart.js colors to match app theme
      Chart.defaults.color = '#ffffff';
      Chart.defaults.borderColor = '#FFCC08';

      // Fetch transaction data
      fetch('http://127.0.0.1:8000/momo/api/transaction-data/')
          .then(response => response.json())
          .then(data => {
              // Transaction Volume Chart
              new Chart(document.getElementById('transactionVolumeChart'), {
                  type: 'bar',
                  data: {
                      labels: Object.keys(data.transaction_volumes),
                      datasets: [{
                          label: 'Transaction Volume',
                          data: Object.values(data.transaction_volumes),
                          backgroundColor: 'rgba(255, 204, 8, 0.5)',
                          borderColor: '#FFCC08',
                          borderWidth: 1
                      }]
                  },
                  options: {
                      responsive: true,
                      maintainAspectRatio: false,
                      plugins: {
                          legend: {
                              position: 'top',
                          }
                      },
                      scales: {
                          y: {
                              beginAtZero: true,
                              grid: {
                                  color: 'rgba(255, 255, 255, 0.1)'
                              }
                          },
                          x: {
                              grid: {
                                  display: false
                              }
                          }
                      }
                  }
              });

              // Monthly Trends Chart
              new Chart(document.getElementById('monthlyTrendsChart'), {
                  type: 'line',
                  data: {
                      labels: Object.keys(data.monthly_data),
                      datasets: [{
                          label: 'Monthly Transactions',
                          data: Object.values(data.monthly_data),
                          borderColor: '#FFCC08',
                          tension: 0.4,
                          fill: true,
                          backgroundColor: 'rgba(255, 204, 8, 0.1)'
                      }]
                  },
                  options: {
                      responsive: true,
                      maintainAspectRatio: false,
                      plugins: {
                          legend: {
                              position: 'top',
                          }
                      },
                      scales: {
                          y: {
                              beginAtZero: true,
                              grid: {
                                  color: 'rgba(255, 255, 255, 0.1)'
                              }
                          }
                      }
                  }
              });

              // Service Provider Distribution Chart
              new Chart(document.getElementById('providerDistributionChart'), {
                  type: 'doughnut',
                  data: {
                      labels: Object.keys(data.provider_data),
                      datasets: [{
                          data: Object.values(data.provider_data),
                          backgroundColor: [
                              'rgba(255, 204, 8, 0.8)',
                              'rgba(255, 159, 64, 0.8)',
                              'rgba(255, 99, 132, 0.8)',
                              'rgba(75, 192, 192, 0.8)',
                              'rgba(54, 162, 235, 0.8)'
                          ]
                      }]
                  },
                  options: {
                      responsive: true,
                      maintainAspectRatio: false,
                      plugins: {
                          legend: {
                              position: 'top',
                          }
                      }
                  }
              });
          });
  };
});
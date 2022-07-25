
const ctx = document.getElementById('myChart1').getContext('2d');
const myChart1 = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Total Subscriptions', 'Active Subscription'],
        datasets: [{
            label: 'Subscriptions',
            data: [12, 19],

            backgroundColor: [
                '#ff4444',
                '#00C851',
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(23, 255, 23, 0.2)',
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

const ctx2 = document.getElementById('myChart2').getContext('2d');
const myChart2 = new Chart(ctx2, {
    type: 'doughnut',
    data: {

        labels: ['Prop Firm Accounts', 'Active Subscription'],
        datasets: [{
            label: 'Plans',
            data: [12, 19],

            backgroundColor: [
                '#ff4444',
                '#00C851',
               
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(23, 255, 23, 0.2)',
               
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

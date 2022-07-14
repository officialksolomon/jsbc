const closeAlerts = () => {
    const alerts = document.querySelectorAll(".alert");
    setTimeout(() => {
        alerts.forEach((alert) => {
            alert.classList.add('d-none');
        });
    }, 5000);
};
document.addEventListener('DOMContentLoaded', closeAlerts);
const closeAlerts = () => {
    const alerts = document.querySelectorAll(".alert");
    setTimeout(() => {
        alerts.forEach((alert) => {
            alert.classList.add('d-none');
        });
    }, 5000);
};
document.addEventListener('DOMContentLoaded', closeAlerts);

const closeLoader = () => {
    const loaderWrapper = document.querySelector('.loader-wrapper');
    window.addEventListener('load', () => {
        loaderWrapper.classList.add('d-none');

    });
};

closeLoader();

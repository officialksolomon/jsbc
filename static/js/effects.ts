const serviceElements = document.querySelectorAll('.service-col')
console.log(serviceElements);
const serviceElementsIcons = document.querySelectorAll('.service-col > i')
console.log(serviceElements);

serviceElements.forEach(element => element.addEventListener('mouseenter', () => {
    element.classList.toggle(' animate__animated animate__fadeIn');

}))
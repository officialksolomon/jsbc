// Dom elements 
const serviceElements = document.querySelectorAll('.service-col')
const serviceElementsIcons = document.querySelectorAll('.service-col > i')

// Eventlisteners
serviceElements.forEach(element => element.addEventListener('mouseenter', () => {
    element.classList.toggle('animate__fadeIn');

}))
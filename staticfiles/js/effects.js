"use strict";
const serviceElements = document.querySelectorAll('.service-col');
console.log(serviceElements);
const serviceElementsIcons = document.querySelectorAll('.service-col > i');
console.log(serviceElements);

serviceElements.forEach(element => element.addEventListener('mouseover', (event) => {
    element.classList.toggle('animate__fadeIn');

}));
"use strict";
const serviceElements = document.querySelectorAll('.service-col');
const serviceElementsIcons = document.querySelectorAll('.service-col > i');

serviceElements.forEach(element => element.addEventListener('mouseover', (event) => {
    element.classList.toggle('animate__fadeIn');

}));
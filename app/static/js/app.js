const elem = document.querySelector('#testing');
console.log(elem);
// elem.class('z-index', 1000);

let container = document.querySelector(".container");
let lastScrollY = window.scrollY;


window.addEventListener("scroll", () => {
    if (window.scrollY > 100) {
        elem.classList.add('z1000')

        console.log("we are going down", lastScrollY);
    } else {
        elem.classList.remove('z1000')
        console.log("we are going up", lastScrollY)
    }
})
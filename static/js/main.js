const loader = document.querySelector('.loader')
document.addEventListener('DOMContentLoaded',()=>{
loader.style.display = 'none'
const rootElement = document.documentElement
const scrollUp = document.querySelector('.back-to-top')
scrollUp.addEventListener('click', ()=>{
    rootElement.scrollTo({
        top: 0,
        behavior: "smooth",
    })

// var theme = localStorage.getItem('theme')
// const light = document.getElementById('themeLight')
// const dark = document.getElementById('themeDark')
// light.addEventListener('click',(e)=>{
//     e.preventDefault()
//     document.body.classList.add('light')
//     dark.classList.remove('d-none')
//     light.classList.add('d-none')
//     localStorage.setItem('theme','light')
// })
// dark.addEventListener('click',(e)=>{
//     e.preventDefault()
//     document.body.classList.remove('light')
//     light.classList.remove('d-none')
//     dark.classList.add('d-none')
//     localStorage.setItem('theme','dark')
// })
// if (theme==='light'){
//         document.body.classList.add('light')
//         dark.classList.remove('d-none')
//         light.classList.add('d-none')
// }
// else if(theme==='dark'){
//         document.body.classList.remove('light')
//         light.classList.remove('d-none')
//         dark.classList.add('d-none')
// }
const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))
})
 // navbar style change based on scroll position
const navbar = document.querySelector('.navbar')
let isMobile = window.matchMedia("only screen and (max-width: 760px)").matches;
if (!isMobile){
window.addEventListener('scroll',()=>{
    if (document.body.scrollTop > 200 || document.documentElement.scrollTop > 200 ){
        navbar.classList.add('nav-sticky')
        scrollUp.style.display = 'block'
    }
    else  {
        scrollUp.style.display = 'none'
        navbar.classList.remove('nav-sticky')
    }
    if (document.body.scrollTop > 0 || document.documentElement.scrollTop > 0 ){
        navbar.classList.add('nav-sticky')
    }
    else  {
        navbar.classList.remove('nav-sticky')
    }
})
    }
})
//close navbar on outside click
window.onload = function () {
    document.addEventListener("click", function (event) {
        // if the clicked element isn't child of the navbar, you must close it if is open
        if (!event.target.closest("#navbarCollapse") && document.getElementById("navbarCollapse").classList.contains("show")) {
            document.getElementById("navbar-toggler-icon").click();
        }
    });
}
var w = window.innerWidth || document.documentElement.clientWidth|| document.body.clientWidth;
if ( w> 992){
const hoverAble = document.getElementsByClassName('dropdown-toggle')
    for(let i=0;i < hoverAble.length; i++ ){
        hoverAble[i].addEventListener('mouseover',(e)=>{
            if(!hoverAble[i].classList.contains('show')){
            e.target.click()
                }
        })
    }
// The mouseout event triggers when the mouse pointer leaves any child elements as well the selected element.
// The mouseleave event is only triggered when the mouse pointer leaves the selected element.
const btnGroup = document.getElementsByClassName('btn-group')
    for(let i=0; i <btnGroup.length; i++){
        btnGroup[i].addEventListener('mouseleave',()=>{
            btnGroup[i].firstElementChild.click()
        })
    }
}
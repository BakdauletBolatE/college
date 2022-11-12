window.addEventListener('scroll', (e)=>{
    const header = document.querySelector('.header');
    const body = document.querySelector('body');

    const scrollY = window.scrollY;
    if (scrollY > 47) {
        header.classList.add('header--fixed');
        body.classList.add('body--fixed');
    }
    else{
        header.classList.remove('header--fixed');
        body.classList.remove('body--fixed');
    }
})

const mainSlider = new Swiper('.main-slider__container', {
    speed: 400,
    direction: 'horizontal',
    loop: true,
  });

const shortSlider = new Swiper('.short-slider__container', {
    speed: 400,
    slidesPerView: 4,
    spaceBetween: 10,
    direction: 'vertical',
    loop: true,
})

const burger_mobile = document.getElementById('burger-mobile');
const burger_mobile_exit = document.getElementById('burger-mobile-exit');
const navbar__list = document.querySelector('.navbar__list');

burger_mobile.addEventListener('click', ()=>{
    navbar__list.classList.add('navbar__list--active');
});

burger_mobile_exit.addEventListener('click', ()=>{
    navbar__list.classList.remove('navbar__list--active');
});

const datapluses = document.querySelectorAll('[data-plus]');


datapluses.forEach(elem=>{
    elem.addEventListener('click', ()=>{
        const dataName = elem.getAttribute('data-plus');

        const navbar = document.querySelector(`[data-toggle="${dataName}"]`);
        if (navbar) {
            elem.classList.toggle('navbar__plus--active');
            navbar.classList.toggle('sub-navbar__list--active');
        }
    })
})
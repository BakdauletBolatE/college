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
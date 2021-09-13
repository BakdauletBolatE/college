window.addEventListener('scroll', (e)=>{
    const header = document.querySelector('.header');
    const mainSlider = document.querySelector('.main-slider');

    const scrollY = window.scrollY;
    if (scrollY > 47) {
        header.classList.add('header--fixed');
        mainSlider.classList.add('main-slider--fixed');
    }
    else{
        header.classList.remove('header--fixed');
        mainSlider.classList.remove('main-slider--fixed');
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
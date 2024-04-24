const siteHeader = document.getElementById('header');
const siteHeaderHeight = siteHeader.offsetHeight;

window.addEventListener('scroll', () => {
    const top = document.documentElement.scrollTop || document.body.scrollTop;
    if(top > siteHeaderHeight) {
        siteHeader.classList.add('sticky-header');
    } else {
        siteHeader.classList.remove('sticky-header');
    }
}, false);
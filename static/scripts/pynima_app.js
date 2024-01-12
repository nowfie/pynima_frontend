const navbar = document.querySelector('#navmain');
window.addEventListener('scroll', () => {
    const scrollPosition = window.scrollY;
    if (scrollPosition > 0) {
        navbar.style.backgroundColor = 'var(--bg-color-secondary)';
        navbar.style.boxShadow = 'rgba(100, 100, 111, 0.2) 0px 7px 29px 0px';
    } else {
        navbar.style.backgroundColor = '#fff';
        navbar.style.boxShadow = 'none';
    }
});
function toggleMenu(){
    const menu = document.querySelector('.menu-item');
    const icon = document.querySelector('.hamburger-icon');

    menu.classList.toggle('open');
    icon.classList.toggle('open');
    console.log("hello");
}

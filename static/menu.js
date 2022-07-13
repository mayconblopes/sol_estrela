const botaoMenu = document.getElementById('ham-menu');
const menu = document.querySelector('.menu-lateral');

botaoMenu.addEventListener('click', () => {
    menu.classList.toggle('menu-lateral--ativo');
})

window.addEventListener('mouseup', function(event){
    const menu = document.querySelector('.menu-lateral--ativo');
    if (event.target != menu && event.target.parentNode != menu){
        menu.classList.toggle('menu-lateral--ativo');
    }
});
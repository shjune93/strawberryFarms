const toggleBtn=document.querySelector('.navbar__toogleBtn');//토글 버튼 연결
const menu=document.querySelector('.navbar__menu');
const icons=document.querySelector('.navbar__icons');


toggleBtn.addEventListener('click',()=>{
    menu.classList.toggle('active');
    icons.classList.toggle('active');
});
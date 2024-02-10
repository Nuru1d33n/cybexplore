window.addEventListener('load', () => {
    document.querySelector('.p_content').innerText = document.querySelector('.p_content').innerHTML.substring(0, 150)+"...";
});


let lightMode = localStorage.getItem('lightMode');
const switchModeElements = document.getElementsByClassName('switch-mode');

function enableLightMode(){
    document.documentElement.classList.add('lightMode');
    localStorage.setItem('lightMode', 'active');
}

function disableLightMode(){
    document.documentElement.classList.remove('lightMode');
    localStorage.setItem('lightMode', null);
}

//loop for each switchModeClass
for (let i = 0; i < switchModeElements.length; i++) {
    switchModeElements[i].addEventListener('click', () => {
        lightMode = localStorage.getItem('lightMode');
        if (lightMode !== "active") {
            enableLightMode();
        } else {
            disableLightMode();
        }
    });
}

//dark and light mode
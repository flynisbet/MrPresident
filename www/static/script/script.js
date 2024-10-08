function toggleMenu(){
    const menu = document.querySelector('.menu-item');
    const icon = document.querySelector('.hamburger-icon');

    menu.classList.toggle('open');
    icon.classList.toggle('open');
}

let jsonData = null;
async function getData() {
    const url = "http://127.0.0.1:5000/pres";
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
        }
        jsonData = await response.json();
    } catch (error) {
        console.error(error.message);
    }
}

function placeInfo(){
    // Get the timeline containers class to add containers to once we create them
    let conts = document.querySelector('.timeline-containers');

    for (pres in jsonData){
        // Get president info
        let presInfo = jsonData[pres];

        // Create container to add all the stuff to
        let cont = document.createElement('div');
        cont.classList = 'timeline-container';

        // Add name since it isn't in the textbox
        // Create text node, create element, append
        let presNum = document.createTextNode(presInfo['No']);
        let num = document.createElement('div');
        num.classList = 'timeline-rank';
        num.appendChild(presNum);
        cont.appendChild(num);

        // picture, desc, years, name all in textbox
        let box = document.createElement('div');
        box.classList = 'textbox';

        //pic
        let picture = document.createElement('img');
        picture.src = presInfo['IMG filepath'];
        box.appendChild(picture);
    
        //name
        let presName = document.createTextNode(presInfo['Name']);
        let name = document.createElement('h3');
        name.className = 'title';
        name.appendChild(presName);
        box.appendChild(name);

        //years
        let presYears = document.createTextNode(presInfo['Term Years']);
        let years = document.createElement('p');
        years.className = 'serving-years';
        years.appendChild(presYears);
        box.appendChild(years);

        //description
        let presDescription = document.createTextNode(presInfo['Description']);
        let description = document.createElement('p');
        description.appendChild(presDescription);
        box.appendChild(description);

        // Add textbox to container, add container to list of containers
        cont.appendChild(box);
        conts.appendChild(cont);
    }
}

window.addEventListener('DOMContentLoaded', getData);
window.addEventListener('DOMContentLoaded', placeInfo);
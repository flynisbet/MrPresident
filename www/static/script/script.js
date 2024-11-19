function toggleMenu(){
    const menu = document.querySelector('.hamburger-menu'); 
    const icon = document.querySelector('.hamburger-icon');

    menu.classList.toggle('open');
    icon.classList.toggle('open');
}

async function getData() {
    const url = "http://127.0.0.1:81/pres";
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
        }
        jsonData = await response.json();
        placeInfo()
    } catch (error) {
        console.error(error.message);
    }
}

let presidents = []; 
function placeInfo(){
    // Get the timeline containers class to add containers to once we create them
    let conts = document.querySelector('.timeline-containers');
    const keys = Object.keys(jsonData).map(Number);

    for (let i = keys.length; i > 0; i--) {
        // Get president info
        let presInfo = jsonData[i];

        // Create container to add all the stuff to
        let cont = document.createElement('div');
        cont.classList = 'timeline-container';

        //add identifying ID to each div 
        cont.id = `president-${presInfo['No']}`;

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

       // console.log(presInfo['Name'])
       presidents.push(presInfo['Name'])
       let name = document.createElement('h3');
       let presName = document.createTextNode(presInfo['Name']);
       name.className = 'title';
       name.appendChild(presName);
       let name_link = document.createElement('a');
       name_link.appendChild(name);
       name_link.href = `/president/${presInfo['No']}`;
       box.appendChild(name_link);

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


// searchBar powered by : sheCodes
//link : https://www.shecodes.io/athena/38555-how-to-create-a-search-bar-using-html-css-json-and-javascript#:~:text=%22:%22F.-,Scott%20Fitzgerald%22%2C%22year%22:%221925%22%7D,types%20in%20the%20search%20input.

// SearchBar: Get input element and results list
let search = document.getElementById('search');
let results = document.getElementById('results');

search.addEventListener('keyup', function(event){

     // Clear results list
    results.innerHTML = '';

    let searchTerm = event.target.value.toLowerCase();

    presidents.forEach(function(name){
        if(name.toLowerCase().indexOf(searchTerm) > -1){
            let item = document.createElement('li');
            item.innerHTML = name;

            // onclick if user click on the result
            item.onclick = function() {
                scrollToPresident(name); 
            };

            results.appendChild(item);
        }
    })
});

function scrollToPresident(name) {
    console.log(`Searching for president: ${name}`);
  
    // Finding the president 
    let foundPresident = Object.values(jsonData).find(pres => 
        pres['Name'].toLowerCase().trim() === name.toLowerCase().trim()
    );
    
    if (foundPresident) {
        console.log(`Found president: ${foundPresident['Name']} with id president-${foundPresident['No']}`);
        let element = document.getElementById(`president-${foundPresident['No']}`);
        
        if (element) {
            console.log(`Scrolling to president: ${foundPresident['Name']}`);
            element.scrollIntoView({ behavior: 'smooth' });
        } else {
            console.log(`Element with id president-${foundPresident['No']} not found.`);
        }
    } else {
        console.log('President not found.');
    }
}

// Function to toggle the theme, needs work to apply to all pages and save state
function toggleTheme() {
    let light = document.getElementById('theme-toggle');
    if (light.checked) {
        document.querySelectorAll("*").forEach(element => {
            element.classList.add("light-mode");
        });
    } 
    else {
        document.querySelectorAll("*").forEach(element => {
            element.classList.remove("light-mode");
        });
    }
}


// link resource: https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollIntoView
//MDN: 
function scrollUp(){
    window.scrollTo({
        top: 0,           // Scroll to the top of the page
        behavior: 'smooth' // Optional: Use 'smooth' for smooth scrolling
    });
}

// window.onload = function() {
//     document.querySelector('#first-section').scrollIntoView({
//         behavior: 'smooth', // Optional: Smooth scrolling
//         block: 'start'      // Aligns the element to the top of the viewport
//     });
// };
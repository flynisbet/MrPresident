let jsonData3; 

async function getData2() {
    const url = "./static/json/mrPresident.json";
    try {
        if (jsonData3) {
            console.log("Data already fetched, skipping fetch.");
            return; 
        }

        console.log("Fetching data from:", url);
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
        }
        jsonData3 = await response.json();
        getpicture2();
    } catch (error) {
        console.error("Error fetching data:", error.message);
    }
}

function getRandomInt(min, max) {
    min = Math.ceil(min);   
    max = Math.floor(max); 
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function getFirstAndLastName(fullName) {
    if (!fullName.trim()) {
        return { firstName: "", lastName: "" }; 
    }

    const nameParts = fullName.trim().split(/\s+/);
    const firstName = nameParts[0];
    const lastName = nameParts[nameParts.length - 1];

    return { firstName, lastName };
}

let store = []; 
function getpicture2() {
    let conts = document.querySelector('.mypresident');
    console.log("getpicture2 called");
    const keys = Object.keys(jsonData3).map(Number);
    const easy = 5;

    for (let i = 0; i < easy; i++) {
        let generated;
        do {
            generated = getRandomInt(0, keys.length - 1);
        } while (store.includes(generated));
        store.push(generated);
    }

    console.log("Generated store array:", store);

    for (let i = 0; i < easy; i++) {
        let info = jsonData3[store[i]];
        if (!info) {
            console.error(`Invalid index: ${store[i]} in jsonData3`);
            continue;
        }

        let box = document.createElement('div');
        box.classList = 'presidentpic';

        // pic
        let picture = document.createElement('img');
        picture.classList.add(`pic-${store[i]}`);
        picture.src = info['IMG filepath'];
        console.log(info['IMG filepath']);
        box.appendChild(picture);
        conts.appendChild(box);
    }
}

let inputBox = document.getElementById('input-box');
let score = 0; 

inputBox.addEventListener("keydown", function(event) {
    if (event.key === 'Enter') {
        const enterValue = inputBox.value.trim();
        console.log("User pressed Enter", enterValue);

        for (let i = 0; i < store.length; i++) {
            let mydata = jsonData3[store[i]];
            if (!mydata) continue;

            console.log(mydata['Name']);
            const { firstName, lastName } = getFirstAndLastName(mydata['Name']);

            if (
                mydata['Name'].toLowerCase() === enterValue.toLowerCase() ||
                firstName.toLowerCase() === enterValue.toLowerCase() ||
                lastName.toLowerCase() === enterValue.toLowerCase()
            ) {
                let mypic = document.getElementsByClassName(`pic-${store[i]}`);
                for (let element of mypic) {
                    element.style.setProperty('border', '15px solid green', 'important');
                    console.log(element);
                }
                score++; 
                console.log(score);
            }
        }

        inputBox.value = "";
    }
});

getData2();

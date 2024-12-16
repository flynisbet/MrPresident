let jsonData3; // Ensure jsonData3 is declared globally once

async function getData2() {
    const url = "./static/json/mrPresidentQuiz.json";
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

let store = []; 
function getpicture2() {
    let conts = document.querySelector('.mypresident');
    
    console.log("getpicture2 called");
    const keys = Object.keys(jsonData3).map(Number);

    const easy = 5;


    for (let i = 0; i < easy; i++)
    {
        let generated = getRandomInt(1,keys.length)
        store.push(generated);
    }
  
    console.log("Generated store array:", store);

    for (let i =0; i < easy; i++){
        let info = jsonData3[store[i]]
        console.log(store[i]);
        let box = document.createElement('div');
        box.classList = 'presidentpic';

        //pic
        let picture = document.createElement('img');
        picture.classList.add(store[i]);
        picture.src = info['IMG filepath'];
        console.log(info['IMG filepath'])
        box.appendChild(picture);
        conts.appendChild(box);
    }

   
}

let inputBox = document.getElementById('input-box');

let score = 0; 
inputBox.addEventListener("keydown", function(event){
    if(event.key === 'Enter'){
        const enterValue = inputBox.value; 
        console.log("User press Enter", enterValue);
        for (let i = 0; i < store.length; i++) {
            mydata = jsonData3[store[i]];
            console.log(mydata['Name'])
            if(mydata['Name'] === enterValue){
                let mypic = document.getElementsByClassName(store[i]);
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
})





getData2();
//game 1d

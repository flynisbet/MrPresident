const questions = [
    {
        question: "Who is the first president of the America?", 
        answers: [
            { text: "Obama" , correct : false}, 
            { text: "Geogrge Wahsinton" , correct : true}, 
            { text: "Trump" , correct : false}, 
            { text: "Biden" , correct : false}, 
        ]
    }, 
    {
        question: "Who is the Last president of the America?", 
        answers: [
            { text: "Obama" , correct : false}, 
            { text: "Geogrge Wahsinton" , correct : false}, 
            { text: "Trump" , correct : false}, 
            { text: "Biden" , correct : true}, 
        ]
    }, 
    {
        question: "Where is Furman University?", 
        answers: [
            { text: "SC" , correct : true}, 
            { text: "NC" , correct : false}, 
            { text: "Geogrgia" , correct : false}, 
            { text: "NY" , correct : false}, 
        ]
    }, 
]; 

const questionElement = document.getElementById("question"); 
const answerButton = document.getElementById("answer-buttons"); 
const nextButton = document.getElementById("next-btn"); 

let currentQuestionIndex = 0; 
let score = 0; 

function startQuiz(){
    currentQuestionIndex =0; 
    socre = 0; 
    nextButton.innerHTML = "Next"; 
    showQuestion(); 
}

function showQuestion(){
    while(answerButton.firstChild){
        answerButton.removeChild(answerButton.firstChild)
    }
    nextButton.style.display = "none";
    let questionNo = currentQuestionIndex + 1; 
    let currentQuestion = questions[currentQuestionIndex]; 
    
    questionElement.innerHTML = questionNo + ". " + currentQuestion.question; 
    
    currentQuestion.answers.forEach(answer =>{
        const button = document.createElement("button");
        button.innerHTML = answer.text;
        button.classList.add("btn");
        answerButton.appendChild(button); 

        button.addEventListener("click",()=> selectAnswer(button, answer.correct));
    })
}

function selectAnswer(button, isCorrect){
       // Disable all buttons after one selection
       Array.from(answerButton.children).forEach(btn => {
        btn.disabled = true;               // Disable the button
        btn.style.pointerEvents = "none";  // Additional style to prevent further clicks
    });

    if (isCorrect){
        score = score +1; 
        button.style.backgroundColor = "green";
    }
    else{
        button.style.backgroundColor = "red";
    }
       // Highlight the correct answer in green
       Array.from(answerButton.children).forEach(btn => {
        if (btn.textContent === questions[currentQuestionIndex].answers.find(answer => answer.correct).text) {
            btn.style.backgroundColor = "green";
        }
    });

    nextButton.style.display = "block";
    nextButton.onclick = function(){
        if(currentQuestionIndex < questions.length){
            handlenextButton()
        }else{
        startQuiz();
        }
       
    }
}

function handlenextButton(){
    currentQuestionIndex++;
    if(currentQuestionIndex < questions.length){
        showQuestion()
    }else{
        showScore();
    }
}

function showScore(){
    while(answerButton.firstChild){
        answerButton.removeChild(answerButton.firstChild)
    }
    questionElement.innerHTML = `Your Score is ${score} out of ${questions.length}`;
}

window.onload = function() {
    startQuiz();
};
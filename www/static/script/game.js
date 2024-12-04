async function getQuestion() {
    const url = "http://127.0.0.1/preQuiz";
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
        }
        questions = await response.json();
    } catch (error) {
        console.error(error.message);
    }
    return questions;
}

const questionElement = document.getElementById("question"); 
const answerButton = document.getElementById("answer-buttons"); 
const nextButton = document.getElementById("next-btn"); 

let currentQuestionIndex = 0; 
let score = 0; 

function startQuiz(){
    nextButton.innerHTML = "Next"; 
    showQuestion(); 
}

async function showQuestion(){
    let questions = getQuestion();
    const currentQuestionIndex = 0; 
    let score = 0; 

    console.log(questions);
    while(answerButton.firstChild){
        answerButton.removeChild(answerButton.firstChild)
    }
    nextButton.style.display = "none";
    let questionNo = currentQuestionIndex + 1; 
    console.log("hello");
    console.log(questions[currentQuestionIndex]);
    console.log("end");
    let currentQuestion = questions[currentQuestionIndex]; 
    console.log(currentQuestion);
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
        nextButton.innerHTML = "Play Again"; 
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

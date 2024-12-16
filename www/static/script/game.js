let questions = [];
let currentQuestionIndex = 0; 
let score = 0;

async function getQuestion() {
    const url = "./static/json/mrPresidentQuiz.json";
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
        }

        questions = await response.json(); 
        console.log(questions);
    
        startQuiz(); 
        
    } catch (error) {
        console.error(error.message);
    }
}

const questionElement = document.getElementById("question"); 
const answerButton = document.getElementById("answer-buttons"); 
const nextButton = document.getElementById("next-btn"); 

function startQuiz() {
    currentQuestionIndex = 0; 
    score = 0; 
    nextButton.innerHTML = "Next"; 
    showQuestion(); 
}

async function showQuestion() {
    if (currentQuestionIndex >= questions.length) {
        showScore();
        return;
    }

    while(answerButton.firstChild) {
        answerButton.removeChild(answerButton.firstChild);
    }
    nextButton.style.display = "none";

    let questionNo = currentQuestionIndex + 1;
    let currentQuestion = questions[currentQuestionIndex]; 

    questionElement.innerHTML = `${questionNo}. ${currentQuestion.question}`; 
    
    currentQuestion.answers.forEach(answer => {
        const button = document.createElement("button");
        button.innerHTML = answer.text;
        button.classList.add("btn");
        answerButton.appendChild(button); 

        button.addEventListener("click", () => selectAnswer(button, answer.correct));
    });
}

function selectAnswer(button, isCorrect) {
    // Disable all buttons after one selection
    Array.from(answerButton.children).forEach(btn => {
        btn.disabled = true;
        btn.style.pointerEvents = "none";
    });

    if (isCorrect) {
        score += 1; 
        button.style.backgroundColor = "green";
    } else {
        button.style.backgroundColor = "red";
    }

   
    Array.from(answerButton.children).forEach(btn => {
        if (btn.textContent === questions[currentQuestionIndex].answers.find(answer => answer.correct).text) {
            btn.style.backgroundColor = "green";
        }
    });

    nextButton.style.display = "block";
    nextButton.onclick = function() {
        if (currentQuestionIndex < questions.length - 1) {
            handleNextButton();
        } else {
            showScore(); 
        }
    };
}

function handleNextButton() {
    currentQuestionIndex++;
    showQuestion();
}

function showScore() {
    while (answerButton.firstChild) {
        answerButton.removeChild(answerButton.firstChild);
    }
    questionElement.innerHTML = `Your Score is ${score} out of ${questions.length}`;
    nextButton.innerHTML = "Restart"; 
    nextButton.style.display = "block";
    nextButton.onclick = startQuiz; 
}

window.onload = function() {
    getQuestion(); 
};

const questions = [
    {
        question: "Who was the first president of the United States?", 
        answers: [
            { text: "Barack Obama" , correct : false}, 
            { text: "George Washington" , correct : true}, 
            { text: "Donald Trump" , correct : false}, 
            { text: "Joe Biden" , correct : false}, 
        ]
    }, 
    {
        question: "Who is the most recent president of the United States?", 
        answers: [
            { text: "Ulysses S. Grant" , correct : false}, 
            { text: "George Washington" , correct : false}, 
            { text: "Donald Trump" , correct : false}, 
            { text: "Joe Biden" , correct : true}, 
        ]
    }, 
    {
        question: "Which president issued the Emancipation Proclamation?", 
        answers: [
            { text: "Abraham Lincoln" , correct : true}, 
            { text: "Franklin D. Roosevelt" , correct : false}, 
            { text: "Abraham Lincoln" , correct : false}, 
            { text: "Theodore Roosevelt" , correct : false}, 
        ]
    }, 
     {
        question: "Who was the only U.S. president to serve more than two terms?", 
        answers: [
            { text: "Woodrow Wilson" , correct : false}, 
            { text: "Franklin D. Roosevelt" , correct : true}, 
            { text: "Dwight D. Eisenhower" , correct : false}, 
            { text: "Harry S. Truman" , correct : false}, 
        ]
    }, 
     {
        question: "Which president famously said, \"The only thing we have to fear is fear itself\"?", 
        answers: [
            { text: "John F. Kennedy" , correct : false}, 
            { text: "Franklin D. Roosevelt" , correct : true}, 
            { text: "Lyndon B. Johnson" , correct : false}, 
            { text: "Ronald Reagan" , correct : false}, 
        ]
    }, 
         {
        question: "Which president is known for the Louisiana Purchase?"", 
        answers: [
            { text: "James Madison" , correct : false}, 
            { text: "Thomas Jefferson" , correct : true}, 
            { text: "John Quincy Adams" , correct : false}, 
            { text: "James Monroe" , correct : false}, 
        ]
    }
         {
        question: "Who was the president during the Cuban Missile Crisis?", 
        answers: [
            { text: "John F. Kennedy" , correct : true}, 
            { text: "Richard Nixon" , correct : false}, 
            { text: "Lyndon B. Johnson" , correct : false}, 
            { text: "Dwight D. Eisenhower" , correct : false}, 
        ]
    }
         {
        question: "Which president is known for the \"New Deal\"?", 
        answers: [
            { text: "Martin Van Buren" , correct : false}, 
            { text: "Franklin D. Roosevelt" , correct : true}, 
            { text: "Bill Clinton , correct : false}, 
            { text: "Dwight D. Eisenhower" , correct : false}, 
        ]
    }
         {
        question: "Who was the first president to resign from office?", 
        answers: [
            { text: "John F. Kennedy" , correct : false}, 
            { text: "Richard Nixon" , correct : true}, 
            { text: "Donald J. Trump" , correct : false}, 
            { text: "George Washington" , correct : false}, 
        ]
    }
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

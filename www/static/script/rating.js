document.addEventListener('DOMContentLoaded', ()=>{
    const stars = document.querySelectorAll('.star');
    const ratingValue = document.getElementById('rating-value');
    const ratingContainer = document.querySelector('.rating-container');
    let presidentName = ratingContainer.getAttribute('data-president-name');
    console.log('president Name',presidentName); 
    let selectedRating = 0; 

    const submitButton = document.getElementById('submit-rating');
    const localStorageKey = `rating_${presidentName}`; 

    // Check if a rating is already saved in localStorage
    const savedRating = localStorage.getItem(localStorageKey);
    if (savedRating) {
        selectedRating = savedRating; // Set the selected rating from localStorage
        setRating(selectedRating); // Apply the rating visually
        disableSubmission(); // Disable interactions
    }


    stars.forEach( star =>{
        star.addEventListener('click', ()=>{
            const rating = star.getAttribute('data-value');
            setRating(rating); 
        });

        star.addEventListener('mouseover', ()=> {
            const rating = star.getAttribute('data-value'); 
            highlightStars(rating); 
        });

        star.addEventListener('mouseout', resetStars);
    });

    function setRating(rating){
        selectedRating = rating; 
        stars.forEach(star => {
            star.classList.toggle('selected', star.getAttribute('data-value') <= rating);
        })
        ratingValue.textContent = `Rating: ${selectedRating}`;
    }

    function highlightStars(rating){
        stars.forEach(star=> {
            star.style.color = star.getAttribute('data-value') <= rating ? '#ffa500' : '#ccc';
        });
    }

    function resetStars() {
        stars.forEach(star => {
            star.style.color = star.classList.contains('selected') ? '#ffa500' : '#ccc';
        });
    }
    
    
    // Handle rating submission
    submitButton.addEventListener('click', () => {
        if (!selectedRating) {
            alert('Please select a rating before submitting.');
            return;
        }

        // Mock saving to the server
        const data = {
            president: presidentName,
            score: selectedRating
        };

        fetch('http://127.0.0.1:81/add-rating', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(result => {
            alert('Rating submitted successfully!');
            // Save the submission to localStorage
            localStorage.setItem(localStorageKey, selectedRating);
            disableSubmission();
        })
        .catch(error => {
            alert('Rating UNNNubmitted successfully!');
            console.error('Error:', error);
            alert('Failed to submit rating. Please try again.');
        });
    });

    function disableSubmission() {
        submitButton.disabled = true;
        submitButton.textContent = "Rating Submitted";
        stars.forEach(star => {
            star.style.color = star.getAttribute('data-value') <= selectedRating ? 'red' : '#ccc';
            star.style.pointerEvents = "none"; // Disable clicking on stars

        });
    }

})


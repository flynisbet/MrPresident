 const container = document.getElementById("president-cards");
  
  // Loop through the presidents array and add content dynamically
  presidents.forEach((president) => {
    // Create the card container
    const card = document.createElement("div");
    card.classList.add("card");
  
    // Create and append the image
    const img = document.createElement("img");
    img.src = president.image;
    img.alt = president.name;
    card.appendChild(img);
  
    // Create and append the name
    const name = document.createElement("h3");
    name.textContent = president.name;
    card.appendChild(name);
  
    // Create and append the title
    const title = document.createElement("p");
    title.textContent = president.title;
    card.appendChild(title);
  
    // Append the card to the container
    container.appendChild(card);
  });



document.addEventListener('DOMContentLoaded', () => {
    const timelineButton = document.getElementById('timelineButton');
    const profilesButton = document.getElementById('profileButton');
    const timelineContent = document.getElementById('timeline');
    const profileContent = document.getElementById('profiles');

    // Add event listeners to buttons
    timelineButton.addEventListener('click', () => {
       
        // Show timeline content and hide profiles content
        timelineContent.style.display = 'block';
        profileContent.style.display = 'none';

        if (!timelineButton || !profilesButton || !timelineContent || !profileContent) {
            console.error('One or more elements are missing in the DOM');
            return;
        }

        // Update button styles
        timelineButton.classList.add('active');
        profilesButton.classList.remove('active');
    });

    profilesButton.addEventListener('click', () => {
       
        // Show profiles content and hide timeline content
        profileContent.style.display = 'block';
        timelineContent.style.display = 'none';

        // Update button styles
        profilesButton.classList.add('active');
        timelineButton.classList.remove('active');
    });
});

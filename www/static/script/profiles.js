 const container = document.getElementById("president-cards");

  presidents.forEach((president) => {

    const card = document.createElement("div");
    card.classList.add("card");
  
    const img = document.createElement("img");
    img.src = president.image;
    img.alt = president.name;
    card.appendChild(img);
  
    const name = document.createElement("h3");
    name.textContent = president.name;
    card.appendChild(name);
  

    const title = document.createElement("p");
    title.textContent = president.title;
    card.appendChild(title);
  
    container.appendChild(card);
  });

  document.addEventListener('DOMContentLoaded', () => {
    // Get elements for button logic
    const timelineButton = document.getElementById('timelineButton');
    const profilesButton = document.getElementById('profileButton');
    const timelineContent = document.getElementById('timeline');
    const profileContent = document.getElementById('profiles');
    const searchBox = document.querySelector('.searchBox');
    const container = document.getElementById("president-cards");

    profileContent.style.display = 'none';

    // Add button event listeners
    timelineButton.addEventListener('click', () => {
        timelineContent.style.display = 'block';
        profileContent.style.display = 'none';
        searchBox.style.display = 'block';
        timelineButton.classList.add('active');
        profilesButton.classList.remove('active');
    });

    profilesButton.addEventListener('click', () => {
        profileContent.style.display = 'block';
        timelineContent.style.display = 'none';
        searchBox.style.display = 'none';
        profilesButton.classList.add('active');
        timelineButton.classList.remove('active');
    });

    // Fetch presidents data and render cards
    fetch('/pres')
        .then(response => response.json())
        .then(presidents => {
            presidents.forEach(president => {
                const card = document.createElement("div");
                card.classList.add("card");

                const img = document.createElement("img");
                img.src = president.image;
                img.alt = president.name;
                card.appendChild(img);

                const name = document.createElement("h3");
                name.textContent = president.name;
                card.appendChild(name);

                const title = document.createElement("p");
                title.textContent = president.title;
                card.appendChild(title);

                container.appendChild(card);
            });
        })
        .catch(err => console.error('Error fetching presidents:', err));
});

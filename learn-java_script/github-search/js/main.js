
const gitHubetails = document.querySelector("#git-details");
const searchBtn = document.querySelector('.search');
const userInput = document.querySelector('.user');



searchBtn.addEventListener('click', () => {
 console.log(userInput.value);
    
    getUsereDetails(userInput.value);
});

const getUsereDetails = async(Username) => {
    

    const url = `https://api.github.com/users/${Username}`;
    

    const response = await fetch(url);
    const data = await response.json();

    console.log(data);
    gitHubetails.innerHTML = `<h2>${data.name}</h2>
    
    <img style="border-radius: 50%;" src="${data.avatar_url}" alt="${data.name}"/>
    <p>${data.bio}</p>
    <p>${data.location}</p>
    <p>${data.public_repos}</p>
    <p>${data.public_gists}</p>
    <p>${data.followers}</p>
    <p>${data.following}</p>
    <p>${data.created_at}</p>
    <p>${data.updated_at}</p>
    <p>${data.html_url}</p>
    <p>${data.repos_url}</p>

    `;
    
};


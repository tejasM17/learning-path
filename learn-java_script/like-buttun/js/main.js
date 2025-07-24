const likebtn = document.querySelector('.like');
const unlikebtn = document.querySelector('.unlike');


const likecount = document.querySelector('.like-count');


let likes = 0;

likebtn.addEventListener('click', () => {
    console.log('like btn clicked');

    likecount.innerHTML = `like = ${likes += 1}`
});

unlikebtn.addEventListener('click', () => {
    console.log('unlike btn clicked');

    if (likes > 0) {
        likes -= 1;
    }

    likecount.innerHTML = `like = ${likes}`
});

console.log('Hi brothers and sisters');

const projectName = document.querySelector('.title');
console.log(projectName);

projectName.innerHTML = 'Learn something big';

const anotherProject = document.querySelector('#sub-title');
console.log(anotherProject);

anotherProject.innerHTML =  "its changed!!";

const mynbtten = document.querySelector('#btn');

console.log(mynbtten);

// mynbtten.onclick = () => {
   
//     console.log('clicked');
//     alert('clicked-onclick');
// };

mynbtten.addEventListener('click', () => {
    console.log('clicked');
    alert('clicked-addEventListener');
});


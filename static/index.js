/*

Pure JS, not JSX.
Resources used for deploying asyncs to backend:

-
-


*/
// mongo contanier logic

// DOMContentLoaded

const mongoContainer = document.getElementById('books')

function dataContainer(data) {

    // empty the content box
    mongoContainer.innerHTML = '';

    data.array.forEach(element => {

        const listed = document.createElement('li')

        listed.textContent = JSON.stringify(element, null, 2);

        mongoContainer.appendChild(li);
        
    });

}


// post
async function post(filmData)

// get all
async function getAll()

// get one
async function getOne(filmData)
// delete
async function deleteOne(filmData)


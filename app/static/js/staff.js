window.onload = function(event){
    let cards = document.querySelectorAll("to-hide")

    cards.forEach(element => {
        element.addEventListener('click', (event) => {
            event.preventDefault();
            element.classList.add('hide');
        })
    })
}
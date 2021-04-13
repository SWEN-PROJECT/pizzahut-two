window.onload = function(event){
    let cards = document.querySelectorAll("to-hide")
    const card_cont = document.querySelector('card-set');

    // function check_container(){
    //     if(card_cont.children.length <= 3){

    //     }
    // }

    cards.forEach(element => {
        element.addEventListener('click', (event) => {
            event.preventDefault();
            element.classList.add('hide');
        })
    })
}
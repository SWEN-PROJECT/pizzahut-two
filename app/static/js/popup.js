window.onload = function(e){
    const checkout = document.querySelector('.checkout');
    const confirms = document.querySelector('.confirm');
    const fades = document.querySelectorAll('.has-fade');
    const body = document.querySelector('body');

    checkout.addEventListener('click', function(event){
        event.preventDefault();
        console.log("Y")
        if (confirms.classList.contains('open')){
            body.classList.remove("notscroll");
            confirms.classList.remove('open');
            fades.forEach(function(element){
                element.classList.remove('fade-in');
                element.classList.add('fade-out');
            })
        }else{
            console.log("Yo")
            body.classList.add("notscroll");
            confirms.classList.add('open');
            fades.forEach(function(element){
                element.classList.remove('fade-out');
                element.classList.add('fade-in');
            });
        }
    });
}
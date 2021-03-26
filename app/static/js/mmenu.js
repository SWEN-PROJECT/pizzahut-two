window.onload = function(event){

    const additem = document.querySelector('.additem');
    const edititem = document.querySelector('.edititem');
    const confirms = document.querySelector('.confirm');
    const fades = document.querySelectorAll('.has-fade');
    const body = document.querySelector('body');
    const back = document.querySelector('.back');
    const ex = document.querySelector('.bi')
    const addbtn =  document.getElementById('addbtn')

    let card_list = document.querySelectorAll(".card");

    additem.addEventListener('click', (event) => {
        event.preventDefault();

        body.classList.add("notscroll");
        body.classList.add("back");
        confirms.classList.add('open');
        fades.forEach(function(element){
        element.classList.remove('fade-out');
        element.classList.add('fade-in');
        });
        
    });
    edititem.addEventListener('click', (event) => {
        event.preventDefault();

        body.classList.add("notscroll");
        body.classList.add("back");
        confirms.classList.add('open');
        fades.forEach(function(element){
        element.classList.remove('fade-out');
        element.classList.add('fade-in');
        });
        
    });

    ex.addEventListener('click', (event) =>{
        event.preventDefault();
        if (confirms.classList.contains('open')){
            body.classList.remove("notscroll");
            confirms.classList.remove('open');
            fades.forEach(function(element){
                element.classList.remove('fade-in');
                element.classList.add('fade-out');
            })
        }
    })

    let card_footer = confirms.querySelector(".card-footer");
    
    addbtn.addEventListener('click', (event) =>{
        event.preventDefault();
        let form = document.forms[0]
        form.submit();
        if (confirms.classList.contains('open')){
            body.classList.remove("notscroll");
            confirms.classList.remove('open');
            fades.forEach(function(element){
                element.classList.remove('fade-in');
                element.classList.add('fade-out');
            })
        }
    });
    
};
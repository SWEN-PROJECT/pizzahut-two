window.onload = function(event){

    const checkout = document.querySelector('.checkout');
    const confirms = document.querySelector('.confirm');
    const fades = document.querySelectorAll('.has-fade');
    const body = document.querySelector('body');
    const back = document.querySelector('.back');
    const ex = document.querySelector('.bi')

    let card_list = document.querySelectorAll(".card");

    card_list.forEach(element => {

        let data  = element.id;
        let card_button = element.querySelector(".card-footer");
        if (card_button != null){
            card_button.addEventListener('click', (event) => {
                event.preventDefault();

                fetch(`/menu/${data}`, {
                    method: 'POST' ,
                }).then(response => response.text())
                  .then(datar => {
                        console.log(datar)
                        if(datar.length < 2){
                            console.log("We are here");
                            checkout.textContent = `Checkout (${datar})`;
                        }
                   })
                  .catch(error => {
                        console.log(error);
                   });
            });
        }
    });

    checkout.addEventListener('click', (event) => {
        event.preventDefault();
        body.classList.add("back")
        confirms.classList.add('open');
        fades.forEach(function(element){
        element.classList.remove('fade-out');
        element.classList.add('fade-in');
        });
        

        fetch(`/menu/checkout`)
            .then(response => response.json())
            .then(receive => {
            
                let lst = receive.list
                if( lst == 'NOWM'){

                }else{
                    let section = document.querySelector('.order-info');
                    let result = "";
                    for(i = 0; i < lst.length; i++){
                        result += `<div class="cell"> <p>${i+1} ${lst[i].name}</p> <p>${lst[i].qty}</p> <p>${lst[i].price}</p></div>`;
                    }
                    section.innerHTML = result;
                    checkout.innerHTML = 'Checkout';

                }
            })
            .catch(error => {
                console.log(error);
            });

        
    });

    ex.addEventListener('click', (event) =>{
        event.preventDefault();
        if (confirms.classList.contains('open')){
            confirms.classList.remove('open');
            fades.forEach(function(element){
                element.classList.remove('fade-in');
                element.classList.add('fade-out');
            })
        }
    })

    let card_footer = confirms.querySelector(".card-footer");
    
    card_footer.addEventListener('click', (event) =>{
            event.preventDefault();

            let section = document.querySelector('.item-info').querySelector('form').querySelectorAll("select");
            let typesection = section[0]
            let pointsection = section[1]
            let val = typesection.value;
            let rp = pointsection.value;


            var searchParams = new URLSearchParams();
            searchParams.append('type', val);
            searchParams.append('points', rp);

            fetch(`/menu/confirm`, {
                method: 'POST' ,
                body: searchParams,
            }).then(response => response.text())
            .then(received => {
                    if( received == 'OK'){
                        checkout.innerHTML = 'Checkout';
                        if (confirms.classList.contains('open')){
            
                            confirms.classList.remove('open');
                            fades.forEach(function(element){
                                element.classList.remove('fade-in');
                                element.classList.add('fade-out');
                            })
                        }
                        window.location.href = '/complete';
                    }
                    
                })
                .catch(error => {
                    console.log(error);
                });
    });
    
};
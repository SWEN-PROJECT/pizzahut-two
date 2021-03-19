window.onload = function(event){
    
    let card_list = document.querySelectorAll(".card");
    let address = window.location.href;
    card_list.forEach(element => {
        let data  = element.id;
        let card_button = element.querySelector(".card-footer");

        card_button.addEventListener('click', (event) => {
            event.preventDefault();
            fetch(`/menu/${data}`)
                .then(response => response.text())
                .then(datar => {
                    let checkout = document.querySelector(".checkout");
                    checkout.textContent = `Checkout(${datar})`;
                })
                .catch(error => {
                    console.log(error);
                });
        });

    });

    let checkout = document.querySelector(".checkout");

    checkout.addEventListener('click', (event) => {
        event.preventDefault();
        fetch(`/menu/checkout`)
            .then(response => response.text())
            .then(receive => {
                if( receive  == 'NOWM'){
                }else{
                    checkout.textContent = 'Checkout';
                }
            })
            .catch(error => {
                console.log(error);
            });
    });
    
};
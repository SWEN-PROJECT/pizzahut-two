window.onload = function(event){

    const additem = document.querySelector('.additem');
    const edititem = document.querySelector('.edititem');
    // const deletebtn = document.querySelectorAll('.deletebtn');
    const confirms = document.querySelector('.confirm');
    const fades = document.querySelectorAll('.has-fade');
    const body = document.querySelector('body');
    const back = document.querySelector('.back');
    const ex = document.querySelector('.bi')
    const addbtn =  document.getElementById('addbtn');

    // const deletebtn= document.getElementById('deletebtn');
    let operation = null;
    let item = null;
    let card_list = document.querySelectorAll(".icard");

    additem.addEventListener('click', (event) => {
        event.preventDefault();
        operation = 'add';

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
            confirms.classList.remove('open');
            fades.forEach(function(element){
                element.classList.remove('fade-in');
                element.classList.add('fade-out');
            })
        }
    })

    card_list.forEach(element => {
        let edititem = element.querySelector(".edititem");
        let deletebtn = element.querySelector(".deletebtn");
        edititem.value = element.id;

        edititem.addEventListener('click', (event) => {
            event.preventDefault();

            item = edititem.value;

            fetch(`/menu/${item}`, {
                method: 'GET' 
            }).then(response => response.json())
            .then(received => {
                let form = document.forms[0];
                let lst = form.elements;
                let result = received.result[0]

                for(i=1; i < lst.length - 1; i++){
                    switch(lst[i].name) {
                        case 'description':
                            lst[i].value = result.desc
                            break;

                        case 'name':
                            lst[i].value = result.name
                            break;
                            
                        case 'tag':
                            switch(result.tag){
                                case 'Pizza':
                                    lst[i].selectedIndex = 0
                                    break;
                                
                                case 'Beverage':
                                    lst[i].selectedIndex = 1
                                    break;

                                case 'Side':
                                    lst[i].selectedIndex = 2
                                    break;
                                
                                case 'Crust':
                                    lst[i].selectedIndex = 3
                                    break;

                                case 'Topping':
                                    lst[i].selectedIndex = 4
                                    break;
                            }
                            break;
                            
                        case 'price':
                            lst[i].value = result.price
                            break;
                        
                        default:
                            break;
                    }

                }

            }).catch(error => {
                console.log(error);
            });
        

            let p = confirms.querySelector(".card-title");
            p.textContent = 'Edit-Item: ID# ' + item;
            operation = 'edit';
            
            addbtn.textContent = 'Edit Item' ;
            addbtn.setAttribute("id",item);
            body.classList.add("back");
            confirms.classList.add('open');
            fades.forEach(function(element){
            element.classList.remove('fade-out');
            element.classList.add('fade-in');
            });
            
        });
        
        deletebtn.addEventListener('click', (event) => {
            event.preventDefault();
            fetch(`/menu/${item}`, {
                method: 'DELETE' 
            }).then(response => response.text())
            .then(received => {
                window.location.reload(); 
            }).catch(error => {
                console.log(error);
            });      
        });

    });
    
    let card_footer = confirms.querySelector(".card-footer");
    
    addbtn.addEventListener('click', (event) =>{
        if(operation == 'add'){
            event.preventDefault();
            let form = document.forms[0]
            form.name = "addform";
            var formtype = document.createElement("input");
            formtype.type = "hidden";
            formtype.name = "addform";
            form.appendChild(formtype);
            form.submit();
        }else if(operation == 'edit'){
        
            event.preventDefault();
            let form = document.forms[0]
            form.name = "editform";

            //adding a hidden field to form for checking the type of form request ie edit or add
            var formtype = document.createElement("input");
            formtype.type = "hidden";
            formtype.name = "editform";
            form.appendChild(formtype);

            //adding the id of the item to the form
            var itemid = document.createElement("input");
            itemid.type = "hidden";
            itemid.name = "itemid";
            itemid.value = item;
            form.appendChild(itemid);
            form.submit();
        }
        
        if (confirms.classList.contains('open')){
            confirms.classList.remove('open');
            fades.forEach(function(element){
                element.classList.remove('fade-in');
                element.classList.add('fade-out');
            })
        }
    });

        
};
elem = document.getElementById('log-form').addEventListener('submit', checkForm)

function checkForm(event){
    event.preventDefault();

    var elem=document.getElementById('main-form');
    var name = elem.name.value;
    var pass= elem.pass.value;

    var error="";

    if(name=="" || pass=="")
        error="Заполните все поля";
    else if(name.length<=1 || name.length>50)
        error="Введите корректное имя";
    

    if(error!="")
        document.getElementById('error').innerHTML = error;
    else {
        alert("Данные введены корректно!");
        window.location(document.location = "blog.html");
    }
}
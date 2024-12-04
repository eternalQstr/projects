elem = document.getElementById('main-form').addEventListener('submit', checkForm)

function checkForm(event){
    event.preventDefault();

    var elem=document.getElementById('main-form');
    var name = elem.name.value;
    var pass= elem.pass.value;
    var repass=elem.repass.value;
    var state=elem.state.value;

    var error="";

    if(name=="" || pass=="" || repass=="" || state=="")
        error="Заполните все поля";
    else if(name.length<=1 || name.length>50)
        error="Введите корректное имя";
    else if(pass!=repass)
        error="Введите корректно пароли";
    

    if(error!="")
        document.getElementById('error').innerHTML = error;
    else {
        alert("Данные введены корректно!");
        window.location(document.location = "D:/localhost/IT-TOP project/blog.html");
    }
}
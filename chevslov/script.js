
const formulaire=document.getElementById("formulaire");
const password=document.getElementById("password");
const envoyer=document.getElementById("envoyer");

function infoMessage(event){
    event.preventDefault();
    if(password.value.length >= 8) {
        info.textContent = "Vous êtes connecté";
        info.style.color = "green";
    }else{
        info.textContent = "Entrez un email valide";
        info.style.color = "red;"
    }
}
formulaire.addEventListener("submit",infoMessage);
// Recuperer les elements Passwords 
const passwordInput = document.getElementById("pwd");
const confirmPasswordInput=document.getElementById("cpwd");

const checkPasswords=function(){
    // Comparer passwordInput value avec confirmPasswordInput value
    const passwordMatch =passwordInput.value===confirmPasswordInput.value;
     // Verifier les passwords
    if(passwordMatch)
    {      // Effacer le message d'erreur precedent.
        confirmPasswordInput.setCustomValidity("");
    }
    else{
         // Le formulaire ne sera pas envoyé en cas d'erreur. Un message sera affiché à l'utilisateur
        confirmPasswordInput.setCustomValidity("Vos mots de passe ne correspondent pas. Veuillez retaper le même mot de passe.")
        }
};

const addPasswordInputEventListeners =  function(){
    // Ajouter l' ecouteur d'evenement "input" aux elements passwordInput et confirmPasswordInput.
     //       Appeler la fonction checkPasswords
    passwordInput.addEventListener("input",checkPasswords);
    confirmPasswordInput.addEventListener("input",checkPasswords);



}

addPasswordInputEventListeners();
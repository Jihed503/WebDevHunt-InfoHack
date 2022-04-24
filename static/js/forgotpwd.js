function generatePassword() {
    var length = 8,
        charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
        retVal = "";
    for (var i = 0, n = charset.length; i < length; ++i) {
        retVal += charset.charAt(Math.floor(Math.random() * n));
    }
    return retVal;
}


function sendMail() {

    var mail = document.getElementById("mail").value
    var link = "mailto:"
             + mail
             + "?subject=" + encodeURIComponent("Password reset")
             + "&body=" + "Here is your new password: " + encodeURIComponent(generatePassword())
    ;
    
    window.location.href = link;
}

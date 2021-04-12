const registerButton = document.getElementById("register-button");
const registerForm = document.getElementById("registration-form");
const registerErrorMsg = document.getElementById("registration-error-msg");
const backButton = document.getElementById("back-button");

registerButton.addEventListener("click",(e) =>{
    e.preventDefault();
    const email = registerForm.username.value;
    const password = registerForm.password.value;
   
    if(email==="user" && password==="web_dev"){
        location.href="home.html";
    }
    else{
        registerErrorMsg.style.opacity=1;
    }
})

backButton.addEventListener("click",(e) =>{
    e.preventDefault();
    location.href="login.html";
})
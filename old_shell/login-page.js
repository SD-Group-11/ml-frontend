const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");
const loginErrorMsg = document.getElementById("login-error-msg");
const registerButton = document.getElementById("login-form-register");

loginButton.addEventListener("click", (e) => {
    e.preventDefault();
   const username = loginForm.username.value;
   const password = loginForm.password.value;
    if (username == "user" && password == "web_dev") {
        window.location.href = "home.html"
    }
    else{
        loginErrorMsg.style.opacity = 1;
    }
})


registerButton.addEventListener("click", (e) => {

    e.preventDefault();

    window.location.href ="registration.html";

})


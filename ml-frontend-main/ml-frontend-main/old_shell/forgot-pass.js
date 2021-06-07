const changePassForm = document.getElementById("forgot-pass-form");
const changePassButton = document.getElementById("password-change-submit");
const changePassErrorMsg = document.getElementById("forgot-pass-error-msg");
const loginButton = document.getElementById("forgot-pass-login");

changePassButton.addEventListener("click", (e) => {
    e.preventDefault();
   const username = changePassForm.username.value;
   const password = changePassForm.password.value;
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


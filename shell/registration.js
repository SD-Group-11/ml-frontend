//very similiar to login page code, just with few minor adjustments
const registerButton = document.getElementById("register-button"); 
const registrationForm = document.getElementById("registration-form"); //register button that will go to home page
const registrationErrorMsg = document.getElementById("registration-error-msg");
const backButton = document.getElementById("registration-form-back"); //back button go to login page

//when register button clicked -> 2 cases (successful vs. unsuccessful registration)
registerButton.addEventListener("click", (e) => {
    e.preventDefault();
   const username = registrationForm.username.value;
   const password = registrationForm.password.value;
   const password2 = registrationForm.password2.value; 
   const f_name = registrationForm.first_name.value;
   const s_name = registrationForm.last_name.value;
   const email = registrationForm.mail.value; 
  //make sure registration is legit:
  //2nd password for double checking
    if(password == "" || password2 == "" || username == "" || email == "" || f_name == "" || s_name == ""){
      registrationErrorMsg.textContent = 'Missing fields.'; // change message
        registrationErrorMsg.style.opacity = 1;
    }
    //can add in other password requirements e.g. numbers and such
    else if(password != password2){ //passwords must match - pls work
      registrationErrorMsg.textContent = 'Passwords do not match'; // change message
        registrationErrorMsg.style.opacity = 1;
    }
    else if (password.length < 6) { //password must be 6 letters long
        registrationErrorMsg.textContent = 'Password too short, needs 6 characters or more.'; // change message
        registrationErrorMsg.style.opacity = 1;
    }
    else{ //successful registration, above cases didnt run
    
         window.location.href = "landing_page.html";
        
    }
  
    if (username == "user" && password == "web_dev"){
         window.location.href = "landing_page.html";
    }
	
    if (username == "user"){ //shortcut - remove later
      window.location.href = "landing_page.html";
    }
})


//go back to home page
backButton.addEventListener("click", (e) => {

    e.preventDefault();

    window.location.href ="login.html";

})

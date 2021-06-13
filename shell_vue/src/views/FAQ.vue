<template>
  <div class="container">  
    <section class="hero is-light" style=" background-color:lightyellow">
      <div class="get-head"></div>
      <div class="get-body">

          <template v-if="$store.state.isAuthenticated">
          <div class="columns is-multiline"> 
           <div class="column  is-half"> 
            <div class="card">
              <header class="card-header">
                <p class="card-header-title">
              I forgot my password, how do I reset it?
            </p>
          <button class="card-header-icon" aria-label="more options" @click="toggle= !toggle">
            <span class="icon">
              <img src="@/assets/images/arrow-down-sign-to-navigate.png" alt="Logo">
            </span>
          </button>
        </header>
 
          <div class="card-content" v-show='toggle'>
            <div class="content" v-show='toggle'>
              You can always reset your password from the sign in form.
            </div>
          </div>
          </div>
          </div>
        <br/>
        <div class="column  is-half"> 
          <div class="card">
              <header class="card-header">
                <p class="card-header-title">
              I have not received an email to reset my password, what should I do?
            </p>
          <button class="card-header-icon"  aria-label="more options" @click="toggle1= !toggle1 ">
            <span class="icon" >
              <img src="@/assets/images/arrow-down-sign-to-navigate.png" alt="Logo">
            </span>
          </button>
        </header>
          <div class="card-content" v-show='toggle1'>
            <div class="content" v-show='toggle1'>
              If you have not received an email to change your password try checking your spam folder. Otherwise please contact mlfframework@gmail.com.
            </div>
          </div>
          </div>
          </div>
          
          
        <div class="column  is-half"> 
          <div class="card">
              <header class="card-header">
                <p class="card-header-title">
              Do I need an account to access this platform?
            </p>
          <button class="card-header-icon" aria-label="more options" @click="toggle2= !toggle2">
            <span class="icon">
             <img src="@/assets/images/arrow-down-sign-to-navigate.png" alt="Logo">
            </span>
          </button>
        </header>
          <div class="card-content" v-show='toggle2'>
            <div class="content" v-show='toggle2'>
              You are welcome to browse the site to find out what we offer but you would need an account to use the models listed.
            </div>
          </div>
          </div>
        </div>  
        <div class="column  is-half"> 
          <div class="card">
              <header class="card-header">
                <p class="card-header-title">
              My data is not being read correctly, what should I do?
            </p>
          <button class="card-header-icon" aria-label="more options" @click="toggle3= !toggle3">
            <span class="icon">
              <img src="@/assets/images/arrow-down-sign-to-navigate.png" alt="Logo">
            </span>
          </button>
        </header>
          <div class="card-content" v-show='toggle3'>
            <div class="content" v-show='toggle3'>
              Make sure that your data is correctly formatted according to the guidelines listed on the information page.
            </div>
          </div>
          </div>
         </div> 
        </div>  

        <div class="card" style="max-width:800px">
         <header class="card-header">
                <p class="card-header-title is-centered">
              Upload a CSV file where the last column must be the targets/categories.
                </p>
         </header>    
         <div class="card-content">
           <div class="content is-medium">
             <ol type="1">
               <li>Click on "Choose File".</li>
               <li>Select a .csv file from your local device.</li>
               <li>Click on "Submit".</li>
               <li>Wait and let the magic happen!</li>
             </ol>  
             <br/>
           </div>
         </div>    
        </div>
            <!-- <header id="gettingstarted" > -->
            <!-- <h1><strong>General</strong></h1>
            
            <p><strong>Q. </strong>I forgot my password, how do I reset it?</p>
            <p><strong>A. </strong>You can always reset your password from the sign in form.</p>
            <br>
            <p><strong>Q. </strong>I have not received an email to reset my password, what should I do?</p>
            <p><strong>A. </strong>If you have not received an email to change your password try checking your spam folder. Otherwise please contact mlfframework@gmail.com.</p>
            <br>
            <p><strong>Q. </strong>Do I need an account to access this platform?</p>
            <p><strong>A. </strong>You are welcome to browse the site to find out what we offer but you would need an account to use the models listed.</p>
            <br>
            <h1><strong>Data</strong></h1>
            <p><strong>Q. </strong>My data is not being read correctly, what should I do?</p>
            <p><strong>A. </strong>Make sure that your data is correctly formatted according to the guidelines listed on the information page.</p>  
          
            <br>
            <h1><strong>Uploading for Linear Regression</strong></h1>
            <br> -->
            <!-- <p><strong>Upload a CSV file where the last column must be the targets/categories.</strong></p>
             <br>
            <h3>  1) Click on "Choose File" <br>
                     2) Select a .csv file from your local device.<br>
                     3) Click on "Submit"<br>
                     4) Wait and let the ✨magic✨ happen!<br>
                </h3>  
          
          </header> -->
          </template>
          <template v-else>
          <div class="columns is-multiline"> 
           <div class="column  is-half"> 
            <div class="card">
              <header class="card-header">
                <p class="card-header-title">
              I forgot my password, how do I reset it?
            </p>
          <button class="card-header-icon" aria-label="more options" @click="toggle= !toggle">
            <span class="icon">
             <img src="@/assets/images/arrow-down-sign-to-navigate.png" alt="Logo">
            </span>
          </button>
        </header>
 
          <div class="card-content" v-show='toggle'>
            <div class="content" v-show='toggle'>
              You can always reset your password from the sign in form.
            </div>
          </div>
          </div>
          </div>
        <br/>
        <div class="column  is-half"> 
          <div class="card">
              <header class="card-header">
                <p class="card-header-title">
              I have not received an email to reset my password, what should I do?
            </p>
          <button class="card-header-icon"  aria-label="more options" @click="toggle1= !toggle1 ">
            <span class="icon" >
              <img src="@/assets/images/arrow-down-sign-to-navigate.png" alt="Logo">
            </span>
          </button>
        </header>
          <div class="card-content" v-show='toggle1'>
            <div class="content" v-show='toggle1'>
              If you have not received an email to change your password try checking your spam folder. Otherwise please contact mlfframework@gmail.com.
            </div>
          </div>
          </div>
          </div>
          
          
        <div class="column  is-half"> 
          <div class="card">
              <header class="card-header">
                <p class="card-header-title">
              Do I need an account to access this platform?
            </p>
          <button class="card-header-icon" aria-label="more options" @click="toggle2= !toggle2">
            <span class="icon">
             <img src="@/assets/images/arrow-down-sign-to-navigate.png" alt="Logo">
            </span>
          </button>
        </header>
          <div class="card-content" v-show='toggle2'>
            <div class="content" v-show='toggle2'>
              You are welcome to browse the site to find out what we offer but you would need an account to use the models listed.
            </div>
          </div>
          </div>
        </div> 
        </div>  
          </template>
          
      </div>
      <div class="get-foot"></div>
    </section>
  </div>  
</template>

<style scoped>
  @import '../assets/styles/homepage.css';
  .card {
    /* max-width: 500px; */
    margin-left: auto;
    margin-right: auto;
  }
  .message-body {
    padding: 0;
    max-height: 10em;
    overflow: hidden;
    transition: 0.3s ease all;
  }
  .is-closed .message-body {
    max-height: 0;
  }
  .message-content {
    padding: 20px;
  }
</style>



<script>
export default {
  name: 'FAQ',
  data() {
    return {
      toggle: false,
      toggle1: false,
      toggle2: false,
      toggle3: false
    }
  }
}
</script>

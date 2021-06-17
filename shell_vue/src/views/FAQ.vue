<template>
  <div class="container is-fluid">  


    <div class="container is-fluid p-2">
        <div class="notification is-info" >
            <strong><h3 class="title is-1">Frequetly Asked Questions</h3></strong>
        </div>

    </div>

    <div class="block" > </div>

      <template v-if="$store.state.isAuthenticated">
        
        <div class="container is-fluid"> 
            
          <div class="control"> 
            
            <article class="message is-warning">
              <div class="message-header">
                <p>I forgot my password, how do I reset it?
                </p>
                
                <button class="button is-warning is-light "  @click="toggle= !toggle">
                  <span class="icon is-small">
                    <i class="fas fa-chevron-circle-down"></i>
                  </span>
                </button>
              </div>
              <div class="message-body" v-show='toggle'>
                <div class="notification is-info  is-light">
                  You can reset your password from the sign-in form.
                </div>
                
              </div>
            </article>

            <article class="message is-warning">
              <div class="message-header">
                <p>I have not received an email to reset my password, what should I do?
                </p>
                
                <button class="button is-warning is-light"  @click="toggle1= !toggle1">
                  <span class="icon is-small">
                    <i class="fas fa-chevron-circle-down"></i>
                  </span>
                </button>
              </div>
              <div class="message-body" v-show='toggle1'>
                <div class="notification is-info  is-light">
                  If you have not received an email to change your password try checking your spam folder. Otherwise please contact mlfframework@gmail.com.

                </div>
                </div>
            </article>


            <article class="message is-warning">
              <div class="message-header">
                <p>Do I need an account to access this platform?
                </p>
                
                <button class="button is-warning is-light"   @click="toggle2= !toggle2">
                  <span class="icon is-small">
                    <i class="fas fa-chevron-circle-down"></i>
                  </span>
                </button>
              </div>
              <div class="message-body" v-show='toggle2'>
                <div class="notification is-info  is-light">
                  You are welcome to browse the site to find out what we offer but you do need an account to use the listed models.

                </div>
              </div>
            </article>


            <article class="message is-warning">
              <div class="message-header">
                <p> My data is not being read correctly, what should I do?
                </p>
                
                <button class="button is-warning is-light" @click="toggle3= !toggle3">
                  <span class="icon is-small">
                    <i class="fas fa-chevron-circle-down"></i>
                  </span>
                </button>
              </div>
              <div class="message-body" v-show='toggle3'>
                <div class="notification is-info  is-light">
                    Make sure that your data is correctly formatted according to the guidelines listed on the information page.
                </div>
              </div>
            </article>

            <article class="message is-warning">
              <div class="message-header">
                <p> How do I upload my dataset?
                </p>
                
                <button class="button is-warning is-light" @click="toggle4= !toggle4">
                  <span class="icon is-small">
                    <i class="fas fa-chevron-circle-down"></i>
                  </span>
                </button>
              </div>
              <div class="message-body" v-show='toggle4'>
                <div class="notification is-info  is-light ml-5">
                  <ol type="1">
                    <li>Click on "Choose File".</li>
                    <li>Select a .csv file from your local device.</li>
                    <li>Click on "Submit".</li>
                    <li>Wait and let the magic happen!</li>
                  </ol>             
                </div>
              </div>
            </article>

          </div>
 
        
        </div>  

      </template>

      <template v-else>
        <div class="control"> 
            
            <article class="message is-warning">
              <div class="message-header">
                <p>I forgot my password, how do I reset it?
                </p>
                
                <button class="button is-warning is-light"  @click="toggle= !toggle">
                  <span class="icon is-small">
                    <i class="fas fa-chevron-circle-down"></i>
                  </span>
                </button>
              </div>
              <div class="message-body" v-show='toggle'>
                <div class="notification is-info  is-light">
                  You can reset your password from the sign-in form.
                </div>
                
              </div>
            </article>

            <article class="message is-warning">
              <div class="message-header">
                <p>I have not received an email to reset my password, what should I do?
                </p>
                
                <button class="button is-warning is-light"  @click="toggle1= !toggle1">
                  <span class="icon is-small">
                    <i class="fas fa-chevron-circle-down"></i>
                  </span>
                </button>
              </div>
              <div class="message-body" v-show='toggle1'>
                <div class="notification is-info  is-light">
                  If you have not received an email to change your password try checking your spam folder. Otherwise please contact mlfframework@gmail.com.

                </div>
                </div>
            </article>


            <article class="message is-warning">
              <div class="message-header">
                <p>Do I need an account to access this platform?
                </p>
                
                <button class="button is-warning is-light"   @click="toggle2= !toggle2">
                  <span class="icon is-small">
                    <i class="fas fa-chevron-circle-down"></i>
                  </span>
                </button>
              </div>
              <div class="message-body" v-show='toggle2'>
                <div class="notification is-info  is-light">
                  You are welcome to browse the site to find out what we offer but you do need an account to use the listed models.

                </div>
              </div>
            </article>
          </div>
    </template>

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
      toggle3: false,
      toggle4: false,
    }
  }
}
</script>

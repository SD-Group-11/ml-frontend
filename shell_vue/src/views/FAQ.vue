<template>
    <section class="hero is-light">
      <div class="get-head"></div>
      <div class="get-body">

          <template v-if="$store.state.isAuthenticated">
            <header id="gettingstarted" >
            <h1><strong>General</strong></h1>
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
            <br>
            <p><strong>Upload a CSV file where the last column must be the targets/categories.</strong></p>
             <br>
            <h3>  1) Click on "Choose File" <br>
                     2) Select a .csv file from your local device.<br>
                     3) Click on "Submit"<br>
                     4) Wait and let the magic happen!<br>
                </h3>
          
          </header>
          </template>

          <template v-else>
            <header id="gettingstarted" >
            <h1><strong>General</strong></h1>
            <p><strong>Q. </strong>I forgot my password, how do I reset it?</p>
            <p><strong>A. </strong>You can always reset your password from the sign in form.</p>
            <br>
            <p><strong>Q. </strong>I have not received an email to reset my password, what should I do?</p>
            <p><strong>A. </strong>If you have not received an email to change your password try checking your spam folder. Otherwise please contact mlfframework@gmail.com.</p>
            <br>
            <p><strong>Q. </strong>Do I need an account to access this platform?</p>
            <p><strong>A. </strong>You are welcome to browse the site to find out what we offer but you would need an account to use the models listed.</p>
            <br>
            </header>    
          </template>
          
      </div>
      <div class="get-foot"></div>
    </section>
</template>

<style scoped>
  @import '../assets/styles/homepage.css';
</style>



<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'FAQ',
  components: {
    HelloWorld
  }
}
</script>

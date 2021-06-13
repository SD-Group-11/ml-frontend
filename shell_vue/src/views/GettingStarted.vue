<template>
    <div class="container">  
    <section class="hero is-light" style=" background-color:lightyellow">
      <div class="get-head"></div>
      <div class="get-body">
          <div class="card" style="max-width:800px">
         <header class="card-header">
                <p class="card-header-title is-centered" style="font-size:40px">
             Getting Started
                </p>
         </header>    
         <div class="card-content">
           <div class="content is-medium">
             <ol type="1">
               <li>Select the model you would like to use.</li>
               <li>Upload your data.</li>
               <li>Apply the model.</li>
               <li>Interpret the results.</li>
               <li>Download your results.</li>

             </ol>
           </div>
           <div class="github-card" data-github="SD-Group-11/ml-frontend" data-width="400" data-height="" data-theme="default"></div>
          
         </div>    
         <div class="card">
          <footer class="card-footer">
            <router-link to="/faq" class="card-footer-item">FAQ</router-link>
            <router-link to="/dashboard" class="card-footer-item is-link">Account</router-link>
          </footer>
        </div>
        </div>
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
</style>


<script>
// @ is an alias to /src

export default {
  name: 'GettingStarted'
}
</script>

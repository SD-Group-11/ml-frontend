<template>
<div class = "container">

  <div class="columns is-mobile is-centered is-vcentered">
  <div class="column is-one-fifth">
    <img src="@/assets/images/confused-icon-6-yellow.png" alt="Logo">
  </div>
  <div class="column">
    <span class="title is-1">Machine Learning Front-End Framework</span><br>
    <span class="subtitle is-info">Making machine learning quick and easy</span>
  </div>
  </div>

  <br>

  <div class="columns">
      <div class="column is-full is-warning ">
          <div class="box" style="background-color:#FFD55A;"></div>
      </div>
  </div>

  <div class="card has-background-info-light">
  <div class="card-content has-text-centered is-3">
    <p>
      Recently machine learning models have become popular at performing automatic 
       classification. However, researchers have to constantly code up the training procedure 
       of common networks such as Naive Bayes or Logistic Regression which can be tedious.
       We streamline this process by providing the frontend application where the user
       can choose an existing network and can receive and interpret results instantly. 
    </p>
  </div>

  <div class="container has-text-centered">
    <a class="button is-info is-outlined is-rounded is-normal"><router-link class="card-footer-item is-centered" to="/getting-started"><strong>Get Started</strong></router-link></a>
  </div>  
  <br>

  </div>

  <br>


   <!-- <div class="columns">
      <div class="column is-full is-warning ">
            
      </div>
  </div> -->

  <div class="columns is-mobile is-centered is-vcentered">
  <div class="column is-half">
        <div class="card">
            <header class="card-header has-background-info">
            <p class="card-header-title is-3">
            Datasets
            </p>
            <button class="card-header-icon" aria-label="more options">
              <span class="icon">
                <i class="fas fa-angle-down" aria-hidden="true"></i>
              </span>
            </button>
          </header>
          <div class="card-content">
            <div class="content">
              Find datasets on our public datasets page, these are shared by other users and you can contribute too. Alternatively there is Kaggle, an online community of published data.
              <br>
            </div>
          </div>
          <footer class="card-footer is-centered has-background-info-light">
            <router-link class="card-footer-item is-centered" to="/public-datasets"><strong>Public Datasets</strong></router-link>
            <!-- <a href="#" class="card-footer-item">Public Datasets</a> -->
            <a href="https://www.kaggle.com" class="card-footer-item"><strong>Kaggle</strong></a>
          </footer>
        </div>
  </div>
  <div class="column is-half">
      <div class="card">
            <header class="card-header has-background-info">
              <p class="card-header-title is-3">
              More about Machine Learning
              </p>
              <button class="card-header-icon" aria-label="more options">
                <span class="icon">
                  <i class="fas fa-angle-down" aria-hidden="true"></i>
                </span>
              </button>
            </header>
            <div class="card-content">
              <div class="content">
                Here are some resources to help learn more about Machine Learning and the various available models.
                <br>
                <br>
              </div>
            </div>
            <footer class="card-footer is-centered has-background-info-light">
              <a href="https://www.expert.ai/blog/machine-learning-definition/" class="card-footer-item"><strong>Machine Learning</strong></a>
              <a href="https://www.educba.com/machine-learning-models/" class="card-footer-item"><strong>Models</strong></a>
            </footer>
        </div>
  </div>

  </div>


  





</div>
</template>

<style scoped>
  img 
  { 
    max-width:75%;
    height:75%;
    /* resizing robot for landing page */
  }

  .container
  {
    padding: 5px;
  }

  
</style>




<script>
// @ is an alias to /src
//import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  components: {
    //HelloWorld
  }
}

</script>

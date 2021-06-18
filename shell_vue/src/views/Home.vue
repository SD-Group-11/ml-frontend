<template>
<div class = "container">
    <section class="hero is-small" style=" background-color:lightblue">
      <div class="hero-body">
          <header id="showcase" >
            <img src="@/assets/images/confused-icon-6.png" alt="Logo">
            <h1 class = "title is-1 has-text-centered has-text-black mt-5"><strong><i>Machine Learning Front-End Framework</i></strong></h1>
          </header>
      </div>
    </section>

    <br>

    <div>
    <h1 class = "title is-1 has-text-centered has-text-black mt-5 pt-6"><strong><i>Introduction</i></strong></h1>
     <p class="info has-text-centered pb-6 ">Recently machine learning models have become popular at performing automatic 
       classification. However, researchers have to constantly code up the training procedure 
       of common networks such as Resnet or Alexnet which can be tedious.
       We can streamline this process by providing a frontend application where the user
       can choose an existing network and specify the classification task. 
       The user should be able to construct a data pipeline, be able to download 
       their trained models and test pre-trained models within application.</p>
    </div>

</div>
</template>

<style scoped>
  @import '../../assets/styles/homepage.css';
  img 
  { 
    max-width:10%;
    height:10%;
    /* resizing robot for landing page */
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

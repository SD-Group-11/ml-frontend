<template>
<div>
  <Navbar />

  <div class="is-loading-bar has-text-centered" v-bind:class="{'is-loading': $store.state.isLoading }">
            <div class="lds-dual-ring"></div>
    </div>
  
  <section class="section">
   <transition name="router-anim" enter-active-class="animated fadeInUp" leave-active-class="animated fadeOutUp">
   <router-view/>
   </transition> 
   <!--PAGE ANIMATIONS ADDED HERE -->
   <!-- FOOTER why is it so THICK?!! -->
   <footer class = "footer has-background-info-light mt-6">
     <div class = "container pt-6">
       <div class = "columns">
         <div class = "column has-text-grey-light has-text-centered">
           <p><i>Brought to you by <strong>IllegalSkillsException</strong>.</i></p>
         </div>
       </div>
     </div>
   </footer>

  </section>
</div>
</template>

<script>
  import axios from 'axios'
  import Navbar from '@/components/layout/Navbar'
  

  export default {
    name: "App",
    components: {
      Navbar
    },
    beforeCreate(){
      this.$store.commit('initializeStore')
      if(this.$store.state.token){
        axios.defaults.headers.common['Authorization']="Token " + this.$store.state.token
      }
      else{
        axios.defaults.headers.common['Authorization']=""
      }
    }
}
</script>

<style lang="scss">
@import "../node_modules/bulma/sass/utilities/initial-variables";
@import '../node_modules/bulma';
@import "https://cdn.jsdelivr.net/npm/animate.css@3.5.1"; //animation lib

.lds-dual-ring {
    display: inline-block;
    width: 80px;
    height: 80px;
}
.lds-dual-ring:after {
    content: " ";
    display: block;
    width: 64px;
    height: 64px;
    margin: 8px;
    border-radius: 50%;
    border: 6px solid #ccc;
    border-color: #ccc transparent #ccc transparent;
    animation: lds-dual-ring 1.2s linear infinite;
}
@keyframes lds-dual-ring {
    0% {
        transform: rotate(0deg);
    }
    100% {
        transform: rotate(360deg);
    }
}
.is-loading-bar {
    height: 0;
    overflow: hidden;
    -webkit-transition: all 0.3s;
    transition: all 0.3s;
    
    &.is-loading {
        height: 80px;
    }
}



</style>


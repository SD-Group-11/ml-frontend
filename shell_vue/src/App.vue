<template>
  <div class="page">
    <Navbar/>

    <div class="is-loading-bar has-text-centered" v-bind:class="{'is-loading': $store.state.isLoading }">
      <div class="lds-dual-ring"></div>
    </div>
  
    <section class="page-content">
      <section class="section">
   
        <!-- <transition name="router-anim" enter-active-class="animated fadeInUp" leave-active-class="animated fadeOutUp">
          <router-view/>
        </transition>  -->

        <!-- <transition>
          <router-view/>
        </transition>  -->

        <router-view v-slot="{ Component,route }">
          <!-- <transition name="fade" mode="out-in"> -->
          <transition :name="route.meta.transitionName || 'fade'" mode="out-in">
            <component :is="Component" />
          </transition>
        </router-view>
      
      </section>
    </section>

    <!--PAGE ANIMATIONS ADDED HERE -->
    <!-- FOOTER why is it so THICK?!! -->
    <!-- <footer class = "footer has-background-info-light mt-6">
      <div class = "container pt-6">
        <div class = "columns">
          <div class = "column is-full has-text-grey-light has-text-centered">
            <p><i>Brought to you by <strong>IllegalSkillsException</strong>.</i></p>
          </div>
        </div>
      </div>
    </footer> -->

    <Footer/>

  </div>
</template>

<script>
  import axios from 'axios'
  import Navbar from '@/components/layout/Navbar'
  import Footer from '@/components/layout/Footer'
  

  export default {
    name: "App",
    components: {
      Navbar,
      Footer
    },
    // watch: {
    //   "$route" (to){
    //     document.title = to.meta.title || "MLFE";
    //   }
    // },
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

// change bulma variables variables
@import "../node_modules/bulma/sass/utilities/initial-variables";
  $yellow: #ffde38;
  $warning-light: #ffe60085;
  $blue: #024091;
  $green: #065dff;
  $turquoise: #06b8ff;

//import bulma
@import '../node_modules/bulma';

//import other modules
@import "../node_modules/bulma-responsive-tables/bulma-responsive-tables";
@import '../node_modules/@fortawesome/fontawesome-free';
@import "../node_modules/ag-grid-community/dist/styles/ag-grid.css";
@import "../node_modules/ag-grid-community/dist/styles/ag-theme-alpine.css";
@import "../node_modules/@creativebulma/bulma-tooltip/dist/bulma-tooltip.css";
@import "../node_modules/bulma-o-steps/bulma-steps.css";
// @import "https://cdn.jsdelivr.net/npm/animate.css@3.5.1"; //animation lib

  .page {
    display: flex;
    min-height: 100vh;
    flex-direction: column;
  }
  .page-content {
    flex: 1;
  }

  .fade-enter-active,
  .fade-leave-active {
    transition: opacity 0.5s ease;
  }

  .fade-enter-from,
  .fade-leave-to {
    opacity: 0;
  }

  .slide-left-leave-active,
  .slide-left-enter-active,
  .slide-right-leave-active,
  .slide-right-enter-active {
    transition: 0.4s;
  }

  .slide-left-enter {
    transform: translate(100%, 0);
  }

  .slide-left-leave-to {
    transform: translate(-100%, 0);
  }

  .slide-right-enter {
    transform: translate(-100%, 0);
  }

  .slide-right-leave-to {
    transform: translate(100%, 0);
  }


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


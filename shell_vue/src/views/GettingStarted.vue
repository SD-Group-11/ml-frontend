<template>
    <section class="hero is-light">
      <div class="get-head"></div>
      <div class="get-body">
          <header id="gettingstarted" >
            <h1><strong>Getting Started</strong></h1>
            <p><strong>1. </strong>Select the model you would like to use.</p>
            <p><strong>2. </strong>Upload your data.</p>
            <p><strong>3. </strong>Apply the model.</p>
            <p><strong>4. </strong>Interpret the results.</p>
            <p><strong>5. </strong>Download your results.</p>
          </header>
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
  name: 'GettingStarted',
  components: {
    HelloWorld
  }
}
</script>

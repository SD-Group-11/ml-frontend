<template>
    <section class="hero is-light">
      <div class="hero-head"></div>
      <div class="hero-body">
          <header id="showcase" >
            <h1><strong>Decision Trees</strong></h1>
            <p>Decision trees are commonly used in operations research and operations management. If, in practice, decisions have to be taken online with no recall under incomplete knowledge, a decision tree should be paralleled by a probability model as a best choice model or online selection model algorithm. Another use of decision trees is as a descriptive means for calculating conditional probabilities.

</p>
          </header>
      </div>
	<fieldset id="showcase" class="hero-head">
		<input type="file" name="File Upload" id="txtFileUpload" accept=".csv" />
	</fieldset>
      <div class="hero-foot"></div>
    </section>
</template>

<style scoped>
  @import '../assets/styles/homepage.css';
</style>


<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  components: {
    HelloWorld
  }
}
</script>

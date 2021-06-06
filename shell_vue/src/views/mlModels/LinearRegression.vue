<template>   
    <div class="container">

        <section class="hero" style=" background-color:lightblue">
            <div class="hero-body">
                <h1 class="title is-1 has-text-centered" style=" background-color:lightblue; border-radius:200px"><strong>Linear Regression</strong></h1>
            </div>
        </section>    

        <div class="columns is-multiline is-mobile">

            <div class="column is-full is-warning has-text-centered">
                
                
                <div class="box" style="background-color:lightyellow;">
                    <h2 class="title is-3 has-text-centered">Enter Hyperparameters</h2>
                    
                    <div class="field">
                        <label class="label">Learning Rate hello</label>
                        <div class="control">
                            <input class="input" type="text" placeholder="hello">
                        </div>
                    </div>

                    <div class="field">
                        <label class="label">Tolerance</label>
                        <div class="control">
                            <input class="input" type="email" placeholder="0.5">
                        </div>
                    </div>

                </div>

            </div>
        </div>
    </div>
</template>


<script>
    import axios from 'axios'

    import {toast} from 'bulma-toast'

    export default {
        name: "LinearRegression",
        data() {
            return{

            }
        },
        mounted(){

        },
        methods:{
            
        }
    }
</script>
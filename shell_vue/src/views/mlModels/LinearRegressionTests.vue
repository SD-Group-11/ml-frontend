<template>   
    
    <div class="container is-fluid " >
        <!-- <KeyboardEvents v-on:keyup="keyboardEvent"></KeyboardEvents> -->
        <GlobalEvents
            @keydown.left="pageNav('/linear-regression')"
            @keydown.right="pageNav('/linear-regression-datasets')"
        />

        <div class="container is-fluid">
            <!-- <div class="container is-fluid"> -->
                
                <div class="notification is-info has-text-centered" >
                    
                <div class="columns">
                    <div class="column is-one-fifth">
                        <div class="button is-pulled-left is-medium is-rounded is-warning has-tooltip-warning" @click="$router.push('/linear-regression')" data-tooltip="Train a model">
                            <span class="icon is-normal">
                                <i class="fas fa-lg fa-arrow-left"></i>                                
                            </span>
                        </div>
                    </div>
                    
                    <div class="column">
                        <strong><h3 class="title is-3">Model Testing</h3></strong>
                    </div>
                    
                    <div class="column is-one-fifth">
                        <div class="button is-pulled-right is-medium is-rounded is-warning has-tooltip-warning" @click="$router.push('/linear-regression-datasets')" data-tooltip="Manage datasets">
                            <span class="icon is-normal">
                                <i class="fas fa-lg fa-arrow-right"></i>
                            </span>
                        </div>
                    </div>
                    
                </div>

            </div>
            <div class="block"></div>
        </div>

    </div>
</template>

<style scoped>


</style>


<script>

    import { GlobalEvents } from 'vue-global-events'

    export default {
        name: "LinearRegressionTests",
        data() {},
        components: {
            GlobalEvents
        },
        mounted(){},
        methods:{
            pageNav(route){
                this.$router.push(route)
            }
        }

    }
</script>
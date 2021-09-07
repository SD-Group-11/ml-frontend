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
            
            <form @submit.prevent="submitForm"> <!-- style="background-color:lightyellow;" -->
                <div class="columns">
                    <!-- <div class="column is-pulled-right">
                        <button class="button is-primary has-tooltip-right" style="background-color: #ADD8E6;color: #363636;text-align:left" data-tooltip="Upload Your CSV file here!&#10;1) Click on 'Choose File'&#10;2) Select a .csv file from your local device&#10;3) Click on 'Submit'&#10;4) Wait and let the magic happen!&#10;&#10;Upload a CSV file where the first column is a number (this indicates the row number)&#10;and the last column must be the targets/categories (your 'y' value).">?</button>
                    </div> -->
                    <div class="column">
                        <div class="field">
                            <div class="control">
                                <div class="file has-name is-medium is-warning" >
                                    <label class="file-label">
                                        
                                        <input class="file-input" id="myFile" type="file" accept=".csv"  v-on:input="fileValidation">
                                            
                                            <div class="file-cta">
                                                <div class="file-label" >
                                                    <strong>Choose a file…</strong>
                                                </div>
                                            </div>

                                        <div class="file-name">  
                                            {{uploadedName}}    
                                        </div>

                                    </label>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="column">
                        <div class="field">
                            <div class="control is-pulled-right  ml-3">
                                <!-- <button id = 'uploadFile' v-if="uploadable" type="submit" v-on:click = 'Upload' class="button is-info has-text-black"><strong>Submit</strong></button> -->
                                <button  class="button is-medium  is-info is-outlined " id = 'uploadFile' type="submit" v-if="uploadable" v-on:click = 'Upload'><strong>Upload</strong></button>

                            </div>
                        </div>
                    </div>
                </div>                    

            </form>
        </div>

            <div class="block" > </div>

        <!-- </section> -->

    </div>
</template>

<style scoped>

    
    ::v-deep .modal-container {
        display: flex;
        justify-content: center;
        align-items: center;
    }

    ::v-deep .modal-content {
        position: relative;
        display: flex;
        flex-direction: column;
        max-height: 90%;
        margin: 0 1rem;
        padding: 1rem;
        border: 1px solid #e2e8f0;
        border-radius: 0.25rem;
        background: #fff;
    }

    .modal__title {
        margin: 0 2rem 0 0;
        font-size: 1.5rem;
        font-weight: 700;
    }
    .modal__content {
        flex-grow: 1;
        /* overflow-y: auto;
        overflow-x: auto; */
    }
    .modal__close {
        position: absolute;
        top: 0.5rem;
        right: 0.5rem;
    }

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
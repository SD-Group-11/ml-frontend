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
                    
                    <form>
                    
                    <div class="field">
                        <label class="label">Learning Rate</label>
                        <div class="control">
                            <input class="input" id="learningRate" type="text" placeholder="0.1">
                        </div>
                    </div>

                    <div class="field">
                        <label class="label">Tolerance</label>
                        <div class="control">
                            <input class="input" id = "tol" type="email" placeholder="0.5">
                        </div>
                        
                    </div>

                    

                    <div class="field">
                        <label class="label">Split</label>
                        <div class="control">
                            <input class="input" id="split" type="email" placeholder="Training Split">
                        </div>
                        
                    </div>

                    <div class="control">
                    <div id="v-model-select" class="demo">
                        <select v-model="selected" >
                            <option v-for="dataset in userFiles" v-bind:key="dataset.id">
                                {{dataset.filename}}
                            </option>
                        </select>
                    </div>
                     </div>

                    <div class="control">

                     <button v-on:click='TrainModel'> Okay</button>
                    </div>
            
                    </form>

                </div>

                <template v-if="returned">
                    <section class="section">
                    <div class="container">
                        <div class="image">
                            <img src="@/assets/images/confused-icon-6-yellow.png">
                        </div>    
                    </div>
                </section>

                    <section class="section">
                        <div class="container">
                            <div class="image">
                                <img src="@/assets/images/confused-icon-6-yellow.png">
                            </div>     
                        </div>
                    </section>
                
                </template>
                

            </div>
        </div>
    </div>
</template>


<script>
    import axios from 'axios'

    import {toast} from 'bulma-toast'

    export default {
        name: "LinearRegressionDatasets",
        data() {
            return{
                userDetails: [],
                UserFiles: [],
                uploadedName: '',
                uploadable: false,
                hasDatasets: false,
                userFiles: [],
                returned: false,
            }
        },
        mounted(){
            this.getAccount()
        },
        methods:{
            async getAccount(){
                this.$store.commit('setIsLoading',true)

                await axios
                    .get('/api/v1/users/me')

                    .then(response => {
                        this.userDetails=response.data
                        this.getUserDatasets()
                    })

                    .catch(error => {
                        console.log(error)
                    })

                this.$store.commit('setIsLoading',false)

            },
            async getUserDatasets(){
                this.$store.commit('setIsLoading',true)
                this.userFiles=[] 
                var data ={"UserId":this.userDetails.id}
                await axios
                .post('/datasets/getDatasetsInfo',data)
                
                .then(response =>{
                              
                    if(response.data['error']=="No datasets have been uploaded."){
                        console.log("has no datasets")
                        console.log(response.data)
                        this.hasDatasets = false        
                    }
                    else{
                        console.log("has datasets")
                        //console.log(response.data[0])
                        this.hasDatasets = true
                        //idk why but accessing UserFiles out of this scope returns empty. Please check what im doing wrong
                        // response.data though holds all the datasets of a user and their respective summary details
                        //this.userFiles = response.data;
                        // Tell us how many datasets are associated with the user 
                        // you can loop from 1 to number_of_datasets+1 and use that to index response.data[i] to get a dataset and its summary

                        var number_of_datasets = Object.keys(response.data).length
                        console.log(number_of_datasets)
                        for(var i=1;i<number_of_datasets+1;i++){
                            this.userFiles.push(response.data[i])
                        }
                        console.log(this.userFiles)
                    }
                    
                })
                .catch(error => {
                    console.log(error)
                })

                this.$store.commit('setIsLoading',false)
            },
            // Call this method when the user clicks Train Model 
            async TrainModel(){
                this.returned=false
                var id = this.userDetails.id;
                //Please get the filename from the dropdown and set it here 
                //var filename = "CP.csv";
                // tol and learningRate must be decimal values
                var filename = this.selected
                var tol = document.getElementById("tol").value;
                var learningRate = document.getElementById("learningRate").value;
                // Must be a value between 0 and 100 representing a percentage of data that must be assigned to the training data
                var split = document.getElementById("split").value;
                var data ={"UserId":id,"filename":filename,"learningRate":learningRate,"tol":tol,"split":split}

                console.log('data: ',data)
                await axios
                .post("/datasets/doLinearRegression",data)

                .then(response =>{
                    //Michael will use response.data for his graphing 
                    this.returned=true
                    console.log(response.data)
                });
            }
        }
    }
</script>
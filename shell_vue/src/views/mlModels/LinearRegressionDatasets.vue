<template>   
    <div class="container">

        <section class="hero" style=" background-color:lightblue">
            <div class="hero-body">
                <h1 class="title is-1 has-text-centered" style=" background-color:lightblue; border-radius:200px"><strong>Linear Regression Datasets</strong></h1>
            </div>
        </section>

        <div class="column is-multiline">

            <div class="column">    

                <div class="columns is-multiline is-mobile">
                    
                    <div class="column is-half">
                        
                        <div class="box" style="background-color:lightyellow;" >
                            <form @submit.prevent="submitForm" >
                                
                                <div class="field">
                                    <div class="control">
                                        <div class="file has-name is-medium is-warning" >
                                            <label class="file-label">
                                                
                                                <input class="file-input" id="myFile" type="file" accept=".csv"  v-on:input="fileValidation">
                                                    
                                                    <div class="file-cta">
                                                        <div class="file-label" >
                                                            Choose a file…
                                                        </div>
                                                    </div>

                                                <div class="file-name">  
                                                    {{uploadedName}}    
                                                </div>

                                            </label>
                                        </div>
                                    </div>
                                </div>

                                <div class="field">
                                    <div class="control">
                                        <button id = 'uploadFile' v-if="uploadable" type="submit" v-on:click = 'Upload' class="button is-info has-text-black"><strong>Submit</strong></button>
                                    </div>
                                </div>

                            </form>
                        </div>

                    </div>
                
                    <div class="column is-half">
                        
                        <div class="box" style="background-color:lightyellow;" >
                            <h2 class="title is-3">Uploaded data</h2>
                            <p id="data" ref="para"> Metadata will appear here
                            </p>
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
        name: "LinearRegressionDatasets",
        data() {
            return{
                userDetails: [],
                UserFiles: [],
                uploadedName: '',
                uploadable: false,
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
                        console.log(response)
                        var id=  this.userDetails.id;
                        var data ={"UserId":id}
                         axios
                        .post('/datasets/getDatasetsInfo',data)
                        
                        .then(response =>{
                           //idk why but accessing UserFiles out of this scope returns empty. Please check what im doing wrong
                           // response.data though holds all the datasets of a user and their respective summary details
                            this.UserFiles = response.data;
                            // Tell us how many datasets are associated with the user 
                            // you can loop from 1 to number_of_datasets+1 and use that to index response.data[i] to get a dataset and its summary
                            var number_of_datasets = Object.keys(response.data).length

                            for(var i=1;i<number_of_datasets+1;i++){
                                
                                console.log(response.data[i])
                                //Do whatever with each dataset
                                //reponse.data[i].anything below will give you it's value
                                //filename gives filename
                                //datapoints gives number of datapoints
                                //columns give number of columns
                                //featureNames gives an array of all the features 
                                //nullValues gives how many nulls in the dataset
                                
                            }
                            
                        });
                       
                        })

                    .catch(error => {
                        console.log(error)
                    })

                this.$store.commit('setIsLoading',false)

            },
            async Upload(){
                this.$store.commit('setIsLoading',true)
                var file = document.getElementById("myFile").files[0];
                var formData = new FormData();
                formData.append("dataset",file);
                formData.append("id",this.userDetails.id);
                await axios
                    .post('/datasets/uploadData',formData)

                    .then(response => {
                        var resp =  response.data['response'];
                        var Type;
                        if (resp == 'Data Uploaded Successfully'){
                            Type = 'is-warning';
                            this.uploaded=true;
                            var filename = file.name;
                            var id=  this.userDetails.id;
                            var data ={"id":id,"filename":filename}

                        }
                        else{
                            this.uploaded=false;
                            Type = 'is-danger';
                        }
                        toast({
                            message: resp,
                            type: Type,
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-center',
                        })
                    });

                 this.$store.commit('setIsLoading',false)
            },
            //This method will get the actual data of a dataset once it's selected from the dropdown list
            async GetDatasetData(){
                
                var id =  this.userDetails.id;
                //Please fill in the file name that will be sent once they have selected in from the dropdown
                var filename ;
                var data = {'UserId':id,"filename":filename}
                await axios
                .post("/datasets/getDatasetData",data)

                .then(response => {
                    //Store the response and use it to get converted into a csv file for download
                    // First implement a check that the response is not "error: Failed to load dataset. Please try again"
                    // That will happen if the backend fails to load the data of the selected file. 
                    console.log(response.data)
                })

            },
            async fileValidation(){
                this.$store.commit('setIsLoading',true)
                
                this.uploadable=false

                var fileInput = document.getElementById("myFile").files[0];
                var fileName = fileInput.name;

                const allowedExtensions =  ['csv']

                const fileExtension = fileName.split(".").pop();

                if(!allowedExtensions.includes(fileExtension)){
                    toast({
                            message: 'Please upload a .csv file',
                            type: 'is-danger',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-center',
                        })
                    fileInput.value = '';
                    this.uploadedName = '';
                    this.uploadable = false;
                    this.$store.commit('setIsLoading',false)
                    return false;
                }
                else{
                    toast({
                            message: 'File ready for upload',
                            type: 'is-warning',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-center',
                        })
                    
                    this.uploadedName = fileInput.name;
                    this.uploadable = true;
                    this.$store.commit('setIsLoading',false)
                    return true;
                }         
            }
        }
    }
</script>
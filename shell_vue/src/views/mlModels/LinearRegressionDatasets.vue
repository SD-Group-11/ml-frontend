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

                    <div class="column is-half is-multiline">
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
                            <div class="column">
                                <button class="button is-primary has-tooltip-left has-tooltip-multiline" style="background-color: #ADD8E6;color: #363636" data-tooltip="Tooltip with a long Text. So we use has-tooltip-multiline modifier to force multiline display.">?</button>
                            </div>    

  
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
    import {tooltip} from 'bulma-tooltip'

    

    export default {
        name: "LinearRegressionDatasets",
        components: {
            tooltip
        },
        data() {
            return{
                userDetails: [],
                SummaryData: [],
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
                formData.append("id",this.details.id);
                console.log(this.details.id);
                await axios
                    .post('/datasets/uploadData',formData)

                    .then(response => {
                        var resp =  response.data['response'];
                        var Type;
                        if (resp == 'Data Uploaded Successfully'){
                            Type = 'is-warning';
                            this.uploaded=true;
                            var filename = file.name;
                            var id=  this.details.id;
                            var data ={"id":id,"filename":filename}

                            axios
                            .post('/datasets/dataSummary',data)
                            
                            .then(response =>{
                                this.SummaryData = response.data;
                                this.$refs.para.innerText="File Name:"+ this.SummaryData.filename +"\nNumber of data points:"+this.SummaryData.datapoints+" \nNumber of Columns:"+this.SummaryData.columns;
                            });
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

            async Summary(){
                this.$store.commit('setIsLoading',true)
                
                var file = document.getElementById("myFile").files[0];
                var filename = file.name;
                var id=  this.details.id;
                var data ={"id":id,"filename":filename}
                await axios
                .post('/datasets/dataSummary',data)
                
                .then(response =>{
                    this.SummaryData = response.data;

                });
                console.log(this.SummaryData);
                this.$store.commit('setIsLoading',false)
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
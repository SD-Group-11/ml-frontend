<template>   
    <div class="container">

        <section class="hero" style=" background-color:lightblue">
            <div class="hero-body">
                <h1 class="title is-1 has-text-centered" style=" background-color:lightblue; border-radius:200px"><strong>Linear Regression Datasets</strong></h1>
            </div>
        </section>

        <section class="section">
            <div class="container">
                <div class="column is-multiline">
                <div class="column">    
                <div class="columns is-multiline is-mobile">
                    <div class="column is-half is-multiline">
                        <div class="box" style="background-color:lightyellow;" >
                            <div class="column is-pulled-right">
                                <button class="button is-primary has-tooltip-left" style="background-color: #ADD8E6;color: #363636;text-align:left" data-tooltip="Upload Your CSV file here!&#10;1) Click on 'Choose File'&#10;2) Select a .csv file from your local device&#10;3) Click on 'Submit'&#10;4) Wait and let the magic happen!&#10;&#10;Upload a CSV file where the first column is No (this indicates the row number)&#10;and the last column must be the targets/categories.">?</button>
                            </div>   
                            <form @submit.prevent="submitForm" >
                                
                                <div class="column">
                                    <div class="field">
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
                                    <h2 class="title is-3">Uploaded data {{hasDatasets ? "✔️" : "🗅"}}</h2>
                                    <p id="data" ref="para" v-if=" !userFiles ">
                                            Metadata will appear here.
                                    </p>
                                    <p id="data" ref="para" v-if=" userFiles ">
                                        <ul>
                                            <li v-for='file in userFiles' v-bind:key=" file " >
                                                <h3><b>{{file.filename}}</b></h3>
                                                Datapoints: {{file.datapoints}}<br/>
                                                Columns: {{file.columns}}<br/>
                                                Feature Names: {{file.featureNames.join(", ")}}<br/>
                                                Null Values: {{file.nullValues}}<br/>
                                                <br/>
                                                <br/>
                                            </li>
                                        </ul>
                                    </p>
                                </div>

                            </div>
                        </div>
                        
                    </div>
                </div>
            </div>
        </section>


        <section class="hero is-light">
            <div class="hero-body">
                <div class="container">
                    <h1 class="title">Expandable Bulma table rows CSS & HTML</h1>
                    <h3 class="subtitle">Check desktop & mobile layout</h3>
                </div>
            </div>
        </section>

        <section class="section">
            <div class="container">
                <div class="b-table">
                <div class="table-wrapper has-mobile-cards">
                    <table class="table is-fullwidth is-hoverable is-fullwidth">
                    <thead>
                        <tr>
                            <th class="is-chevron-cell"></th>
                            <th></th>
                            <th>Name</th>
                            <th>Created</th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>
                    <tr>
                        <td class="is-chevron-cell">
                            <a role="button">
                                <span class="icon is-expanded"><i class="fas fa-angle-right"></i></span>
                            </a>
                        </td>
                        <td class="is-image-cell">
                            <div class="image">
                                <!-- <img src="@/assets/images/confused-icon-6-yellow.png"> -->
                            </div>
                        </td>
                        <td data-label="Name">Rebecca Bauch</td>
                        <td data-label="Created">
                            <small class="has-text-grey is-abbr-like" title="Oct 25, 2020">Oct 25, 2020</small>
                        </td>
                        <td class="is-actions-cell">
                            <div class="buttons is-right">
                                <button class="button is-small is-primary" type="button">
                                    <span class="icon"><i class="mdi mdi-eye"></i></span>
                                </button>
                                <button class="button is-small is-danger jb-modal" data-target="sample-modal" type="button">
                                    <span class="icon"><i class="mdi mdi-trash-can"></i></span>
                                </button>
                            </div>
                        </td>
                    </tr>
                    <tr class="detail">
                        <td colspan="8">
                        <div class="detail-container">
                            <article class="media">
                            <figure class="media-left">
                                <div class="image is-64x64">
                                    <!-- <img src="@/assets/images/csv-icon/128x128.png"> -->
                                </div>
                            </figure>
                            <div class="media-content">
                                <div class="content">
                                <p><strong>Rebecca Bauch</strong> <small>@rbauch</small> <small>1d</small><br>
                                    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                                    Proin ornare magna eros, eu pellentesque tortor vestibulum ut.
                                    Maecenas non massa sem. Etiam finibus odio quis feugiat facilisis.
                                </p>
                                </div>
                            </div>
                            </article>
                        </div>
                        </td>
                    </tr>
                    </tbody>
                    </table>
                </div>
                </div>
            </div>
        </section>

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
                datasetDetails: [],
                uploadedFilename: '',
                hasDatasets: false,
                userFiles: ''
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

                var data ={"UserId":this.userDetails.id}
                await axios
                .post('/datasets/getDatasetsInfo',data)
                .then(response =>{

                    if(response.data['error']=="No datasets have been uploaded."){
                        console.log(response.data)
                        this.hasDatasets = false
                    }
                    else{
                        this.hasDatasets = true
                        //idk why but accessing UserFiles out of this scope returns empty. Please check what im doing wrong
                        // response.data though holds all the datasets of a user and their respective summary details
                        this.userFiles = response.data;
                        // Tell us how many datasets are associated with the user 
                        // you can loop from 1 to number_of_datasets+1 and use that to index response.data[i] to get a dataset and its summary

                        var number_of_datasets = Object.keys(this.userFiles).length
                        for(var i=1;i<number_of_datasets+1;i++){
                            console.log(this.userFiles[i])
                            //Do whatever with each dataset
                            //reponse.data[i].anything below will give you it's value
                            //filename gives filename
                            //datapoints gives number of datapoints
                            //columns give number of columns
                            //featureNames gives an array of all the features 
                            //nullValues gives how many nulls in the dataset
                        }
                    }

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
                            this.getUserDatasets()

                             
                            this.uploadedFilename = `"${file.name}"`;
                            console.log(this.uploadedFilename);
                            console.log(this.userFiles);
                            

                            // var data = {'UserId':this.userDetails.id,"filename":this.uploadedFilename}
                            // axios
                            // .post("/datasets/getDatasetData",data)
                            // .then(response => {
                            //     //Store the response and use it to get converted into a csv file for download
                            //     // First implement a check that the response is not "error: Failed to load dataset. Please try again"
                            //     // That will happen if the backend fails to load the data of the selected file. 
                            //     console.log(response.data)
                            // })  
                              
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
                console.log(this.userDetails.id)
                console.log('poo')
                console.log(this.uploadedFilename)
                var id =  this.userDetails.id;
                //Please fill in the file name that will be sent once they have selected in from the dropdown
                var filename ;
                //var data = {'UserId':id,"filename":filename}
                var data = {'UserId':id,"filename":this.uploadedFilename}
                await axios
                .post("/datasets/getDatasetData",data)

                .then(response => {
                    //Store the response and use it to get converted into a csv file for download
                    // First implement a check that the response is not "error: Failed to load dataset. Please try again"
                    // That will happen if the backend fails to load the data of the selected file. 
                    console.log(response.data)
                })
                console.log(this.userFiles);

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
            },
            // async Summary(){
            //     this.$store.commit('setIsLoading',true)
                
            //     var file = document.getElementById("myFile").files[0];
            //     var filename = file.name;
            //     var id=  this.details.id;
            //     var data ={"id":id,"filename":filename}
            //     await axios
            //     .post('/datasets/dataSummary',data)
                
            //     .then(response =>{
            //         this.SummaryData = response.data;

            //     });
            //     console.log(this.SummaryData);
            //     this.$store.commit('setIsLoading',false)
            // },

        }
    }
</script>
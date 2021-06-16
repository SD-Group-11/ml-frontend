<template>   
    <div class="container">

        <section class="hero" style=" background-color:lightblue">
            <div class="hero-body">
                <h1 class="title is-1 has-text-centered" style=" background-color:lightblue; border-radius:200px"><strong>Upload New Dataset</strong></h1>
            </div>
        </section>

        <section class="section">
            <div class="container">
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


        <section class="hero" style=" background-color:lightblue">
            <div class="hero-body">
                <h1 class="title is-1 has-text-centered" style=" background-color:lightblue; border-radius:200px"><strong>Uploaded Datasets</strong></h1>
            </div>
        </section>

        <section class="section">
            <div class="container">
                <div class="b-table">
                <div class="table-wrapper has-mobile-cards">
                    <table class="table is-fullwidth is-hoverable is-fullwidth">
                    <thead>
                        <tr>
                            <!-- <th class="is-chevron-cell"></th> -->
                            <th></th>
                            <th>Name</th>
                            <th>No. Datapoints</th>
                            <!-- <th>Features</th> -->
                            <th>No. Features</th>
                            <th>Null Values</th>
                            <th>Date Created</th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>
                        
                        <tr v-for="dataset in userFiles" v-bind:key="dataset.id">
                            <!-- <td class="is-chevron-cell">
                                <a role="button">
                                    <span class="icon is-expanded"><i class="fas fa-angle-right"></i></span>
                                </a>
                            </td> -->

                            <td class="is-image-cell">
                                <div class="image">
                                    <img src="@/assets/images/confused-icon-6-yellow.png">
                                </div>
                            </td>

                            <td data-label="Name">{{dataset.filename}}</td>

                            <td data-label="No. Datapoints">{{dataset.datapoints}}</td>
  
                            <td data-label="No. Features">{{dataset.columns-1}}</td>

                            <td data-label="Null Values">{{dataset.nullValues}}</td>

                            <td data-label="Null Values">{{dataset.created}}</td>

                            <td class="is-actions-cell">                       
                                <!-- <div class="buttons"> -->
                                <div class="field has-addons">
                                    
                                    <p class="control">
                                        <button class="button is-normal is-primary" type="button" @click="showReportModal = true">
                                    
                                        
                                            <span class="icon is-normal">
                                                <!-- <i class="fas fa-brain"></i> -->
                                                <i class="fas fa-lg fa-file-medical-alt"></i>
                                            </span>

                                            <!-- <span><strong>View Model Report</strong></span> -->
                                            <!-- <span>Model</span> -->

                                        </button>
                                    </p>

                                    <p class="control">
                                        <button class="button is-normal is-info is-inverted" type="button" v-on:click ="getData(dataset.filename)">
                                    
                                        
                                            <span class="icon is-normal">
                                                <i class="far fa-lg fa-eye"></i>
                                            </span>

                                            <!-- <span><strong>View Dataset</strong></span> -->
                                            <!-- <span>Data</span> -->

                                        </button>
                                    </p>

                                    <p class="control">
                                        <button class="button is-normal is-link" type="button" v-on:click ="getDatasetData(dataset.filename)">
                                        
                                            <span class="icon is-normal">
                                                <i class="fas fa-lg fa-file-download"></i>
                                            </span>

                                            <!-- <span><strong>Download</strong></span> -->
                                            <!-- <span>Download</span> -->

                                        </button>
                                    </p>

                                </div>
                                    
                                
                            </td>

                            
                        </tr>
                    
                    </tbody>
                    </table>
                </div>
                </div>

                <vue-final-modal v-model="showReportModal" classes="modal-container" content-class="modal-content">

                    <span class="modal__title">
                        Model Report
                         <button class="delete is-pulled-right" @click="showReportModal = false"></button>
                    </span>

                    <div class="modal__content">
                        <p>
                            {{}}
                        </p>
                    </div>

                </vue-final-modal>
              
  
                <vue-final-modal
                    v-model="showDatasetModal"
                    v-if="showDatasetModal"
                    classes="modal-container"
                    content-class="modal-content"
                    :drag="true"
                >

                    <div class="modal__title">
                        Dataset
                        <button class="delete is-pulled-right" @click="showDatasetModal = false"></button>

                    </div>
                    <div class="modal__content">

                        <ag-grid-vue
                            style="width: 600px; height: 400px;"
                            class="ag-theme-alpine"
                            :columnDefs="columnDefs"
                            :rowData="rowData"
                            rowSelection="multiple">
                            
                        </ag-grid-vue>
                    </div>

                </vue-final-modal>

            </div>
        </section>

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
    import axios from 'axios'

    import {toast} from 'bulma-toast'

    import { AgGridVue } from "ag-grid-vue3"

    export default {
        name: "LinearRegressionDatasets",
        data() {
            return{
                userDetails: [],
                SummaryData: [],
                uploadedName: '',
                uploadable: false,
                datasetDetails: [],
                uploadedFilename: '',
                hasDatasets: false,
                userFiles: [],
                showReportModal: false,
                showDatasetModal: false,
                showModal: false,
                columnDefs: [],
                rowData: [],
            }
        },
        components: {
            AgGridVue
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
                        this.hasDatasets = true
                        //idk why but accessing UserFiles out of this scope returns empty. Please check what im doing wrong
                        // response.data though holds all the datasets of a user and their respective summary details
                        // Tell us how many datasets are associated with the user 
                        // you can loop from 1 to number_of_datasets+1 and use that to index response.data[i] to get a dataset and its summary

                        var number_of_datasets = Object.keys(response.data).length
                        for(var i=1;i<number_of_datasets+1;i++){
                            //Do whatever with each dataset
                            //reponse.data[i].anything below will give you it's value
                            //filename gives filename
                            //datapoints gives number of datapoints
                            //columns give number of columns
                            //featureNames gives an array of all the features 
                            //nullValues gives how many nulls in the dataset
                            this.userFiles.push(response.data[i])
                            
                        }
                        console.log(this.userFiles[0].filename)
                        console.log(this.userFiles)
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
                            this.uploadedFilename = `"${file.name}"`
                              
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
            async getDatasetData(filename){
                console.log(filename)
                console.log(this.userDetails.id)
                const id =  this.userDetails.id
                const data = {'UserId':id,"filename":filename}
                await axios
                .post("/datasets/getDatasetData",data)
                //Store the response and use it to get converted into a csv file for download
                // First implement a check that the response is not "error: Failed to load dataset. Please try again"
                // That will happen if the backend fails to load the data of the selected file.
                .then(response => {
                    if(response.data['error']=="Failed to load dataset. Please try again"){
                        console.log(response.data)
                    }
                    else{
                        const parsedJson = response.data.data
                        console.log(parsedJson)
                        const heading = Object.keys(parsedJson[0]).join(",")
                        const body = parsedJson.map((j) => Object.values(j).join(",")).join("\n")
                        const csv = `${heading}\n${body}`
                        
                        const MLFEF = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
                        
                        if (navigator.msSaveBlob) { // IE 10+
                            navigator.msSaveBlob(MLFEF, filename)
                        }
                        else {
                            const link = document.createElement("a")
                            
                            if (link.download !== undefined) { // feature detection
                                // Browsers that support HTML5 download attribute
                                const url = URL.createObjectURL(MLFEF)
                                link.setAttribute("href", url)
                                link.setAttribute("download", filename)
                                link.style.visibility = 'hidden'
                                document.body.appendChild(link)
                                link.click()
                                document.body.removeChild(link)
                            }
                        }

                        //console.log(keys)
                    } 
                })

            },
            async getData(filename){
                const id =  this.userDetails.id
                const data = {'UserId':id,"filename":filename}
                await axios
                .post("/datasets/getDatasetData",data)
                .then(response => {
                    if(response.data['error']=="Failed to load dataset. Please try again"){
                        console.log(response.data)
                    }
                    else{
                        this.columnDefs=[]
                        this.rowData=[]
                        const tableData = response.data.data
                        const tableHeadings = Object.keys(tableData[0])
                        console.log(tableHeadings)
                        for(var i=0;i<tableHeadings.length;i++){
                           this.columnDefs.push({ field: tableHeadings[i], sortable: true, filter: true })  
                        }
                        console.log(this.columnDefs)
                        this.rowData=tableData
                        console.log(this.rowData)
                        this.showDatasetModal = true
                    } 
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
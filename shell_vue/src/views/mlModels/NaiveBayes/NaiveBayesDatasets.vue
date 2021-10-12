<template>   
    <div class="container is-fluid">

        <GlobalEvents
            @keydown.left="pageNav('/naive-bayes-tests')"
            @keydown.right="pageNav('/naive-bayes-training')"
        />

        <div class="container is-fluid">
            <!-- <div class="container is-fluid"> -->
                
                <div class="notification is-info has-text-centered" >
                    
                <div class="columns">
                    <div class="column is-one-fifth">
                        <div class="button is-pulled-left is-medium is-rounded is-warning has-tooltip-warning" @click="$router.push('/naive-bayes-tests')" data-tooltip="Test a model">
                            <span class="icon is-normal">
                                <i class="fas fa-lg fa-arrow-left"></i>                                
                            </span>
                        </div>
                    </div>
                    
                    <div class="column is-three-fifths">
                        <strong><h3 class="title is-3">Datasets</h3></strong>
                    </div>
                    
                    <div class="column is-one-fifth">
                        <div class="button is-pulled-right is-medium is-rounded is-warning has-tooltip-warning" @click="$router.push('/naive-bayes-training')" data-tooltip="Train a model">
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
                                        <form id="trainForm">
                                            <input class="file-input" id="myFile" type="file" accept=".csv"  v-on:input="fileValidation('myFile')">
                                        </form>
                                        
                                            
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
                                <button  class="button is-medium  is-info is-outlined " id = 'uploadFile' type="submit" v-if="uploadable && !testsetUploadable && uploadedName != ''" v-on:click = 'Upload'><strong>Upload</strong></button>
                                <button  class="button is-medium  is-info is-outlined " id = 'uploadFile' type="submit" v-if="uploadable && testsetUploadable && uploadedName != ''" v-on:click = 'uploadTestDataset(tempTrainFilename)'><strong>Upload</strong></button>
                            </div>
                        </div>
                    </div>
                </div>                    

            </form>
        </div>

            <div class="block" > </div>

            <div class="container">
                <div class="b-table">
                <div class="table-wrapper has-mobile-cards">
                    <table class="table is-fullwidth is-hoverable is-fullwidth">
                    <thead>
                        <tr>
                            <th></th>
                            <th>Name</th>
                            <th>Datapoints</th>
                            <th>Features</th>
                            <th>Null Values</th>
                            <th>Date Created</th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>
                        
                        <tr v-for="dataset in userFiles" v-bind:key="dataset.id">

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
                                    
                                    <p class="control px-1">
                                        <template v-if="dataset.Info">
                
                                            <!-- <button class="button is-normal is-primary has-tooltip-arrow has-tooltip-info" data-tooltip="View trained model report" type="button" @click="showNoReportModal = true">
                                        
                                            
                                                <span class="icon is-normal">
                                                    <i class="fas fa-lg fa-file-medical-alt"></i>
                                                </span>


                                            </button> -->
                                        </template>
                                        <!-- <template v-else>
                                            <button class="button is-normal is-primary has-tooltip-arrow has-tooltip-info" data-tooltip="View trained model report" type="button" v-on:click ="getReport(dataset.MSE, dataset.TrainAccuracy, dataset.TestAccuracy)">
                                        
                                                <span class="icon is-normal">
                                                    <i class="fas fa-lg fa-file-medical-alt"></i>
                                                </span>


                                            </button>
                                        </template> -->
                                    </p>


                                    <p class="control px-1">
                                        <button class="button is-normal is-info is-inverted has-tooltip-arrow has-tooltip-info" data-tooltip="View dataset" type="button" v-on:click ="getData(dataset.filename)">
                                    
                                        
                                            <span class="icon is-normal">
                                                <i class="far fa-lg fa-eye"></i>
                                            </span>

                                            <!-- <span><strong>View Dataset</strong></span> -->
                                            <!-- <span>Data</span> -->

                                        </button>
                                    </p>


                                    <p class="control px-1">
                                        <button class="button is-normal is-link has-tooltip-arrow has-tooltip-info" data-tooltip="Download dataset" type="button" v-on:click ="getDatasetData(dataset.filename)">
                                            
                                            <span class="icon is-normal">
                                                <i class="fas fa-lg fa-file-download"></i>
                                            </span>
                                            

                                            <!-- <span><strong>Download</strong></span> -->
                                            <!-- <span>Download</span> -->

                                        </button>
                                    </p>

                                    <p class="control px-1">
                                        <button class="button is-normal is-danger is-dark has-tooltip-arrow has-tooltip-info" data-tooltip="Delete dataset" type="button" v-on:click ="DeleteDataset(dataset.filename)">
                                            
                                            <span class="icon is-normal ">
                                                <i class="fas fa-trash-alt " style="color: #ff9999"></i>
                                            </span>
                                            

                                            <!-- <span><strong>Download</strong></span> -->
                                            <!-- <span>Download</span> -->

                                        </button>
                                    </p>

                                    <p class="control px-1">
                                        
                                        <button class="button is-normal is-inverse has-tooltip-arrow has-tooltip-info" data-tooltip="Add test dataset" type="button" v-on:click ="inputTestset = true; tempTrainFilename = dataset.filename;">
                                        
                                            <input class="file-input" v-bind:id="dataset.filename" type="file" accept=".csv" v-if="inputTestset"  v-on:input="fileValidation(dataset.filename); testsetUploadable = true;">
                                            
                                            <span class="icon is-normal">
                                                <i class="fas fa-upload"></i>
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

                
                <vue-final-modal v-model="showUploadedModal" classes="modal-container" content-class="modal-content">
                    
                    <span class="modal__title">
                        Dataset Uploaded Successfully 
                        {{uploaded ? "✔️" : "🗅"}}
                        <button class="delete is-pulled-right" @click="showUploadedModal = false"></button>
                    </span>

                    <div class="modal__content">
                        <div class="box" style="background-color:lightyellow;" >
                            <p id="data" ref="para" v-if=" uploadedSummary ">
                                <ul>
                                    <li v-for='file in uploadedSummary' v-bind:key=" file " >
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

                </vue-final-modal>
                
                <vue-final-modal v-model="showReportModal" classes="modal-container" content-class="modal-content">

                    <span class="modal__title">
                        Model Report
                        <button class="delete is-pulled-right" @click="showReportModal = false"></button>
                    </span>

                    <div class="modal__content">
                        <div class="container mt-3">
                            <div class="notification is-info">
                                <strong>Mean Squared Error: </strong> {{datasetReport.MSE}}
                            </div>
                            <div class="notification is-info">
                                <strong>Training Accuracy: </strong> {{datasetReport.TrainAccuracy}}
                            </div>
                            <div class="notification is-info">
                                <strong>Testing Accuracy: </strong> {{datasetReport.TestAccuracy}}
                            </div>
                        </div>
                        
                    </div>

                </vue-final-modal>

                <vue-final-modal v-model="showNoReportModal" classes="modal-container" content-class="modal-content">

                    <span class="modal__title">
                        No model trained for dataset 
                        <button class="delete is-pulled-right" @click="showNoReportModal = false"></button>
                    </span>

                    <!-- <div class="modal__content">
                        <p>
                            {{}}
                        </p>
                    </div> -->

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
    import axios from 'axios'
    import {toast} from 'bulma-toast'
    import { AgGridVue } from "ag-grid-vue3"
    import { GlobalEvents } from 'vue-global-events'

    export default {
        name: "NaiveBayesDatasets",

        data() {
            return{
                userDetails: [],
                uploadedFilename: '',
                uploadedTestFilename: '',
                uploadedSummary: [],
                uploadable: false,
                uploaded: false,
                uploadedTestData: false,
                showUploadedModal: false,
                inputTestset: false,
                testsetUploadable: false,
                tempTrainFilename: '',
                
                hasDatasets: false,
                userFiles: [],
                showReportModal: false,
                showNoReportModal: false,
                datasetReport: {
                    MSE: "",
                    TrainAccuracy: "",
                    TestAccuracy: ""
                },
                columnDefs: [],
                rowData: [],
                showDatasetModal: false,
            }
        },
        components: {
            AgGridVue,
            GlobalEvents
        },
        mounted(){
            this.getAccount()
        },
        methods:{
            pageNav(route){
                this.$router.push(route)
            },
            async getAccount(){
                this.$store.commit('setIsLoading',true)
                this.userDetails=[]
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
                .post('/NaiveBayes/getDatasetsInfo',data)
                .then(response =>{
                              
                    if(response.data['error']=="No datasets have been uploaded."){
                        this.hasDatasets = false 
                        console.log(response.data)       
                    }
                    else{
                        this.hasDatasets = true
                        var number_of_datasets = Object.keys(response.data).length
                        for(var i=1;i<number_of_datasets+1;i++){
                            //filename gives filename
                            //datapoints gives number of datapoints
                            //columns give number of columns
                            //featureNames gives an array of all the features 
                            //nullValues gives how many nulls in the dataset
                            var dateTime = response.data[i].created.replace("T"," ").split(".")[0].slice(0,-3)
                            response.data[i].created=dateTime
                            
                            this.userFiles.push(response.data[i])                  
                        }
                    }  
                })
                .catch(error => {
                    console.log(error)
                })
                this.$store.commit('setIsLoading',false)
            },
            async Upload(){
                this.uploaded=false;
                this.$store.commit('setIsLoading',true)
                var file = document.getElementById("myFile").files[0];
                

                var formData = new FormData();
                formData.append("dataset",file);
                formData.append("id",this.userDetails.id);
                formData.append("model","Naive Bayes");
                await axios
                    .post('/datasets/uploadData',formData)
                    .then(response => {
                        var resp =  response.data['response'];
                        var Type;
                        if (resp == 'Data Uploaded Successfully'){
                            Type = 'is-warning';
                            this.uploaded=true;
                            this.uploadedFilename = `${file.name}`
                            this.getUploaded(this.uploadedFilename) 
                            this.getUserDatasets() 
                        }
                        else{
                            this.uploaded=false;
                            Type = 'is-danger';
                            toast({
                                message: resp,
                                type: Type,
                                dismissible: true,
                                pauseOnHover: true,
                                duration: 1000,
                                position: 'bottom-center',
                            })  
                        }
                    });
                this.uploadedName = '';
                this.$store.commit('setIsLoading',false)
            },

            async uploadTestDataset(trainsetFilename){
                console.log('trainsetFilename',trainsetFilename)
                this.uploadedTestData=false;
                this.$store.commit('setIsLoading',true)
                var testFile = document.getElementById(trainsetFilename).files[0];
                var testFormData = new FormData();
                testFormData.append("dataset",testFile);
                testFormData.append("id",this.userDetails.id);
                testFormData.append("TrainingFileName", trainsetFilename);
                testFormData.append("model","Naive Bayes");
                await axios
                    .post('/datasets/uploadTestData',testFormData)
                    .then(response => {
                        var resp =  response.data['response'];
                        
                        var Type;
                        if (resp == 'Successfully uploaded test data.'){
                            Type = 'is-success';
                            this.uploadedTestData=true;
                            //this.uploadedTestFilename = `${testFile.name}`
                            // Not sure if the next two lines are necesssary just yet
                            // this.getUploaded(this.uploadedTestFilename) 
                            // this.getUserDatasets() 
                            toast({
                                message: resp,
                                type: Type,
                                dismissible: true,
                                pauseOnHover: true,
                                duration: 1000,
                                position: 'bottom-center',
                            }) 
                        }
                        else{
                            this.uploadedTestData =false;
                            Type = 'is-danger';
                            toast({
                                message: resp,
                                type: Type,
                                dismissible: true,
                                pauseOnHover: true,
                                duration: 1000,
                                position: 'bottom-center',
                            })  
                        }
                    });
                    this.uploadedName = '';
                this.testsetUploadable = false;
                this.$store.commit('setIsLoading',false)
            },

            async getUploaded(filename){
                this.showUploadedModal=false
                this.$store.commit('setIsLoading',true)
                this.uploadedSummary = []
                var id ={"UserId":this.userDetails.id}
                await axios
                .post('/NaiveBayes/getDatasetsInfo',id)
                .then(response =>{
                    var number_of_datasets = Object.keys(response.data).length
                    for(var i=1;i<number_of_datasets+1;i++){
                        if(response.data[i].filename==filename){
                            this.uploadedSummary.push(response.data[i])
                            this.showUploadedModal=true
                        }
                    }                    
                })
                .catch(error => {
                    console.log(error)
                })
                this.$store.commit('setIsLoading',false)
            },
            //This method will get the actual data of a dataset once it's selected from the dropdown list
            async getDatasetData(filename){
                this.$store.commit('setIsLoading',true)
                console.log(filename)
                console.log(this.userDetails.id);
                const id =  this.userDetails.id;
                const model = "Naive Bayes";
                const data = {'UserId':id,"filename":filename,"ModelName":model};
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
                        
                        if (navigator.msSaveBlob) {a
                            navigator.msSaveBlob(MLFEF, filename)
                        }
                        else {
                            const link = document.createElement("a")
                            
                            if (link.download !== undefined) {
                                const url = URL.createObjectURL(MLFEF)
                                link.setAttribute("href", url)
                                link.setAttribute("download", filename)
                                link.style.visibility = 'hidden'
                                document.body.appendChild(link)
                                link.click()
                                document.body.removeChild(link)
                            }
                        }
                    } 
                })
                this.$store.commit('setIsLoading',false)
            },
            async getData(filename){
                this.$store.commit('setIsLoading',true)
                const id =  this.userDetails.id
                const model = "Naive Bayes";
                const data = {'UserId':id,"filename":filename,"ModelName":model}
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
                this.$store.commit('setIsLoading',false)
            },
            async getReport(mse,trainAccuracy,testAccuracy){
                this.$store.commit('setIsLoading',true)
                
                this.datasetReport.MSE = mse
                this.datasetReport.TrainAccuracy = trainAccuracy
                this.datasetReport.TestAccuracy = testAccuracy
                this.showReportModal = true
                this.$store.commit('setIsLoading',false)
            },

            // elementID is the name of the html element which chooses the file to be validated
            async fileValidation(elementID){
                
                try {
                    this.$store.commit('setIsLoading',true)
                    this.uploadable=false    
                    var fileInput = document.getElementById(elementID).files[0];
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
                }catch {
                    //Nothing should happen
                    this.$store.commit('setIsLoading',false)
                }
                
            },

            async DeleteDataset(filename){
                    this.$store.commit('setIsLoading',true)
                    console.log(filename)
                    console.log(this.userDetails.id)
                    const id =  this.userDetails.id
                    const model = "Naive Bayes"
                    const data = {'UserID':id,"Filename":filename,"ModelName":model}
                    await axios
                    .post("/NaiveBayes/deleteDataset",data)
                    .then(response => {
                        var resp
                        try {
                            resp = response.data['success']

                            var Type = 'is-warning';
                            this.uploadedTestData=true;
                           
                            this.getUserDatasets() 
                            toast({
                                message: resp,
                                type: Type,
                                dismissible: true,
                                pauseOnHover: true,
                                duration: 2000,
                                position: 'bottom-center',
                            }) 
                        }catch {
                            resp = response.data['error']

                            var Type = 'is-danger';
                            this.uploadedTestData=true;
                          
                            toast({
                                message: resp,
                                type: Type,
                                dismissible: true,
                                pauseOnHover: true,
                                duration: 1000,
                                position: 'bottom-center',
                            }) 
                        }

                    });
                this.$store.commit('setIsLoading',false)
            }
        }
    }
</script>
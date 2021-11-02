<template>
<div class="container is-fluid">
    <div class="container is-fluid p-2">
        <div class="notification is-info has-text-centered" >
            <strong><h3 class="title is-2">Public Datasets</h3></strong>
        </div>
    </div>
<div class="container">
                <div class="b-table">
                <div class="table-wrapper has-mobile-cards">
                    <table class="table is-fullwidth is-hoverable is-fullwidth">
                    <thead>
                        <tr>
                            <th></th>
                            <th>Model</th>
                            <th>Datapoints</th>
                            <th>Features</th>
                            <th>Null Values</th>
                            <th>Date Created</th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>
                        
                        <tr v-for="dataset in DatasetDetails" v-bind:key="dataset.id">

                            <td class="is-image-cell">
                                <div class="image">
                                    <img src="@/assets/images/confused-icon-6-yellow.png">
                                </div>
                            </td>

                            <td data-label="Model">{{dataset.Model}}</td>

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
                                        <button class="button is-normal is-info is-inverted has-tooltip-arrow has-tooltip-info" data-tooltip="View training data" type="button" v-on:click ="getTrainingData(dataset.filename,dataset.Model)">
                                    
                                        
                                            <span class="icon is-normal">
                                                <i class="far fa-lg fa-eye"></i>
                                            </span>

                                            <!-- <span><strong>View Dataset</strong></span> -->
                                            <!-- <span>Data</span> -->

                                        </button>
                                    </p>


                                    <p class="control px-1">
                                        <button class="button is-normal is-link has-tooltip-arrow has-tooltip-info" data-tooltip="View test data" type="button" v-on:click ="getTestData(dataset.filename,dataset.Model)">
                                            
                                            <span class="icon is-normal">
                                               <i class="fas fa-chart-line"></i>
                                            </span>
                                            

                                            <!-- <span><strong>Download</strong></span> -->
                                            <!-- <span>Download</span> -->

                                        </button>
                                    </p>
                                    
                                    <p class="control px-1">
                                        <button class="button is-primary has-tooltip-arrow has-tooltip-info" data-tooltip="Download data" type="button" v-on:click ="downloadDataset(dataset.filename,dataset.Model)">
                                            
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
                        Training Dataset
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

      
            <vue-final-modal
                    v-model="showDatasetTestModal"
                    v-if="showDatasetTestModal"
                    classes="modal-container"
                    content-class="modal-content"
                    :drag="true"
                >

                    <div class="modal__title">
                        Test Dataset
                        <button class="delete is-pulled-right" @click="showDatasetTestModal = false"></button>
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
  name: 'PublicDatasets',
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
                DatasetDetails: [],
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
                showDatasetTestModal: false,
            }
        },
        components: {
            AgGridVue,
            GlobalEvents
        },
        mounted(){
            this.getPublicSets()
        },
        methods:{
            pageNav(route){
                this.$router.push(route)
            },
            async getPublicSets(){
                this.$store.commit('setIsLoading',true)
                this.DatasetDetails=[]
                await axios
                    .post('datasets/getPublicDatasetsInfo')
                    .then(response => {
                        var number_of_datasets = Object.keys(response.data).length
                        for(var i=1;i<number_of_datasets+1;i++){
                            //filename gives filename
                            //datapoints gives number of datapoints
                            //columns give number of columns
                            //featureNames gives an array of all the features 
                            //nullValues gives how many nulls in the dataset
                            var dateTime = response.data[i].created.replace("T"," ").split(".")[0].slice(0,-3)
                            response.data[i].created=dateTime
                            
                            this.DatasetDetails.push(response.data[i])                  
                        }
                    })
                    .catch(error => {
                        console.log(error)
                    })
                this.$store.commit('setIsLoading',false)
            },
            async getTrainingData(filename,model){
                this.$store.commit('setIsLoading',true)
                const id =  this.userDetails.id
                const data = {'UserId':id,"filename":filename,"ModelName":model}
                await axios
                .post("datasets/getPublicDatasetTrainData",data)
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
            async getTestData(filename,model){
                this.$store.commit('setIsLoading',true)
                const id =  this.userDetails.id
                const data = {'UserId':id,"filename":filename,"ModelName":model}
                await axios
                .post("datasets/getPublicDatasetTestData",data)
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
                        this.showDatasetTestModal = true
                    } 
                })
                this.$store.commit('setIsLoading',false)
            },
            async downloadDataset(filename, model){
                this.$store.commit('setIsLoading',true)
                console.log(filename)
                console.log(this.userDetails.id);
                const id =  this.userDetails.id;
                const data = {'UserId':id,"filename":filename,"ModelName":model};
                await axios
                .post("datasets/getPublicDatasetTrainData",data)
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
                        const csv = `${heading}\n${body}\n`
                        
                        const MLFEF = new Blob([csv], { type: 'text/csv;charset=utf-8;' });

                        const csvFilename = filename.split(".")[0] + " train data." + filename.split(".")[1] 

                        
                        if (navigator.msSaveBlob) {a
                            navigator.msSaveBlob(MLFEF, csvFilename)
                        }
                        else {
                            const link = document.createElement("a")
                            
                            if (link.download !== undefined) {
                                const url = URL.createObjectURL(MLFEF)
                                link.setAttribute("href", url)
                                link.setAttribute("download", csvFilename)
                                link.style.visibility = 'hidden'
                                document.body.appendChild(link)
                                link.click()
                                document.body.removeChild(link)
                            }
                        }
                    } 
                })

                await axios
                .post("datasets/getPublicDatasetTestData",data)
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
                        const csv = `${heading}\n${body}\n`
                        
                        const MLFEF = new Blob([csv], { type: 'text/csv;charset=utf-8;' });

                        const csvFilename = filename.split(".")[0] + " test data." + filename.split(".")[1] 
                        
                        if (navigator.msSaveBlob) {a
                            navigator.msSaveBlob(MLFEF, csvFilename)
                        }
                        else {
                            const link = document.createElement("a")
                            
                            if (link.download !== undefined) {
                                const url = URL.createObjectURL(MLFEF)
                                link.setAttribute("href", url)
                                link.setAttribute("download", csvFilename)
                                link.style.visibility = 'hidden'
                                document.body.appendChild(link)
                                link.click()
                                document.body.removeChild(link)
                            }
                        }
                    } 
                })

                this.$store.commit('setIsLoading',false)
            }
        }
}
</script>
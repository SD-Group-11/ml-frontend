<template>   
    <div class="container is-fluid">
        <GlobalEvents
            @keydown.left="pageNav('/logistic-regression-datasets')"
            @keydown.right="pageNav('/logistic-regression-tests')"
        />

        <div class="container is-fluid">
            <!-- <div class="notification is-info has-text-centered" >
                <strong><h3 class="title is-3">Linear Regression Model Trainer</h3></strong>
            </div> -->
            <div class="notification is-info has-text-centered" >

            <div class="columns">
                    <div class="column is-one-fifth">                        
                        <div class="button is-pulled-left is-medium is-rounded is-warning has-tooltip-warning" @click="$router.push('/logistic-regression-datasets')" data-tooltip="Manage datasets">
                            <span class="icon is-normal">
                                <i class="fas fa-lg fa-arrow-left"></i>                                
                            </span>
                        </div>
                    </div>
                    
                    <div class="column">
                        <strong><h3 class="title is-3">Model Training</h3></strong>
                    </div>
                    
                    <div class="column is-one-fifth">
                        <div class="button is-pulled-right is-medium is-rounded is-warning has-tooltip-warning" @click="$router.push('/logistic-regression-tests')" data-tooltip="Test a model">
                            <span class="icon is-normal">
                                <i class="fas fa-lg fa-arrow-right"></i>
                            </span>
                        </div>
                    </div>
                    
                </div>
            
            </div>
                
            <div class="block"></div>

            <form @submit.prevent="submitForm"> 
                <div class="columns">
                    <div class="column is-one-fifth">
                        <!-- Selecting a dataset -->
                        <div class="field ">
                            <label class="label">Dataset</label>
                            <select v-model="selected" id = "files" class="select is-normal is-size-6 is-info" style="width: 100%;">
                                <option  disabled value="">Select dataset</option>
                                <option  v-for="dataset in userFiles" v-bind:key="dataset.id" >{{dataset.filename}}</option>
                            </select>
                        </div>
                        
                    </div>

                </div>
            </form>

            <div class="columns">

                <div class="column is-full is-warning ">
                    <div class="box" style="background-color:#FFD55A;">
                        <!-- <h2 class="title is-3 has-text-centered">Enter Hyperparameters</h2> -->
                        
                    </div>

                </div>
            </div>

            <!-- Train model button -->
            <div>
                <button style="text-align: center;" class="button is-info has-text-black" v-if="selected"  v-on:click='TrainModel(); showTestButton = true; showTestingGraphs = false'><strong>Train Model</strong></button>
            </div>
            <div class="block"></div>
        
        </div> 

               
               
        <!-- Training Results -->
        <div class="container is-fluid" v-if="showTrainingResults">
            <span><h2 v-if="showTrainingResults">Results:<span class="accuracy"></span></h2></span>
            
            <div class="columns">
                <div class="column is-one-third">
                    <div class="notification is-warning has-text-black has-text-left" >
                        <strong>F1 Scores</strong>
                        <li v-for="f1 in f1Score" v-bind:key="f1.class">
                                Class {{ f1.class }} :
                                    {{ (f1.score).toFixed(2) }}
                        </li>
                    </div>
                    
                </div>
                <div class="column is-two-thirds is-warning">
                    
                    <div class="notification is-warning has-text-black has-text-left" >
                        <strong>AUC</strong>
                        <li v-for="auc in AUC" v-bind:key="auc.class">
                                Class {{ auc.class }} :
                                    {{ (auc.value) }}
                        </li>
                    </div>
                </div>
            </div>
        </div>
        <div class="block"></div>
                  
        <!-- confusion Matrix for Training Data-->
        <!-- GRAPH TABS FOR TESTING -->
        <div class="tabs is-toggle is-toggle-rounded is-centered" v-if="showTrainingResults">
            <ul>
                <li id="show_CF_Btn" class="is-active tablinks" v-on:click="openTab($event, 'confusionMatrix','show_CF_Btn')">
                    <a>
                        <span class="icon is-small"><i class="fas fa-table" aria-hidden="true"></i></span>
                        <span>Confusion Matrix</span>
                    </a>
                </li>
                <li id="show_ROC_Btn" class="tablinks" v-on:click="openTab($event, 'ROC','show_ROC_Btn')">
                    <a>
                        <span class="icon is-small"><i class="fas fa-chart-line" aria-hidden="true"></i></span>
                        <span>ROC curve</span>
                    </a>
                </li>
            </ul>
        </div>


        <!-- TAB CONTENTS -->
        <div id="confusionMatrix" class="tabcontent">
                <!-- testing line graph -->
                <apexchart v-if="showConfusionMatrix&&tabsInitialized"  height="600" type="heatmap" :options="confusionMatrixOptions" :series="confusionMatrixSeries"></apexchart>
        </div>

        <div id="ROC" class="tabcontent">
                <!-- testing predicted vs actual-->
            <apexchart v-if="showROC&&tabsInitialized"  height="600" type="line" :options="ROCOptions" :series="ROCSeries"></apexchart>
        </div>
        <!-- Discard Results Button -->
        <button class="button is-danger is-pulled-right"  v-if="showTrainingResults" v-on:click='DiscardTrainResults'><strong>Discard Results</strong></button>
 
          
    </div>
</template>

<style scoped>   
    /* .button {
        font-weight:500;
        border-color: #007EFF;
        color: rgb(0, 0, 0);
        background-image: -webkit-linear-gradient(45deg, #0273E5 50%, transparent 50%);
        background-image: linear-gradient(45deg, #3F99F5 50%, transparent 50%);
        background-position: 100%;
        background-size: 400%;
        -webkit-transition: background 300ms ease-in-out;
        transition: background 300ms ease-in-out;
    }
    .button:hover {
        background-position: 0;
    } */

    h2 {
        color: black;
        font-size: 30px;
        margin: 20px;
        font-family: Tahoma, sans-serif, Georgia, serif;
        font-weight: 500;
        text-align: center;
    }

    .accuracy {
        color: #037BF7;
        font-size: 30px;
    }
</style>


<script>
    import axios from 'axios'
    import Chart from 'chart.js'
    import VueApexCharts from "vue3-apexcharts"
    import { GlobalEvents } from 'vue-global-events'
    import {toast} from 'bulma-toast'

    export default {
        name: "LogisticRegressionTraining",
        components: {
            apexchart: VueApexCharts,
            GlobalEvents
        },
        data() {
            return{
                // Variables involving the files and user details
                userDetails: [],
                userFiles: [],
                uploadedName: '',
                uploadable: false,
                hasDatasets: false,
                selected: '',
                // Response data
                f1Score:[],
                AUC:-1,
                numberFeatures:-1,
                confusionMatrix:[],
                ROC:[],
  

                
               //Apex chart data for confusion matrix and ROC
                confusionMatrixOptions:[],
                confusionMatrixSeries: [],
                ROCOptions: [],
                ROCSeries:[],
            

                //booleans to control whether the confusion matrix and the ROC chart should be displayed
                showConfusionMatrix:false,
                showROC:false,
                tabsInitialized:false,

                //controls wether training results are displayed
                showTrainingResults:false,
            }
        },
        mounted(){
            this.getAccount()
            //init confusion matrix remove this line

        },
        methods:{
            //create confusion Matrix
            createConfusionMatrix(){
                var confusionMatrixOptions ={
                    dataLabels: {
                        enabled: true,
                        style: {
                                fontSize: '1rem',
                                colors: ["#000000"]
                            } 
                        },
                    colors: ["#008FFB"],
                    
                
                    xaxis: {
                        type: 'category',
                        title: {
                            text: 'Predicted',
                            style: {
                                fontSize: '1.2rem'
                            }
                        },
                        labels: {
                            style: {
                                fontSize: '1rem'
                            }  
                        }                      

                    },
                    yaxis: {
                        title: {
                            text: 'Actual',
                            style: {
                                fontSize: '1.2rem'
                            }
                        },
                        labels: {
                            style: {
                                fontSize: '1rem'
                            }
                        }
                    },
                    title: {
                        text: 'Confusion Matrix',
                        align: 'center',
                        margin:40,
                        style: {
                            fontweight: 'bold',
                            fontSize: '1.5rem',
        
                        }
                        
                    },
    
                }
                var confusionMatrixSeries=[]
                var results = this.confusionMatrix
                for(let i=results.length-1;i>=0;i--){
                    var result = results[i];
                    var obj = {
                        name:result.class,
                        data:[]
                    }
                    for(let j=0;j<results.length;j++){
                        obj.data.push({ 
                            x:results[j].class,
                            y:results[i].predictions[j]
                        })
                    }
                    confusionMatrixSeries.push(obj)
                }
                this.confusionMatrixOptions = confusionMatrixOptions
                this.confusionMatrixSeries = confusionMatrixSeries
                this.showConfusionMatrix = true;
                return
            },
            
            createROCChart(){
                var ROC_SeriesArray = []
                for(let i=0;i<this.ROC.length;i++){
                    //lineObj is a JSON object containing the name of the class for the ROC curve and the data for the curve
                    var lineObj = this.ROC[i]
                    var XYPairs = []
                    for(let j=0;j<lineObj.fpr_values.length;j++){
                          XYPairs.push({x: lineObj.fpr_values[j], y: lineObj.tpr_values[j]})
                    }
                    var ROC_Series = {
                        name:"class: " + lineObj.class,
                        data:XYPairs
                    }
                    ROC_SeriesArray.push(ROC_Series)
               
                }
                this.ROCSeries = ROC_SeriesArray
                this.ROCOptions={
                    stroke: {
                        curve: 'stepline',
                    },
                    dataLabels: {
                        enabled: false
                    },
                    title: {
                        text: 'ROC chart',
                        align: 'center',
                        margin:40,
                        style: {
                            fontweight: 'bold',
                            fontSize: '1.5rem',
        
                        }
                    },
                    markers: {
                        hover: {
                            sizeOffset: 4
                            }
                    },
                    xaxis: {
                        min:0,
                        max:1,
                        decimalsInFloat: 4,
                        type: 'numeric',
                        title: {
                            text: 'False Positive Rate',
                            offsetY:5,
                            style: {
                                fontSize: '1.2rem'
                            }

                        },
                        labels: {
                            style: {
                                fontSize: '1rem'
                            }
                        },
                    },
                    yaxis: {
                        title: {
                            text: 'True Positive Rate',
                            style: {
                                fontSize: '1.2rem',
                    
                            },
                        
                        },
                        decimalsInFloat: 2,
                        min: 0,
                        max: 1,
                        labels: {
                            style: {
                                fontSize: '1rem'
                            }
                        }
                    }
                }
                
                // this.ROCSeries=[
                //     {
                //     data: ROC_XYPairs[0]
                // }
                // ]
                this.showROC=true;
            },

            pageNav(route){
                this.$router.push(route)
            },
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
                .post('/LogisticRegression/getDatasetsInfo',data)
                .then(response =>{
                    if(response.data['error']=="No datasets have been uploaded."){
                        console.log("has no datasets")
                        console.log(response.data)
                        this.hasDatasets = false
                    }
                    else{
                        //console.log(response.data[0])
                        this.hasDatasets = true
                        //idk why but accessing UserFiles out of this scope returns empty. Please check what im doing wrong
                        // response.data though holds all the datasets of a user and their respective summary details
                        //this.userFiles = response.data;
                        // Tell us how many datasets are associated with the user 
                        // you can loop from 1 to number_of_datasets+1 and use that to index response.data[i] to get a dataset and its summary
                        var number_of_datasets = Object.keys(response.data).length
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
                this.$store.commit('setIsLoading',true)
                var id = this.userDetails.id;
                //Please get the filename from the dropdown and set it here 
                var filename = this.selected;
                var data ={"UserId":id,"filename":filename}

                console.log('data: ',data)
                await axios
                .post("/LogisticRegression/PerformLogisticRegression",data)

                .then(response =>{
                    this.extractData(response.data)
                    this.createConfusionMatrix()
                    this.createROCChart()
                    //neither the confusion matrix or the ROC graph will show unitl one of the tabes is clicked on
                    //to fix this openTab is called once here to display the confusion matrix by default
                    this.$nextTick(()=> {
                        // DOM updated
                        document.getElementById('show_CF_Btn').click();

                    })
                    this.$store.commit('setIsLoading',false)

                })
            },
            // We require the UserID as well as the corresponding filename to delete the results we get from training
            async DiscardTrainResults(){
                var id = this.userDetails.id;
                //get the filename from what has been selected.
                var filename = document.getElementById("files").value ;
                //create the dict that will be the data for backend
                var data = {"UserID":id,"Filename":filename};
                await axios
                .post('/LogisticRegression/discardResults',data)
                .then(response => {
                    // get response from backend
                    var resp = response.data['response'];
                    var Type;
                    //indicates successful deleting of the data
                    if(resp == "Results discarded."){
                         Type = 'is-success';
                         //Toast to give user indication of outcome of action
                        toast({
                            message: "Results successfully discarded.",
                            type: Type,
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 1000,
                            position: 'bottom-center',
                        })  
                    }
                    else{
                        // Failed to discard the data
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
                })

            },

            // We require the UserID as well as the corresponding filename to delete the results we get from training
            async DiscardTrainResults(){
                var id = this.userDetails.id;
                //get the filename from what has been selected.
                var filename = document.getElementById("files").value ;
                //create the dict that will be the data for backend
                var data = {"UserID":id,"Filename":filename};
                await axios
                .post('/LogisticRegression/discardResults',data)
                .then(response => {
                    // get response from backend
                    var resp = response.data['response'];
                    var Type;
                    //indicates successful deleting of the data
                    if(resp == "Results discarded."){
                         Type = 'is-success';
                         //Toast to give user indication of outcome of action
                        toast({
                            message: "Results successfully discarded.",
                            type: Type,
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 1000,
                            position: 'bottom-center',
                        })  
                    }
                    else{
                        // Failed to discard the data
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
                })
            },
            //Extract http response into accessible javascript data
            extractData(responseData) {
                this.$store.commit('setIsLoading',true)
                console.log('responseData', responseData)
                
                this.confusionMatrix =responseData['cm']
              
                // f1 score and AUC
                this.f1Score = responseData['f1']
            
                this.AUC = responseData['auc']
                this.ROC = responseData['ROC']
                this.showTrainingResults=true;
                //number of features
                // this.numberFeatures = Object.values(responseData['jsonFeatures'])[0].length -1
                this.$store.commit('setIsLoading',false)
            },

            

            // tabs
            openTab(event, tabId,tabBtnId){
                this.tabsInitialized=true;
            //get all elements w the tab content and hide it
               var tabcontent = document.getElementsByClassName('tabcontent')
               for(let i=0; i<tabcontent.length; i++)
               {
                   tabcontent[i].style.display = 'none';
               }
            //get all the elements w the class tablinks and remove is-active
               var tablinks = document.getElementsByClassName('tablinks')
               for(let i=0; i<tablinks.length; i++)
               {
                   tablinks[i].className = tablinks[i].className.replace('is-active', '')
               }

            //show curr tab and add is-active to that tab
                document.getElementById(tabId).style.display = 'block'
                document.getElementById(tabBtnId).classList.add('is-active')
                //event.target.classList.add('is-active')
            }
        }
    }
</script>

<template>   
    <div class="container is-fluid">
        <GlobalEvents
            @keydown.left="pageNav('/linear-regression-datasets')"
            @keydown.right="pageNav('/linear-regression-tests')"
        />

        <div class="container is-fluid">
            <!-- <div class="notification is-info has-text-centered" >
                <strong><h3 class="title is-3">Linear Regression Model Trainer</h3></strong>
            </div> -->
            <div class="notification is-info has-text-centered" >

            <div class="columns">
                    <div class="column is-one-fifth">                        
                        <div class="button is-pulled-left is-medium is-rounded is-warning has-tooltip-warning" @click="$router.push('/linear-regression-datasets')" data-tooltip="Manage datasets">
                            <span class="icon is-normal">
                                <i class="fas fa-lg fa-arrow-left"></i>                                
                            </span>
                        </div>
                    </div>
                    
                    <div class="column">
                        <strong><h3 class="title is-3">Model Training</h3></strong>
                    </div>
                    
                    <div class="column is-one-fifth">
                        <div class="button is-pulled-right is-medium is-rounded is-warning has-tooltip-warning" @click="$router.push('/linear-regression-tests')" data-tooltip="Test a model">
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

                    <div class="column is-four-fifths">
                        <div class="field is-grouped">
                            
                            <div class="control">
                                <label class="label">Learning Rate</label>
                                <input class="input" id="learningRate" type="text" placeholder="0.1">
                            </div>
                        
                            
                            <div class="control">
                                <label class="label">Tolerance</label>
                                <input class="input" id = "tol" type="email" placeholder="0.5">
                            </div>

                            <!-- <div class="control ml-6">
                                <label class="label">Split</label>
                                <input type="range" id="split" min="1" max="99" step="1" v-model="initialSplit" style="width: 210%;"/>
                                <div class="output">Training and test data split: {{ initialSplit }}/{{ 100-initialSplit }}</div>
                            </div> -->
                            
                        </div>
    
                    </div> 

                    <div class="column is-one-fifth">
                        <!-- Selecting a dataset -->
                        <div class="field ">
                            <label class="label">Dataset</label>
                            <select v-model="selected" id = "files" class="select is-normal is-size-6 is-info" style="width: 100%;">
                                <option disabled value="">Select dataset</option>
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
                <button style="text-align: center;" class="button is-info has-text-black"  v-on:click='TrainModel(); showTestButton = true; showTestingGraphs = false'><strong>Train Model</strong></button>
            </div>
            <div class="block"></div>
        
        </div> 

               
               
        <!-- Training Graphs -->
        <div class="container is-fluid" v-if="showTrainingGraphs">
            <span><h2 v-if="showTrainingGraphs">Results:<span class="accuracy"></span></h2></span>
            
            <div class="columns">
                <div class="column is-one-third">
                    <div class="notification is-warning has-text-black has-text-left" >
                        <strong>Coefficient of Determination: {{ (trainAccuracy).toFixed(2) }}</strong>
                        
                    </div>
                    
                </div>
                <div class="column is-two-thirds is-warning">
                    
                    <div class="notification is-warning has-text-black has-text-left" >
                        <strong>Coefficients: {{ coefficients }}</strong>
                    </div>
                </div>
            </div>
        </div>
        <div class="block"></div>
                  
        <!-- Predicted VS actual for Training Data-->
        <apexchart v-if="showTrainingGraphs" type="line" :options="trainingOptionsPredictedVSActual" height=600 :series="trainingSeriesPredictedVSActual"></apexchart>

        <!-- Test Model Button -->
        <!-- <button class="button" id="testModelButton" v-if="showTrainingGraphs" v-on:click='showTestGraphs'> Test Model</button> -->
        
        <!-- Discard Results Button -->
        <button class="button is-danger is-pulled-right"  v-if="showTrainingGraphs" v-on:click='DiscardTrainResults'><strong>Discard Results</strong></button>
        
        
        <!-- Testing Graphs -->
        <span><h2 v-if="showTestingGraphs">Testing results: <span class="accuracy">{{ (testAccuracy*100).toFixed(2) }}% </span></h2></span>
        <!-- Line of best fit for Training Data-->
        <apexchart v-if="showTestingGraphs && numberFeatures==1" type="line" :options="optionsLOBF" height=600 :series="seriesLOBF"></apexchart>
        <br>
        <!-- Predicted VS actual for Testing-->
        <apexchart v-if="showTestingGraphs" type="line" :options="testingOptionsPredictedVSActual" height=600 :series="testingSeriesPredictedVSActual"></apexchart>
          
          
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
        name: "LinearRegressionDatasets",
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

                initialSplit: 70,

                // Response data
                trainX: [],
                trainY: [],
                testX: [],
                testY: [],
                trainPredictedY: [],
                testPredictedY: [],
                trainAccuracy: -1,
                testAccuracy: -1,
                // coefficients: 0,
                coefficients: [],
                meanSquaredError: -1,
                intercept: 0,
                numberFeatures: -1,

                // Line of best fit chart data
                bestFitYValues: {},   
                seriesLOBF: [],
                optionsLOBF: [],
                
                // Actual VS Predicted chart data
                trainingSeriesPredictedVSActual: [],
                testingSeriesPredictedVSActual: [],
                trainingOptionsPredictedVSActual: [],
                testingOptionsPredictedVSActual: [],

                // If the graphs should be displayed and if so, which ones, training or testing?
                showTestButton: false,
                isTraining: false,
                isTesting: false,
                showTrainingGraphs: false,
                showTestingGraphs: false,
                

            }
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
                // tol and learningRate must be decimal values
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
                    console.log(response.data)
                    this.extractData(response.data);

                    this.isTraining = true

                    
                    this.plotPredictedVSActual(this.trainX.length, this.trainY, this.trainPredictedY)

                    this.showTrainingGraphs = true
                    this.isTraining = false

                    // Create graphs for Test dataset
                    this.isTesting = true

                    //If there is only one feature we can plot the line of best fit
                    if (this.numberFeatures == 1) {
                        // Since testX is received and stored as a 2D array, even if there is only one feature
                        // we need to reshape it into a 1D array to plot the line of best fit

                        // Reshape Test X data
                        var tempTestX = []
                        for (let i = 0; i < this.testX.length; i++) {
                            tempTestX.push(this.testX[i][0])
                        }
                        this.testX = tempTestX

                        this.plotLineOfBestFit(this.testX, this.testY, this.coefficients, this.intercept);
                    }

                    this.plotPredictedVSActual(this.testX.length, this.testY, this.testPredictedY)

                    // this.showTestingGraphs = true

                });
                this.$store.commit('setIsLoading',false)
            },

            // We require the UserID as well as the corresponding filename to delete the results we get from training
            async DiscardTrainResults(){
                var id = this.userDetails.id;
                //get the filename from what has been selected.
                var filename = document.getElementById("files").value ;
                //create the dict that will be the data for backend
                var data = {"UserID":id,"Filename":filename};
                await axios
                .post('/LinearRegression/discardMetrics',data)
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
            // Used in order to show Test data charts on button click
            showTestGraphs() {
                this.$store.commit('setIsLoading',true)
                this.showTestingGraphs = true
                var btn = document.getElementById('testModelButton')
                // btn.remove()
                if (btn.style.display === "none") {
                    btn.style.display = "block";
                }
                this.$store.commit('setIsLoading',false) 
            },

            //Extract http response into accessible javascript data
            extractData(responseData) {
                this.$store.commit('setIsLoading',true)
                console.log('responseData', responseData)
                
                // Train data
                this.trainX = Object.values(responseData['TrainX'])
                this.trainY = Object.values(responseData['TrainY'])
                this.trainPredictedY = Object.values(responseData['Train_PredictY'])


                // // Test data
                // this.testX = Object.values(responseData['TestX'])
                // this.testY = Object.values(responseData['TestY'])
                // this.testPredictedY = Object.values(responseData['Test_PredictY'])


                // Train and Test accuracy
                this.trainAccuracy = responseData['Train_accuracy']
                // this.testAccuracy = responseData['Test_accuracy']


                //Mean Squared Error, Coefficients, Intercept and number of Features
                this.meanSquaredError = responseData['meansquared']
                // this.coefficients = Object.values(responseData['coefficients'])[0]
                this.coefficients = Object.values(responseData['coefficients'])
                this.coefficients = this.coefficients.map(function(each_element){
                    return Number(each_element.toFixed(2));
                });
                this.intercept = Object.values(responseData['Intercept'])[0]
                this.numberFeatures = Object.values(responseData['jsonFeatures'])[0].length -1
                this.$store.commit('setIsLoading',false)
            },

            plotLineOfBestFit(xValues, yValues, m, c) {
                this.$store.commit('setIsLoading',true)
                //Pair together each X-value with its corresponding Y-value, thus creating a 2D array being a list of pairs.
                var actualXYPairs = []
                //var predictedXYPairs =[]
                
                var minX = 999999999
                var maxX = -99999999
                for (let i = 0; i < xValues.length; i++) {
                    actualXYPairs.push({x: xValues[i], y: yValues[i]})
                    //predictedXYPairs.push({x: xValues[i], y: (m*xValues[i]+c)})

                    // Find the min and max X values, used to plot the line using only 2 points instead of all,
                    // also used to set domain of chart
                    if (xValues[i] < minX) {
                        minX = xValues[i]
                    }
                    if (xValues[i] > maxX) {
                        maxX = xValues[i]
                    }
                }

                // Series is used to plot different types of graphs on the same chart. e.g Scatter and line
                this.seriesLOBF = [{
                    name: "Actual Values",
                    type: 'scatter',
                    color: '#FF9600',
                    data: actualXYPairs
                },{
                    // Not drawing a line connecting every point, only the min and max, saving computation and time
                    // This is the line of best fit, calculated using equation y = mx+c
                    name: "Best fit",
                    type: 'line',
                    color: '#0085FF',
                    data: [{x:minX, y:(m*minX+c)}, {x:maxX, y:(m*maxX+c)}]
                    //data: predictedXYPairs
                }]

                // Options and settings to customise the chart
                this.optionsLOBF = {
                    chart: {
                        height: 300,
                        type: 'line',
                        zoom: {
                            enabled: true,
                            type: 'xy'
                        },
                    },
                    title: {
                        text: 'Line of best fit',
                        align: 'center',
                    },
                    fill: {
                        type:'solid',
                    },
                    markers: {
                        size: [4, 6], //Size of markers of different types of chart, in this case [scatter, line]
                    },
                    tooltip: {
                        shared: false,
                        intersect: true,
                    },
                    xaxis: {
                        tickPlacement: 'on',
                        type: 'numeric',
                        min: minX,
                        max: maxX,
                        tickAmount: 12,
                        decimalsInFloat: 2,
                        title: {
                            text: 'X value'
                        },
                    },
                    yaxis: {
                        title: {
                            text: 'Y value'
                        },
                        decimalsInFloat: 2,
                    }
                }
                this.$store.commit('setIsLoading',false)
            },

            plotPredictedVSActual(xSize, yValues, yPredicated) {
                this.$store.commit('setIsLoading',true)
                var xyPairs = []
                var xyPredicted = []
                for (let i = 0; i < xSize; i++) {
                    xyPairs.push({x: i, y: yValues[i]})
                    xyPredicted.push({x: i, y: yPredicated[i]})
                }


                // Series is used to plot different types of graphs on the same chart. e.g Scatter and line
                var seriesPredictedVSActual = [{
                    name: "Actual Values",
                    type: 'line',
                    color: '#FF9600',
                    
                    data: xyPairs
                },{
                    name: "Predicted values",
                    type: 'line',
                    color: '#0085FF',
                    data: xyPredicted
                }]

                // Options and settings to customise the chart
                var optionsPredictedVSActual = {
                    chart: {
                        type: 'line',
                        zoom: {
                            enabled: true,
                            type: 'xy'
                        },
                    },
                    title: {
                        text: 'Predicted Y VS Actual Y',
                        align: 'center',
                    },
                    fill: {
                        type:'solid',
                    },
                    markers: {
                        size: [4, 4], //Size of markers of different types of chart, in this case [scatter, line]
                    },
                    tooltip: {
                        shared: false,
                        intersect: true,
                    },
                    xaxis: {
                        tickPlacement: 'on',
                        min: 0,
                        max: xSize,
                        tickAmount: 12,
                        decimalsInFloat: 2,
                        title: {
                            text: 'X index'
                        },
                    },
                    yaxis: {
                        title: {
                            text: 'Y value'
                        },
                        decimalsInFloat: 2,
                    }
                }

                // Since we cannot use the same variables for training and testing we allocate them separately
                if (this.isTraining) {
                    this.trainingSeriesPredictedVSActual = seriesPredictedVSActual
                    this.trainingOptionsPredictedVSActual = optionsPredictedVSActual
                }
                if (this.isTesting){
                    this.testingSeriesPredictedVSActual = seriesPredictedVSActual
                    this.testingOptionsPredictedVSActual = optionsPredictedVSActual
                }
                this.$store.commit('setIsLoading',false)
            }
        }
    }
</script>

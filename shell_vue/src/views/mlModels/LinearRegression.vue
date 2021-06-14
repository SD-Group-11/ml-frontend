<template>   
    <div class="container">

        <section class="hero" style=" background-color:#000080">
            <div class="hero-body">
                <h1 class="title is-1 has-text-centered" style="color:#FFFFFF; background-color:#000080; border-radius:200px"><strong>Linear Regression</strong></h1>
            </div>
        </section>    

        <div class="columns is-multiline is-mobile">

            <div class="column is-full is-warning has-text-centered">
                
                
                <div class="box" style="background-color:#FFD55A;">
                    <h2 class="title is-3 has-text-centered">Enter Hyperparameters</h2>
                    
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

                    

                    <!-- <div class="field">
                        <label class="label">Split</label>
                        <div class="control">
                            <input class="input" id="split" type="email" placeholder="Training Split">
                        </div>
                        
                    </div> -->
                    
                    <!-- Trying a slider for the user to pick the data split -->
                    <div class="field">
                        <label class="label">Split</label>
                        <input type="range" id="split" min="1" max="99" step="1" v-model="initialSplit" style="width: 60%;"/>
                        <div class="output">Training and test data split: {{ initialSplit }}/{{ 100-initialSplit }}</div>
                    </div>

                    <div class="control">
                    <div id="v-model-select" class="demo">
                        <select v-model="selected" >
                            <option  v-for="dataset in userFiles" v-bind:key="dataset.id" >{{dataset.filename}}</option>

                        </select>
                    </div>
                     </div>
                     <button class="button"  v-on:click='TrainModel'> Train Model</button>
                    
                    <!-- Line of best fit -->
                    <apexchart v-if="showTrainPlots && numberFeatures==1" type="line" :options="chartOptions" height=400 :series="series"></apexchart>


                </div>

            </div>
        </div>
    </div>
</template>

<style>
    .button {
        border-color: #fd0b0b;
        color: rgb(0, 0, 0);
        background-image: -webkit-linear-gradient(45deg, #fd1201 50%, transparent 50%);
        background-image: linear-gradient(45deg, #ff5e5e 50%, transparent 50%);
        background-position: 100%;
        background-size: 400%;
        -webkit-transition: background 300ms ease-in-out;
        transition: background 300ms ease-in-out;
    }
    .button:hover {
        background-position: 0;
    }
</style>


<script>
    import axios from 'axios'
    import Chart from 'chart.js'
    import VueApexCharts from "vue3-apexcharts";
    import {toast} from 'bulma-toast'

    export default {
        name: "LinearRegressionDatasets",
        components: {
            apexchart: VueApexCharts,
        },
        data() {
            return{
                // Variables involving the files and user details
                userDetails: [],
                UserFiles: [],
                uploadedName: '',
                uploadable: false,
                hasDatasets: false,

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
                coefficients: 0,
                meanSquaredError: -1,
                intercept: 0,
                numberFeatures: -1,

                // Chart data
                showTrainPlots: false,
                bestFitYValues: {},   
                series: [],
                chartOptions: {},
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
                var id = this.userDetails.id;
                //Please get the filename from the dropdown and set it here 
                var filename = "train.csv";
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
                    //If there is only one feature we can plot the line of best fit
                    if (this.numberFeatures == 1) {
                        // Since trainX and testX is received and stored as a 2D array, even if there is only one feature
                        // we need to reshape it into a 1D array to plot the line of best fit

                        // Reshape Train X data
                        var tempTrainX = []
                        for (let i = 0; i < this.trainX.length; i++) {
                            tempTrainX.push(this.trainX[i][0])
                        }
                        this.trainX = tempTrainX

                        // Reshape Testing X data
                        var tempTestX = []
                        for (let i = 0; i < this.testX.length; i++) {
                            tempTestX.push(this.testX[i][0])
                        }
                        this.testX = tempTrainX

                        this.plotLineOfBestFit(this.trainX, this.trainY, this.coefficients, this.intercept);
                    }
                    
                });
            },

            //Extract http response into accessible javascript data
            extractData(responseData) {
                console.log('responseData', responseData)
                // Train data
                this.trainX = Object.values(responseData['TrainX'])
                this.trainY = Object.values(responseData['TrainY'])
                this.trainPredictedY = Object.values(responseData['Train_PredictY'])

                // Test data
                this.testX = Object.values(responseData['TestX'])
                this.testY = Object.values(responseData['TestY'])
                this.testPredictedY = Object.values(responseData['Train_PredictY'])

                // Train and Test accuracy
                this.trainAccuracy = responseData['Train_accuracy']
                this.testAccuracy = responseData['Test_accuracy']

                //Mean Squared Error, Coefficients, Intercept and number of Features
                this.meanSquaredError = responseData['meansquared']
                this.coefficients = Object.values(responseData['coefficients'])[0]
                this.intercept = Object.values(responseData['Intercept'])[0]
                this.numberFeatures = Object.values(responseData['jsonFeatures'])[0].length -1
            },

            plotLineOfBestFit(xValues, yValues, m, c) {
                this.showTrainPlots = false

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
                this.series = [{
                    name: "Actual Values",
                    type: 'scatter',
                    data: actualXYPairs
                },{
                    // Not drawing a line connecting every point, only the min and max, saving computation and time
                    // This is the line of best fit, calculated using equation y = mx+c
                    name: "Best fit",
                    type: 'line',
                    color: '#Ff5e5e',
                    data: [{x:minX, y:(m*minX+c)}, {x:maxX, y:(m*maxX+c)}]
                    //data: predictedXYPairs
                }]

                // Options and settings to customise the chart
                this.chartOptions = {
                    chart: {
                        height: 300,
                        type: 'line',
                        zoom: {
                            enabled: true,
                            type: 'xy'
                        },
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
                this.showTrainPlots = true
            },

            plotPredictedVSActual() {
                
            }
        }
    }
</script>
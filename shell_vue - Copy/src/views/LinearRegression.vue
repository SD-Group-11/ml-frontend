<template>   
    

    
    <div class="container">

            <section class="hero" style=" background-color:lightblue">
                <div class="hero-body">
                    <h1 class="title is-1 has-text-centered" style=" background-color:lightblue; border-radius:200px"><strong>Linear Regression</strong></h1>
                </div>
            </section>

            <div class="column is-multiline">

            

                <!-- <div class="column">
                    <div class="control" >
        
                        <h1 class="title is-1 has-text-centered" style=" background-color:lightblue; border-radius:200px"><strong>Linear Regression</strong></h1>
                    </div>
                </div> -->
            <div class="column"> 
            

            </div>

            <div class="column">    

            <div class="columns is-multiline is-mobile">
                <div class="column is-half">
                    <div class="box" style="background-color:lightyellow;" >
                        <div class="control">
                        <h2 class="title is-3"> Upload Your CSV file here!</h2>
                        
                        <h3> 1) Click on "Choose File" <br>
                        2) Select a .csv file from your local device.<br>
                        3) Click on "Submit" when it appears<br>
                        4) Wait and let the magic happen!<br>
                        </h3>
                    </div>
                        <!-- <form @submit.prevent="submitForm" style="background-color:lightgrey; border-radius:50px"> -->
                        <form @submit.prevent="submitForm" >

                            <!-- <input type="file" id="myFile" name="filename" accept=".csv" v-on:input="fileValidation"> -->
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
                            <!-- <input v-on:click = 'Upload' type="submit" id = 'uploadFile'> -->
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

                <div class="column is-full is-warning has-text-centered" v-if="uploaded">
                    <h2 class="title is-3 has-text-centered">Enter Hyperparameters</h2>
                    <div class="box" style="background-color:lightyellow;">
                     <div class="field">
                            <label class="label">Learning Rate</label>
                            <div class="control">
                                <input class="input" type="text" placeholder="0.01">
                            </div>
                            </div>

                            <div class="field">
                            <label class="label">Tolerance</label>
                            <div class="control">
                                <input class="input" type="email" placeholder="0.5">
                            </div>
                            </div>
                            
                         
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
        name: "LinearRegression",
        data() {
            return{
                details: [],
                SummaryData: [],
                uploadedName: '',
                uploadable: false,
                uploaded: false,
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
                        this.details=response.data
                        console.log(response)

                        toast({
                                message: 'Upload a CSV file where the first column is No (this indicates the row number) and the last column must be the targets/categories.',
                                type: 'is-warning',
                                dismissible: true,
                                pauseOnHover: true,
                                duration: 50000,
                                position: 'bottom-center',
                            })
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
                //this.$refs.para.style.color="blue";
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
                            axios.post('/datasets/dataSummary',data)
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
                axios.post('/datasets/dataSummary',data)
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
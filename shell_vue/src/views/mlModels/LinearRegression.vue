<template>
    <div class="container">
        <div class="column is-multiline">
        <header id="showcase" style="background-color:lightyellow; border-radius:50px">
        <h1><strong>Linear Regression</strong></h1>
        <p>In statistics, linear regression is a linear approach to modelling the relationship between a scalar response and one or more explanatory variables (also known as dependent and independent variables). The case of one explanatory variable is called simple linear regression; for more than one, the process is called multiple linear regression. This term is distinct from multivariate linear regression, where multiple correlated dependent variables are predicted, rather than a single scalar variable.
</p>
</header>
            <div  id="showcase">
                <div class="box" style="background-color:lightblue" >
                <h2 style="font-size:30px"> Upload Your CSV file here!</h2>
                <h3> 1) Click on "Choose File" <br>
                     2) Select a .csv file from your local device.<br>
                     3) Click on "Submit"<br>
                     4) Wait and let the magic happen!<br>
                </h3>
                <br>
                    <form @submit.prevent="submitForm" style="background-color:lightgrey; border-radius:50px">
                        <input type="file" id="myFile" name="filename" accept=".csv">
                        <br>
                        <input v-on:click = 'Upload' type="submit" id = 'uploadFile'>
                    </form>
                </div>

                <div  id="showcase">
                    <div class="box" style="background-color:lightblue" >
                    <h2 style="font-size:30px"> Uploaded data</h2>
                    <p id="data" ref="para"> Metadata will appear here
                    </p>
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
                SummaryData: []
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
                    })
                    .catch(error => {
                        console.log(error)
                    })

                this.$store.commit('setIsLoading',false)

            },
             Upload: function(){
                var file = document.getElementById("myFile").files[0];
                var formData = new FormData();
                formData.append("dataset",file);
                this.$refs.para.style.color="blue";
                formData.append("id",this.details.id);
                console.log(this.details.id);
                axios.post('/datasets/uploadData',formData)
                .then(response => {
                    var resp =  response.data['response'];
                    var Type;
                    if (resp == 'Data Uploaded Successfully'){
                        Type = 'is-success';
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
            },
            Summary: function(){
                var file = document.getElementById("myFile").files[0];
                var filename = file.name;
                var id=  this.details.id;
                var data ={"id":id,"filename":filename}
                axios.post('/datasets/dataSummary',data)
                .then(response =>{
                    this.SummaryData = response.data;

                });
                console.log(this.SummaryData);
            }
        }
    }
</script>
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
                                    <h2 class="title is-3">Uploaded data</h2>
                                    <p id="data" ref="para"> Metadata will appear here
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
            <th>Company</th>
            <th>City</th>
            <th>Progress</th>
            <th>Created</th>
            <th></th>
          </tr>
          </thead>
          <tbody>
          <tr>
            <td class="is-chevron-cell">
              <a role="button">
                <span class="icon is-expanded"><i class="mdi mdi-chevron-right mdi-24px"></i></span>
              </a>
            </td>
            <td class="is-image-cell">
              <div class="image">
                <img src="https://avatars.dicebear.com/v2/initials/rebecca-bauch.svg" class="is-rounded">
              </div>
            </td>
            <td data-label="Name">Rebecca Bauch</td>
            <td data-label="Company">Daugherty-Daniel</td>
            <td data-label="City">South Cory</td>
            <td data-label="Progress" class="is-progress-cell">
              <progress max="100" class="progress is-small is-primary" value="79">79</progress>
            </td>
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
                      <img src="https://avatars.dicebear.com/v2/initials/rebecca-bauch.svg">
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
          <tr>
            <td class="is-chevron-cell">
              <a role="button">
                <span class="icon"><i class="mdi mdi-chevron-right mdi-24px"></i></span>
              </a>
            </td>
            <td class="is-image-cell">
              <div class="image">
                <img src="https://avatars.dicebear.com/v2/initials/felicita-yundt.svg" class="is-rounded">
              </div>
            </td>
            <td data-label="Name">Felicita Yundt</td>
            <td data-label="Company">Johns-Weissnat</td>
            <td data-label="City">East Ariel</td>
            <td data-label="Progress" class="is-progress-cell">
              <progress max="100" class="progress is-small is-primary" value="67">67</progress>
            </td>
            <td data-label="Created">
              <small class="has-text-grey is-abbr-like" title="Jan 8, 2019">Jan 8, 2019</small>
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
          <tr>
            <td class="is-chevron-cell">
              <a role="button">
                <span class="icon"><i class="mdi mdi-chevron-right mdi-24px"></i></span>
              </a>
            </td>
            <td class="is-image-cell">
              <div class="image">
                <img src="https://avatars.dicebear.com/v2/initials/mr-larry-satterfield-v.svg" class="is-rounded">
              </div>
            </td>
            <td data-label="Name">Mr. Larry Satterfield V</td>
            <td data-label="Company">Hyatt Ltd</td>
            <td data-label="City">Windlerburgh</td>
            <td data-label="Progress" class="is-progress-cell">
              <progress max="100" class="progress is-small is-primary" value="16">16</progress>
            </td>
            <td data-label="Created">
              <small class="has-text-grey is-abbr-like" title="Dec 18, 2020">Dec 18, 2020</small>
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
          <tr>
            <td class="is-chevron-cell">
              <a role="button">
                <span class="icon"><i class="mdi mdi-chevron-right mdi-24px"></i></span>
              </a>
            </td>
            <td class="is-image-cell">
              <div class="image">
                <img src="https://avatars.dicebear.com/v2/initials/mr-broderick-kub.svg" class="is-rounded">
              </div>
            </td>
            <td data-label="Name">Mr. Broderick Kub</td>
            <td data-label="Company">Kshlerin, Bauch and Ernser</td>
            <td data-label="City">New Kirstenport</td>
            <td data-label="Progress" class="is-progress-cell">
              <progress max="100" class="progress is-small is-primary" value="71">71</progress>
            </td>
            <td data-label="Created">
              <small class="has-text-grey is-abbr-like" title="Sep 13, 2020">Sep 13, 2020</small>
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
          <tr>
            <td class="is-chevron-cell">
              <a role="button">
                <span class="icon"><i class="mdi mdi-chevron-right mdi-24px"></i></span>
              </a>
            </td>
            <td class="is-image-cell">
              <div class="image">
                <img src="https://avatars.dicebear.com/v2/initials/barry-weber.svg" class="is-rounded">
              </div>
            </td>
            <td data-label="Name">Barry Weber</td>
            <td data-label="Company">Schulist, Mosciski and Heidenreich</td>
            <td data-label="City">East Violettestad</td>
            <td data-label="Progress" class="is-progress-cell">
              <progress max="100" class="progress is-small is-primary" value="80">80</progress>
            </td>
            <td data-label="Created">
              <small class="has-text-grey is-abbr-like" title="Jul 24, 2019">Jul 24, 2019</small>
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

    export default {
        name: "LinearRegressionDatasets",
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
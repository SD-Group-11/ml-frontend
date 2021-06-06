<template>
    <section class="section">
    <div class="container ">
        <div class="columns is-centered ">
            <div class="column is-one-third ">
                <h1 class="title has-text-centered">Forgot Password</h1> 
                    
                <form @submit.prevent="submitForm">
                           
                    <div class="field">
                        <label>Email</label>
                        <div class="control pt-1">
                            <input type="text" name="email" placeholder="enter your email address..." class="input" v-model="email">
                        </div>

                        <p class="help is-danger" v-if="field_errors.email">
                            {{field_errors.email}}
                        </p>

                        <p class="help is-danger" v-for="email_error in email_errors" v-bind:key="email_error">{{ email_error }}</p>
                        
                        <p class="help is-danger" v-for="credential_error in credential_errors" v-bind:key="credential_error">{{ credential_error }}</p>


                    </div>

                    <div class="field is-grouped is-grouped-centered pt-3">
                            <div class="control">
                                <button class="button is-info has-text-black"><strong>Confirm email</strong></button>
                            </div>
                        <div class="field ml-6">
                            <div class="control">
                                <router-link to="/log-in" class="button is-ghost">return to login?</router-link>
                            </div>      
                        </div> 
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                </form>

                <!-- <div class="closer">
                    <div class="animation">
                        <div class="animationContainer">
                        <span></span>
                        <span></span>
                        <span></span>
                        <span></span>
                        <span></span>
                        <span></span>
                        </div>
                    </div>
                </div> -->
                
            </div>
        </div>
    </div>
    </section>
</template>


<style scoped>
    /* @import '../assets/styles/rotatingSquares.css';   */
      
</style>


<script>
    import axios from 'axios'

    import {toast} from 'bulma-toast'

    export default {
        name: "ForgotPassword",
        data(){
            return{
                email:'',
                errors:[],
                field_errors:{},
                email_errors:[],
                credential_errors:[],
            }
        },
        methods: {
            async submitForm(){ 
                this.field_errors={}
                this.email_errors=[]
                this.credential_errors=[]

                if (this.email === '') {
                    //this.errors.push('Please enter your email address.')
                    this.field_errors['email']='Please enter your email address.'
                }
            

                if (!this.errors.length && !Object.keys(this.field_errors).length) {
                    this.$store.commit('setIsLoading',true)


                    const formData = {
                        email: this.email,
                    }

                    await axios
                        .post('/api/v1/users/reset_password/', formData)
                        .then(response =>{
                            
                            
                            this.$router.push('/log-in')

                            toast({
                                message: 'A reset link will be sent to the provided email address',
                                type: 'is-warning',
                                dismissible: true,
                                pauseOnHover: true,
                                duration: 3000,
                                position: 'bottom-right',
                            })

                        })
                        .catch(error => {
                                if (error.response) {
                                    for (const property in error.response.data) {
                                        
                                        if(property==='email'){
                                        
                                            for (var i = 0; i < error.response.data[property].length; i++){
                                                if(error.response.data[property][i]=='Enter a valid email address.'){
                                                    this.email_errors.push('Please enter a valid email address')    
                                                }
                                                else{
                                                    this.email_errors.push(error.response.data[property][i]) 
                                                }        
                                            } 
                                        }
                                        else if(property==0 && error.response.data[property]=='User with given email does not exist.'){
                                            this.credential_errors.push('provided email is not registered')
                                             
                                        }
                                        else{
                                            this.errors.push(`${property}: ${error.response.data[property]}`)
                                        } 

                                    
                                    }
                                } else if (error.message) {
                                    this.errors.push('Something went wrong. Please try again!')
                                }
                            })

                    this.$store.commit('setIsLoading',false) 

                }
            }
        }
    }
</script>
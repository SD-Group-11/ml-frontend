<template>
    <section class="section">
    <div class="container">
        <div class="columns is-centered ">
            
            
            <div class="column is-one-third">
                <h1 class="title has-text-centered">Login </h1>
                    
                <form @submit.prevent="submitForm">
                        
                    <div class="field">
                        <label>Email</label>
                        <div class="control">
                            <input type="text" name="email" placeholder="please enter your email address..." class="input" v-model="email">
                        </div>
                        <p class="help is-danger" v-if="field_errors.email">
                                {{field_errors.email}}
                        </p>

                        

                    </div>

                    <div class="field">
                        <label>Password</label>
                        <div class="control">
                            <input type="password" name="password" placeholder="please enter your account password..." class="input" v-model="password">
                        </div>
                        <p class="help is-danger" v-if="field_errors.password">
                            {{field_errors.password}}
                        </p>

                    </div>


                    <!--
                    <div class="field">
                        <div class="control">
                            <button class="button is-success">Submit</button>
                        </div>
                    </div> 
                    -->
                    <div class="field is-grouped is-grouped-centered pt-2">
                            <div class="control">
                                <button class="button is-info has-text-black"><strong>Log In</strong></button>
                            </div>
                        <div class="field ml-2">
                            <div class="control">
                                <router-link to="/forgot-password" class="button is-ghost">Forgot Password?</router-link>
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
        name: "LogIn",
        data(){
            return{
                email:'',
                password:'',
                errors:[],
                field_errors:{},


            }
        },
        methods: {
            async submitForm(){ 
                this.errors=[]
                this.field_errors={}

                if (this.email === '') {
                    //this.errors.push('Please enter your account email.')
                    this.field_errors['email']='Please enter your account email.'
                }
                    
                if (this.password === '') {
                    //this.errors.push('Please enter your password.')
                    this.field_errors['password']='Please enter your account password.'
                }


                if (!this.errors.length && !Object.keys(this.field_errors).length) {
                    this.$store.commit('setIsLoading',true)

                    
                    axios.defaults.headers.common['Authorization']=''
                    localStorage.removeItem('token')


                    const formData = {
                        email: this.email,
                        password: this.password
                    }

                    await axios
                        .post('/api/v1/token/login/', formData)
                        .then(response =>{
                            const token = response.data.auth_token

                            this.$store.commit('setToken',token)

                            axios.defaults.headers.common['Authorization']='Token '+token

                            localStorage.setItem('token',token)
                            
                            
                            this.$router.push('/dashboard')

                            toast({
                                message: 'Welcome :D !',
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
                                        //
                                        //non_field_errors: Unable to log in with provided credentials.
                                        if(property==='non_field_errors' && error.response.data[property][0]=='Unable to log in with provided credentials.'){
                                            this.errors.push(error.response.data[property][0])
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
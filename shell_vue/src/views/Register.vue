<template>
    <div class="container">
    <div class="container has-text-centered">
        <div class="columns is-centered ">
            <div class="column is-one-third ">
                    <h1 class="title has-text-centered">Registration</h1>
                    <form @submit.prevent="submitForm">
                        
                        <div class="field is-grouped is-grouped-centered">
                            
                            <div class="control">
                                <div class="field">
                                    <label>First Name</label>
                                    <div class="control">
                                        <input
                                            type="text"
                                            name="first_name"
                                            placeholder="enter your first name..."
                                            class="input" pattern="[A-Za-z]+"
                                            v-model="first_name"
                                        >
                                    </div>
                                    <p class="help is-danger" v-if="field_errors.first_name">
                                        {{field_errors.first_name}}
                                    </p>
                                </div>
                                
                                
            
                            </div>

                            
                            <div class="control">
                                <div class="field is-half">
                                    <label>Last Name</label>
                                    <div class="control">
                                        <input
                                            type="text"
                                            name="first_name"
                                            placeholder="enter your last name..."
                                            class="input" pattern="[A-Za-z]+"
                                            v-model="last_name"
                                        >
                                    </div>
                                    <p class="help is-danger" v-if="field_errors.last_name">
                                        {{field_errors.last_name}}
                                    </p>
                                </div>
                            </div>

                        </div>
                        

                        <div class="field">
                            <label>Username</label>
                            <div class="control">
                                <input
                                    type="text"
                                    name="username"
                                    placeholder="enter a username..."
                                    class="input"
                                    v-model="username"
                                >
                            </div>
                            <p class="help is-danger" v-if="field_errors.username">
                                {{field_errors.username}}
                            </p>
                        </div>
                        
                        <div class="field">
                            <label>Email</label>
                            <div class="control ">
                                <input
                                    type="text"
                                    name="email"
                                    placeholder="enter your email address..."
                                    class="input"
                                    v-model="email"
                                >
                                
                            </div>
                            <p class="help is-danger" v-if="field_errors.email">
                                {{field_errors.email}}
                            </p>
                            <p class="help is-danger" v-for="email_error in email_errors" v-bind:key="email_error">{{ email_error }}</p>


                        </div>       

                        <div class="field">
                            <label>Password</label>
                            <div class="control">
                                <input
                                type="password"
                                name="password1"
                                placeholder="enter new password..."
                                class="input"
                                v-model="password1"
                                >
                            </div>
                            <p class="help is-danger" v-if="field_errors.password">
                                {{field_errors.password}}
                            </p>

                            <p class="help is-danger" v-if="password_errors.length">
                                {{field_errors.password}}
                            </p>
                            
                        </div>

                        <div class="field">
                            <label>Confirm password</label>
                            <div class="control">
                                <input
                                type="password"
                                name="password2"
                                placeholder="confirm new password..."
                                class="input"
                                v-model="password2"
                                >
                            </div>
                            <p class="help is-danger" v-if="field_errors.password_confirm">
                                {{field_errors.password_confirm}}
                            </p>
                            <p class="help is-danger" v-for="password_error in password_errors" v-bind:key="password_error">{{ password_error }}</p>
                        </div>
                        

                        <div class="field has-text-centered">
                            <div class="control">
                                <button class="button is-info has-text-black"><strong>Submit</strong></button>
                            </div>
                        </div>

                        
                        <div class="notification is-danger" v-if="errors.length">
                            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                        </div>


                    </form>
                
            </div>
        </div>

        

    </div>

    <div class="closer">
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
            </div>
    </div>
</template>


<style scoped>
    @import '../assets/styles/rotatingSquares.css';  
      
</style>

<script>

    import axios from 'axios'

    import {toast} from 'bulma-toast'

    export default {
        name: "Register",
        data(){
            return{
                first_name:'',
                last_name:'',
                username:'',
                email:'',
                password1:'',
                password2:'',
                errors:[],
                field_errors:{},
                password_errors:[],
                email_errors:[],

            }
        },
        methods: {
            async submitForm(){
                this.errors=[]
                this.field_errors={}
                this.password_errors=[]
                this.email_errors=[]
                if (this.first_name === '') {
                    //this.errors.push('Please enter your first name.')
                    this.field_errors['first_name']='Please enter your first name.'
                }
                if (this.last_name === '') {
                    //this.errors.push('Please enter your last name.')
                    this.field_errors['last_name']='Please enter your last name.'
                }

                if (this.username === '') {
                    //this.errors.push('Please enter a username.')
                    this.field_errors['username']='Please enter a username.'
                }

                if (this.email === '') {
                    //this.errors.push('Please enter a valid email address.')
                    this.field_errors['email']='Please enter a email address.'
                }

                if (this.password1 === '') {
                    //this.errors.push('Please enter a password.')
                    this.field_errors['password']='Please enter a password.'
                }
                else{
                    if (this.password2 === '') {
                        //this.errors.push('Please confirm the password.')
                        this.field_errors['password_confirm']='Please confirm the password.'
                    }
                    else{
                        if (this.password1 !== this.password2) {
                            //this.errors.push('The entered passwords do not match.')
                            this.field_errors['password_mismatch']='The entered passwords do not match.'
                        }
                    }
                }
                

                if (!this.errors.length && !Object.keys(this.field_errors).length) {
                    this.$store.commit('setIsLoading', true)
                    
                    const formData = {
                        first_name: this.first_name,
                        last_name: this.last_name,
                        username: this.username,
                        email: this.email,
                        password: this.password1,
                        re_password: this.password2

                    }

                    await axios
                        .post('/api/v1/users/',formData)
                        .then(respone => {
                            toast({
                                message: 'Your account has been created, please log in.',
                                type: 'is-warning',
                                dismissible: true,
                                pauseOnHover: true,
                                duration: 2000,
                                position: 'bottom-right',
                            })

                            this.$router.push('/log-in')
                        })
                        .catch(error => {
                            if (error.response) {
                                for (const property in error.response.data) {
                                    
                                    
                                    if(property==='password'){
                                        
                                        for (var i = 0; i < error.response.data[property].length; i++){
                                            this.password_errors.push(error.response.data[property][i])   
                                        }
                                           
                                    }
                                    else if(property==='email'){
                                        
                                        for (var i = 0; i < error.response.data[property].length; i++){
                                            if(error.response.data[property][i]=='Enter a valid email address.'){
                                                this.email_errors.push('Please enter a valid email address')    
                                            }
                                            else{
                                                this.email_errors.push(error.response.data[property][i]) 
                                            }
                                              
                                        }
                                           
                                    }
                                    else{
                                        this.errors.push(`${property}: ${error.response.data[property]}`)
                                    }

                                }
                                console.log(this.errors)
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
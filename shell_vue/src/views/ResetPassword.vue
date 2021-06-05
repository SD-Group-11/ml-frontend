<template>
    <section class="section">
    <div class="container">
        <div class="columns is-centered ">
            

            
            <div class="column is-one-third ">
                <h1 class="title  has-text-centered">Reset Password</h1>        
                <form @submit.prevent="submitForm">
                    
                        
                    <div class="field">
                            <label>New Password</label>
                            <div class="control">
                                <input
                                type="password"
                                name="password1"
                                placeholder="enter a new password..."
                                class="input"
                                v-model="password1"
                                >
                            </div>

                            <p class="help is-danger" v-if="field_errors.password">
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


                    <div class="field pt-2 has-text-centered">
                        <div class="control">
                                <button class="button is-info has-text-black"><strong>Reset password</strong></button>
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
        name: "ResetPassword",
        data(){
            return{
                password1:'',
                password2:'',
                errors:[],
                field_errors:{},
                password_errors:[],

            }
        },
        methods: {
            async submitForm(){ 
                
                this.errors=[]
                this.field_errors={}
                this.password_errors=[]

                if (this.password1 === '') {
                    //this.errors.push('Please enter a password.')
                    this.field_errors['password']='Please enter a new password.'
                }
                else{
                    if (this.password2 === '') {
                        //this.errors.push('Please confirm the password.')
                        this.field_errors['password_confirm']='Please confirm the new password.'
                    }
                    else{
                        if (this.password1 !== this.password2) {
                            //this.errors.push('The entered passwords do not match.')
                            this.field_errors['password_confirm']='The entered passwords do not match.'
                        }
                    }
                }


                if (!this.errors.length && !Object.keys(this.field_errors).length) {
                    this.$store.commit('setIsLoading',true)

                    const formData = {
                        uid: this.$route.params.uid,
                        token: this.$route.params.token,
                        new_password: this.password1,
                        re_new_password: this.password2 
                    }

                    await axios
                        .post('/api/v1/users/reset_password_confirm/', formData)
                        .then(response =>{
                            
                            
                            this.$router.push('/log-in')

                            toast({
                                message: 'Your password has been reset!',
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
                                        
                                        
                                        if(property==='new_password'){
                                        
                                            for (var i = 0; i < error.response.data[property].length; i++){
                                                this.password_errors.push(error.response.data[property][i])   
                                            }
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
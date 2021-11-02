<template>
    <nav class="navbar is-warning" role="navigation" aria-label="dropdown navigation">
        <div class="navbar-brand">
            <!-- <a class="navbar-item" href="http://getdrawings.com/confused-icon"> -->
            <a class="navbar-item" href="">
                <img src="@/assets/images/confused-icon-6-yellow.png" alt="Logo">
            </a>
            
        </div>

        <div class="navbar-menu">
            <div class="navbar-start">
                <template v-if="!$store.state.isAuthenticated">
                    <router-link to="/" class="navbar-item"><strong>Home</strong></router-link>
                    
                </template>

                <template v-else>
                    <router-link to="/dashboard" class="navbar-item"><strong>Home</strong></router-link>    
                </template>

                <div class="navbar-item has-dropdown is-hoverable">
                    <a class="navbar-link">
                        <strong>Guide</strong>
                    </a>

                    <div class="navbar-dropdown ">
                        <a class="navbar-item">
                             <router-link to="/getting-started" class="navbar-item"><strong>Getting Started</strong></router-link> 
                        </a>
                        <a class="navbar-item">
                             <router-link to="/faq" class="navbar-item"><strong>FAQ</strong></router-link> 
                        </a>
                    </div>
                </div>


                <div class="navbar-item has-dropdown is-hoverable">
                    <a class="navbar-link">
                        <strong>About Us</strong>
                    </a>

                    <div class="navbar-dropdown">
                        <a class="navbar-item">
                            <router-link to="/about" class="navbar-item"><strong>Team</strong></router-link>
                        </a>
                    </div>
                </div>


                <template v-if="$store.state.isAuthenticated">
                    <!-- <div class="navbar-item has-dropdown is-hoverable">
                        <a class="navbar-link">
                            <strong>Linear Regression</strong> 
                        </a>

                        <div class="navbar-dropdown">
                            <router-link to="/linear-regression" class="navbar-item"><strong>Train Model</strong></router-link>
                            <router-link to="/linear-regression-test" class="navbar-item"><strong>Test Model</strong></router-link>
                            <router-link to="/linear-regression-datasets" class="navbar-item"><strong>Manage Datasets</strong></router-link>   
                        </div>
                    </div> -->

                    <a class="navbar-item ">
                            <router-link to="/linear-regression-datasets"><strong>Linear Regression</strong></router-link>
                    </a>

                    <a class="navbar-item">
                            <router-link to="/naive-bayes-datasets"><strong>Naive Bayes</strong></router-link>
                    </a>

                      <a class="navbar-item">
                            <router-link to="/logistic-regression-datasets"><strong>Logistic Regression</strong></router-link>
                    </a>
                    <a class="navbar-item ">
                            <router-link to="/model-comparison"><strong>Compare Classification Models</strong></router-link>
                    </a>

                   <a class="navbar-item ">
                            <router-link to="/public-datasets"><strong>Public Datesets</strong></router-link>
                    </a>


                </template>

            </div>

            <div class="navbar-end">

                <template v-if="!$store.state.isAuthenticated">
                    <div class="navbar-item">
                        <div class="buttons">
                            <router-link to="/register" class="button is-info has-text-black"><strong>Register</strong></router-link>
                            <router-link to="/log-in" class="button is-info has-text-black"><strong>Log In</strong></router-link>
                        </div>
                    </div>
                </template>

                <template v-else>
                    
                    <div class="navbar-item has-dropdown is-hoverable">
                        <a class="navbar-link">
                            <strong>My Account</strong>
                            
                        </a>

                        <div class="navbar-dropdown">
                            <router-link to="/dashboard/my-account" class="navbar-item"><strong>Account Page</strong></router-link>
                            
                            <a @click="showLogoutModal=true" class="navbar-item"><strong>Sign Out?</strong></a>
                            
                            <vue-final-modal v-model="showLogoutModal" classes="modal-container" content-class="modal-content"> 
                                
                                
                                <span class="modal__title">
                                    Are you sure you want to sign out?
                                    <button class="delete is-pulled-right" @click="showLogoutModal = false"></button>
                                </span>

                                <div class="modal__content">
                                    <div class="box">
                                    </div>    
                                </div>

                                <div  class="control">
                                    <div class="modal__action">
                                    <button class="button is-medium is-info" @click="logout(); showModal=false;"><strong>I want to break free!</strong></button>
                                    <!-- <button @click="showModal=false;" class="action_cancel">CANCEL</button> -->
                                </div>
                                </div>
                                
                            </vue-final-modal>
                            
                        </div>
                    </div>

                </template>
            </div>
        </div>
    </nav>     
</template>

<script>
    

    import axios from 'axios'

    import {toast} from 'bulma-toast'

    export default {

        name: "Navbar",
        data: () => ({
            showLogoutModal: false
        }),
        methods:{
            async logout(){
                await axios
                    .post('/api/v1/token/logout/')
                    .then(response => {
                        toast({
                                message: 'You have been signed out',
                                type: 'is-warning',
                                dismissible: true,
                                pauseOnHover: true,
                                duration: 3000,
                                position: 'bottom-right',
                            })
                    })
                    .catch(error => {
                        console.log(JSON.stringify(error))   
                    })
                axios.defaults.headers.common['Authorization']=''
                localStorage.removeItem('token')
                this.$store.commit('removeToken')

                this.$router.push('/')
            }
        }
    }
</script>

<style scoped>



::v-deep .modal-container{
    display: flex;
    justify-content: center;
    align-items: center;
}

::v-deep .modal-content{
    position: relative;
    display: flex;
    flex-direction: column;
    max-height: 90%;
    margin: 0 1rem;
    padding: 1rem;
    border: 1px solid #e2e8f0;
    border-radius: 0.25rem;
    background: #fff;
}

.modal__title{
    margin: 0 2rem 0 0;
    font-size: 1.5rem;
    font-weight: 700;
    align-items: center;
    text-align: center;
}

.modal__content{
    flex-grow: 1;
    overflow-y: auto;
}

.modal__action{
    display: flex;
    justify-content: center;
    /* align-items: center; */
    /* flex-shrink: 0; */
}

.modal__close{
    position: absolute;
    top: 0.5rem;
    right: 0.5rem;
}

.action_confirm{
  background-color: #4CAF50; /* Green */
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 20px;

}

.action_cancel{
  background-color: #ee1414; /* Green */
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 20px;

}


</style>

<style scoped>
.dark-mode div::v-deep .modal-content{
    border-color: #2d3748;
    background-color: #1a202c;
}
</style>
<template>
    <nav class="navbar is-warning " role="navigation" aria-label="dropdown navigation">
        <div class="navbar-brand">
            <a class="navbar-item" href="http://getdrawings.com/confused-icon">
                <img src="@/assets/images/confused-icon-6.png" alt="Logo">
            </a>
            
        </div>

        <div class="navbar-menu">
            <div class="navbar-start">
                <template v-if="!$store.state.isAuthenticated">
                    <router-link to="/" class="navbar-item">Home</router-link>
                </template>

                <template v-else>
                    <router-link to="/dashboard" class="navbar-item">Home</router-link>    
                </template>

                <div class="navbar-item has-dropdown is-hoverable">
                    <a class="navbar-link">
                        Info
                    </a>

                    <div class="navbar-dropdown ">
                        <a class="navbar-item is-danger">
                             <router-link to="/getting-started" class="navbar-item">Getting Started</router-link> 
                        </a>
                        <a class="navbar-item">
                             <router-link to="/faq" class="navbar-item">FAQ</router-link> 
                        </a>
                    </div>
                </div>


                <div class="navbar-item has-dropdown is-hoverable">
                    <a class="navbar-link">
                        About Us
                    </a>

                    <div class="navbar-dropdown">
                        <a class="navbar-item">
                            Team
                        </a>
                    </div>
                </div>

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
                            Models
                        </a>

                        <div class="navbar-dropdown">
                            <!--
                            <a class="navbar-item">
                                <router-link to="/decision-trees" class="navbar-item">Decision Trees</router-link>
                            </a>
                            -->
                            <router-link to="/linear-regression" class="navbar-item">Linear Regression</router-link>
                            <a class="navbar-item">
                                Naive Bayes
                            </a>
                                
                            <!--
                            <a class="navbar-item">
                                Logistic Regression
                            </a>
                            <a class="navbar-item">
                                Neural Networks
                            </a>
                            -->
                        </div>
                    </div>

                    <div class="navbar-item has-dropdown is-hoverable">
                        <a class="navbar-link">
                            My Account
                        </a>

                        <div class="navbar-dropdown">
                            <router-link to="/dashboard/my-account" class="navbar-item">Account Page</router-link>
                            <a @click="logout()" class="navbar-item">Sign Out?</a>
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

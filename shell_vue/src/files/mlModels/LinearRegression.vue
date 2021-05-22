<template>
    <div class="container">
        <div class="column is-multiline">
            <div class="column is-12">
                <h1 class="title">Linear Regression</h1>
            </div>

            <div class="column is-6">
                <div class="box">


                    <p><strong>First Name: </strong>{{ details.first_name }}</p>
                    <p><strong>Last Name: </strong>{{ details.last_name }}</p>
                    <p><strong>Email: </strong>{{ details.email }}</p>
                    <p><strong>User id: </strong>{{ details.id }}</p>
                    
                </div>

                <div class="box">
                    <form >
                        <input type="file" id="myFile" name="filename">
                        <input type="submit" id = 'uploadFile'>
                    </form>
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
                details: []
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
                    
            }
        }
    }
</script>
<template>
    <div class="card column is-half is-offset-one-quarter" style="padding: 0px">
        <div class="card-image">
            <figure class="image is-3by3">
            <img src="https://i.ibb.co/1sfHctK/yello-blue-robots.jpg" alt="Placeholder image">
            </figure>
        </div>
        <header class="card-header">
            <p class="card-header-title is-centered" style="font-size:30px;">
            My Account Information
            </p>
        </header>
        <div class="column is-multiline">
            <div class="column is-12">
                <div>

                    <p><strong>Username: </strong>{{ details.username }}</p>
                    <p><strong>First Name: </strong>{{ details.first_name }}</p>
                    <p><strong>Last Name: </strong>{{ details.last_name }}</p>
                    <p><strong>Email: </strong>{{ details.email }}</p>
                    <p id="Get Date"><strong>Member Since: </strong>{{ details.date_joined }}</p>
                    
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'

    import {toast} from 'bulma-toast'

    export default {
        name: "MyAccount",
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

<style scoped>
.container{
    align-items: center;
    width: 50%;
    background-color: #a8dcec;
    margin: auto;
}

.title{
    text-align: center;

    background-color: #a8dcec;
    margin: auto;
}

.box{
    
    background-color:#fffcdc;
    font-size: 20px;
}

.subtitle{
    font-size: 25px;
    text-align: center;

}
</style>

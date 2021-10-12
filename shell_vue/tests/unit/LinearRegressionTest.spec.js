import NaiveBayesTests from '@/views/mlModels/NaiveBayes/NaiveBayesTesting.vue';
import { createStore } from 'vuex'
import { mount, flushPromises,  shallowMount  } from '@vue/test-utils'
import axios from 'axios'



const store = createStore({
    state: {
      isLoading: false,
      isAuthenticated: false,
      token: '',
    },
    mutations: {
      initializeStore(state){
        if(localStorage.getItem('token')){
          state.token = localStorage.getItem('token')
          state.isAuthenticated=true
        }
        else{
          state.token=''
          state.isAuthenticated=false
        }
      },
      setIsLoading(state,status){
        state.isLoading = status
      },
      setToken(state,token){
        state.token=token
        state.isAuthenticated=true
      },
      removeToken(state){
        state.token=''
        state.isAuthenticated=false
      }
    },
    actions: {
    },
    modules: {
    }
  })
const mockrouter = {
  push: jest.fn()
}

function factory(){
    return shallowMount(NaiveBayesTests,{
      global: { 
        plugins: [store]
      },
      data(){
        return{
        }
      }
    })
  }


describe('LinearRegressionDatasets.vue', () => {
    test('page renders',() => {
        const wrapper = factory()
        expect(wrapper.exists()).toBe(true)
      })

 

})

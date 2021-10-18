import { flushPromises, shallowMount } from '@vue/test-utils'
import NaiveBayesDatasets from '@/views/mlModels/NaiveBayes/NaiveBayesDatasets.vue'
import { createStore } from 'vuex'
import {mount} from '@vue/test-utils'
import { nextTick } from 'vue'
import axios from 'axios'

const store = createStore({
    state: {
      isLoading: false,
      isAuthenticated: false,
      token: '',
      created:false,
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


const mockAxiosGet = jest.spyOn(axios, "get")
mockAxiosGet.mockImplementation((url) => {return Promise.resolve() })
const mockAxiosPost = jest.spyOn(axios, "post")
mockAxiosPost.mockImplementation((url) => {return Promise.resolve() })
function factory(){
  return shallowMount(NaiveBayesDatasets,{
    global: { 
      plugins: [store]
    },
    mocks: {
    },
    data(){
      return{
        userDetails:{
          "id":1
        },
        selected:"file"
        
      }
    },
  })
}
describe('NaiveBayesTraining.vue', () => {

  it('page renders', () => {
    const wrapper = factory()
      expect(wrapper.exists()).toBe(true)
  })

  it('check wether the correct api call is made to get the user acount info',async()=>{
    const wrapper = factory()
    await flushPromises()
    expect(mockAxiosGet.mock.calls[0][0]).toBe('/api/v1/users/me')
  })
  it('check wether the correct api call is made to get the user datasets info',async()=>{
    const wrapper = factory()
    wrapper.vm.getUserDatasets()
    await flushPromises()
    expect(mockAxiosPost.mock.calls[0][0]).toEqual('/NaiveBayes/getDatasetsInfo',{
      'UserId':1,
    })
  })
  
})

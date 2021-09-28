import { shallowMount } from '@vue/test-utils'
import NaiveBayesTraining from '@/views/mlModels/NaiveBayes/NaiveBayesTraining.vue'
import { createStore } from 'vuex'
import {mount} from '@vue/test-utils'

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


function factory(){
  return shallowMount(NaiveBayesTraining,{
    global: { 
      plugins: [store]
    },
    data(){
      return{
        // trainingSeriesPredictedVSActual: trainingSeriesPredictedVSActual,
        // trainingOptionsPredictedVSActual: trainingOptionsPredictedVSActual,
        // showTrainingGraphs: true,
      }
    }
  })
}
describe('LinearRegression.vue', () => {

  it('page renders', () => {
    const wrapper = factory()
      expect(wrapper.exists()).toBe(true)
  })
//   test('training graphs render when train button clicked', async () => {
//     const wrapper = factory()
//     //wrapper.get method means that the test case will fail if the graph is not rendered i.e does not exist
//     const trainingGraph = wrapper.get("#trainingGraph") 
//   })
  
})

import LinearRegressionDatasets from '@/views/mlModels/LinearRegressionDatasets.vue'
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
const mockGet_UserDetails = {
  "data": {
    "id": 1,
    "email": "guest@guest.guest",
    "username": "guest",
    "first_name": "guest",
    "last_name": "guest",
    "date_joined": "2000-03-03T00:00:00Z"
  },
  "status": 200,
  "statusText": "OK",
  "headers": {
    "content-length": "133",
    "content-type": "application/json"
  },
  "config": {
    "url": "/api/v1/users/me",
    "method": "get",
    "headers": {
      "Accept": "application/json, text/plain, */*",
      "Authorization": "Token a590961f079feba520325c4c7b22986e06312347"
    },
    "baseURL": "http://127.0.0.1:8000",
    "transformRequest": [
      null
    ],
    "transformResponse": [
      null
    ],
    "timeout": 0,
    "xsrfCookieName": "XSRF-TOKEN",
    "xsrfHeaderName": "X-XSRF-TOKEN",
    "maxContentLength": -1,
    "maxBodyLength": -1,
    "transitional": {
      "silentJSONParsing": true,
      "forcedJSONParsing": true,
      "clarifyTimeoutError": false
    }
  },
  "request": {}
}
const mockPost_getDatasetsInfo={
  "data": {
    "1": {
      "id": 1,
      "filename": "CarPrice_Assignment.csv",
      "datapoints": 205,
      "columns": 26,
      "featureNames": [
        "car_ID",
        "symboling",
        "CarName",
        "fueltype",
        "aspiration",
        "doornumber",
        "carbody",
        "drivewheel",
        "enginelocation",
        "wheelbase",
        "carlength",
        "carwidth",
        "carheight",
        "curbweight",
        "enginetype",
        "cylindernumber",
        "enginesize",
        "fuelsystem",
        "boreratio",
        "stroke",
        "compressionratio",
        "horsepower",
        "peakrpm",
        "citympg",
        "highwaympg",
        "price"
      ],
      "nullValues": 0,
      "created": "2021-08-31 18:41",
      "Info": "Model not trained yet."
    },
    "2": {
      "id": 2,
      "filename": "Linear Regression - Sheet1.csv",
      "datapoints": 300,
      "columns": 2,
      "featureNames": [
        "X",
        "target"
      ],
      "nullValues": 0,
      "created": "2021-08-31 18:45",
      "MSE": 432.0431209771,
      "TrainAccuracy": 0.9426832298,
      "TestAccuracy": 0.8736248279
    }
  },
  "status": 200,
  "statusText": "OK",
  "headers": {
    "content-length": "752",
    "content-type": "application/json"
  },
  "config": {
    "url": "/datasets/getDatasetsInfo",
    "method": "post",
    "data": "{\"UserId\":1}",
    "headers": {
      "Accept": "application/json, text/plain, */*",
      "Authorization": "Token a590961f079feba520325c4c7b22986e06312347",
      "Content-Type": "application/json"
    },
    "baseURL": "http://127.0.0.1:8000",
    "transformRequest": [
      null
    ],
    "transformResponse": [
      null
    ],
    "timeout": 0,
    "xsrfCookieName": "XSRF-TOKEN",
    "xsrfHeaderName": "X-XSRF-TOKEN",
    "maxContentLength": -1,
    "maxBodyLength": -1,
    "transitional": {
      "silentJSONParsing": true,
      "forcedJSONParsing": true,
      "clarifyTimeoutError": false
    }
  },
  "request": {}
}

jest.mock('axios')

axios.get.mockImplementation((url) => {
  return Promise.resolve(mockGet_UserDetails)
})
axios.post.mockImplementation((url) => {
  return Promise.resolve(mockPost_getDatasetsInfo)
})
function factory(){
  return shallowMount(LinearRegressionDatasets,{
    global: { 
      plugins: [store],
      mocks:{
        $router: mockrouter
      }
  }
  })
}


describe('LinearRegressionDatasets.vue', () => {
  //add these back when buttons have been added
  // test('back arrow redirects to testing page', async () => {

  //   const wrapper = factory()
  //   // const backbutton = wrapper.find('#backButton')
  //   // expect(backbutton.exists()).toBe(true)
  //   await wrapper.find('#backButton').trigger('click')
  //   expect(mockrouter.push).toHaveBeenCalledWith('/linear-regression-tests')
  // })
  // test('forward arrow redirects to training page', async () => {
  //   const wrapper = factory()
  //   // const backbutton = wrapper.find('#backButton')
  //   // expect(backbutton.exists()).toBe(true)
  //   await wrapper.find('#forwardButton').trigger('click')
  //   expect(mockrouter.push).toHaveBeenCalledWith('/linear-regression')
  // })
  test('get request for user details after mount', async () => {
      const wrapper = factory()
      await flushPromises()
      expect(axios.get).toHaveBeenCalledWith('/api/v1/users/me')

  })
   test('page renders',() => {
    const wrapper = factory()
    expect(wrapper.exists()).toBe(true)
  })

 

})

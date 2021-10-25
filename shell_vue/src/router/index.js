import { createRouter, createWebHistory } from 'vue-router'

import store from '../store'

import Home from '../views/Home.vue'
import FAQ from '../views/FAQ.vue'
import GettingStarted from '../views/GettingStarted.vue'
import Register from '../views/Register.vue'
import LogIn from '../views/LogIn.vue'


import ForgotPassword from '../views/ForgotPassword.vue'
import ResetPassword from '../views/ResetPassword.vue'
import PublicDatasets from '../views/PublicDatasets.vue'

import Dashboard from '../views/dashboard/Dashboard.vue'
import MyAccount from '../views/dashboard/MyAccount.vue'

import DecisionTrees from '../views/DecisionTrees.vue'
import LinearRegression from '../views/mlModels/LinearRegression/LinearRegression.vue'
import LinearRegressionDatasets from '../views/mlModels/LinearRegression/LinearRegressionDatasets.vue'
import LinearRegressionTests from '../views/mlModels/LinearRegression/LinearRegressionTests.vue'



import NaiveBayesTraining from '../views/mlModels/NaiveBayes/NaiveBayesTraining.vue'
import NaiveBayesDatasets from '../views/mlModels/NaiveBayes/NaiveBayesDatasets.vue'
import NaiveBayesTests from '../views/mlModels/NaiveBayes/NaiveBayesTesting.vue'

import LogisticRegressionTraining from '../views/mlModels/LogisticRegression/LogisticRegressionTraining.vue'
import LogisticRegressionDatasets from '../views/mlModels/LogisticRegression/LogisticRegressionDatasets.vue'
import LogisticRegressionTests from '../views/mlModels/LogisticRegression/LogisticRegressionTesting.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/faq',
    name: 'FAQ',
    component: FAQ
  },
  {
    path: '/getting-started',
    name: 'GettingStarted',
    component: GettingStarted
  },
  {
    path: '/register',
    name: 'Register',
    component: Register
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/forgot-password',
    name: 'ForgotPassword',
    component: ForgotPassword
  },
  {
    path: '/reset-password/:uid/:token',
    name: 'ResetPassword',
    component: ResetPassword
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/my-account',
    name: 'MyAccount',
    component: MyAccount,
    meta: {
      requireLogin: true
    }
  }, 
  {
    path: '/public-datasets',
    name: 'PublicDatatsets',
    component: PublicDatasets,
    meta: {
      requireLogin: true,
    }    
  },
  {
    path: '/decision-trees',
    name: 'DecisionTrees',
    component: DecisionTrees,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/linear-regression-datasets',
    name: 'LinearRegressionDatasets',
    component: LinearRegressionDatasets,
    meta: {
      requireLogin: true,
      model: true,
      modelName: 'linReg',
      type: 0
    }
  },
  {
    path: '/linear-regression',
    name: 'LinearRegression',
    component: LinearRegression,
    meta: {
      requireLogin: true,
      model: true,
      modelName: 'linReg',
      type: 1
    }
  },
  {
    path: '/linear-regression-tests',
    name: 'LinearRegressionTests',
    component: LinearRegressionTests,
    meta: {
      requireLogin: true,
      model: true,
      modelName: 'linReg',
      type: 2
    }    
  },
  {
    path: '/naive-bayes-training',
    name: 'NaiveBayesTraining',
    component: NaiveBayesTraining,
    meta: {
      requireLogin: true,
      model: true,
      modelName: 'NaiveBayes',
      type: 2
    }    
  },
  {
    path: '/naive-bayes-datasets',
    name: 'NaiveBayesDatasets',
    component: NaiveBayesDatasets,
    meta: {
      requireLogin: true,
      model: true,
      modelName: 'NaiveBayes',
      type: 2
    }    
  },

  {
    path: '/naive-bayes-tests',
    name: 'NaiveBayesTests',
    component: NaiveBayesTests,
    meta: {
      requireLogin: true,
      model: true,
      modelName: 'NaiveBayes',
      type: 2
    }    
  },

  {
    path: '/logistic-regression-training',
    name: 'LogisticRegressionTraining',
    component: LogisticRegressionTraining,
    meta: {
      requireLogin: true,
      model: true,
      modelName: 'LogisticRegression',
      type: 1
    }    
  },
  {
    path: '/logistic-regression-datasets',
    name: 'LogisticRegressionDatasets',
    component: LogisticRegressionDatasets,
    meta: {
      requireLogin: true,
      model: true,
      modelName: 'LogisticRegression',
      type: 0
    }    
  },

  {
    path: '/logistic-regression-tests',
    name: 'LogisticRegressionTests',
    component: LogisticRegressionTests,
    meta: {
      requireLogin: true,
      model: true,
      modelName: 'LogisticRegression',
      type: 2
    }    
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to,from,next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated){
    next('/log-in')
  }
  else{
    next()
  }
})

router.afterEach((to, from) => {
  if(to.meta.model){
    // if(to.meta.type>from.meta.type || to.meta.type-from.meta.type==-2){
    // }
    if(to.meta.modelName==from.meta.modelName){
      to.meta.transitionName = (to.meta.type>from.meta.type || to.meta.type-from.meta.type==-2) && to.meta.type-from.meta.type!=2 ? 'slide-left' : 'slide-right'
    }

  }
})


export default router

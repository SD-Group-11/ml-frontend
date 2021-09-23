import { createRouter, createWebHistory } from 'vue-router'

import store from '../store'

import Home from '../views/Home.vue'
import FAQ from '../views/FAQ.vue'
import GettingStarted from '../views/GettingStarted.vue'
import Register from '../views/Register.vue'
import LogIn from '../views/LogIn.vue'


import ForgotPassword from '../views/ForgotPassword.vue'
import ResetPassword from '../views/ResetPassword.vue'

import Dashboard from '../views/dashboard/Dashboard.vue'
import MyAccount from '../views/dashboard/MyAccount.vue'

import DecisionTrees from '../views/DecisionTrees.vue'
import LinearRegression from '../views/mlModels/LinearRegression.vue'
import LinearRegressionDatasets from '../views/mlModels/LinearRegressionDatasets.vue'
import LinearRegressionTests from '../views/mlModels/LinearRegressionTests.vue'

import NaiveBayesTest from '../views/mlModels/NaiveBayesTest.vue'

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
    path: '/naive-bayes-test',
    name: 'NaiveBayesTest',
    component: NaiveBayesTest,
    meta: {
      requireLogin: true,
      model: true,
      modelName: 'linReg',
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

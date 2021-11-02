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
import LinearRegression from '../views/mlModels/LinearRegression/LinearRegression.vue'
import LinearRegressionDatasets from '../views/mlModels/LinearRegression/LinearRegressionDatasets.vue'
import LinearRegressionTests from '../views/mlModels/LinearRegression/LinearRegressionTests.vue'


import NaiveBayesTraining from '../views/mlModels/NaiveBayes/NaiveBayesTraining.vue'
import NaiveBayesDatasets from '../views/mlModels/NaiveBayes/NaiveBayesDatasets.vue'
import NaiveBayesTests from '../views/mlModels/NaiveBayes/NaiveBayesTesting.vue'

import LogisticRegressionTraining from '../views/mlModels/LogisticRegression/LogisticRegressionTraining.vue'
import LogisticRegressionDatasets from '../views/mlModels/LogisticRegression/LogisticRegressionDatasets.vue'
import LogisticRegressionTests from '../views/mlModels/LogisticRegression/LogisticRegressionTesting.vue'

import PublicDatasets from '../views/PublicDatasets.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    meta: {
      requireLogin: false,
      title: 'Welcome to MLFE'
    }
  },
  {
    path: '/faq',
    name: 'FAQ',
    component: FAQ,
    meta: {
      requireLogin: false,
      title: 'FAQ'
    }
  },
  {
    path: '/getting-started',
    name: 'GettingStarted',
    component: GettingStarted,
    meta: {
      requireLogin: false,
      title: 'Getting Started'
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
    path: '/register',
    name: 'Register',
    component: Register,
    meta: {
      requireLogin: false,
      title: 'Register'
    }
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: LogIn,
    meta: {
      requireLogin: false,
      title: 'Log In'
    }
  },
  {
    path: '/forgot-password',
    name: 'ForgotPassword',
    component: ForgotPassword,
    meta: {
      requireLogin: false,
      title: 'Forgot Password'
    }
  },
  {
    path: '/reset-password/:uid/:token',
    name: 'ResetPassword',
    component: ResetPassword,
    meta: {
      requireLogin: false,
      title: 'Reset Password'
    }
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
      requireLogin: true,
      title: 'MLFE Home'
    }
  },
  {
    path: '/dashboard/my-account',
    name: 'MyAccount',
    component: MyAccount,
    meta: {
      requireLogin: true,
      title: 'My Account'
    }
  },
  {
    path: '/decision-trees',
    name: 'DecisionTrees',
    component: DecisionTrees,
    meta: {
      requireLogin: true,
      title: 'Decision Trees'
    }
  },
  {
    path: '/linear-regression-datasets',
    name: 'LinearRegressionDatasets',
    component: LinearRegressionDatasets,
    meta: {
      requireLogin: true,
      title: 'Linear Regression Datasets',
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
      title: 'Linear Regression Training',
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
      title: 'Linear Regression Tests',
      model: true,
      modelName: 'linReg',
      type: 2
    }    
  },
  
  {
    path: '/naive-bayes-datasets',
    name: 'NaiveBayesDatasets',
    component: NaiveBayesDatasets,
    meta: {
      requireLogin: true,
      title: 'Naive Bayes Datasets',
      model: true,
      modelName: 'NaiveBayes',
      type: 0
    }    
  },

  {
    path: '/naive-bayes-training',
    name: 'NaiveBayesTraining',
    component: NaiveBayesTraining,
    meta: {
      requireLogin: true,
      title: 'Naive Bayes Training',
      model: true,
      modelName: 'NaiveBayes',
      type: 1
    }    
  },

  {
    path: '/naive-bayes-tests',
    name: 'NaiveBayesTests',
    component: NaiveBayesTests,
    meta: {
      requireLogin: true,
      title: 'Naive Bayes Tests',
      model: true,
      modelName: 'NaiveBayes',
      type: 2
    }    
  },

  {
    path: '/logistic-regression-datasets',
    name: 'LogisticRegressionDatasets',
    component: LogisticRegressionDatasets,
    meta: {
      requireLogin: true,
      title: 'Logistic Regression Datasets',
      model: true,
      modelName: 'LogisticRegression',
      type: 0
    }    
  },

  {
    path: '/logistic-regression-training',
    name: 'LogisticRegressionTraining',
    component: LogisticRegressionTraining,
    meta: {
      requireLogin: true,
      title: 'Logistic Regression Training',
      model: true,
      modelName: 'LogisticRegression',
      type: 1
    }    
  },

  {
    path: '/logistic-regression-tests',
    name: 'LogisticRegressionTests',
    component: LogisticRegressionTests,
    meta: {
      requireLogin: true,
      title: 'Logistic Regression Tests',
      model: true,
      modelName: 'LogisticRegression',
      type: 2
    }    
  },
  {
    path: '/model-comparison',
    name: 'ModelComparison',
    component: ModelComparison,
    meta: {
      requireLogin: true,
      model: true,
      modelName: 'ModelComparison',
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
    if(to.meta.modelName==from.meta.modelName){
      to.meta.transitionName = (to.meta.type>from.meta.type || to.meta.type-from.meta.type==-2) && to.meta.type-from.meta.type!=2 ? 'slide-left' : 'slide-right'
    }
  }
  
  if(to.meta.title){
    document.title = to.meta.title
  }

})


export default router

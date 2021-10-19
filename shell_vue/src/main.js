import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { fab } from '@fortawesome/free-brands-svg-icons'
import { far } from '@fortawesome/free-regular-svg-icons'
import { dom } from '@fortawesome/fontawesome-svg-core'
import VueFinalModal  from 'vue-final-modal'


library.add(fas);
library.add(fab);
library.add(far);
dom.watch();

axios.defaults.baseURL='https://mlfe-vue-app.herokuapp.com'

createApp(App).component('font-awesome-icon', FontAwesomeIcon).use(VueFinalModal()).use(store).use(router, axios).mount('#app')

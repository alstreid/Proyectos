import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import '../node_modules/bootstrap/dist/css/bootstrap.css'
import '../node_modules/bootstrap-icons/font/bootstrap-icons.min.css'


// import '../no/boostrap/dist/css/boostrap.css'
// import './assets/main.css'

const app = createApp(App)

app.use(router)

app.mount('#app')

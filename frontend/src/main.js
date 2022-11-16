import { createApp } from 'vue'
import { createWebHistory, createRouter } from "vue-router"

import "./style.css"
import App from './App.vue'
import Login from "./views/Login.vue"
import Home from "./views/Home.vue"
import Dashboard from "./components/Dashboard.vue"
import Planetas from "./components/Planetas.vue"
import Personagens from "./components/Personagens.vue"
import Naves from "./components/Naves.vue"
import Veiculos from "./components/Veiculos.vue"
import Usuarios from "./components/Usuarios.vue"
import InfoUser from "./components/InfoUser.vue"

const routes = [
  {
    path: "/",
    name: "Login",
    component: Login,
  },
  {
    path: "/home",
    name: "Home",
    component: Home,
    children: [
        { path: "dashboard", component: Dashboard },
        { path: "personagens", component: Personagens },
        { path: "planetas", component: Planetas },
        { path: "veiculos", component: Veiculos },
        { path: "naves", component: Naves },
        { path: "usuarios", component: Usuarios },
        { path: "info", component: InfoUser }
    ]
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

createApp(App).use(router).mount('#app')
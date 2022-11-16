<script>
import { setCookie } from '../services/cookies';

export default {
  data() {
    return {}
  },
  methods: {
    async logout(){
      setCookie("session_app_user","",-1)
      window.location.href = "/"
    }
  }
}
</script>

<template>
  <div class="container_navbar">
    <div class="container_navbar_list">
        <img src="./../assets/imagens/logo.png" alt="logo">
        <router-link to="/home/dashboard">
        <li>
            <img src="./../assets/imagens/dashboard_white.png" alt="dashboard_white">
            <span>Dashboard</span>
        </li>
        </router-link>
        <router-link to="/home/personagens">
        <li>
            <img src="./../assets/imagens/pesornagens_white.png" alt="pesornagens_white">
            <span>Personagens</span>
        </li>
        </router-link>
        <router-link to="/home/planetas">
        <li>
            <img src="./../assets/imagens/planetas_white.png" alt="planetas_white">
            <span>Planetas</span>
        </li>
        </router-link>
        <router-link to="/home/veiculos">
        <li>
            <img src="./../assets/imagens/veiculos_white.png" alt="veiculos_white">
            <span>Veiculos</span>
        </li>
        </router-link>
        <router-link to="/home/naves">
        <li>
            <img src="./../assets/imagens/naves_white.png" alt="naves_white">
            <span>Naves</span>
        </li>
        </router-link>
        <router-link to="/home/usuarios">
        <li>
            <img src="./../assets/imagens/usuarios_white.png" alt="usuarios_white">
            <span>Usuarios</span>
        </li>
        </router-link>
    </div>
    <div class="container_navbar_logout">
        <router-link to="/home/info">Usuario&nbsp|&nbsp</router-link>
        <a style="cursor: pointer;" @click="logout">Sair</a>
    </div>
    </div>
</template>

<style scoped>
  .container_navbar {
    width: 300px;
    height: 100vh;
    background-color: #000;
  }

  .container_navbar img {
    width: 100%;
    height: 100%;
  }

  .container_navbar a {
    margin: 20px;
  }
  .container_navbar a li {
    display: flex;
    justify-content: left;
    align-items: center;
    margin-left: 20px;
  }

  .container_navbar a li span {
    font-weight: 600;
    font-size: 1.2em;
    color: #FFF;
    margin-left: 20px;
  }

  .container_navbar a li img {
    width: 80px;
    height: 80px;
  }

  .container_navbar_logout {
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .container_navbar_logout a {
    font-weight: 600;
    font-size: 1em;
    color: #FFF;
    margin: 20px 0px 0px 0px;
    text-decoration: none;
  }
</style>

<script>
import { getCookie, setCookie } from '../services/cookies';

export default {
  data() {
    return {
      email: "",
      password: "",
      name: "",
      isStatusLogin: true
    }
  },
  methods: {
    statusLogin(){
      this.isStatusLogin = !this.isStatusLogin
    },
    
    async enviarFormulario(e){
      e.preventDefault();

      
      if(!!!this.email.trim()) return alert("Preencha todos os campos!")
      if(!!!this.password.trim()) return alert("Preencha todos os campos!")

      if(this.isStatusLogin){
        const data = new FormData();
        data.append("email", this.email)
        data.append("password", this.password)
        const response = await fetch("http://127.0.0.1:3000/app/login",{method: "POST", body: data })
        const person = await response.json()

        if(person.status){
          const data = person.email + "/" + person.name;
          setCookie("session_app_user",data,1);
          window.location.href = "/home/dashboard"
        }else{
          alert("Email ou senha invalidos!")
        }
      }else{
        if(!!!this.name.trim()) return alert("Preencha todos os campos!")
        
        const data = new FormData();
        data.append("email", this.email)
        data.append("password", this.password)
        data.append("name", this.name)
        const response = await fetch("http://127.0.0.1:3000/app/create",{method: "POST", body: data })
        const person = await response.json()

        if(!person.status) alert("Usuario não cadastrado!")
        else alert("Usuario cadastrado com sucesso!")
      }
    }

  },
  async created(){
    const cookies = getCookie("session_app_user");
    if(!!cookies.trim()) window.location.href = "/home/dashboard"
  }
}
</script>

<template>
    <main>
      <form method="post" @submit="enviarFormulario">
        <img src="src/assets/imagens/logo.png" class="logo" alt="logo" />
        <div class="container_options">
          <span :class="(isStatusLogin) ? 'active' : ''" @click="statusLogin">LOGIN</span>
          <span :class="(!isStatusLogin) ? 'active' : ''" @click="statusLogin">CADASTRAR</span> 
        </div>
        <div class="container_form_login" v-if="isStatusLogin">
          <input type="text" name="email" v-model="email" placeholder="Digite seu email"> 
          <input type="password" name="password" v-model="password" placeholder="Digite sua senha"> 
          <div style="width: calc(100% + 20px); display: flex; flex-direction: row-reverse;">
            <input type="submit" value="ENTRAR">
            <a href="http://127.0.0.1:3000/login"> <img src="src/assets/imagens/google.png" alt="" srcset=""> </a>
          </div>
        </div>
        <div class="container_form_login" v-else>
          <input type="text" name="name" v-model="name" placeholder="Digite seu nome"> 
          <input type="text" name="email" v-model="email" placeholder="Digite seu email"> 
          <input type="password" name="password" v-model="password" placeholder="Digite sua senha"> 
          <div style="width: calc(100% + 20px); display: flex; flex-direction: row-reverse;">
            <input type="submit" value="CADASTRAR">
          </div>
        </div>
      </form>
    </main>
</template>

<style scoped>
  main {
    display: flex;
    justify-content: center;
    align-items: center;
    background: #000;
    height: 100vh;
  }

  main form {
    display: flex;
    justify-content: center;
    align-items: flex-end;
    flex-direction: column;
    width: 400px;
  }

  main form img {
    width: 100%;
  }

  main form {
    display: flex;
    justify-content: center;
    align-items: center;
  }

  main form input {
    display: block;
    width: 100%;
    padding: 10px;
    border-radius: 4px;
    font-weight: 600;
    color: #000;
    margin: 4px 0px;
  }

  main form input[type="submit"] {
    width: 100px;
    color: #000;
    font-weight: 600;
    background-color: #FFE300;
    border: 0;
    cursor: pointer;
  }

  main form button {
    width: 100px;
    height: 36px;
    color: #000;
    font-weight: 600;
    background-color: #FFE300;
    border: 0;
    cursor: pointer;
    margin-top: 4px;
    border-radius: 4px;
    margin-left: 6px;
  }

  main form div a {
    width: 120px;
    height: 38px;
    margin-top: 2px;
    margin-right: 6px;
  }

  main form div a img {
    width: 100%;
    height: 100%;
    border-radius: 4px;
  }

  .container_options {
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 40px;
    width: calc(100% + 20px);
  }

  .container_options span {
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    color: #FFF;
    font-weight: 600;
  }

  .container_options .active {
    background-color: #FFE300;
    color: #000;
  }

  .container_form_login {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
  }
</style>

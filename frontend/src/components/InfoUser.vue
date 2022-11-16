<script>
import { getCookie } from '../services/cookies';

export default {
  data() {
    return {
      data: []
    }
  },
  methods: {},
  created(){
    this.data = getCookie("session_app_user").replace(/\"/g, '').split("/")
  }
}
</script>

<template>
   <div class="container_info">
      <div>
        <p>Informações do usuario</p>
        <label for="name">
          Nome:
          <input type="text" name="name" id="name" disabled :value="data[1]">
        </label>
        <label for="email">
          Email:
          <input type="text" name="email" id="email" disabled :value="data[0]">
        </label>
      </div>
   </div>
</template>

<style scoped>
  .container_info {
    display: flex;
    align-items: center;
    flex-direction: column;
    width: 100%;
    height: 100%;
    padding: 20px;
  }

  .container_info div {
    width: 60%;
    height: 400px;
    box-shadow: rgba(149, 157, 165, 0.2) 0px 8px 24px;
    border-radius: 4px;
    padding: 20px;
  }

  .container_info div input {
    width: 100%;
    height: 10px;
    margin: 10px 0px;
    padding: 10px;
  }

  .container_info div p {
    font-size: 1.2em;
    color: black;
    font-weight: 600;
  }
</style>

<script>
import Navbar from "../components/Navbar.vue"
import { getCookie } from "../services/cookies";

export default {
  components: {
    Navbar
  },
  data() {
    return {}
  },
  methods: {},
  created(){
    const cookies = getCookie("session_app_user");
    if(!!!cookies.trim()) window.location.href = "/"
  }
}
</script>

<template>
   <div class="container">
      <Navbar />
      <div class="container_content">
        <router-view />
      </div>
   </div>
</template>

<style scoped>
  .container {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .container_content {
    width: calc(100% - 300px);
    height: 100vh;
    overflow: hidden;
  }
</style>

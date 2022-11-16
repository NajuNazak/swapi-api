<script>
import { getUsuarios } from '../services/swapi';

export default {
  data() {
    return {
      data: [],
      statusNext: false,
      statusPrevious: false
    }
  },
  methods: {
    async previous(){
      const page = this.data.previous;
      this.data = await getUsuarios(page);
      this.statusNext = (!!this.data.next) ? true : false;
      this.statusPrevious = (!!this.data.previous) ? true : false;
    },
    async next(){
      const page = this.data.next;
      this.data = await getUsuarios(page);
      this.statusNext = (!!this.data.next) ? true : false;
      this.statusPrevious = (!!this.data.previous) ? true : false;
    }
  },
  async created(){
    const data = await getUsuarios();
    this.data = data
    this.statusNext = (!!data.next) ? true : false;
  }
}
</script>

<template>
   <div class="container_list">
      <p>Listagem de usuarios</p>
      <li v-for="d in data.results"><b>Nome:</b>{{d[1]}}</li>
      <div class="options">
        <button v-if="statusPrevious" @click="previous">Previous</button>
        <button v-if="statusNext" @click="next">Next</button>
      </div>
   </div>
</template>

<style scoped>
  .container_list {
    display: flex;
    align-items: flex-start;
    width: 100%;
    flex-direction: column;
    height: 100%;
    padding: 20px;
  }

  .container_list p {
    font-size: 1.2em;
    color: black;
    font-weight: 600;
  }

  .container_list li {
    height: 20px;
    width: calc(100% - 80px);
    display: flex;
    align-items: center;
    padding: 10px 20px;
    box-shadow: rgba(149, 157, 165, 0.2) 0px 8px 24px;
    border-radius: 4px;
  }

  .container_list li b {
    margin-right: 10px;
  }

  .options {
    width: calc(100% - 40px);
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 10px;
  }

  .options button {
    height: 40px;
    width: 80px;
    border-radius: 4px;
    border: 0px;
    background: #FFE300;
    font-size: 0.9em;
    font-weight: 600;
    cursor: pointer;
  }
</style>

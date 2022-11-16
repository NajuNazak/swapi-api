<script>
import {getPesonagens, getPlanetas, getVeiculos, getNaves} from './../services/swapi'

export default {
  data() {
    return {
        qtdPersonagens: 0,
        qtdPlanetas: 0,
        qtdNaves: 0,
        qtdVeiculos: 0
    }
  },
  methods: {},
  async created(){
    const personagens = await getPesonagens();
    this.qtdPersonagens = personagens.count;
    
    const planetas = await getPlanetas();
    this.qtdPlanetas = planetas.count;

    const naves = await getNaves();
    this.qtdNaves = naves.count;

    const veiculos = await getVeiculos();
    this.qtdVeiculos = veiculos.count;
  }
}
</script>

<template>
   <div class="container_dashboard">
        <div class="container_dashboard_card">
            <div class="container_dashboard_card_title">
                <span>Personagens</span>
            </div>
            <div class="container_dashboard_card_values">
                <span>{{qtdPersonagens}}</span>
                <img src="./../assets/imagens/pesornagens.png" alt="" srcset="">
            </div>
        </div>
        <div class="container_dashboard_card">
            <div class="container_dashboard_card_title">
                <span>Planetas</span>
            </div>
            <div class="container_dashboard_card_values">
                <span>{{qtdPlanetas}}</span>
                <img src="./../assets/imagens/planetas.png" alt="" srcset="">
            </div>
        </div>
        <div class="container_dashboard_card">
            <div class="container_dashboard_card_title">
                <span>Veiculos</span>
            </div>
            <div class="container_dashboard_card_values">
                <span>{{qtdVeiculos}}</span>
                <img src="./../assets/imagens/veiculos.png" alt="" srcset="">
            </div>
        </div>
        <div class="container_dashboard_card">
            <div class="container_dashboard_card_title">
                <span>Naves</span>
            </div>
            <div class="container_dashboard_card_values">
                <span>{{qtdNaves}}</span>
                <img src="./../assets/imagens/naves.png" alt="" srcset="">
            </div>
        </div>
   </div>
</template>

<style scoped>

    .container_dashboard {
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .container_dashboard_card{
        box-shadow: rgba(149, 157, 165, 0.2) 0px 8px 24px;
        width: 140px;
        height: 120px;
        margin: 20px;
        padding: 20px;
        border-radius: 4px;
        
    }

    .container_dashboard_card_title {
        text-align: center;
    }

    .container_dashboard_card_title span {
        font-weight: 600;
        font-size: 1.2em;
        color: #000;
    }

    .container_dashboard_card_values {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 10px;
    }

    .container_dashboard_card_values span {
        font-weight: 600;
        font-size: 3em;
        color: #FFE300;
    }

    .container_dashboard_card_values img {
        width: 80px;
        margin-left: 10px;
    }
</style>

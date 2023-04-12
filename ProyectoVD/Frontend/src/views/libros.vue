<script setup>
    import {ref} from 'vue'
    const data = ref([
        {
            titulo: "La Divina Comedia",
            autor: "Dante Alighieri",
            num_pag: "384",
            portada: "/src/assets/img01.jpg"
        },
        {
            titulo: "El principito",
            autor: "Antoine de Saint-Exupéry",
            num_pag: "120",
            portada: "/src/assets/img02.jpg"
        }
    ])
</script>
<template>
  <main>
    <h1>Libros</h1>
    <div v-for="(item,i) in data " v-bind:key="i" class="card" style="width: 18rem;">
        <img :src="item.portada" class="card-img-top" alt="...">
        <div class="card-body">
            <h5 class="card-title">{{ item.titulo }}</h5>
            <p class="card-text">{{ item.num_pag }}</p>
            <a href="#" class="btn btn-primary">{{item.autor}}</a>
        </div>
    </div>
  </main>
</template>

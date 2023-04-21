<script setup>
    import {onMounted, ref} from 'vue'
    import axios from 'axios'

   const data = ref();

   onMounted(
    axios.get('http://localhost:8000/api/libros')
    .then((result) =>{
        console.log(result.data);
        data.value = result.data;
    })
    .catch((error) => {
        console.log(error)
    })
   )
</script>

<template>
  <div class="container">
    <main>
        <h1>Libros</h1>
        <div v-for="(item,i) in data " v-bind:key="i" class="card" style="width: 18rem;">
            <img :src="item.portada" class="card-img-top" alt="...">
            <div class="card-body">
                <h5 class="card-title">{{ item.titulo }}</h5>
                <p class="card-text">{{ item.num_pag }}</p>
                <a href="#" class="btn btn-primary">{{item.autores[0]}} - Pags. {{ item.num_pag }}</a>
            </div>
        </div>
    </main>
  </div>
</template>

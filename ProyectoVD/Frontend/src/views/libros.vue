<script setup>
    import {onMounted, ref} from 'vue'
    import axios from 'axios'
    import router from '../router'

   const data = ref([{
    id: "",
    titulo: "",
    sinopsis: "",
    portada: "",
    fecha_publicacion: "",
    num_pag: "",
    genero: "",
    autores: [{}],
    calificacion: "",
   }])

   onMounted( () =>{
        axios.get('http://localhost:8000/api/libros')
        .then((result) =>{
            console.log(result.data);
            data.value = result.data;
        })
        .catch((error) => {
            console.log(error)
        })
    })
   function goToBook(id) {
        router.push ({name: 'libro', params: { id: id}})
    }
</script>

<template>
  <div class="container">
    <main>
        <h1>Libros</h1>
        <div v-for="(item,i) in data " v-bind:key="i" class="card" style="width: 18rem;" @click="goToBook(item.id)">
            <img :src="item.portada" class="card-img-top" alt="...">
            <div class="card-body">
                <h5 class="card-title">{{ item.titulo }}</h5>
                <p class="card-text">{{ item.fecha_publicacion }}</p>
                <p href="#" class="btn btn-primary">{{item.autores[0].nombre + " " + item.autores[0].apellido}} - Pags. {{ item.num_pag }}</p>
            </div>
        </div>
    </main>
  </div>
</template>

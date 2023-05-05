<script setup>
    import { onMounted, ref } from 'vue'
    import axios from 'axios'
import router from '../router';
    const props = defineProps (['id'])
    const libro = ref([{
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
        axios.get('http://localhost:8000/api/libros/'+props.id+'/')
        .then (result => {
            console.log(result.data)
            libro.value = result.data
        })
        .catch (error => {
            console.log(error)
        })
    })

    function eliminarLibro(){
        axios.delete('http://localhost:8000/api/libros/'+libro.value.id)
            .then(() => {
                router.push({name: 'libros'});
            })
            .catch(error =>{
                console.log(error)
            })
    }

    function editarLibro(){
        router.push({name: 'editar_libro', params: { id: props.id} });
    }
</script>

<template>
        <div class="container">
            <h1 class="mt-5">{{ libro.titulo }}</h1>
            <img :src="libro.portada">
            <p href="#">
                Autor: {{ libro.autores}} <br/>
                Páginas: {{ libro.num_pag }} <br/>
                Género: {{ libro.genero }} <br/>
            </p>
            <p>Sinopsis: {{ libro.sinopsis }}</p>
        </div>
        <button class="btn btn-primary" @click="eliminarLibro()">Eliminar</button>
        <button class="btn btn-primary" @click="editarLibro()">Editar</button>
</template>
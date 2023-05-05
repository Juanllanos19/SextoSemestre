<script setup>
    import { onMounted, ref } from 'vue';
    import axios from 'axios';
    import router from '../router';

    const props = defineProps(['id'])
    const libro = ref();

    onMounted(
        axios.get('http://localhost:8000/api/libros/'+props.id+'/')
            .then(result =>{
                libro.value = result.data
            })
            .catch(error =>{
                console.log(error)
            })
    )

    function editaLibro(){
        var info = {
            "titulo": libro.value.titulo,
            "num_pag": libro.value.num_pag,
            "sinopsis": libro.value.sinopsis,
            "fecha_publicacion": libro.value.fecha_publicacion,
            "genero": libro.value.genero.id,
            "autores": [libro.value.autores[0].id]
        };
        var headers = {'Content-type': 'application/json'};
            axios.put('http://localhost:8000/api/libros'+props.id+'/', info, headers)
            .then(result => {
                console.log(result.data)
                router.push({name: 'libros'})
            })
            .catch(error => {
                console.log(error)
            })
    }
</script>

<template>
    <div class="container">
        <h1 class="mt-5">Edita el libro</h1>
        <form @submit.prevent="editaLibro()">
            <div class="mb-3">
                <label class="form-label">Título</label>
                <input type="text" class="form-control" v-model="libro.titulo">
            </div>
            <div class="mb-3">
                <label class="form-label">Páginas</label>
                <input type="text" class="form-control" v-model="libro.num_pag">
            </div>
            <div class="mb-3">
                <label class="form-label">Sinopsis</label>
                <input type="text" class="form-control" v-model="libro.sinopsis">
            </div>
            <button type="submit" class="btn btn-primary">Editar</button>
        </form>
    </div>
</template>
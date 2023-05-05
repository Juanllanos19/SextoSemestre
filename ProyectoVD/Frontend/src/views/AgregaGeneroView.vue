<script setup>
    import {ref} from 'vue'
    import axios from 'axios'

    const nombre = ref();

    function agregaGenero(){
        var genero = {"nombre": nombre.value};
        var headers = {'Content-Type': 'application/json'};
        axios.post('http://localhost:8000/api/generos/', genero, headers)
            .then(result => {
                console.log(result.data)
            })
            .catch(error =>{
                console.log(error)
            })
    }
</script>

<template>
    <div class="container">
        <h1 class="mt-5">Agrega un nuevo género</h1>
        <form @submit.prevent="agregaGenero()">
            <div class="mb-3">
                <label class="form-label">Nombre del género</label>
                <input type="text" class="form-control" v-model="nombre">
            </div>
            <button type="submit" class="btn btn-primary">Agregar</button>
        </form>
    </div>
</template>
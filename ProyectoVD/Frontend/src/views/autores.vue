<script setup>
    import {ref} from 'vue'
    const data = ref([
        {
            Nombre: "Dante",
            Apellido: "Alighieri",
            FechaDeNacimiento: "29/05/1265",
            portada: "/src/assets/img03.jpg"
        },
        {
            Nombre: "Antoine",
            Apellido: "De Saint-Exupéry",
            FechaDeNacimiento: "29/06/1900",
            portada: "/src/assets/img04.jpg"
        }
    ])
</script>

<template>
  <div class="container">
    <main>
        <h1>Autores</h1>
        <div v-for="(item,i) in data " v-bind:key="i" class="card" style="width: 18rem;">
            <img :src="item.portada" class="card-img-top" alt="...">
            <div class="card-body">
                <h5 class="card-title">{{ item.Nombre }}</h5>
                <p class="card-text">{{ item.Apellido }}</p>
                <a href="#" class="btn btn-primary">{{item.FechaDeNacimiento}}</a>
            </div>
        </div>
        <table class="table">
          <thead>
            <tr>
              <th scope="col">#</th>
              <th scope="col">Nombre</th>
              <th scope="col">Apellido</th>
              <th scope="col">Fecha de Nacimiento</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(item,i) in data " v-bind:key="i">
              <th scope="row">{{ i + 1 }}</th>
              <td>{{ item.Nombre }}</td>
              <td>{{ item.Apellido }}</td>
              <td>{{ item.FechaDeNacimiento }}</td>
            </tr>
          </tbody>
        </table>
    </main>
  </div>
</template>

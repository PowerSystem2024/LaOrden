<script setup>


const title = 'Ortiz Nicolas';
const descripcion = 'Estudiante de Tecnicatura en Programacion - UTN';
const residencia = 'San Rafael, Mendoza. Argentina';
const presentacion = '¡Bienvenidos a mi portfolio!';
const redesSociales = [
    {id: 1, name: 'Instagram', src:'/src/assets/instagram_icon.svg', url: 'https://instagram.com'}
]
const telefono = '+54 9 2604-452653'

</script>

<template>

<section class="datos-personales">
    <did class="card">
        <h1>{{ title }}</h1>
        <h2>{{ descripcion }}</h2>
        <p>{{ presentacion }}</p>
        <ul class="container-lista">
            <li v-for="red in redesSociales" :key="red.id">
                <a :href="red.url"><img class="icon-redsocial" :src="red.src" width="35rem" :alt="red.name"></a>
            </li>
            <li><a href=""><img class="icon-redsocial" src="" width="35rem" alt="">Curriculum vitae</a></li>
        </ul>
        <h3> Mi telefono personal {{ telefono }}</h3>
        <h4>{{ residencia }}</h4>
    </did>
</section>

</template>

<style scoped>
h1 {
    font-size: 2.5rem
}
</style>
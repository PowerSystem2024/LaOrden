<script setup>
import img1 from '/src/components/icons/js.svg';
import img2 from '/src/components/icons/python.svg';
import img3 from '/src/components/icons/html-css.svg';
import img4 from '/src/components/icons/java.svg';
import img5 from '/src/components/icons/sql.svg';
import img6 from '/src/components/icons/react.svg';
import img7 from '/src/components/icons/vue.svg';
import img8 from '/src/components/icons/node.svg';
import img9 from '/src/components/icons/django.svg';
import img10 from '/src/components/icons/bootstrap.svg';
import img11 from '/src/components/icons/git.svg';
import img12 from '/src/components/icons/docker.svg';
import img13 from '/src/components/icons/cypress.svg';
import img14 from '/src/components/icons/figma.svg';
import img15 from '/src/components/icons/visual.svg';
import img16 from '/src/components/icons/mongo.svg';
import img17 from '/src/components/icons/mysql.svg';
import img18 from '/src/components/icons/postgres.svg';
import img19 from '/src/components/icons/arg.svg';
import img20 from '/src/components/icons/eeuu.svg';
import img21 from '/src/components/icons/office.svg';

import {ref} from 'vue';
const habilidades = ref([
    {
        id: 1, nombre: 'Lenguajes de Programación', habilidades: [
            {id: 1, nombre: 'JavaScript', nivel:'Avanzado', icono: img1},
            {id: 2, nombre: 'Java', nivel:'Intermedio', icono: img4},
            {id: 3, nombre: 'Python', nivel:'Avanzado', icono: img2}
        ]
    },
    {
        id: 2, nombre: 'Herramientas y Software', habilidades: [
            {id: 1, nombre: 'Visual Studio Code', nivel:'Avanzado', icono: img15},
            {id: 2, nombre: 'Git', nivel:'Avanzado', icono: img11},
            {id: 3, nombre: 'Paquete Office', nivel:'Avanzado', icono: img21}
    ]
    },
    {
        id: 3, nombre: 'Idiomas', habilidades: [
            {id: 1, nombre: 'Español', nivel:'Avanzado', icono: img19},
            {id: 2, nombre: 'Ingles', nivel:'Basico', icono: img20}
    ]
    }


])
</script>

<template>
<div class="skills-contenedor">
    <div v-for= "habilidad in habilidades" :key="habilidad.id" class="skills-categoria">
        <h3>{{habilidad.nombre}}</h3>
        <ul class="skills">
            <li v-for="habilidad in habilidad.habilidades" :key="habilidad.id" class="skill">
                <img :src="habilidad.icono" :alt="habilidad.nombre">
                <span>{{habilidad.nombre}}: {{ habilidad.nivel }}</span>
            </li>

        </ul>
    </div>
  </div>
</template>

<style scopped>
.skills-contenedor{
    padding: 2rem;
    background-color: rgb(28, 41, 52);
}
.skills-categoria{
    margin-bottom: 20px;
}
.skills-categoria h3{
    display: flex;
    justify-content:left;
    margin-bottom: 10px;
    font-size: 1.5em;
    color: aliceblue;
    font-size: 1.5em;
    font-weight: bold;
}
.skills{
    display: flex;
    justify-content: space-evenly;
    flex-wrap: wrap;
    gap: 20px;
}
.skill{
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 10px;
    background-color: rgba(241, 245, 243, 0.856);
    padding: 0.3em;
    border-radius:8px;
    box-shadow: 0px 4px 12px rgba(2, 151, 151, 0.963);
    flex: 1 1 200px;
    max-width: 250px;
}
.skill:hover{
    background-color: rgba(2, 151, 151, 0.963);
}
.skill img{
    width: 35px;
    height: 35px;
}
.skill span{
    font-size: 1em;
    color: #333;
}
.skill:hover{
    font-size: 1.3em;
    transition: 2s ease;
}
@media (max-width: 768px){
    .skills-categoria h3{
        justify-content: center;
    }
    .skill{
        justify-content: center;
    }
}
</style>
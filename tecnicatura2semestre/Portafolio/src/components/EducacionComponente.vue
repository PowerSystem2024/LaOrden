<script setup>
import { ref } from "vue";
const fechaColor = ref([]);
/*Esta es otra forma de utilizar el arreglo, con el metodo value*/
fechaColor.value = [
  { color: "#41516c" },
  { color: "#FBCA3E" },
  { color: "#E24A68" },
  { color: "#1B5F8C" },
  { color: "#4CADAD" },
];
/*Esta es la forma de utilizar el arreglo, sin el metodo value*/
const educacion = ref([
  {
    fecha: "2025",
    title: "Tecnicatura Universitaria en Programacion",
    universidad: "Universidad Tecnologica Nacional",
  },
  {
    fecha: "2023",
    title: "Desarrollador Java",
    universidad: "Universidad de la Punta",
  },
  {
    fecha: "2019",
    title: "Arquitecto",
    universidad: "Universidad Catolica de Santa Fe",
  },
  {
    fecha: "2011",
    title: "Tecnico en reparacion de computadoras",
    universidad: "IESA",
  },
  {
    fecha: "2011",
    title: "Lengua Inglesa",
    universidad: "Instituto Play and Learn",
  },
]);
</script>

<template>
<div class="card">
    <ul>
      <li
        v-for="(item, index) in educacion"
        :key="index"
        :style="{ '--fecha-color': fechaColor[index].color }"
      >
        <div class="fecha">{{ item.fecha }}</div>
        <div class="title">{{ item.title }}</div>
        <div class="universidad">{{ item.universidad }}</div>
      </li>
    </ul>
  </div>
</template>

<style scoped>
.card {
  background:linear-gradient(180deg,rgb(249, 245, 241), rgb(227, 223, 220));
  border-radius: 30px;
  text-align: center;
  transition: transform 0.6s ease;
  transition: transform 0.8s ease, box-shadow 0.3s ease;
  box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.2);
}
.card:hover {
  transform: scale(1.01);
  box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.2);
    }




div{
  text-align: left;
  font-family:system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  font-size: 1rem;
  font-weight: 600;
  padding: 5px 12px;
  margin: 0px;


}
.fecha{
  font-family:system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  font-size:2rem;
  font-weight: 600;
}
ul{
  margin:0px;
  padding: 20px;
}
.title,.universidad{
  color: rgb(121, 121, 121);
}
li{
  margin:0px 0px 20px 0px
}
</style>

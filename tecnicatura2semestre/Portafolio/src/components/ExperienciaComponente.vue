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
const experiencias = ref([
  {
    puesto: "Landscape Designer",
    empresa: "Yardzen",
    fecha: "2022 - actualidad",
    ubicacion: "California, USA",
  },
  {
    puesto: "Renderista",
    empresa: "Von Tharigen estudio",
    fecha: "2023 - actualidad",
    ubicacion: "Buenos Aires, Argentina",
  },
  {
    puesto: "Fundador",
    empresa: "Estudio Matva",
    fecha: "2021",
    ubicacion: "Misiones, Argentina",
  },
  {
    puesto: "Responsable de obra",
    empresa: "Dinarco",
    fecha: "2021 - 2022",
    ubicacion: "Misiones, Argentina",
  },
  {
    puesto: "Diseñador",
    empresa: "Estudio Fohrholtz",
    fecha: "2016 - 2020",
    ubicacion: "Misiones, Argentina",
  },
]);
</script>

<template>
  <div class="card">
    <ul>
      <li
        v-for="(item, index) in experiencias"
        :key="index"
        :style="{ '--fecha-color': fechaColor[index].color }"
      >
        <div class="puesto">{{ item.puesto }}</div>
        <div class="empresa">{{ item.empresa }}</div>
        <div class="fecha">{{ item.fecha }}</div>
        <div class="ubicacion">{{ item.ubicacion }}</div>
      </li>
    </ul>
  </div>
</template>

<style scoped>
.card {
  background: linear-gradient(100deg, rgb(199, 219, 218), rgb(127, 163, 165));
  border-radius: 30px;
  text-align: center;
  transition: transform 0.8s ease, box-shadow 0.3s ease;
  box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.2);
}

.card:hover {
  transform: scale(1.01);
  box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.2);
}
div {
  text-align: left;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
    Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  font-size: 1rem;
  font-weight: 600;
  padding: 5px 12px;
  margin: 0px;
}
.puesto {
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
    Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  font-size: 2rem;
  font-weight: 600;
}
.empresa,
.fecha,
.ubicacion {
  color: rgb(120, 120, 120);
}
ul {
  margin: 0px;
  padding: 20px;
}
li {
  margin: 0px 0px 20px 0px;
}
</style>

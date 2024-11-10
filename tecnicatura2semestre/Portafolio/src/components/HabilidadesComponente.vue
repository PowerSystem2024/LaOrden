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
    categoria: "Lenguajes",
    id1: "JavaScript. Intermedio.",
    id2: "Java. Intermedio",
    id3: "Python. Intermedio",
    id4: "HTML. Avanzado ",
    id5: "CSS. Intermedio",
  },
  {
    categoria: "Herramientas",
    id1: "Git. Avanzado.",
    id2: "Notion. Avanzado.",
    id3: "Jira. Avanzado.",
    id4: "Visual Studio Code. Avanzado.",
  },
  {
    categoria: "Frameworks",
    id1: "React. Basico.",
    id2: "Vue js. Intermedio ",
    id3: "Node js. basico",
  },
  {
    categoria: "Base de datos",
    id1: "MariaDB. Intermedio",
    id2: "MySQL. basico",
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
        <div class="categoria">{{ item.categoria }}</div>
        <div class="id1">{{ item.id1 }}</div>
        <div class="id2">{{ item.id2 }}</div>
        <div class="id3">{{ item.id3 }}</div>
        <div class="id4">{{ item.id4 }}</div>
        <div class="id5">{{ item.id5 }}</div>
      </li>
    </ul>
  </div>
</template>

<style scoped>
.card {
  background:black;
  background-image: url(./imagenfondo.png);
  background-size: 120%;
  border-radius: 30px;
  text-align: center;
  background-repeat: no-repeat;
  background-position: 450px 100px;
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
  color: white;
}
.categoria {
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
    Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  font-size: 2rem;
  font-weight: 600;
}
.id1,
.id2,
.id3,
.id4,
.id5 {
  color: rgb(135, 135, 135);
}
ul {
  margin: 0px;
  padding: 20px;
}
li {
  margin: 0px 0px 20px 0px;
}
</style>

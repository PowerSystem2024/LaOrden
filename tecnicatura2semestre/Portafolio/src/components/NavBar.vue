<template>
  <nav class="navbar">
    <div class="navbar-menu">
      <ul>
        <!--Se coloco el operador v-bind al atributo href utilizando su minima expreción el operador : / y se soluciono el enlace a las distintas secciones-->
        <a
          v-for="nav in navegacion"
          :key="nav.nombre"
          :href="nav.enlace"
          class="nav-item"
          >{{ nav.nombre }}</a
        >
      </ul>
    </div>
  </nav>
</template>

<script setup>
import { ref } from "vue";
const navegacion = ref([
  { id: 1, nombre: "Educación", enlace: "#educacion" },
  { id: 2, nombre: "Experiencia", enlace: "#experiencia" },
  { id: 4, nombre: "Habilidades", enlace: "#habilidades" },
]);
</script>

<style scoped>
.navbar {
  background-color: rgb(
    250,
    250,
    252
  ); /* Establece el color de fondo usando una variable CSS */
  color: rgb(29, 29, 31); /* Establece el color del texto en blanco */
  padding: 1rem 1rem; /* Añade un padding de 0.5rem arriba y abajo, y 1rem a los lados */
  align-items: center; /* Centra verticalmente los elementos dentro de la navbar */

}

.navbar-item {
  color: rgb(0, 0, 0); /* Establece el color del texto en blanco */
text-decoration: none;
  margin-right: 1rem; /* Añade un margen derecho de 1rem entre los elementos */
}

.navbar-menu {
  display: flex; /* Organiza los elementos en línea usando flexbox */
  justify-content: flex-end; /* Alinea los elementos al final de la navbar */

}

.nav-list {
  list-style: none; /* Elimina los puntos o números de las listas */

}

a {
  padding: 5px; /* Añade un padding de 5px alrededor del contenido */
  color: rgb(0, 0, 0);
  font-family:system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  font-weight: 500;
  text-decoration: none;
}

a:hover {
  background-color: rgb(
    250,
    250,
    252
  ); /* Cambia el color de fondo al pasar el mouse sobre un enlace */
}

@media (max-width: 768px) {
  .navbar-menu {
    display: flex; /* Organiza los elementos en línea usando flexbox */
    justify-content: flex-end; /* Alinea los elementos al final de la navbar */
    width: 100%; /* Asegura que la navbar ocupe el 100% del ancho en pantallas pequeñas */
  }
}
</style>

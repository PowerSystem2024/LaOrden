<script setup>

//puro js
import DatosPersonales from './components/DatosPersonales.vue';
import Educacion from './components/Educacion.vue';
import HelloWorld from './components/HelloWorld.vue'
import NavBar from './components/NavBar.vue';
import TheWelcome from './components/TheWelcome.vue'
</script>

<template>
  <!--html-->
  <header>
    <!-- Barra de Navegación -->
     <NavBar></NavBar>
     <!-- Componente de Datos Personales  -->
      <DatosPersonales></DatosPersonales>

    <img alt="Vue logo" class="logo" src="./assets/logo.svg" width="125" height="125" />

    <div class="wrapper">
      <HelloWorld msg="You did it!" />
    </div>
  </header>

  <main>
    <TheWelcome />

    <section id="educacion"><h2> Educacion - Cursos</h2>
      <Educacion />
    </section>
    <section id="experiencia"><h2> Experiencia </h2></section>
    <section id="proyectos"><h2> Proyectos </h2></section>
    <section id="habilidades"><h2> Habilidades </h2></section>
    <section id="intereses"><h2> Intereses </h2></section>
  </main>
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>

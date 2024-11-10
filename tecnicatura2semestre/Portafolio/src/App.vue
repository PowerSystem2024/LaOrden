<script setup>
import NavBar from "./components/NavBar.vue";
import DatosPersonales from "./components/DatosPersonales.vue";
import Educacion from "./components/EducacionComponente.vue";
import ExperienciaComponente from "./components/ExperienciaComponente.vue";
import HabilidadesComponente from "./components/HabilidadesComponente.vue";
</script>

<template>
  <header id="top">
    <!--Barra de Navegacion-->
    <NavBar />
    <!--Componente Datos Personales-->

    <DatosPersonales />
  </header>
  <main>
    <!--el estilo css de section se encuentra en base.css-->
    <section id="educacion">
      <h2>Educación.</h2>
      <!--Componente Educación-->
      <Educacion />
    </section>
    <section id="experiencia">
      <h2>Experiencia.</h2>
      <!--Componente Experiencia-->
      <ExperienciaComponente />
    </section>
    <section id="habilidades">
      <!--Componente Habilidades-->
      <h2>Habilidades</h2>
      <HabilidadesComponente />
    </section>
  </main>
  <footer>
    <p>© 2024 Leandro Enriquez - Portafolio web</p>
    <span class="separator">|</span>
    <a class="link" href="https://github.com/enriquezleandro" title="GitHub"
      >GitHub</a
    >
    <span class="separator">|</span>
    <a class="link" href="https://www.linkedin.com/in/enriquezleandro/"
      >Linkedin</a
    >
    <span class="separator">|</span>
    <a class="link" href="https://www.instagram.com/enriquezleandro/"
      >Instagram</a
    >
  </footer>
</template>

<style scoped>
footer {
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
    Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  font-weight: 100;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  padding: 2rem;
  font-size: 0.9rem;
  color: rgb(108, 108, 108);
  border-top: 1px solid #ccc;
  display: flex;
}
.separator {
  color: #666;
  margin: 4px 4px;
  padding: 2px 2px;
}
.link {
  text-decoration: none;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
    Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  font-weight: 400;
  color: rgb(108, 108, 108);
}
.link:hover {
  text-decoration: underline;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
    Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  font-weight: 400;
  color: rgb(108, 108, 108);
}
h2 {
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
    Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  font-weight: 600;
  font-size: 3rem;
  color: rgb(29, 29, 31);
  text-align: left;
  font-size: 3rem;
}
</style>

<script setup>


const title = 'La Orden';
const presentacion = '¡Bienvenidos a La Orden, nuestro espacio de crecimiento y colaboración! Somos un grupo de estudiantes de la Universidad Tecnológica Nacional con una fuerte pasión por la programación, la tecnología, y la innovación. Aquí, nos dedicamos a explorar nuevas ideas, compartir conocimiento y desarrollar proyectos emocionantes que reflejan nuestro aprendizaje y creatividad. A través de nuestros repositorios en GitHub, podrás ver el fruto de nuestro esfuerzo colectivo, desde soluciones tecnológicas innovadoras hasta proyectos desafiantes. Únite a nosotros en este viaje de descubrimiento y aprendizaje continuo, donde cada línea de código es una oportunidad para crecer y cada proyecto es un paso más hacia el futuro. ¡Explora nuestro trabajo y sé parte de La Orden!';

</script>

<template>
  <section class="datos-personales">
    <h1>{{ title }}</h1>
    <div class="card">

      <h4>{{ presentacion }}</h4>
    </div>
  </section>
</template>

<style scoped>
h1 {
  font-family:system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  font-weight: 600;
  font-size: 3rem;
  color: rgb(29, 29, 31);
  text-align: left;
  margin: 0;
  padding: 0;
}
.card {
  background:linear-gradient(135deg,rgb(238, 75, 44), rgb(72, 123, 240));
  margin: auto;
  margin-top: 10px;
  transition: transform 0.8s ease, box-shadow 0.3s ease;
  box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.2);
  border-radius: 25px;
  padding: 20px;
  box-sizing: border-box;
  font-family: sans-serif;
  color: #444;
  text-align: center;
}
.card:hover {
  transform: scale(1.01);
  box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.2);
    }

.container-lista {
  display: flex;
  justify-content: center;
  list-style: none;
  padding: 0;
  margin: 0;
  text-align: right;
}

h2{
  font-family:system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  font-weight: 600;
  font-size: 2rem;
  color: rgb(255, 255, 255);
  text-align: left;
  padding: 5px 12px;
  margin: 0;
}
h4{
  text-align: left;
  font-family:system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  font-size: 1rem;
  font-weight: 600;
  padding: 5px 12px;
  margin: 0px;
  color: white;
}
</style>

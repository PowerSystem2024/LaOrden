/*
//while
let contador = 0;
while (contador < 3) {
  console.log(contador);
  contador++;
}
console.log("Fin del ciclo while");

//do while
let conteo = 0;
do {
  console.log(conteo);
  conteo++;
} while (conteo < 3);

console.log("Fin del cilo do while");

//for
//Se pueden declarar mas de una variable dentro del cilo for espaciandolas con una coma,
for (let contando = 0; contando < 3; contando++) {
  console.log(contando);
}
console.log("Fin del cilo for");

//palabra reservada break
for (let contando = 0; contando <= 10; contando++) {
  if (contando % 2 == 0) {
    console.log(contando);
    break; //Con esto el ciclo termina al haber encontrado la primera coincidencia, una vez encontrado rompe el ciclo y sale
  }
}

console.log("Termina el ciclo al encontrar pares");
*/
//Palabra reservada continue
for (let contando = 0; contando <= 10; contador++) {
  if (contando % 2 !== 0) {
    continue; //Ira a la siguiente iteracion
  }
  console.log(contando);
}

//Etiquetas label
//Nos permite ir a una parte especifica de nuestro programa, asi como continue pero a un lugar especifico programacion tipo go to(no son recomendadas)
inicio:
for (let contando = 0; contando <= 10; contador++) {
    if (contando % 2 !== 0) {
      continue inicio; //Ira a la siguiente iteracion
    }
    console.log(contando);
  }
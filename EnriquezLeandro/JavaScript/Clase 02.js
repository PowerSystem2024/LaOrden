//Array

//Sintaxis vieja
//let autos = new Array("Ferrari", "Renault", "BMW");

//Sintaxis nueva
const autos = ["Ferrari", "Renault", "BMW"];
console.log(autos);

//Recorremos los elementos del array
//forma manual
console.log(autos[0]);
//con ciclo for
for (let i = 0; i < autos.length; i++) {
  console.log(i + 1 + ": " + autos[i]);
}

//Modificamos los elementos del array
autos[1] = "Volvo";
console.log(autos[1]);

//Agregamos nuevos valores al array
//Forma 1
autos.push("Tesla");
console.log(autos);

//Forma 2
autos[autos.length] = "Porche";
console.log(autos);

//Forma 3
//Aca hay que tener cuidado porque al indicar mal el indice podes sobrescribir o saltear un lugar como en este caso
autos[6] = "Ranch";
console.log(autos);

//Como preguntar si es un array
console.log(typeof autos); //Esto solo nos aclara que es un objeto
console.log(Array.isArray(autos)); //En este caso nos devuelve un booleano si es un arreglo
console.log(autos instanceof Array); //Es muy similar al isArray

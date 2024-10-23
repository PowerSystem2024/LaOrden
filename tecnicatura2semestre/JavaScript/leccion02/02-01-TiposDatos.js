// Tipos de datos de JavaScript
/*
La sintaxis en lo que es comentarios
es muy similar a la de java
realmente diriamos que es identica
*/
var nombre = 'Luciana'; //tipo str
console.log(nombre);

var numero = 3000; //tipo numerico
console.log(numero);

var objeto = {
    nombre : "Luciana",
    apellido : "Fragueiro",
    telefono : "234354253"
}
console.log(objeto)

//tipo de dato boolean
var bandera = true;
console.log(bandera);

//Tipo de dato funcion
function miFuncion(){}
console.log(typeof miFuncion);

//tipo de dato symbol
var simbolo = Symbol("Mi simbolo");
console.log(typeof simbolo);

//Tipo de dato undefined
var x;
console.log(x);

x = undefined;
console.log(typeof x);

//null: significa ausencia de valor
var y = null; 
console.log(typeof y);

//Tipo de dato array y empty string
var autos = ['Citroen','Audi','BMW','Ford']
console.log(autos);
console.log(typeof autos); //preguntamos que tipo de dato es

var z = '';
console.log(z); //esto es una cadena vacia
console.log(typeof z)


////while
//let contador = 0;
//while(contador<3){
//    console.log(contador);
//    contador++;
//} 
//console.log("Fin del ciclo while");
////do while
//let conteo = 0;
//do{
//    console.log(conteo);
//    contador++;
//}while(conteo < 3);
//console.log("Fin del ciclo do while");
////for
//for(let contando = 0; contando > 3; contando++){
//    console.log(contando)
//}
//console.log("Fin de el ciclo for")
//// Palabra reservada break 
//for(let contando = 0; contando <= 10; contando++){
//    if(contando % 2 == 0){
//        console.log(contando);
//        break;
//    }
//}
//console.log("Terminando el ciclo al encontrar los pares")
////palabra continue y etiquetas labels
//for(let contando = 0; contando <= 10; contando++){
//    if(contando % 2 == 0){
//        console.log(contando);
//        continue;
//    }
//}
//console.log("Terminando el ciclo al encontrar los pares")
//for (var i=10;i=0;i--){
//    console.log("numero" + i)
//}
//var respuesta = window.prompt("Ya te susccribiste a todo code?", "Si ya estoy suscripto");
//
//alert("Su respuesta fue " + respuesta)
//var confirmacion = window.confirm("estas subscripto a Plas?")
//
//
//if (confirmacion == true){
//    alert("Muchas gracias");
//}
//else{
//    alert("Pegate un tiro mogolico");
//}
//const autos = ["Ferrari", "Renault", "BMW"];
//console.log(autos);
//
/////Recorremos los elementos de un arreglo
//console.log(autos[0]);
//console.log(autos[2]);
//for(let i = 0; i < autos.length; i++ ){
//    console.log(i+" : " + autos[i]);
//}
//autos[1] = "Volvo";
//console.log(autos[1])
////Agragamos nuevos valores al arreglo
//autos.push("Audi")
//console.log(autos)
////Otras formas de agregar elementos ala rreglo
//autos[autos.length] = "Porche";
//console.log(autos)
////Tercera forma de agregar elementos teniendo Cuidado
//autos[6] = "Renault";
//console.log(autos)
////como preguntar si es un array o un arreglo
//console.log(Array.isArray(autos))
//
//console.log(autos instanceof Array) //Preguntamos si esta variable es una instancia de la clase array
//miFuncion(8,2);
//
//function miFuncion(a,b){
//    //console.log("Sumamos: "+ (a+b))
//    return a + b
//}
//miFuncion(4,5);
//
//let resultado = miFuncion(6, 7)
//console.log(resultado)
//
//let x = function(a,b){return a + b}
//
//resultado = x (5,6)
//console.log(resultado)
//
//(function (a, b){
//    console.log("Ejecutando la funcion "+ (a + b));
//})
//(9,6);
//
//console.log(typeof miFuncion);
//function miFuncionDos(a,b){
//    console.log(arguments.length);
//}
//
//miFuncionDos(5, 7, 3, 6)
//
//var miFuncionTexto = miFuncionDos.toString()
//console.log(miFuncionTexto)
//
//const sumarFuncionFlecha = (a, b) => a + b;
//resultado = sumarFuncionFlecha(3, 7);
//console.log(resultado)
//
//let sumar = function(a = 4, b = 8){
//    console.log(arguments[0]);
//    console.log(arguments[1]);
//    return a + b + arguments[2];
//    
//}
//
//resultado = sumar(3, 2, 9)
//console.log(resultado)
//
//let respuesta = sumarTodo(5, 4, 13, 10, 9);
//console.log(respuesta)
//function sumarTodo(){
//    let suma = 0;
//    for(let i = 0; i < arguments.length; i++){
//        suma += arguments[i]
//    }
//    return suma;
//}
//
//let k = 10;
//function cambiarValor(a){
//a = 20}
//cambiarValor(k)
//console.log(k)
//
//const persona = {
//    nombre: "Juan",
//    apellido: "Lepez"
//}
//
//function cambiarValorObjeto(p1){
//    p1.nombre = "Ignacio",
//    p1.apellido = "Perez"
//}
//cambiarValorObjeto(persona)
//console.log(persona)
let x = 10;
console.log(x.length)
console.log("Tipos primitivos")

//objeto

let persona = {
    nombre: "Carlos",
    apellido: "Gil",
    email: "cgil@gmail.com",
    edad: 30,
    idioma:"es",
    get lang(){
        return this.idioma.toUpperCase();
    },
    set lang(lang){
        this.idioma = lang.toUpperCase();
    },
    nombreCompleto: function(){
        return this.nombre + " " + this.apellido;
    },
    get nombreEdad(){
        return "EL nombre es " + this.nombre + " edad: " + this.apellido;
    }
}
console.log(persona.nombre)
console.log(persona.apellido)
console.log(persona.email)
console.log(persona.edad)
console.log(persona)
console.log(persona.nombreCompleto())
console.log("Ejecutando con un objeto")

let persona2 = new Object();
persona2.nombre = "juan";
persona2.direccion = "Salada 14";
persona2.telefono = "5492618282821";

console.log(persona2.telefono)
console.log("Creamos un nuevo objeto")
console.log(persona["apellido"])

//for in 
for(propiedad in persona){
    console.log(propiedad)
    console.log(persona[propiedad])
}
console.log("Cambiamos y eliminamos un error")
persona.apellido = "Bentancud"
delete persona.apellido;
console.log(persona)

console.log(persona.nombre+", "+ persona.apellido);

for(nombrePropiedad in persona){
    console.log(persona[nombrePropiedad]);
}

let  personaArray = Object.values(persona);
console.log(personaArray);

console.log("Distinta formas de imprimir un objeto: forma 3");
let personaString = JSON.stringify(persona);
console.log(personaString)

console.log("Comenzamos a utilizar el metodo get");
console.log(persona.nombreEdad);

console.log("Comenzamos con el metodo get para idiomas");
persona.lang = "en";
console.log(persona.lang);

function Persona3(nombre, apellido, email){
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;   
    this.nombreCompleto = function(){
        return this.nombre + " " + this.apellido
    }
}
let padre = new Persona3("Leo", "Lopez", "lopezl@gmail.com")
this.nombre = "Luis" //modificamos el nombre
padre.telefono = "5492618282821";
console.log(padre)
console.log(padre.nombreCompleto())

let madre = new Persona3("Laura", "Contrera", "contrera@gmail.com");
console.log(madre);
console.log(madre.nombreCompleto())

let miObjeto = new Object();

let miObjeto2 = {}

let miCadena1 = new String("Hola");

let miCadena2 = "Hola";

let miNumero = new Number(1);

let miNumero2 = 1;

let miBoolean1 = new Boolean(false);

let miBoolean2 = false;

let miArreglo1 = new Array();

let miArreglo2 = [];

let miFuncion1 = new Function();

let miFuncion2 = function(){};

Persona3.prototype.telefono = "2618383832"
console.log(padre);
console.log(madre.telefono)
madre.telefono = "5492618383832"

//Uso del call
let persona4 = {
    nombre: "Juan",
    apellido: "Perez",
    nombreCompleto2: function(titulo, telefono){
        return titulo + ": " + this.nombre + " " + this.apellido + " "+ telefono
    }
}

let persona5 = {
    nombre: "Carlos", 
    apellido: "Lara"
}
console.log(persona4.nombreCompleto2("Lic. ", "5492618484845"));
console.log(persona4.nombreCompleto2.call(persona5, "Ing", "5492618585856"))

let arreglo = ["Ing", "5492618686865"]
console.log(persona4.nombreCompleto2.apply(persona5, arreglo))
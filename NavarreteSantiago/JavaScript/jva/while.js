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
const autos = ["Ferrari", "Renault", "BMW"];
console.log(autos);

///Recorremos los elementos de un arreglo
console.log(autos[0]);
console.log(autos[2]);
for(let i = 0; i < autos.length; i++ ){
    console.log(i+" : " + autos[i]);
}
autos[1] = "Volvo";
console.log(autos[1])
//Agragamos nuevos valores al arreglo
autos.push("Audi")
console.log(autos)
//Otras formas de agregar elementos ala rreglo
autos[autos.length] = "Porche";
console.log(autos)
//Tercera forma de agregar elementos teniendo Cuidado
autos[6] = "Renault";
console.log(autos)
//como preguntar si es un array o un arreglo
console.log(Array.isArray(autos))

console.log(autos instanceof Array) //Preguntamos si esta variable es una instancia de la clase array

/* //Clase 10. LUCIANA FRAGUEIRO
//Ejercicio 1: Calcular estacion del año
let mes = 4;
let estacion;
if(mes == 1 || mes == 2 || mes == 12){
    estacion = "Verano";
}else if(mes == 3 || mes == 4 || mes == 5){
    estacion = "Otoñp";
}else if(mes == 6 || mes == 7 || mes == 8){
    estacion = "Invierno";
}else if(mes == 9 || mes == 10 || mes == 11){
    estacion = "Primavera";
}else{
    estacion = "Valor incorrecto"
}
console.log("El valor corresponde a la estacion de :" + estacion);

//Ejercicio 2: Hora del dia 
/*
de 6 a 11 nos saluda: Good Morning
de 12 a 16 nos saluda: Good afternoom
de 17 a 19 nos saluda: Good evening
de 20 a 23 nos saluda: Good night
Trabajaremos con 24 horas
*/
/*
let horaDia = 9;
let mensaje;
if(horaDia >= 6 && horaDia <= 11){
    mensaje = "Good morning";
}else if(horaDia >= 12 && horaDia <= 16){
    mensaje = "Good afternoon";
}else if(horaDia >= 17 && horaDia <= 19){
    mensaje = "Good evening";
}else if(horaDia >= 20 && horaDia <= 23){
    mensaje = "Good night";
}else{
    mensaje = "Valor incorrecto"
}
console.log(mensaje);

// Calcular estaación del año. Estructura switch(La sintaxis es igual a java)
switch(mes){
    case 1: case 2: case 12:
        estacion = "Verano";
        break;
    case 3: case 4: case 5:
        estacion = "Otoño";
        break;
    case 6: case 7: case 8:
        estacion = "Invierno";
        break;
    case 9: case 10: case 11:
        estacion = "Primavera";
        break;
    default:
        estacion = "Valor incorrecto";
}
console.log("Bienvenido a la estacion de: " + estacion);


// NOSE DE QUE CLASE ES ESTO DE ACA ABAJO, VER!!!!!!!!
//Ampliamos el uso de var let y const
/*
Con var puedes reasignar en cualquier momento
esta forma parte del ambito global
Un error es que se sobreescriba
*/

/* var nombre = 'Ariel';
nombre = 'Osvaldo';
console.log(nombre);

function saludar(){
    var nombre3 = 'Natalia'
    console.log(nombre3);
}
//console.log(nombre3); //El problema es que aqui no lee el dato en la funcion

if(true){
    var edad = 34;
    console.log(edad); 
}
console.log(edad); //en la funcion funciono correctamente, en la estructura if fallo

/*
let: esta puede ser reasignada en cualquier momento
la diferencia es que su ambito es de bloque,
solo disponible dentro de un bloque de llaves
o dentro de una funcion
*/

/* function saludar2(){
    let nombre2 = 'Ariel';
    console.log(nombre2);
}
//console.log(nombre2);

if (true){
    let edad2 = 33;
//    console.log(edad2);
}
console.log(edad);

/*
const se utiliza para valores constantes que no pueden ser reasignadas
*/

/*const fechaNacimiento = 2006;
console.log(fechaNacimiento);
//fechaNacimiento = 2003;
//console.log(fechaNacimiento); //Solo se ejecuta el console anterior
*/


//CLASE 11. LUCIANA FRAGUEIRO
//Const se utiliza para valores constantes que no pueden ser reasignadas

const fechaNacimiento = 2006;
console.log(fechaNacimiento);
//fechaNacimiento = 2003;
//console.log(fechaNacimiento); //solo se ejecuta el console anterior

//Evitar repetir tu codigo
//Dry don't repeat yourself
let days = 1;
switch (days){
    case 1:
        console.log('hoy es Lunes');
        break;
    case 2:
        console.log('hoy es Martes');
        break;
    case 3:
        console.log('hoy es Miercoles');
        break;
    case 4:
        console.log('hoy es Jueves');
        break;
    case 5:
        console.log('hoy es Viernes');
        break;
    case 6:
        console.log('hoy es Sabado');
        break;
    case 7:
        console.log('hoy es Domingo');
        break;
    default:
        console.log("Error en el ingreso del dia de la semana");
        break;     
}


let days2 = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'];
function getDay(n){
    if(n < 1 || n > 7){
        throw new Error('out of range');
    }
    return days2[n-1];
}

console.log(getDay(5));

//Ejercicio meses del año, debes hacerlo con la estructura switch
//y luego con la funcion en la opcion mejorada
let months = 13;
switch (months){
    case 1:
        console.log('El mes es Enero');
        break;
    case 2:
        console.log('El mes es Febrero');
        break;
    case 3:
        console.log('El mes es Marzo');
        break;
    case 4:
        console.log('El mes es Abril');
        break;
    case 5:
        console.log('El mes es Mayo');
        break;
    case 6:
        console.log('El mes es Junio');
        break;
    case 7:
        console.log('El mes es Julio');
        break;
    case 8:
        console.log('El mes es Agosto');
        break;
    case 9:
        console.log('El mes es Septiembre');
        break;
    case 10:
        console.log('El mes es Octubre');
        break;
    case 11:
        console.log('El mes es Noviembre');
        break;
    case 12:
        console.log('El mes es Diciembre');
        break;
     default:
        console.log("Error en el ingreso del numero de mes");
        break;
}
//Ejercicio con funcion

let months2 = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"];
function getMonth(n){
  if (n < 1 || n > 12) {
        throw new Errow('out of range');
    }
  return months2[n-1];
}

console.log(getMonth(5));
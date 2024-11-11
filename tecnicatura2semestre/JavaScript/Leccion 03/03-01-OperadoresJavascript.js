//Ejercicio para encontrar numeros pares
let parInpar = 10;
if(parInpar % 2 ==0){
    console.log("Es un número PAR");
}
else{
    console.log("Es un número IMPAR");
}

//ejercicio es mayor de edad
let edad = 18, adulto = 18;
if(edad >= adulto){
    console.log('Usted es una persona adulta');
} 
else{
    console.log('Usted es una persona menor de edad');
}

//ejercicio: Dentro del rango
let dentroRango = 10;
let valMin = 0, valMax = 10;
if( dentroRango >= valMin && dentroRango <= valMax){
    console.log('Esta dentro del rango establecido')
}
else{
    console.log('Esta fuera del rango establecido')
}

// CLASE 9 LUCIANA FRAGUEIRO
//Ejercicio: Si el padre puede asistir al juego de su hijo
let vacaciones = false,
  diaDescanso = true;

if (vacaciones || diaDescanso) {
  console.log("El padre puede ir al partido de su hijo");
} else {
  console.log("El padre no puede ir al partido de su hijo");
}

//Ejercicio: Operador ternario
let numero1 = 3 > 2 ? "Verdadero" : "falso";
console.log(numero1);

let numero2 = 12;
console.log(numero2);

numero2 = numero1 % 2 == 0 ? "Es un numero par" : "Es un numero impar";
console.log(numero2);

//Ejercicio: Convertir de String a Number

let miNumero1 = "21";
console.log(typeof miNumero1);

let miNumero2 = Number(miNumero1);
console.log(typeof miNumero2);

if (miNumero2 >= 18) {
  console.log("Es mayor de edad");
} else {
  console.log("Es menor de edad");
}

//Operador ternario
let resultado3 = miNumero3 >= 18 ? "Es mayor de edad" : "No es mayor de edad";
console.log(resultado3);

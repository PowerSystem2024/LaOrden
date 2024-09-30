
let x = 10;
console.log(x.length);

// Objeto
let persona = {
    nombre: 'Carlos',
    apellido: 'Gil',
    email: 'cgil@gmail.com',
    edad: 28,
    idioma: 'ES',
    get lang(){
        return this.idioma.toUpperCase();
    },
    set lang(lang){
        this.idioma = lang.toUpperCase();
    },
    nombreCompleto: function(){
        return this.nombre+' '+this.apellido;
    },
    get nombreEdad(){
        return 'nombre: ' + this.nombre+' edad: '+this.edad;
    }
}

console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.email);
console.log(persona.edad);
console.log(persona);
console.log(persona.nombreCompleto());

let persona2 = new Object(); // Debe crear un numero objeto en memoria
persona2.nombre = 'Juan';
persona2.direccion = 'Salada 14';
persona2.telefono = '5443263263';
console.log(persona2.telefono);

console.log(persona['apellido']); // Accediendo como si fuera un arreglo

// for in y accedemos al objeto como si fuera un arreglo
for(propiedad in persona){
    console.log(propiedad);
    console.log(persona[propiedad]);
}

console.log('Cambiarmos y eliminamos un error');

persona.apellida = 'Betancud'; // Cambiar dinamicamente un valor del objeto
delete persona.apellida; // ELiminamos el error
console.log(persona);


// Numero 3: La funcion Object.values()
console.log('Distinta forma de imprimir un objeto: forma 3');
let personaArray = Object.values(persona);
console.log(personaArray);

// Numero 4: Utilizaremos el método JSON.stringify
console.log('Distinta forma de imprimir un objeto: forma 4');
let personaString = JSON.stringify(persona);
console.log(personaString);


console.log("Comenzamos a utlizar metodo get");
console.log(persona.nombreEdad);

console.log("Comenzamos a utlizar metodo get para idiomas");
persona.lang = 'en';
console.log(persona.lang);


function Persona3(nombre = "Luis", apellido, email){
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    this.nombreCompleto = function(){
        return this.nombre + " " + this.apellido;
    }
}

let padre = new Persona3("Leo", "Lopez", "lopez@gmail.com")
console.log(padre);
console.log(padre.nombreCompleto());


// Diferentes formas de crear objetos
// Caso numero 1
let miObjeto = new Object();

// Caso numero 2
let miObjeto2 = {};

// Caso string 1
let miCadena1 = new String("hola");

// Caso string 2
let miCadena2 = "hola";

// Caso con numeros 1
let miNumero = new Number(1);

// Caso con numeros 2
let miNumero2 = 1;

// Caso boolean 1
let miBoolean = new Boolean(false);

// Caso boolean 2
let miBoolean2 = false;

// Caso arreglos 1
let miArreglo1 = new Array();

// Caso arreglos 2
let miArreglo2 = [];

// caso funcion 1
let miFuncion1 = new function(){};

// caso funcion 2
let miFuncion2 = function(){}


// Uso de prototype
Persona3.prototype.telefono = "14214322";
console.log(padre);
padre.telefono = "326523653"
console.log(padre.telefono);

// Uso de call
let persona4 = {
    nombre: "Juan",
    apellido: "Perez",
    nombreCompleto2: function(){
        return titulo + ": " + this.nombre+ " "+ this.apellido+" "+ telefono;
    }
}

let persona5 = {
    nombre: "Carlos",
    apellido: "Lara"
}

console.log(persona4.nombreCompleto2("Lic.", "23523525235"));
console.log((persona4.nombreCompleto2.call(persona5, "Ing.", "353463463463")));

// Metodo apply
let arreglo = ["Ing.", "543463634632"];
console.log(persona4.nombreCompleto2.apply(persona5, arreglo));
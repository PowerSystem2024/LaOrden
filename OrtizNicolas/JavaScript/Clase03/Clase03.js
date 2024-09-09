



miFuncion(8,2)

function miFuncion(a,b){
    console.log("Sumamos " + (a+b));
    return a + b;
}

let resultado = miFuncion(5,3)
console.log(resultado);

let x = function(a, b){ return a + b}
resultado = x(5,6)
console.log(resultado);

(function(a, b){
    console.log('Ejecutando la funcion: ' + (a + b));
})(9,6)

console.log(typeof miFuncion);


function miFuncionDos(a,b){
    console.log(arguments.length);
}

miFuncionDos(5,7,3,5)

var miFuncionTexto = miFuncionDos.toString()
console.log(miFuncionTexto);

const sumarFuncionFlecha = (a,b) => a + b
resultado = sumarFuncionFlecha(3,8)
console.log(resultado);

let sumar = function(a= 4, b= 8){
    console.log(arguments[0]);
    console.log(arguments[1]);
    return a + b + arguments[2]
}

resultado = sumar(3, 4 ,8)

let respuesta = sumarTodo(3, 4, 5, 3, 7)

function sumarTodo(){
    let suma = 0;
    for(let i = 0; i < arguments.length; i++){
        suma += arguments[i];
    }
    return suma
}

let k = 10;
function cambiarValor(a){
    a = 20;
}
cambiarValor(k);
console.log(k);


const persona = {
    nombre: 'Juan',
    apellido: 'Lopez'
}

function cambiarValorObjeto(p1){
    p1.nombre = 'Ignacio';
    p1.apellido = 'Perez';
}

cambiarValorObjeto(persona);
console.log(persona);

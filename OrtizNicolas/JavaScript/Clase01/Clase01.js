
// while

let contador = 0;

while(contador < 0){
    console.log(contador);
    contador++;    
}


// do while
let conteo = 0;
do{
    console.log(conteo);
    conteo++
    
} while(conteo < 3)


for(let contando = 0; contando < 3; contando++){
    console.log(contando);
    if(contando % 2 !== 0){
        break;
    }
}

inicio:
for(let contando = 0; contando <= 10; contando++){
    if(contando % 2 !== 0 ){
        break inicio;
    }
}

const autos = ['Ferrari', 'Renault']
console.log(autos);


for (let i = 0; i < autos.length; i++) {
    console.log(i + ' : ' + autos[i]);
}

autos[1] = 'Volvo'

autos.push('Audi')

autos[autos.length] = 'Porsche'
console.log(autos);

console.log(Array.isArray(autos));
console.log(autos instanceof Array);


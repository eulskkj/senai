const readline = require('readline-sync')

const ListaDeNumeros = []
for (let i = 1; i <= 6; i++) {
    numero = readline.questionFloat('Digite um número: ')
    ListaDeNumeros.push(numero)
}

console.log('pares')
const pares = ListaDeNumeros.filter( n => n % 2 === 0)
console.log(pares)
console.log('\nImpares')
const impares = ListaDeNumeros.filter( n => n % 2 !== 0)
console.log(impares)









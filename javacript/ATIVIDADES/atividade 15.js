const readline = require('readline-sync')

const ListaDeNumeros = []
for (let i = 1; i <= 5; i++){
    numero = readline.questionFloat('Digite um numero: ')
    ListaDeNumeros.push(numero)
}

console.log('Negataivo')
const negativo = ListaDeNumeros.filter (n => n < 0)
console.log(negativo)

console.log('Positivo')
const positivo = ListaDeNumeros.filter (n => n > 0)
console.log(positivo)

console.log('Neutro')
const neutro = ListaDeNumeros.filter(n => n == 0)
console.log(neutro)






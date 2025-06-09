const ListaDeNumeros = [1, 2, 3, 4, 5]


console.log('Listando todos os números da lista')
console.log(ListaDeNumeros)

console.log('\nMultiplicando valores por 2: ')
const dobrados = ListaDeNumeros.map(n => n * 2)
console.log(dobrados)


console.log('\nFiltrando elementos pares')
const pares = ListaDeNumeros.filter(n => n % 2 === 0)
console.log(pares)

console.log('\nFiltrando elementos impares')
const impares = ListaDeNumeros.filter(n => n % 2 !== 0)
console.log(impares)

console.log('\nSomando todos os numeros da lista: ')
const soma = ListaDeNumeros.reduce((soma, total) => soma + total, 0)
console.log(soma)










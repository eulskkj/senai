const readline = require('readline-sync')

const listaDeNotas = []

for (let i = 1; i <= 3; i++) {
    nota = readline.questionFloat(`Digite a ${i}ª nota: `)
    listaDeNotas.push(nota)
}

console.log('\nSoma das notas: ')
soma = listaDeNotas.reduce((soma, total) => soma + total, 0)
console.log(soma)


console.log('\nQuantidade de notas: ')
quantidadesdenotas = listaDeNotas.length    
console.log(quantidadesdenotas)

console.log('\nMédia: ')
media = soma / quantidadesdenotas
console.log(media)

console.log('Exibindo todas as notas: ')
listaDeNotas.forEach((nota, index) => console.log(`${++index}ª nota: ${nota}`))




const readline = require('readline-sync')

let numero = readline.questionFloat("Digite um numero: ")


if (numero % 2 === 0) {
    console.log("É par.")
} else {
    console.log("É impar.")
}


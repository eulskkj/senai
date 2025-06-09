const readline = require('readline-sync');


a = readline.questionInt('Informe o valor de A:')
b = readline.questionInt('Informe o valor de B:')
c = readline.questionInt('Informe o valor de C:')

let soma = a + b
if (soma < c) {
    console.log("A + B é menor que C.")
} else {
    console.log("A + B é maior que C.")
}




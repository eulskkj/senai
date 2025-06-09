const readline = require('readline-sync');


a = readline.questionInt("Digite o valor de A: ")
b = readline.questionInt("Digite o valor de B: ")


if (a === b) {
    c = a + b;
} else {
    c = a * b;
}

console.log("O resultado é:", c);




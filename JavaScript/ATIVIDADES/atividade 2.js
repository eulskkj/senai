const readlineSync = require('readline-sync');
soma = 0

let nota = 0

for (let i = 0; i < 4; i++) {
    do {
    nota = parseInt(readlineSync.question("Digite a primeira nota: "));    
} while (nota < 0 || nota > 10);
    soma += nota;

}
media = soma/ 2

console.log(`A media é: ${media}`)











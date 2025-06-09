const readline = require('readline-sync');

let idade = readline.questionInt('Informe sua idade: ')

if (idade >= 65) {
    console.log("Não obrigado a votar.")
} else if (idade > 18 && idade < 65) {
    console.log("Voto obrigatótrio.")
}else if (idade >16  && idade<19) {
    console.log("Voto opcional.");
} else {
    console.log("Não pode votar.");
}





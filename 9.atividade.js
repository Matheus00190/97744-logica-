const readline = require('readline-sync')

 const idade = readline.questionInt('digite sua idade:')

 if (idade < 16) {
    console.log('nao podem votar.')
 }else{
    console.log('menor de idade.')
 }

 if (idade < 16,17) {
    console.log('opcional.')
 }else{   
    console.log('adolescente.')
 }

 if (idade >= 18) {
    console.log('voto obrigatorio.')
 }else{
    console.log('maior de idade.')
 }

 if (idade > 65) {
    console.log('nao sao obrigados a votar.')
 }else{
 }

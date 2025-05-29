 // instalar: rpm install readline-sync
 
 const readline = require('readline-sync')

 const idade = readline.questionInt('digite sua idade:')

 if (idade < 18) {
    console.log('menor de idade.')
 }else{
    console.log('maior de idade.')
 }

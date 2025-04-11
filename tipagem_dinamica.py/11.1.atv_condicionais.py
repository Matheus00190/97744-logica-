import os      
os.system("clear")

primeiro_numero = float(input("digite o primeiro numero: "))
segundo_numero = float(input("digite o segundo numero: "))


match operacao: 
    case "+" :
        resultado = primeiro_numero + segundo_numero
    case "-":   
        resultado = primeiro_numero - segundo_numero
    case "*":   
        resultado = primeiro_numero * segundo_numero
    case "/":   
        resultado = primeiro_numero / segundo_numero
    case _: 
        resultado = 0 
    
        print("Opcao ivalida")  
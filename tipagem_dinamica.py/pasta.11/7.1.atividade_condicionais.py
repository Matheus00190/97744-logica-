# 1 - Limpando o terminal.
import os 
os.system("clear")   

# 2 - Solicitando dados para o usuario.
idade = int(input ("Digite sua idade: ") ) 


if idade < 18 or idade > 65:
    print("Nao e obrigado a votar!")
else:
    print("E brigado a votar!")        
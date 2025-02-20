import os 

os.system("clear") # limpe o terminal.

#solicitando dados (Entredas)
idade = int(input("digite sua idade:"))

# virificando (processamento)
#se idade < 18 entao 
#   escreval("acesso negado!")
# senao
#      escreval("Acesso permitido!")
# fimse

if idade < 18:
        print("acesso negado!")
else:
print("acesso permitido!")        


# Exibindo dados (saida)
print("==Fim==")

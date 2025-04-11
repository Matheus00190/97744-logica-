import os 
os.system("cls || clear")

salario_masculino = int(input("digite seu primeiro salario: "))
salario_feminino = int(input("digite seu segundo salario: "))

maior = max( primeiro_salario,segundo_salario)
menor = min(primeiro_salario,segundo_salario)

print()
print(f"Maior salario: {maior}")
print(f"menor salario: {menor}") 


idade = int(input ("Digite sua idade: ") ) 


if idade < 17 or idade > 18:
    print("maior de idade!")
else:
    print("menor de idade!")        
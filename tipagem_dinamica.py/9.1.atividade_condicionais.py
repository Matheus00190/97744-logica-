import os 
os.system("clear")

primeiro_numero = int(input("digite o primeiro numero: "))
segundo_numero = int(input("digite o segundo numero: "))
terceiro_numero = int(input("digite o terceiro numero: "))

maior = max(primeiro_numero,segundo_numero,terceiro_numero )
menor = min(primeiro_numero,segundo_numero,terceiro_numero )

print()
print(f"Maior numero: {maior}")
print(f"menor numero: {menor}") 



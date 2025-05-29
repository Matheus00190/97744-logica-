import os      

os.system("clear")

primeiro_numero = float(input("digite o primeiro numero: "))
segundo_numero = float(input("digite o segundo numero: "))

soma = primeiro_numero + segundo_numero
produto = primeiro_numero * segundo_numero
media = (primeiro_numero + segundo_numero) / 2

maior_numero = max(primeiro_numero, segundo_numero)
menor_numero = min(primeiro_numero, segundo_numero)

print()
print(f"soma: {soma}")5.1.atividade_condicionais.py
print(f"produto: {produto}")
print(f"media: {media}")
print(f"maior numero: {maior_numero}")
print(f"menor numero: {menor_numero}")



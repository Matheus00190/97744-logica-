import os 
os.system("clear")

print ("""
-------- MENU -------- 
1   \t\tJaneiro
2   \t\tFevereiro
3   \t\tMarço
4  \t\tAbril
5  \t\tMaio
6  \t\tJunho
7   \t\tJulho
8  \t\tAgosto
9  \t\tSetembro
10   \t\tOutubro
11   \t\tNovembro
12  \t\tDezembro
""")

dia = int(input("dijite o numero para o dia da semana: "))

match dia:
    case 1 | 7:
        resultado = "Fim de semana."
    case 2 | 3 | 4 | 5 | 6:
        resultado = "Dia util."
    case _:
     resultado = "Opcao invalida."

print()
print(f"Resultado: {resultado}")
import os 
os.system("clear")

print ("""
-------- MENU --------
1 \tDomingo  
2   \t\tSegunda-feira
3  \t\tTerça-feira
4   \t\tQuarta-feira
5  \t\tQuinta-feira
6   \t\tSexta-feira 
7   \t\tSabado
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
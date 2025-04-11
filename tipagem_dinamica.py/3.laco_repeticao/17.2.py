import os
os.system("cls || clear")

def calcular_imc(peso,altura): 
    return peso / (altura * altura)

def classificar(imc):
    if imc >= 40: 
        resultado = "obesidade grau 3"
    elif imc >= 35:
        resultado = "obesidade grau 2"
    elif imc >= 30:
        resultado = "obesidade grau 1"
    elif imc >= 25:
        resultado = "sobre peso"
    elif imc >= 18.5:
        resultado = "peso normal"
    else:
        resultado = "abaixo do Pesso"
    return resultado

def recomendar(imc):
    if imc >= 40: 
        resultado = "busque assistencia medica."
    elif imc >= 35:
        resultado = "consulte um medico para avaliacao e orientacao."
    elif imc >= 30:
        resultado = "procure orientacao de um profisional de saude."
    elif imc >= 25:
        resultado = "considere uma atividade balanceada e atv fisica."
    elif imc >= 18.5:
        resultado = "mantenha habitos saudaveis."
    else:
        resultado = "consulte um nutri para orientacao."
    return resultado

peso = float(input("digite seu peso:"))
altura = float(input("digite sua altura:"))

imc = calcular_imc(peso,altura)
classificacao = classificar(imc)

print(f"IMC: {imc}")
print(f"classificacao: {classificacao}")


        

ano=int(input("Digite um ano qualquer para descobrir se ele é ano bissexto ou não: "))

if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
    print("O ano digitado é bissexto!")

else:
    print("O ano não é bissexto.")




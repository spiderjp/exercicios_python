kmatual = float (input("Digite a Kilometragem atual: "))
kmanterior = float (input("Digite a Kilometragem anterior: "))
litros = float (input("Digite a quantidade consumida em litros: "))
taxa = (kmatual + kmanterior) / litros
print("A taxa de consumo do automóvel é de: {:.1f}".format(taxa), "Km/L")


print("PRÓXIMO EXERCÍCIO!")
quant_latao= float(input("Digite a quantidade de Latão: "))
porcent1 = quant_latao * (70/100)
porcent2 = quant_latao * (30/100)
print("De acordo com a quantidade de Latão, a quantidade de cobre que o compõe em Kg é de: {:.2f}".format(porcent1), " e a quantidade de zinco: {:.2f}".format(porcent2))


print("PRÓXIMO EXERCÍCIO!")
opcaoinvest = int(input("Digite o tipo de investimento que você quer, 1 (Poupança) ou 2 (Fundo de Renda Fixa): "))
valorinvest = float(input("Digite a quantia em reais do investimento: "))
meses = int(input("Digite a quantidade de mês(es) de quanto tempo estará fazendo o investimento: "))
if opcaoinvest == 1:
    valor_corrigido = (((valorinvest * (3/100)) + valorinvest) * meses)
    print("O valor total, já corrigido é de R$ {:.2f}".format(valor_corrigido))
elif opcaoinvest == 2:
    valor_corrigido2 = (((valorinvest * (4/100)) + valorinvest) * meses)
    print("O valor total, já corrigido é de R$ {:.2f}".format(valor_corrigido2))
else:
    print("O tipo de investimento que você escolheu, não foi o 1 ou 2, retorne e escolha um desses.")
    

print("PRÓXIMO EXERCÍCIO!")
altura = float(input("Digite sua altura: "))
sexo = input("Digite F se seu sexo for feminino, ou M se for masculino: ")
if (sexo == "f" or sexo == "F"):
    Mulheres = (62.1 * altura) - 44.7
    print("O peso ideal para seu corpo é de: {0:.1f}".format(Mulheres), "Kg.")
elif (sexo == "m" or sexo == "M"):
    Homens = (72.7 * altura) - 58
    print("O peso ideal para seu corpo é de: {0:.1f}".format(Homens), "Kg.")
else:
    print("Por favor, diga o seu sexo.")

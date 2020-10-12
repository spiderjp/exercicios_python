produto=float(input("Digite o preço à vista do produto: "))
parcelas=int(input("Digite a quantidade de parcelas que você gostaria: "))
if parcelas>0 and parcelas<=3:
    parcelado= produto*0.10*parcelas
    total_parcelado= parcelado + produto
    print("O preço total com as parcelas é de R$",total_parcelado)
elif parcelas>4:
    mais_de_quatro_parcelas= produto*0.20*parcelas
    total_mais_quatro= mais_de_quatro_parcelas + produto
    print("O preço total com as parcelas é de R$", total_mais_quatro)
else:
    total= produto
    print("O preço total do produto neste caso é de R$",total)


print("Exercício 1) :")


dolar=float(input("Quanto está o Dólar atualmente?: "))
quant=int(input("Quantos dólares você quer converter para Reais?: "))
real=dolar*quant
print("O valor total da conversão de Dólares para Real é: R$",real)

print("Exercício 2) :")

hora=int(input("Qual é a hora atual?: "))
minutos=int(input("Qual é o minuto atual?: "))
horas=hora*60
horario=horas+minutos
print("A quantidade de minutos que se passaram foram: ",horario, "minutos")


print("Exercício 3) :")


real1=float(input("Digite um número: "))
real2=float(input("Digite outro número: "))
resto1=real1%real2
resto2=real2%real1
print("Os valores de restos de cada divisão, tanto do primeiro valor com o segundo, ou vice-versa, são: ",resto1, "e", resto2)


print("Exercício 4) :")


cliente=float(input("Digite a quantidade em dinheiro que terá que pagar: "))
garcom=cliente/100
total=cliente+garcom
print("O cliente representa um gasto de: R$ ",cliente, "entretanto, o garçom receberá 10% de R$",cliente, "sendo então: R$", garcom," e o valor total a ser pago para o restaurante ComaBem é: R$",total)

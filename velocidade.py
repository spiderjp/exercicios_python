space=float(input("Digite o espaço percorrido em Km por um veículo: "))
time=float(input("Digite o tempo utilizado para percorrer essa distância: "))
if space>0 and time>0:
    v=space/time
    print("A velocidade atingida pelo veículo em um MRU foi de: ",v,"Km/h")
else:
    print("Os valores de espaço e tempo foram menores que Zero. Logo, o veículo não percorreu nada.")

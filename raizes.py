import math
a=float(input("Digite um número para 'a': "))
b=float(input("Digite um número para 'b': "))
c=float(input("Digite um número para 'c': "))
delta=(b**2) - (4*a*c)
if delta >= 0:
    x1=(-b+delta**(1/2)) / (2*a)
    x2= (-b-delta**(1/2)) / (2*a)
    print("Os valores das raizes são: ",x1,"e" ,x2)
else:
    print("O valor de Delta é negativo, não podendo calcular as raízes!")

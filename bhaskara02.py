import math
print("A equação de 2º Grau é: +ax^2+bx+c=0")
a=float(input("Determine o valor de a: "))
b=float(input("Determine o valor de b: "))
c=float(input("Determine o valor de c: "))
x=(b**2)-(4*a*c)
if x < 0 :
    print("Raiz negativa não possui valores x1 e x2")
    exit()

else :
    x=math.sqrt(x)
    
    x1=(-b+x)/(2*a)
    x2=(-b-x)/(2*a)
print("Os valores das duas raízes da equação de 2º grau são: ",x1, "e",x2)

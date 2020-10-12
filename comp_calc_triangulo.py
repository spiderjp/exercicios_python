x = int(input("digite o valor x: "))
y = int(input("digite o valor y: "))

if x>y:
    print("O maior valor é o: ",x)
elif x==y:
    print("os valores são de x e y são iguais!")
else:
    print("O maior valor é o: ",y)
    
print("PRÓXIMO EXERCÍCIO utilizando PYTHON Aninhado!")


notaA = float(input("Digite a primeira nota: "))
notaB = float(input("Digite a segunda nota: "))
notaC = float(input("Digite a terceira nota: "))
freq = float(input("Digite a porcentagem da frequência às aulas: "))
media = (notaA + notaB + notaC)/3
if media >= 6.0 and freq >= 75.0:
              print("O aluno está aprovado!")
else:
    if media > 8.0:
        print("O aluno está aprovado de forma direta!")
    else:
        print("O aluno está reprovado!")

print("PRÓXIMO EXERCÍCIO!")

number_one = float(input("Digite um número: "))
number_two = float(input("Digite outro número: "))
operation = input("Digite a operação (o tipo de operador): ")

if operation == "+":
    print("O valor final é: ",number_one + number_two)
elif operation == "-":
    print("O valor final é: ",number_one - number_two)
elif operation == "*":
    print("O valor final é: ",number_one * number_two)
elif operation == "/":
    print("O valor final é: ",number_one / number_two)
else:
    print("Você não escolheu entre as operações de +, - , *, /; para os números fazerem a operação, logo é uma operação inválida ):")


# OU de outro jeito:
#    
#if op == '*':
#    m = a * b
#    print('O valor da sua multiplicação {0}'.format(m))
#elif op == '+':
#    s = a + b
#    print('O valor da soma é {0}'.format(s))
#elif op == '-':
#    su = a - b
#    print('O valor da subtração é {0}'.format(su))
#elif op =='/':
#    d = a / b
#    print('O valor da sua divisão é {0}'.format(d))
#elif op == '%':
#    r = a % b
#   print('O resto da divisão é {0}'.format(r))
#else: print('Seu operador está invalido')

print("PRÓXIMO EXERCÍCIO!")

angA = float(input("Digite o valor do ângulo A: "))
angB = float(input("Digite o valor do ângulo B: "))
angC = float(input("Digite o valor do ângulo C: "))
if angA == angB == angC:
    print("O triângulo é equilátero!")
elif angA == angB or angA == angC or angB == angC:
    print("O triângulo é isósceles!")
elif angA != angB != angC:
    print("O triângulo é escaleno!")
else:
    angA+angB+angC < 180.0
    print("A soma dos três ângulos não é 180 graus, logo não é um triângulo.")



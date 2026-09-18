def Circulo():
    raio = float(input("Digite o raio do Ciruculo! : "))
    pi = 3.14
    area = pi * (raio * raio)
    print(f"a area do seu circulo é : {area}")

def Triangulo():
    altura = float(input("Digite a altura do seu triangulo ! : "))
    base = float(input("Digite a base do seu triangulo ! : "))
    area = (altura * base) / 2
    print(f"a area do seu triangulo é : {area}")

def Quadrado():
    lado = float(input("Digite o lado do seu quadrado ! : "))
    area = lado * lado
    print(f"a area do seu quadrado é : {area}")

def Retangulo():
    altura = float(input("Digite a altura do seu retangulo ! : "))
    base = float(input("Digite a base do seu retangulo ! : "))
    area = (altura * base)
    print(f"a area do seu retangulo é : {area}")

def Paralelogramo():
    altura = float(input("Digite a altura do seu paralelogramo ! : "))
    base = float(input("Digite a base do seu paralelogramo ! : "))
    area = (altura * base)
    print(f"a area do seu paralelogramo é : {area}")

def Losango():
    DiagonalMaior = float(input("Digite o lado da diagonal maior do seu losango ! : "))
    DiagonalMenor = float(input("Digite o lado da diagonal menor do seu losango ! : "))
    area = (DiagonalMaior * DiagonalMenor) / 2
    print(f"a area do seu losango é : {area}")

def Trapezio():
    BaseMaior = float(input("Digite a base maior do seu trapezio ! : "))
    BaseMenor = float(input("Digite a base menor do seu trapezio ! : "))
    altura = float(input("Digite a altura do seu trapezio ! : "))
    area = ((BaseMaior + BaseMenor) * altura) / 2
    print(f"a area do seu trapezio é : {area}")

print("CALCULADORA DE AREA! QUAL FIGURA GEOMETRICA VOCE PRETENDE SABER A AREA?")
print("0 sair")
print("1 Circulo")
print("2 Triangulo")
print("3 quadrado")
print("4 retangulo")
print("5 paralelogramo")
print("6 losango")
print("7 Trapezio")

escolha = int(input("Digite o número correspondente a figura que voce quer calcular : "))

if escolha == 1 :
    Circulo()

elif escolha == 2 :
   Triangulo()

elif escolha == 3 :
    Quadrado()

elif escolha == 4 :
   Retangulo()

elif escolha == 5 :
    Paralelogramo()

elif escolha == 6 :
    Losango()

elif escolha == 7 :
    Trapezio()

elif escolha == 0:
    print("saindo do Programa...")

else:
    print("escolha invalida! digite uma das opçoes")


    
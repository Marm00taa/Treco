import os
import time
import sys

def lerComprimento():
    C = float(input("\nDigite o Comprimento: "))
    return C

def Diametro(C):
    D = C / 3.14
    return D

def Raio(D):
    R = D / 2
    return R

def Area(R):
    A = (R **2) * 3.14
    return A

def Exibir(D, R, A):
    os.system("cls")
    print(f'\nDiametro = {D:.3f}')
    print(f'\nRaio = {R:.3f}')
    print(f'\nArea = {A:.3f}')
    time.sleep(3)

def Menu():
    os.system("cls")
    print("1. Calcular")
    print("2. Sair")
    op = int(input("Digite a Opção Desejada: "))
    if op < 1 or op > 2:
        print("\nOpção Inválida,Tente Novamente")
        time.sleep(3)
        os.system("cls")
    elif op == 2:
        sys.exit()
    elif op == 1:
        Executar()

def Executar():
    C = lerComprimento()
    D = Diametro(C)
    R = Raio(D)
    A = Area(R)
    Exibir(D, R, A)
    os.system("cls")
    Menu()

Menu()

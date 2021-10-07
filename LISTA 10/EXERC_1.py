# -*- coding: utf-8 -*-
import os
import sys
import time

def lerN1():  
    n1 = float ( input ('Nota1:'))   
    return n1

def lerN2():   
    n2 = float ( input ('Nota2:'))  
    return n2
    
def getMedia(n1, n2):   
    media = (n1+n2)/2   
    return media
    
def mostrar(media):   
    os.system('cls')   
    print(f'\nMédia = {media}')   
    if media < 6:      
        print('\nAluno Reprovado')  
    else:      
        print('\nAluno Aprovado')    
    #os.system('sleep 5')
    
def executar():    
    nota1 = lerN1()    
    nota2 = lerN2()    
    media = getMedia(nota1, nota2)    
    mostrar ( media )
    time.sleep(3)
    menu()

def menu():
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
        executar()

menu()
sys.exit
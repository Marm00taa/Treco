import sys,time,os,math

ano=menu=0
bissexto="bissexto"
nbissexto="Não bissexto"

menu=int(input("MENU\n 1.EXECUTAR\n 2.SAIR\n"))

if(menu==1):
    ano=int(input("Digite um ano: "))

    if(ano%4 == 0):
        print(bissexto)
    else:
        print(nbissexto)
import sys,time,os,math

ano=0
bissexto="bissexto"
nbissexto="Não bissexto"

ano=int(input("Digite um ano: "))

if(ano%4 == 0):
    print(bissexto)
else:
    print(nbissexto)
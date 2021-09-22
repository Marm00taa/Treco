import sys,time,os,math

num1=num2=num3=num4=aux=0


num1=int(input("Digite o 1 valor: "))
num2=int(input("Digite o 2 valor: "))
num3=int(input("Digite o 3 valor: "))
num4=int(input("Digite o 4 valor: "))


if(num1>num4):
    aux=num1
    num1=num4
    num4=aux

if(num1>num2):
    aux=num2
    num1=num2
    num2=aux

if(num2>num3):
    aux=num2
    num2=num3
    num3=aux

if(num3>num4):
    aux=num3
    num3=num4
    num4=aux





print (f"{num1}, {num2}, {num3}, {num4}")
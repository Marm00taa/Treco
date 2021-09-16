import sys,time,os,math

num1=num2=num3=num4=0

num1=int(input("Digite o 1 valor: "))
num2=int(input("Digite o 2 valor: "))
num3=int(input("Digite o 3 valor: "))
num4=int(input("Digite o 4 valor: "))


if(num1%2 == 0 and num1%3 == 0):
    print(f"{num1} é divisível por 2 e 3")
if(num2%2 == 0 and num2%3 == 0):
    print(f"{num2} é divisível por 2 e 3")
if(num3%2 == 0 and num3%3 == 0):
    print(f"{num3} é divisível por 2 e 3")
if(num4%2 == 0 and num4%3 == 0):
    print(f"{num4} é divisível por 2 e 3")
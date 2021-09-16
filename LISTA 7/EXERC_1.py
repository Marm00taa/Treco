import sys,time,os,math

Menu=0

menu=int(input("MENU \n1. CALCULAR QUAIS NÚMEROS SÃO DIVISIVEIS POR 2 E 3 \n2. MAIOR NÚMERO\n"))


if(menu==1):
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

if(menu==2):
    num1=num2=num3=num4=num5=aux=0
    num1=int(input("Digite o 1 valor: "))
    num2=int(input("Digite o 2 valor: "))
    num3=int(input("Digite o 3 valor: "))
    num4=int(input("Digite o 4 valor: "))
    num4=int(input("Digite o 4 valor: "))
    num5=int(input("Digite o 5 valor: "))

    if(num1>aux):
       aux=num1
    if(num2>aux):
       aux=num2
    if(num3>aux):
       aux=num3
    if(num4>aux):
       aux=num4
    if(num5>aux):
      aux=num5


    print (f"{aux}")
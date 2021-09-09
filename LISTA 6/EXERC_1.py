import os,sys,time,math

Menu=0

print('Calculadora de equação do 2º grau \n')
print('1. Executar \n2. Sair \n')

Menu = int(input('Digite a opção: '))

if(Menu==1):

    a=0;b=0;c=0
    
    a=int(input('Digite o valor de A:'))
    b=int(input('Digite o valor de B:'))
    c=int(input('Digite o valor de C:'))

    delta= (b**2) - 4*a*c

    if(a==0):
        print('O valor de A deve ser diferente de 0')
    elif delta<0:
        print('Sem raizes reais')
        print(f' A: {a}\n B: {b} \n C: {c} \n Delta: {delta}')
    else:
        x1= (-b+math.sqrt(delta)) / 2*a
        x2= (-b-math.sqrt(delta)) / 2*a
        print(f' A: {a}\n B: {b} \n C: {c} \n Delta: {delta}\n x1: {x1}\n x2: {x2}')

elif(Menu==2):
    print ('Saindo')
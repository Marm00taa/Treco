import os,sys,time,math

Menu=0
A=B=C=0
delta= B*B-4*A*C
x1= -B+math.sqrt(delta)/2*A
x2= -B-math.sqrt(delta)/2*A

print('Calculadora de equação do 2º grau \n')
print('1. Executar \n2. Sair \n')

Menu = int(input('Digite a opção: '))

if(Menu==1):
    print (Menu)
else:
    print ('Saindo')
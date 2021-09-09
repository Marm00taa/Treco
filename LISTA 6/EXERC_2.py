import sys,time,os,math

a=b=c=0
triangulo=False

print('Calculadora de Triângulo \n')
print('1. Executar \n2. Sair \n')

menu = int(input('Digite a opção: '))

if(menu==1):
    a=int(input('Digite o valor de A:'))
    b=int(input('Digite o valor de B:'))
    c=int(input('Digite o valor de C:'))

    if a>=(b+c) or b>=(a+c) or c>=(b+a):
     print('NÃO É UM TRIÂNGULO')   
    else:
        triangulo=True

if(triangulo==True):

    print('\nÉ um triângulo\n')

    if(a==b) and (a==c):
        print('TRIÂNGULO EQUILATERO')
    elif (a==b) or (a==c) or (b==c):
        print('TRIÂNGULO ISÓCELES')
    else:
        print('TRIÂNGULO ESCANELO')

    MedLado1  = a
    MedLado2  = b
    MedLado3  = c
    P= (MedLado1 + MedLado2 + MedLado3) / 2
    A=int(P*(P-MedLado1)*(P-MedLado2)*(P-MedLado3)**(1/2))

    print(f'\nA area do triangulo é: {A}'f'cm² (aproximadamente) \nO semiperímetro é: {P}')
else:
    print('Uma figura qualquer de três lados')
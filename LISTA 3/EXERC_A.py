a=0;b=0;c=0

print('calculadora de diferença\n')

a=float(input('Digite o valor de A: '))
b=float(input('Digite o valor de B: '))

if(a>b): c=a-b
else: c=b-a

c=str(c)

print('O resultado da subtração é: '+c)
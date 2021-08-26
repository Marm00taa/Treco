import math

a=0;b=0;c=0
delta= (b**2) - 4*a*c

a=float(input('Digite o valor de A:'))
b=float(input('Digite o valor de B:'))
c=float(input('Digite o valor de C:'))

if(a==0):
    print('O valor de A deve ser diferente de 0')
elif delta<0:
    print('Sem raizes reais')
else:
   x1= (-b+math.sqrt(delta)) / 2*a
   x2= (-b-math.sqrt(delta)) / 2*a

   print('x1= {}\nx2= {}'.format(x1,x2))

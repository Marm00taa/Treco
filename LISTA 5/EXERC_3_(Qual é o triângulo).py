A=B=C=0

A = float(input('Digite o 1º Valor: '))
B = float(input('Digite o 2º Valor: '))
C = float(input('Digite o 3º Valor: '))

if A>=(B+C) or B>=(A+C) or C>=(B+A):
     print('NÃO É UM TRIÂNGULO')
else:   
    if(A==B) and (A==C):
        print('TRIÂNGULO EQUILATERO')
    elif (A==B) or (A==C) or (B==C):
        print('TRIÂNGULO ISÓCELES')
    else:
        print('TRIÂNGULO ESCANELO')
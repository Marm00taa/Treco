import math

G=9.8; altura=0;TQ=0

altura=float(input('Digite a altura da queda em cm: '))

TQ=(math.sqrt(2*altura))/G

TQ=str(TQ)

print('O tempo de queda é de: '+TQ+' segundos')
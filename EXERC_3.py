raio=0; altura=0; volume=0;pi=3.14

print('Calcularoda de volume de círculo\n')
altura=float(input('digite a altura em cm: '))
raio=float(input('digite o raio em cm: '))

volume= (pi*(raio**2)*altura)
volume=str(volume)

print('Volume '+volume+' cm³')
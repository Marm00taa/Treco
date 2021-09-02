import os
import sys
import time

NumLados = 0;MedLado1 = 0;MedLado2 = 0;MedLado3 = 0;A = 0;P = 0

NumLados = float (input ('Digite o Numero de Lados: '))

if NumLados < 3:
    print ('Não é um poligono')
    sys.exit()


elif NumLados == 3:
    print ('TRIÂNGULO')
    MedLado1  = float (input ('Digite o primeiro lado: '))
    MedLado2  = float (input ('Digite o segundo lado: '))
    MedLado3  = float (input ('Digite o terceiro lado: '))
    P= (MedLado1 + MedLado2 + MedLado3) / 2
    A= (P*(P-MedLado1)*(P-MedLado2)*(P-MedLado3)**(1/2))
    print(f'\n A area do triangulo é: {A}''cm² (aproximadamente) ')
    
    

elif NumLados == 4:
    print ('QUADRADO')
    MedLado1 = float (input ('Digite o lado do quadrado: '))
    A= MedLado1 * MedLado1
    print(f'\n A area do quadrado é de: {A}''cm²')

elif NumLados == 5:
    print ('PENTAGONO')
elif NumLados > 5:
    print('Polígono não identificado')
diametro=0;perimetro=0;raio=0;area=0; pi=3.14

perimetro=float(input('Digite o perimetro di círculo em cm: '))

diametro=perimetro/pi
raio=diametro/2
area=(raio**2)*pi

diametro=str(diametro)
raio=str(raio)
area=str(area)

print('O Diâmetro do circulo é: '+diametro+' cm'+'\nO raio do cículo é: '+raio+' cm'+'\nA área do círculo é:'+area+' cm')
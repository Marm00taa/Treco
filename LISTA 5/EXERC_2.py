import os
import sys
import time

A=B=C=0

A= int(input('Digite o 1º valor: '))
B= int(input('Digete o 2º valor: '))
C= int(input('Digite o 3º valor: '))

if A>B and A>C:
    print(f'O maior valor é: {A}')
elif B>A and B>C:
    print(f'O maior valor é: {B}')
elif C>A and C>B:
    print(f'O maior valor é: {C}')
PRESTACAO = 0; VALOR = 0; TAXA = 0; TEMPO = 0

VALOR=float(input('Digite o valor da prestação em R$: '))
TAXA=float(input('Digite a taxa de atraso: '))
TEMPO=float(input('Digite o tempo de atraso em meses: '))

PRESTACAO = (VALOR + (VALOR * TAXA/100) * TEMPO)
PRESTACAO=str(PRESTACAO)

print('R$ '+PRESTACAO)
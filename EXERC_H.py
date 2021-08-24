VOLUME = 0; COMPRIMENTO = 0; LARGURA = 0; ALTURA = 0

COMPRIMENTO=float(input('Digite o comprimento da caixa em cm: '))
LARGURA=float(input('Digite a largura da caixa em cm: '))
ALTURA=float(input('Digite a altura da caixa em cm: '))

VOLUME = COMPRIMENTO * LARGURA * ALTURA
VOLUME = str(VOLUME)

print('A caixa tem '+VOLUME+' cm³')
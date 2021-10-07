import sys,time,os,math

txmulta=0.02
txjuros=0.02

valor = float(input("Digite o valor da prestação em atraso: R$"))
dias = int(input("Quantos dias de atraso: "))

multa=valor*txmulta
juros=txjuros*1/30*dias*valor
vlpagar=valor+multa+juros

print("")
print(f"O valor da sua prestação é de: R${valor:,.2f}.\n\
O total de dias em atrazo é de:{dias} dias.\n\
O valor da Multa: R${multa:,.2f}.\n\
O valor dos Juros: R${juros:,.2f}.\n\
E o total a pagar R${vlpagar:,.2f}")
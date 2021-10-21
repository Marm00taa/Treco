import sys,time,os

def calcular(i,t):
    c=i/(0.05*t)
    return c

def leri():
    i=float(input("Qual foi o montante recebido:"))
    return i

def lert():
    t=int(input("Qual foi o período em meses aplicado: "))
    return t

def rerun():
    reiniciar=int(input("Deseja executar o programa novamente? 1=SIM 2=NÃO"))
    if(reiniciar==1):
        Menu()
    else:
        sys.exit

def listar(c,t,i):
    print(f'O valor iniciar era de: R${c:,.2f} \
        \nO periodo de aplicação foi de: {t} meses \
        \nO montante recebido foi de: R${i:,.2f}')

def executar():
    i=leri()
    t=lert()
    c=calcular(i,t)
    d=listar(c,t,i)
    time.sleep(5)
    rerun()

def Menu():
    os.system("cls")
    print("1. Calcular")
    print("2. Sair")
    ep = int(input("Digite a Opção Desejada: "))
    if ep < 1 or ep > 2:
        print("\nOpção Inválida,Tente Novamente")
        time.sleep(3)
        os.system("cls")
    elif ep == 2:
        sys.exit()
    elif ep == 1:
        executar()

Menu()
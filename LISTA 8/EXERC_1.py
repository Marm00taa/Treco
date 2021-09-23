import sys,time,os,math

nome=str(input("digite o seu nome: \n"))
email=str(input("digite o seu e-mail: \n"))
idade=int(input("digite a sua idade: \n"))
telefone=int(input("digite o seu telefone: \n"))
rua=str(input("digite o seu endereço: \n"))
numero=int(input("digite o número da sua casa: \n"))
cep=int(input("digite o seu cep: \n"))
bairro=str(input("digite o seu bairro: \n"))
cidade=str(input("digite a sua cidade: \n"))
estado=str(input("digite o seu estado: \n"))
pais=str(input("digite o seu país: \n"))
salario=float(input("digite o seu salário: \n"))

print("Olá, meu nome é {}, tenho {} anos.\n\
meu e-mail é: {}, e meu telefone: {}\n\
Moro na rua {} número {} CEP:{}, bairro {} - {},{}.{}.\n\
Meu salário é: R${:.2f}".format(nome,idade,email,telefone,rua,numero,cep,bairro,cidade,estado,pais,salario)) 
peso_pessoa = float(input("Insira seu peso em quilogramas: "))
altura_pessoa = int(input("Insira sua altura em centímetros: "))
calculo_imc = (peso_pessoa * 10000 ) / (altura_pessoa * altura_pessoa)

print("Modos de exercício: ")
print("Para intenso leve 1")
print("Para moderado insira 2")
print("Para leve insira 3")
intensidade_exercicio = int(input("Insira o quão intenso gostaria de ser seu exercício: "))

meta_hidratacao = (peso_pessoa * 0.035) + (intensidade_exercicio * 0.5)

print("Qual o tipo de exercício que você irá realizar: ")
print("Para Aeróbico insira 1")
print("Para Cardiovascular insira 2")
print("Para alongamento insira 3")
tipo_exercicio = int(input("Insira o tipo de exercício: "))

if tipo_exercicio == 1:
    print()
elif tipo_exercicio == 2:
    print()
elif tipo_exercicio == 3:
    print()
else:
    print()


print(calculo_imc)
print(meta_hidratacao)
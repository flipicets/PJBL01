peso_pessoa = float(input("Insira seu peso em quilogramas: "))
altura_pessoa = int(input("Insira sua altura em centímetros: "))
calculo_imc = (peso_pessoa * 10000 ) / (altura_pessoa * altura_pessoa)

print("Modos de exercício: ")
print("Para intenso leve 1")
print("Para moderado insira 2")
print("Para leve intenso 3")
intensidade_exercicio = int(input("Insira o quão intenso gostaria de ser seu exercício: "))

meta_hidratacao = (peso_pessoa * 0.035) + (intensidade_exercicio * 0.5)


print(calculo_imc)
print(meta_hidratacao)
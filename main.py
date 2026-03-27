print("Qual funcionalidade deseja acessar")
print("Para cálculo de IMC, digite 1")
print("Para meta diária de hidratação, digite 2")
print("Para saber seu gasto calórico em atividade física, digite 3")
print("Para verificar a meta diária de exercício, digite 4")
print("Para mostrar seu resumo diário, digite 5")
print("Para sair, digite 6")
menu_iniciar = int(input())

if menu_iniciar == 1:
    peso_pessoa = float(input("Insira seu peso em quilogramas: "))
    altura_pessoa = int(input("Insira sua altura em centímetros: "))
    calculo_imc = (peso_pessoa * 10000 ) / (altura_pessoa * altura_pessoa)
    print("Seu IMC é de ", calculo_imc)

elif menu_iniciar == 2:
    peso_pessoa = float(input("Insira seu peso em quilogramas: "))
    meta_hidratacao = (peso_pessoa * 0.035)
    print("Você precisa beber, no mínimo, ", meta_hidratacao, "litros de água por dia")

elif menu_iniciar == 3:
    print("Modos de exercício: ")
    print("Para intenso leve 1")
    print("Para moderado insira 2")
    print("Para leve insira 3")
    intensidade_exercicio = int(input())
    print("Qual o tipo de exercício que você irá realizar: ")
    print("Para Aeróbico insira 1")
    print("Para Cardiovascular insira 2")
    print("Para Alongamento insira 3")
    tipo_exercicio = int(input("Insira o tipo de exercício: "))
    if tipo_exercicio == 1:
        print()
    elif tipo_exercicio == 2:
        print()
    elif tipo_exercicio == 3:
        print()
    else:
        print()
menu_iniciar = 0
while menu_iniciar != 1 and menu_iniciar != 2 and menu_iniciar != 3 and menu_iniciar != 4 and menu_iniciar != 5 and menu_iniciar != 6:
    print("Qual funcionalidade deseja acessar")
    print("Para cálculo de IMC, digite 1")
    print("Para meta diária de hidratação, digite 2")
    print("Para saber seu gasto calórico em atividade física, digite 3")
    print("Para verificar a meta diária de exercício, digite 4")
    print("Para mostrar seu resumo diário, digite 5")
    print("Para sair, digite 6")
    menu_iniciar = int(input())
    print()

    if menu_iniciar == 1:
        peso_pessoa = float(input("Insira seu peso em quilogramas: "))
        altura_pessoa = int(input("Insira sua altura em centímetros: "))
        calculo_imc = (peso_pessoa * 10000) / (altura_pessoa * altura_pessoa)
        print("Seu IMC é de ", calculo_imc)

    elif menu_iniciar == 2:
        peso_pessoa = float(input("Insira seu peso em quilogramas: "))
        meta_hidratacao = (peso_pessoa * 0.035)
        print("Você precisa beber, no mínimo, ", meta_hidratacao, "litros de água por dia")

    elif menu_iniciar == 3:
        print("Para melhor estimar seu gasto calórico, é necessário informar seu sexo.")
        print("Para sexo masculino, digite 1")
        print("Para sexo feminino, digite 2")
        sexo_pessoa = int(input())

        while sexo_pessoa != 1 and sexo_pessoa != 2:
            print("Por favor, escolha uma opção valida.")
            print("Para sexo masculino, digite 1")
            print("Para sexo feminino, digite 2")
            sexo_pessoa = int(input())


        peso_pessoa = float(input("Insira seu peso em quilogramas: "))
        idade_pessoa = int(input("Insira sua idade em anos: "))
        altura_pessoa = int(input("Insira sua altura em centímetros:"))

        print()
        print("Modos de exercício: ")
        print("Para leve leve 1")
        print("Para moderado insira 2")
        print("Para intenso insira 3")
        intensidade_exercicio = int(input())

        while intensidade_exercicio != 1 and intensidade_exercicio != 2 and intensidade_exercicio != 3:
            print("Por favor, escolha uma opção válida.")
            print()
            print("Modos de exercício: ")
            print("Para leve leve 1")
            print("Para moderado insira 2")
            print("Para intenso insira 3")
            intensidade_exercicio = int(input())

        if sexo_pessoa == 1:
            taxa_metabolica = (10 * peso_pessoa) + (6.25 * altura_pessoa) - (5 * idade_pessoa) + 5
            if intensidade_exercicio == 1:
                calorias_gastas = taxa_metabolica * 1.375
            elif intensidade_exercicio == 2:
                calorias_gastas = taxa_metabolica * 1.55
            else:
                calorias_gastas = taxa_metabolica * 1.9
            print("Você gastou, em média,", calorias_gastas, "calorias hoje.")

        elif sexo_pessoa == 2:
            taxa_metabolica = (10 * peso_pessoa) + (6.25 * altura_pessoa) - (5 * idade_pessoa) - 161
            if intensidade_exercicio == 1:
                calorias_gastas = taxa_metabolica * 1.375
            elif intensidade_exercicio == 2:
                calorias_gastas = taxa_metabolica * 1.55
            else:
                calorias_gastas = taxa_metabolica * 1.9
            print("Você gastou, em média,", calorias_gastas, "calorias hoje.")

    elif menu_iniciar == 4:
        print()

    elif menu_iniciar == 5:
        print()

    elif menu_iniciar == 6:
        break

    else:
        print("Por favor, insira uma opção valida.")
        print()
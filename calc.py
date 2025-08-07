while True:
    print("Bem vindo a calculadora.")
    print("Selecione uma das opções abaixo para prosseguir.")
    print("1- Soma")
    print("2- Subtração")
    print("3- Multiplicação")
    print("4- Divisão")
    print("5- Sair")

    opcao = input("Digite o número da opção desejada:")
    
    if opcao == "1":
            print("A opção escolhida foi soma.")
            input("Pressione ENTER para continuar.")
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado = num1 + num2
            print(resultado)
            input("Pressione enter para voltar ao menu inicial.")
    if opcao == "2":
            print("A opção escolhida foi subtração.")
            input("Pressione ENTER para continuar.")
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado = num1 - num2
            print(resultado)
            input("Pressione enter para voltar ao menu inicial.")
    if opcao == "3":
        print("A opção escolhida foi multiplicação.")
        input("Pressione ENTER para continuar.")
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 * num2
        print(resultado)
        input("Pressione enter para voltar ao menu inicial.")
    if opcao == "4":
        print("A opção escolhida foi divisão.")
        input("Pressione ENTER para continuar.")
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 / num2
        print(resultado)
        input("Pressione enter para voltar ao menu inicial.")
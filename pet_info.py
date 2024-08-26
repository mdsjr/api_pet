def coletar_informacoes_pet():    

    nome = input("Nome do pet: ")

    while True:
        try:
            idade = int(input("Idade do pet (em anos): "))
            if idade < 0:
                print("A idade não pode ser negativa. Tente novamente.")
            else:
                break
        except ValueError:
            print("Por favor, insira um número válido para a idade.")

    while True:
        try:
            peso = float(input("Peso do pet (em kg): "))
            if peso < 0:
                print("O peso não pode ser negativo. Tente novamente.")
            else:
                break
        except ValueError:
            print("Por favor, insira um número válido para o peso.")

    while True:
        try:
            altura = float(input("Altura do pet (em cm): "))
            if altura < 0:
                print("a altura não pode ser negativo. Tente novamente.")
            else:
                break
        except ValueError:
            print("Por favor, insira um número válido para a altura.")       

    print("\nInformações do pet:")
    print(f"Nome: {nome}")
    print(f"Idade: {idade} anos")
    print(f"Peso: {peso} kg")
    print(f"Altura: {altura} cm")

coletar_informacoes_pet()

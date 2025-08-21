class Calculadora:
    def adicao(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        if b == 0:
            return "Erro: divisão por zero não é permitida."
        return a / b

    def porcentagem(self, valor, percentual):
        return (valor * percentual) / 100

    def potenciacao(self, base, expoente):
        resultado = 1
        if expoente < 0:
            for _ in range(-expoente):
                resultado *= base
            return 1 / resultado
        else:
            for _ in range(expoente):
                resultado *= base
            return resultado


# --- Menu interativo com loop ---
calc = Calculadora()

while True:
    print("\n=== Calculadora ===")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Porcentagem")
    print("6 - Potenciação")
    print("7 - Sair")

    opcao = int(input("Escolha a operação: "))

    match opcao:
        case 1:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            print("Resultado:", calc.adicao(a, b))

        case 2:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            print("Resultado:", calc.subtracao(a, b))

        case 3:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            print("Resultado:", calc.multiplicacao(a, b))

        case 4:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            print("Resultado:", calc.divisao(a, b))

        case 5:
            valor = float(input("Digite o valor: "))
            percentual = float(input("Digite o percentual: "))
            print("Resultado:", calc.porcentagem(valor, percentual))

        case 6:
            base = float(input("Digite a base: "))
            expoente = int(input("Digite o expoente: "))
            print("Resultado:", calc.potenciacao(base, expoente))

        case 7:
            print("Saindo da calculadora...")
            break

        case _:
            print("Opção inválida. Tente novamente.")

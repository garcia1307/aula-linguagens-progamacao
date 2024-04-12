valor1 = int(input('Digite um valor: '))
operador = input('Digite um operador: ')
valor2 = int(input('Digite outro valor: '))

while valor1 != -1 and valor2 != -1:

    if operador == '+':
        resultado = valor1 + valor2
    elif operador == '-':
        resultado = valor1 - valor2
    elif operador == '*':
        resultado = valor1 * valor2
    elif operador == '/':
        resultado = valor1 / valor2
    else:
        print('operador inválido')

    print(resultado)

    valor1 = int(input('Digite um valor: '))
    operador = input('Digite um operador: ')
    valor2 = int(input('Digite outro valor: '))
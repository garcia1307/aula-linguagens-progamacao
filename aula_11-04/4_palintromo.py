texto = input("Digite um texto: ")
caracteres = ',.!? '

for i in range(len(caracteres)):
    texto = texto.replace(caracteres[i], '')

texto_maiusculo = texto.upper()
texto_invertido = texto_maiusculo[::-1]

if texto_maiusculo == texto_invertido:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")
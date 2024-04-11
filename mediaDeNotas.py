notas = []
soma = 0
i = 1

nota =  float(input('Nota[1]: '))
while nota != -1:
    notas.append(nota)
    i += 1
    nota =  float(input('Nota[' + str(i) + ']: '))

media = sum(notas)/len(notas)

if media >= 7:
    print('Aprovado')

else:
    print('Reprovado')
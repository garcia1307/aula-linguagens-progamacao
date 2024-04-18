from datetime import datetime

busca = input('Aluno(a): ')
nome_busca, sobrenome_busca = busca.split(' ')

with open('dados.csv', 'r') as alunos:
    next(alunos)
    lista_linhas = alunos.readlines()
    
    for linha in lista_linhas:

        nome_chamada, data_nascimento, matricula = linha.strip('\n').split(',')

        nome,sobrenome,numero = nome_chamada.split(' ')


if (nome.lower() == nome_busca.lower()) and (sobrenome.lower() == sobrenome_busca.lower()):
    data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')
    hoje = datetime.now()
    idade = hoje.year - data_nascimento.year

    print(f'Nome: {nome_chamada} Idade: {idade}')
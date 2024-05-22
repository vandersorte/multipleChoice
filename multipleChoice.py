perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['10', '55', '25', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

print('\t\t\tTeste Múltipla-Escolha\n')

import emoji    # biblioteca para importar emoji no windows
emoji_resposta_correta = emoji.emojize(':check_mark:')
emoji_resposta_errada = emoji.emojize(':cross_mark:')

acertos = 0
for pergunta in perguntas:
    print(pergunta['Pergunta'])
    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i}) {opcao}')
    questoes = input('Resposta: ')

    opcao_escolhida = int(questoes)

    if opcoes[opcao_escolhida] == pergunta['Resposta']:
        acertos+=1
        print(f'Correto {emoji_resposta_correta}\n')
    else:
        print(f'Errado {emoji_resposta_errada}')
        print('Resposta correta:', pergunta['Resposta'],'\n')

print(f'Acertos: {acertos} de {len(perguntas)}')
 
txt = open('acertos.txt', 'a')

acertos = acertos2 = erros = 0
questoes = [
    [1, 'D'], [2, 'C'], [3, 'B'],
    [4, 'D'], [5, 'E'], [6, 'E'],
    [7, 'A'], [8, 'A'], [9, 'A'],
    [10, 'C'], [11, 'A'], [12, 'B'],
    [13, 'B'], [14, 'D'], [15, 'B'],
    [16, 'E'], [17, 'B'], [18, 'A'],
    [19, 'C'], [20, 'C'], [21, 'B'],
    [22, 'E'], [23, 'E'], [24, 'E'], [25, 'C'],
    [26, 'C'], [27, 'B'], [28, 'B'],
    [29, 'D'], [30, 'C'], [31, 'A'],
    [32, 'A'], [33, 'A'], [34, 'D'],
    [35, 'C'], [36, 'C'], [37, 'A'],
    [38, 'B'], [39, 'E'], [40, 'D'], [41, 'B'],
    [42, 'D'], [43, 'E'], [44, 'C'], [45, 'E']
]
questoes2 = [
    [46, 'D'], [47, 'E'], [48, 'A'],
    [49, 'B'], [50, 'E'], [51, 'E'],
    [52, 'D'], [53, 'A'], [54, 'E'],
    [55, 'B'], [56, 'A'], [57, 'A'],
    [58, 'E'], [59, 'C'], [60, 'B'],
    [61, 'E'], [62, 'C'], [63, 'B'],
    [64, 'A'], [65, 'B'], [66, 'C'], [67, 'D'],
    [68, 'D'], [69, 'A'], [70, 'A'], [71, 'A'],
    [72, 'D'], [73, 'B'], [74, 'C'], [75, 'E'],
    [76, 'D'], [77, 'A'], [78, 'E'], [79, 'A'],
    [80, 'C'], [81, 'D'], [82, 'B'], [83, 'B'],
    [84, 'C'], [85, 'D'], [86, 'C'],
    [87, 'B'], [88, 'E'], [89, 'C'], [90, 'A']
]

for c, v in enumerate(questoes):
    resposta = v[1]
    nquestao = v[0]
    if c >= 1:
        print('=' * 50)
        print(f'Acertou {acertos} de {c}')
    print('=' * 50)
    r = str(input(f'Questão {nquestao}:\n'
                  f'Colocou qual? [A~E]\n'
                  )).upper()[0]

    if r != resposta:
        erros += 1
        print(f'ERROU!\n')
    elif r == resposta:
        acertos += 1
        print(f'ACERTOU!\n')
    else:
        break

print('=' * 50)
print(f'Quantidade de Acertos 1° Parte: {acertos}'
      f'\nTotal: 45'
      f'\n')

for c, v in enumerate(questoes2):
    resposta = v[1]
    nquestao = v[0]
    if c >= 1:
        print('=' * 50)
        print(f'Acertou {acertos2} de {c}')
    print('=' * 50)
    r = str(input(f'Questão {nquestao}:\n'
                  f'Colocou qual? [A~E]\n'
                  )).upper()[0]

    if r != resposta:
        erros += 1
        print(f'ERROU!\n')
    elif r == resposta:
        acertos2 += 1
        print(f'ACERTOU!\n')
    else:
        break

print('=' * 50)
print(f'Quantidade de Acertos 2° Parte: {acertos + acertos2}')

txt.write(f'Quantidade de Acertos: {acertos + acertos2}\n'
          f'Do total de 90 Questões\n'
          f'Erros: {erros}')

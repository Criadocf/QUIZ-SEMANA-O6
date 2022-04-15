score = int(0)



jogador = input('QUEM FOI O MELHOR JOGADOR DE FUTEBOL DO MUNDO EM 1998?\n') .upper()
if jogador == ('ZIDANE'):
    print()
elif jogador == ('RONALDO'):
    print()
else:
    print()
if jogador == 'ZIDANE':
    score = score + 1


selecao = input('QUAL SELEÇÃO TEM MAIS TÍTULOS DA COPA DO MUNDO?\n') .upper()
if selecao == 'BRASIL':
    print()
elif selecao == 'ITÁLIA':
    print()
elif selecao == 'ARGENTINA':
    print()
else:
    print()

if selecao == 'BRASIL':
    score = score + 1
    
print(f'SUA PONTUAÇÃO FOI DE {score} PT(S)')
    
if score == 2:
    print('muito bem!')
else:
    print('tente novamente')
    

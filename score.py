score = int(0)



jogador = input('QUEM FOI O MELHOR JOGADOR DE FUTEBOL DO MUNDO EM 1998?') .upper()
if jogador == ('ZIDANE'):
    print('BOA, MANJA MUITO')
elif jogador == ('RONALDO'):
    print('PODERIA TER SIDO, MAS NÃO FOI!')
else:
    print('VOCÊ NÃO ESTÁ TÃO POR DENTRO')
if jogador == 'ZIDANE':
    score = score + 1


selecao = input('QUAL SELEÇÃO TEM MAIS TÍTULOS DA COPA DO MUNDO?') .upper()
if selecao == 'BRASIL':
    print('ACERTOU')
elif selecao == 'ITÁLIA':
    print('OH, NO! ELES TÊM 4, MAS NÃO SÃO O MAIOR CAMPEÃO!')
elif selecao == 'ARGENTINA':
    print('GRAÇAS A DEUS NÃO :) ')
else:
    print('VOCÊ ESTÁ DESANTENADO')

if selecao == 'BRASIL':
    score = score + 1
    

print(f'SEU SCORE FOI DE {score} PT(S).')


    
    
    

    


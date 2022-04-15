def naturalidade(sigla):
    if sigla .upper() == 'CE':
        return 'VOCÊ É CEARENSE'
    elif sigla. upper() == 'SP':
        return 'VOCÊ É PAULISTA'
    elif sigla .upper() == 'PI':
        return 'VOCÊ É PIAUIENSE'
    else:
        print('VOCÊ É DE OUTRO ESTADO')

lugar = input('DE QUAL ESTADO VOCÊ É? \n')

ch = naturalidade(lugar)

print(ch)
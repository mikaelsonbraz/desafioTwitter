units = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
             'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']
dezenas = ['vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
centenas = ['cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos', 'oitocentos', 'novecentos']
casas = [[' real', ' reais'], [' mil', ' mil'], [' milhão', ' milhões'], [' bilhão', ' bilhões'], [' trilhao', ' trilhões']]


def countCents(cents: str) -> str:
    centavos = cents.split('.')[1]
    if len(centavos) > 1 and int(centavos) <= 19:
        value = units[int(centavos)]
    else:
        if len(centavos) == 1 or int(centavos[1]) == 0:
            if centavos == '0':
                value = units[int(centavos)]
            else:
                value = dezenas[int(centavos[0]) - 2]
        else:
            value = dezenas[int(centavos[0]) - 2] + ' e ' + units[int(centavos[1])]
    return value + ' centavos'


def countCentenas(centena: str) -> str:
    casaUnidade = centena[-1]
    casaDezena = centena[-2] if len(centena) >= 2 else ''
    casaCentena = centena[-3] if len(centena) >= 3 else ''
    if casaDezena:
        if int(casaDezena + casaUnidade) <= 19:
            value = units[int(casaDezena + casaUnidade)]
        else:
            value = dezenas[int(casaDezena) - 2] + ' e ' + units[int(casaUnidade)] if casaUnidade != '0' else dezenas[int(casaDezena) - 2]
    else:
        value = units[int(casaUnidade)]
    if casaCentena:
        if casaCentena != '0':
            value = centenas[int(casaCentena) - 1] + ' e ' + value if value != 'zero' else centenas[int(casaCentena) - 1]
    return value


def valorPorExtenso(valor: str) -> str:
    reais = valor.split('.')[0]
    centenas = []
    extenso = ''
    resto = len(reais) % 3
    for item in reversed(reais):
        extenso = item + extenso
        if len(extenso) == 3:
            centenas.append(extenso)
            extenso = ''
    extenso = ''
    for item in range(resto): extenso += reais[item]
    if extenso:
        centenas.append(extenso)
    extenso = ''
    for item in range(len(centenas)):
        if int(centenas[item]) == 0:
            pass
        elif int(centenas[item]) == 1:
            extenso = countCentenas(centenas[item]) + casas[item][0] + ', ' + extenso
        else:
            extenso = countCentenas(centenas[item]) + casas[item][1] + ', ' + extenso
    return extenso[:-2] + ' e ' + countCents(valor)

print(valorPorExtenso("245123.43"))
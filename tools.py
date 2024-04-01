# MOEDAS
def half(n, format = True):
    if format:
        return 'R${:.2f}'.format(n/2)
    else:
        return n/2


def double(n, format = True):
    if format:
        return 'R${:.2f}'.format(n*2)
    else:
        return n * 2


def aumento(n, x = 10, format = True):
    if format:
        return 'R${:.2f}'.format(n*(1+(x/100)))
    else:
        return n * 1.1


def reduçao(n, x = 13, format = True):
    if format:
        return 'R${:.2f}'.format(n * (1 - (x/100)))
    else:
        return n * (1 - (x / 100))


def moeda(n):
    x = float(n)
    return 'R${:.2f}'.format(x)


def resumo(n, a, r):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)
    print(f'Preço analisados:   {moeda(n)}')
    print(f'Dobro do preço:     {double(n)}')
    print(f'Metade do preço:    {half(n)}')
    print(f'{a}% de aumento:     {aumento(n, a)}')
    print(f'{r}% de redução:     {reduçao(n, r)}')
    print('-' * 30)


def leiaInt(msg):
    while True:
        try:
            a = str(input(msg)).strip().replace(',','.')
            a = int(a)
        except KeyboardInterrupt:
            print('Usuário preferiu não informar um número.')
            return 0
        except:
            print('\033[31mERRO! Por favor digite um número inteiro válido.\033[m')
        else:
            return a
            break

def leiaFloat(msg):
    while True:
        try:
            a = str(input(msg)).strip().replace(',','.')
            a = float(a)
        except KeyboardInterrupt:
            print('Usuário preferiu não informar um número.')
            return 0
        except:
            print('\033[31mERRO! Por favor digite um número real válido.\033[m')
        else:
            return a
            break

def leiaNome(msg):
    while True:
        a = str(input(msg)).strip().title()
        listaA = list(a)
        x = listaA.count(' ')
        if x > 0:
            for i in range(x):
                listaA.remove(' ')
        f = ''.join(listaA)

        if len(a) > 0 and f.isalpha():
            return a
            break
        else:
            print('Por favor, digite seu nome.')
            

def leiaInt2(msg):
    while True:
        try:
            a = str(input(msg)).strip().replace(',','.')
            a = str(a)
        except KeyboardInterrupt:
            print('Usuário preferiu não informar um número.')
            return 0
        except:
            print('\033[31mERRO! Por favor digite um número inteiro válido.\033[m')
        else:
            return a
        

def leiaResposta(msg):
    while True:
        a = str(input(msg)).strip().lower()
        # retira espaçoes
        listaA = list(a)
        x = listaA.count(' ')
        if x > 0:
            for i in range(x):
                listaA.remove(' ')
        f = ''.join(listaA)

        if len(a) > 0 and f.isalpha():
            return a
            break
        else:
            print('Por favor, digite sua resposta.')


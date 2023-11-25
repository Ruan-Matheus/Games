# Jogo da forca
# TODO --> Implementar o chute (chute de uma palavra completa)


from random import choice

def input_letra(msg):
    while True:
        char = input(msg)
        if char.isalpha():
            return char
        

def substituir_todas_letras(letra, palavra, palavra_display):
    global over_count
    if letra not in palavra_display:
        indexes = []
        for i, valor in enumerate(palavra):
            if valor == letra:
                indexes.append(i)

        for i in indexes:
            palavra_display[i] = letra
            over_count -= 1
    
    
palavras = ["jogador", "tabuleiro", "vitoria", "derrota", "empate", "linha", "coluna", "diagonal", "espaco",
            "inicio", "fim", "reiniciar", "sair", "jogo", "velha", "estrategia", "turno", "computador", "humano",
            "diversao", "desafio", "ganhar", "perder", "empatar", "marcar", "posicao", "valido", "invalido",
            "jogada", "sequencia", "logica", "vencedor", "mensagem", "escolher", "alternar", "validar", "analisar",
            "processar", "movimento", "simbolo"]


palavra = choice(palavras)
palavra = 'fim'
tam_palavra = len(palavra)
palavra_display = ['_' for x in range(tam_palavra)]
over_count = tam_palavra
vidas = 1
over = False

print(f"{' BEM VINDO ':-^30}\n")

# Mudar cor e talvez centralizar?
print("Tente adivinhar a palavra a seguir...")


# Aqui começa o loop?
while not over:
    print()
    print(' '.join(palavra_display))
    print(f"\nSuas vidas: {vidas}")
    letra = input_letra("Escolha uma letra: ")
    if letra in palavra:
        substituir_todas_letras(letra, palavra, palavra_display)
    else:
        print("Errado! Voce perdeu uma vida!")
        vidas -= 1
        
    # Game over
    if over_count == 0:
        print(f"\033[32m\nVocê venceu! A palavra era: ", end = '')
        print(''.join(palavra_display))
        over = True
    elif vidas == 0:
        print("\033[31m\nVocê perdeu. Suas vidas se esgotaram!\033[m")
        over = True
    

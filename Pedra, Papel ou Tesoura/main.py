from random import choice
from time import sleep

def escolha_mov_input(msg):
    while True:
        try:
            valor = int(input(msg))
            if valor >= 1 and valor <= 3:
                break
            else: 
                print("Valor inválido. Digite um valor entre 1 e 3!")

        except:
            print("Valor inválido. Digite um valor entre 1 e 3!")
    
    return valor
    

escolhas = ["Pedra", "Papel", "Tesoura"]

print("Bem vindo ao jogo da Pedra, Papel ou Tesoura!!!")
sleep(1)
print("\nPreparado? Escolha uma opção dentre as abaixo")
print("1- Pedra \t2- Papel \t3- Tesoura")

pc_escolha = escolhas.index(choice(escolhas)) + 1
usuario_escolha = int(escolha_mov_input("Sua escolha: "))

print("\nJO...")
sleep(0.5)
print("KEN...")
sleep(0.5)
print("PO!!!")
sleep(0.5)

print(f"\nEscolha do usuário: {escolhas[usuario_escolha - 1]}")
sleep(1)
print(f"Escolha do computador: {escolhas[pc_escolha - 1]}\n")

sleep(0.5)
# Empate 
if pc_escolha == usuario_escolha:
    print("EMPATE!!!")
# Derrota
elif (pc_escolha == 1 and usuario_escolha == 3) or (pc_escolha == 2 and usuario_escolha == 1) or (pc_escolha == 3 and usuario_escolha == 2):
    print("DERROTA!!!")
# Vitória
else:
    print("VITÓRIA!!!")

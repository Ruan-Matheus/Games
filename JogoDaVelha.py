flag = 1
array = [[[ ], [ ], [ ]], [[ ], [ ], [ ]], [[ ], [ ], [ ]]]

def posj1():
    global flag
    while(flag != 0):
        print("\n\nJogador 1: Em que posição você quer jogar? ")
        
        j1l = int(input("Digite a linha: "))
        if j1l > 2 or j1l < 0:
            print("Valor inválido! Escolha uma posição entre 0 e 2")
            continue
        
        j1c = int(input("Digite a coluna: "))
        if j1c > 2 or j1c < 0:
            print("Valor inválido! Escolha uma posição entre 0 e 2")
            continue
        
        if vazio(j1l, j1c) == 1:
            array[j1l][j1c].append('X')
        else:
            continue
        break
    
def posj2():
    global flag
    while(flag != 0):
        print("\n\nJogador 2: Em que posição você quer jogar? ")
        
        j2l = int(input("Digite a linha: "))
        if j2l > 2 or j2l < 0:
            print("Valor inválido! Escolha uma posição entre 0 e 2")
            continue
        
        j2c = int(input("Digite a coluna: "))
        if j2c > 2 or j2c < 0:
            print("Valor inválido! Escolha uma posição entre 0 e 2")
            continue
        
        if vazio(j2l, j2c) == 1:
            array[j2l][j2c].append('O')
        else:
            continue
        break

def limite(n):
    if n < 0 or n > 2:
        print("Valor inválido! Escolha uma posição entre 0 e 2")
        flag = 1 
    else:
        print("Aqui")
        flag = 0
        
def vazio(l, c):
    if len(array[l][c]) != 0:
        print("\033[31mEspaço ocupado. Tente outra posição!\033[m")
        return -1
    else:
        return 1
    
def print_array():
    for i in range(3):
        print()
        for j in range(3):
            print(array[i][j], end = '')
            
def vitoria():
    pass
       
msg = " Bem Vindo! "
print(f'{msg:=^20}')

# Tudo isso dentro de um loop

while True:
    print_array()
    posj1()
    print_array()
    posj2()
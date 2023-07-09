import random

#Listas para formular os tabuleiros do computador
jogador1 = [[], [], [], [], [], [], [], [], [], []]
jogador1_limitado = [[], [], [], [], [], [], [], [], [], []]

# 10 valores para cada lista
for l in range(10):
    for c in range(10):
        jogador1[l].append(".")
def tabcomp():
    for l in range(10):
        for c in range(10):
            print(f"[{jogador1[l][c]}]", end=" ")
        print()

#Tabuleiro que irá aparecer para o player sem as posições dos navios
# 10 valores para cada lista
for l in range(10):
    for c in range(11):
        jogador1_limitado[l].append(".")
def tabcomp_limitado():
    print("-0- -1- -2- -3- -4- -5- -6- -7- -8- -9-")
    for l in range(10):
        for c in range(11):
            if c == 10:
                print(f"-{l}-", end = "")
            else:
                print(f"[{jogador1_limitado[l][c]}]", end=" ")
        print()


#NAVIO GRANDE PARA O TABULEIRO DO COMPUTADOR
escolhaG = random.choice(["posicionar_na_coluna", "posicionar_na_linha"])
if escolhaG == "posicionar_na_coluna":
    pos_linhaG = random.randint(0, 5)
    pos_colunaG = random.randint(0, 9)
    for i in range(4):
        jogador1[pos_linhaG + i][pos_colunaG] = "0"
else:
    pos_linha = random.randint(0, 9)
    pos_coluna = random.randint(0, 5)
    for i in range(4):
        jogador1[pos_linha][pos_coluna + i] = "0"
    

#VERIFICAR SE AS POSIÇÕES ESTÃO VAZIAS
def pode_adicionar_navio(jogador1, linha, coluna, tamanho, orientacao):
    for i in range(tamanho):
        if orientacao == "horizontal":
            if coluna + i >= len(jogador1[0]) or jogador1[linha][coluna + i] != ".":
                return False
        else:
            if linha + i >= len(jogador1) or jogador1[linha + i][coluna] != ".":
                return False
    return True


#NAVIO MÉDIO PARA O TABULEIRO DO COMPUTADOR
def navio_medio():
    for i in range(2):
        tamanho_navioM = 3
        while True:
            pos_linha = random.randint(0, 9)
            pos_coluna = random.randint(0, 9)
            escolha = random.choice(["horizontal", "vertical"])
            if pode_adicionar_navio(jogador1, pos_linha, pos_coluna, tamanho_navioM, escolha):
                break

        if escolha == "horizontal":
            for i in range(tamanho_navioM):
                jogador1[pos_linha][pos_coluna + i] = "0"
        else:
            for i in range(tamanho_navioM):
                jogador1[pos_linha + i][pos_coluna] = "0"
navio_medio()

#NAVIO PEQUENO PARA O TABULEIRO DO COMPUTADOR
def navio_pequeno():
    for i in range(3):
        tamanho_navioP = 2
        while True:
            pos_linha = random.randint(0, 9)
            pos_coluna = random.randint(0, 9)
            escolha = random.choice(["horizontal", "vertical"])
            if pode_adicionar_navio(jogador1, pos_linha, pos_coluna, tamanho_navioP, escolha):
                break

        if escolha == "horizontal":
            for i in range(tamanho_navioP):
                jogador1[pos_linha][pos_coluna + i] = "0"
        else:
            for i in range(tamanho_navioP):
                jogador1[pos_linha + i][pos_coluna] = "0"
navio_pequeno()
    
# Printar o tabuleiro para saber as posições dos navios do computador.
# Isso não faz parte do jogo, caso queira jogar corretamente.
print("\nTabuleiro completo do computador para análise do tutor: ")
tabcomp()

print("\n\n\nBATALHA NAVAL\nInício!!!")
# Print do tabuleiro do computador sem as posições dos navios.
print()
tabcomp_limitado()


# Criando tabuleiro do usuário
lista_usuario = [[], [], [], [], [], [], [], [], [], []]
for l in range(10):
    for c in range(10):
        lista_usuario[l].append(".")
def tab_usuario():
    for l in range(10):
        for c in range(10):
            print(f"[{lista_usuario[l][c]}]", end=" ")
        print()

#Posicionamento dos navios do usuario
#NAVIO GRANDE
orientacao_navioG = str(input("Digite se deseja posicionar o navio na \n- Horizontal\n- Vertical\n").lower())
while orientacao_navioG != "horizontal" and orientacao_navioG != "vertical":
    print("\nVocê digitou errado!\nDigite novamente.\n")
    orientacao_navioG = str(input("Digite se deseja posicionar o navio na \n- Horizontal\n- Vertical\n").lower())
if orientacao_navioG == "horizontal":
    while True:
        linha_navioG = int(input("\nDigite o numero da linha que deseja adicionar o navio grande de 0 a 9: "))
        if linha_navioG < 0 or linha_navioG > 9:
            print("Posição incorreta!\nDigite uma posição correta.")
            continue
        coluna_navioG = int(input("Digite o numero da coluna que deseja adicionar o navio grande de 0 a 6: "))
        if coluna_navioG < 0 or coluna_navioG > 6:
            print("Posição incorreta!\nDigite uma posição correta.")
            continue
        for i in range(4):
            lista_usuario[linha_navioG][coluna_navioG + i] = "0"
        break
elif orientacao_navioG == "vertical":
    while True:
        linha_navioG = int(input("Digite o numero da linha que deseja adicionar o navio grande de 0 a 6: "))
        if linha_navioG < 0 or linha_navioG > 6:
            print("Posição incorreta!\nDigite uma posição correta.")
            continue
        coluna_navioG = int(input("Digite o numero da coluna que deseja adicionar o navio grande de 0 a 9: "))
        if coluna_navioG < 0 or coluna_navioG > 9:
            print("Posição incorreta!\nDigite uma posição correta.")
            continue
        for i in range(4):
            lista_usuario[linha_navioG + i][coluna_navioG] = "0"
        break

#Adicionando navios de tamanho médio na matriz do usuário
def navioM_usuario():
    for i in range(2):
        tamanho_navioM = 3
        while True:
            escolha = str(input(f"Digite se deseja posicionar o {i+1}° navio médio na \n- Horizontal\n- Vertical\n").lower())
            while escolha != "horizontal" and escolha != "vertical":
                print("\nVocê digitou errado!\nDigite novamente.\n")
                escolha = str(input("Digite se deseja posicionar o navio na \n- Horizontal\n- Vertical\n").lower())

            print("""\nOBS: Caso sua escolha foi HORIZONTAL, escolha a COLUNA entre ou igual - 0 a 6 e LINHA de 0 a 9 -.
Caso foi VERTICAL, escolha a LINHA entre 0 a 6 e a COLUNA de 0 a 9.
SE A POSIÇÃO ESCOLHIDA FOR INCORRETA OU CRUZAR COM OUTRO NAVIO JÁ ADICIONADO, SERÁ SOLICITADO NOVAS POSIÇÕES!
""")
            
            pos_linha = int(input("Digite o numero da linha que deseja adicionar o navio: "))
            #Verificar(linha) caso haja posições fora da tabela
            while escolha == "horizontal" and pos_linha < 0 or pos_linha > 9:
                print("\nVocê digitou uma posição inválida!\nDigite uma posição correta.")
                pos_linha = int(input("Digite o numero da linha que deseja adicionar o navio: "))
            while escolha == "vertical" and pos_linha < 0 or pos_linha > 9:
                print("\nVocê digitou uma posição inválida!\nDigite uma posição correta.")
                pos_linha = int(input("Digite o numero da linha que deseja adicionar o navio: "))

            pos_coluna = int(input("Digite o numero da coluna que deseja adicionar o navio: "))
            #Verificar(coluna) caso haja posições fora da tabela
            while escolha == "horizontal" and pos_coluna < 0 or pos_coluna > 9:
                print("\nVocê digitou uma posição inválida!\nDigite uma posição correta.")
                pos_coluna = int(input("Digite o numero da coluna que deseja adicionar o navio: "))
            while escolha == "vertical" and pos_coluna < 0 or pos_coluna > 9:
                print("\nVocê digitou uma posição inválida!\nDigite uma posição correta.")
                pos_coluna = int(input("Digite o numero da coluna que deseja adicionar o navio: "))

            #Verificar se já há navio posicionado nesta posição
            if pode_adicionar_navio(lista_usuario, pos_linha, pos_coluna, tamanho_navioM, escolha):
                break
        
        #Adicionando navio ao tabuleiro
        if escolha == "horizontal":
            for i in range(tamanho_navioM):
                lista_usuario[pos_linha][pos_coluna + i] = "0"
        else:
            for i in range(tamanho_navioM):
                lista_usuario[pos_linha + i][pos_coluna] = "0"
navioM_usuario()

#Adicionando navios de tamanho pequeno na matriz do usuário
def navioP_usuario():
    for i in range(3):
        tamanho_navioP = 2
        while True:
            escolha = str(input(f"Digite se deseja posicionar o {i+1}° navio pequeno na \n- Horizontal\n- Vertical\n").lower())
            while escolha != "horizontal" and escolha != "vertical":
                print("\nVocê digitou errado!\nDigite novamente.\n")
                escolha = str(input("Digite se deseja posicionar o navio na \n- Horizontal\n- Vertical\n").lower())

            print("""\nOBS: Caso sua escolha foi HORIZONTAL, escolha a COLUNA entre ou igual - 0 a 6 e LINHA de 0 a 9 -.
Caso foi VERTICAL, escolha a LINHA entre 0 a 6 e a COLUNA de 0 a 9.
SE A POSIÇÃO ESCOLHIDA FOR INCORRETA OU CRUZAR COM OUTRO NAVIO JÁ ADICIONADO, SERÁ SOLICITADO NOVAS POSIÇÕES!
""")
            
            pos_linha = int(input("Digite o numero da linha que deseja adicionar o navio: "))
            #Verificar(linha) caso haja posições fora da tabela
            while escolha == "horizontal" and pos_linha < 0 or pos_linha > 9:
                print("\nVocê digitou uma posição inválida!\nDigite uma posição correta.")
                pos_linha = int(input("Digite o numero da linha que deseja adicionar o navio: "))
            while escolha == "vertical" and pos_linha < 0 or pos_linha > 9:
                print("\nVocê digitou uma posição inválida!\nDigite uma posição correta.")
                pos_linha = int(input("Digite o numero da linha que deseja adicionar o navio: "))

            pos_coluna = int(input("Digite o numero da coluna que deseja adicionar o navio: "))
            #Verificar(coluna) caso haja posições fora da tabela
            while escolha == "horizontal" and pos_coluna < 0 or pos_coluna > 9:
                print("\nVocê digitou uma posição inválida!\nDigite uma posição correta.")
                pos_coluna = int(input("Digite o numero da coluna que deseja adicionar o navio: "))
            while escolha == "vertical" and pos_coluna < 0 or pos_coluna > 9:
                print("\nVocê digitou uma posição inválida!\nDigite uma posição correta.")
                pos_coluna = int(input("Digite o numero da coluna que deseja adicionar o navio: "))

            #Verificar se pode adicionar o navio no tabuleiro
            if pode_adicionar_navio(lista_usuario, pos_linha, pos_coluna, tamanho_navioP, escolha):
                break
        
        #Adicionando navio ao tabuleiro
        if escolha == "horizontal":
            for i in range(tamanho_navioP):
                lista_usuario[pos_linha][pos_coluna + i] = "0"
        else:
            for i in range(tamanho_navioP):
                lista_usuario[pos_linha + i][pos_coluna] = "0"
navioP_usuario()
#Para facilitar a verificação dos navios do computador (para o tutor analisar)
print("\nTabuleiro do computador com as posições dos navios: ")
tabcomp()
print("\nSeu tabuleiro: ")
tab_usuario()
print()
print('\033[0;30;42mDetalhes do jogo:\033[m')
print("""
Os tiros são marcados por:
''*'' caso for derrubado a parte de um navio
''#'' caso for um tiro no mar.
OBS: o ''0'' é a parte de um navio no tabuleiro invisível.
""")
print('\033[0;30;41mComeçando o jogo!\033[m')

#Formulando os tiros
navios_computador = 16
navios_player = 16
while navios_computador != 0 and navios_player != 0:
    #Tiros do computador
    while True:
        # Os tiros são marcados por ''*'' caso for derrubado a parte
        # de um navio e ''#'' caso for um tiro no mar.
        # OBS: o ''0'' é a parte de um navio no tabuleiro invisível.
        tiro_linha = random.randint(0, 9)
        tiro_coluna = random.randint(0, 9)
        if lista_usuario[tiro_linha][tiro_coluna] == ".":
            lista_usuario[tiro_linha][tiro_coluna] = "#"
            print("\nO computador errou o tiro!")
            print(f"O computador ainda falta derrubar {navios_player} partes.")
            print("\nSeu tabuleiro: ")
            tab_usuario()
            print("\nTabuleiro do Computador: ")
            tabcomp_limitado()
            continuar = str(input("Aperte enter para continuar o jogo! "))
            break
        elif lista_usuario[tiro_linha][tiro_coluna] == "0":
            navios_player -= 1
            lista_usuario[tiro_linha][tiro_coluna] = "*"
            print("\nO computador acertou o tiro!\nO qual tem direito a outro tiro consecutivo.")
            print(navios_player, "partes de navios ainda podem ser derrubadas!")
            tab_usuario()
            continuar = str(input("Aperte enter para continuar o jogo! "))
            if navios_player == 0:
                print("Game Over!\nO computador ganhou o jogo.")
                break


    # Tiros do player
    if navios_player != 0:
        while True:
            # Os tiros são marcados por ''*'' caso for derrubado a parte
            # de um navio e ''#'' caso for um tiro no mar.
            # OBS: o ''0'' é a parte de um navio no tabuleiro invisível.
            print("Sua vez de atirar!")
            tiro_linha = int(input("Digite a posição da linha do tiro: "))
            while tiro_linha < 0 or tiro_linha > 9: #Verificar caso seja uma posição fora da tabela
                print("\nVocê digitou uma posição incorreta para a linha!\nPor favor, digite novamente.\n")
                tiro_linha = int(input("Digite a posição da linha do tiro: "))
            tiro_coluna = int(input("Digite a posição da coluna do tiro: "))
            while tiro_coluna < 0 or tiro_coluna > 9: #Verificar caso seja uma posição fora da tabela
                print("\nVocê digitou uma posição incorreta para a coluna!\nPor favor, digite novamente.\n")
                tiro_coluna = int(input("Digite a posição da coluna do tiro: "))

            if jogador1[tiro_linha][tiro_coluna] == ".":
                jogador1[tiro_linha][tiro_coluna] = "#"
                jogador1_limitado[tiro_linha][tiro_coluna] = "#"
                print("\nVocê errou o tiro!")
                print(f"Você ainda falta derrubar {navios_computador} partes para ganhar.")
                tabcomp_limitado()
                continuar = str(input("Aperte enter para continuar o jogo! "))
                break
            elif jogador1[tiro_linha][tiro_coluna] == "0":
                navios_computador -= 1
                jogador1[tiro_linha][tiro_coluna] = "*"
                jogador1_limitado[tiro_linha][tiro_coluna] = "*"
                print("\nVocê acertou o tiro!\nVocê tem direito a outro tiro consecutivo.")
                print(navios_computador, "partes de navios ainda podem ser derrubadas!")
                tabcomp_limitado()
                continuar = str(input("Aperte enter para continuar o jogo! "))
                if navios_computador == 0:
                    print("Parabéns, você ganhou!\nForam afundados todos os navios do oponente!")
                    break

# Autor: Ícaro de Souza Gonçalves
# Componente Curricular: EXA 854 - MI - Algoritmos
# Concluído em: 08/05/2023
# Declaro que este código foi elaborado por mim de forma individual e não contém nenhum trecho
# de código de outro colega ou de outro autor, tais como provindos de livros e apostilas, e páginas
# ou documentos eletrônicos da Internet. Qualquer trecho de código de outra autoria que não a
# minha está destacado com uma citação para o autor e a fonte do código, e estou ciente que estes
# trechos não serão considerados para fins de avaliação.
import pygame

pygame.init()

# Tela
tela_largura, tela_altura = 640, 640
tela = pygame.display.set_mode((tela_largura, tela_altura))
pygame.display.set_caption("Jogo de Xadrez")

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)

# Dimensões das casas
largura_casa = tela_largura // 8
altura_casa = tela_altura // 8

# Carregar peças
peao = pygame.image.load('peao.png')
cavalo = pygame.image.load('cavalo.png')
bispo = pygame.image.load('bispo.png')
rei = pygame.image.load('rei.png')
torre = pygame.image.load('torre.png')
rainha = pygame.image.load('rainha.png')

peao_branco = pygame.image.load('peao_branco.png')
cavalo_branco = pygame.image.load('cavalo_branco.png')
bispo_branco = pygame.image.load('bispo_branco.png')
torre_branco = pygame.image.load('torre_branco.png')
rainha_branco = pygame.image.load('rainha_branco.png')
rei_branco = pygame.image.load('rei_branco.png')

# Redimensionar peças
def redimensionar_pecas():
    return {
        'peao': pygame.transform.scale(peao, (largura_casa, altura_casa)),
        'cavalo': pygame.transform.scale(cavalo, (largura_casa, altura_casa)),
        'bispo': pygame.transform.scale(bispo, (largura_casa, altura_casa)),
        'rei': pygame.transform.scale(rei, (largura_casa, altura_casa)),
        'torre': pygame.transform.scale(torre, (largura_casa, altura_casa)),
        'rainha': pygame.transform.scale(rainha, (largura_casa, altura_casa)),
        'peao_branco': pygame.transform.scale(peao_branco, (largura_casa, altura_casa)),
        'cavalo_branco': pygame.transform.scale(cavalo_branco, (largura_casa, altura_casa)),
        'bispo_branco': pygame.transform.scale(bispo_branco, (largura_casa, altura_casa)),
        'rei_branco': pygame.transform.scale(rei_branco, (largura_casa, altura_casa)),
        'torre_branco': pygame.transform.scale(torre_branco, (largura_casa, altura_casa)),
        'rainha_branco': pygame.transform.scale(rainha_branco, (largura_casa, altura_casa)),
    }

pecas_redimensionadas = redimensionar_pecas()

# Desenhar o tabuleiro
def desenhar_tabuleiro():
    for linha in range(8):
        for coluna in range(8):
            cor = branco if (linha + coluna) % 2 == 0 else preto
            pygame.draw.rect(tela, cor, (coluna * largura_casa, linha * altura_casa, largura_casa, altura_casa))


# Desenhar as peças no tabuleiro
def desenhar_pecas():
    for linha in range(8):
        for coluna in range(8):
            peca = tabuleiro.tabuleiro[linha][coluna]
            if peca:
                # Seleciona a imagem da peça correta com base na cor
                nome_peca = type(peca).__name__.lower()
                if peca.cor == 'branco':
                    nome_peca += '_branco'
                tela.blit(pecas_redimensionadas[nome_peca], (coluna * largura_casa, linha * altura_casa))

def obter_posicao_do_mouse(pos):
    x, y = pos
    coluna = x // largura_casa
    linha = y // altura_casa
    return linha, coluna


#variavel que acompanha posicao da peca

peca_selecionada = None
posicao_inicial = None


#logica do jogo

class Peca:
    def __init__(self, cor, posicao):
        self.cor = cor #branca ou preta
        self.posicao = posicao #linha coluna
        

    def posicao_valida(self, tabuleiro, nova_coluna, nova_linha):
            #verifica se a jogada esta dentro do tabuleiro
            if (0 <= nova_linha <= 8 and 0 <= nova_coluna <=8):
                peca_destino = tabuleiro[nova_linha][nova_coluna] 

                #verifica se a casa de destino esta vazia ou tem peca adversaria / aliada
                if peca_destino is None or peca_destino.cor != self.cor:
                    return True
            return False
    
    def movimentos_validos(self, tabuleiro):
        '''deve ser implementado pelas subclasses'''
        raise NotImplementedError("metodo das subclasses")

    def __str__(self):
        return f"{self.__class__.__name__} {self.cor}"
    
    
#subclasses
  
class Rei(Peca):
    def movimentos_validos(self, tabuleiro):
        '''Movimentos válidos para o rei'''
        movimentos = []
        direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        # Extrair a posição atual da peça (linha_atual, coluna_atual)
        linha_atual, coluna_atual = self.posicao

        for direcao in direcoes:
            nova_linha = linha_atual + direcao[0]
            nova_coluna = coluna_atual + direcao[1]

            # Usar a função posicao_valida para verificar se o movimento é permitido
            if self.posicao_valida(tabuleiro, nova_coluna, nova_linha):
                movimentos.append((nova_linha, nova_coluna))
                
        return movimentos

class Rainha(Peca):
    def movimentos_validos(self, tabuleiro):
        movimentos = []
        return movimentos

class Peao(Peca):
    def movimentos_validos(self, tabuleiro):
        movimentos = []
        linha_atual, coluna_atual = self.posicao
        if self.cor == 'preto':
            #movimentos para frente
            if self.posicao_valida(tabuleiro, coluna_atual, linha_atual + 1):
                if tabuleiro[linha_atual + 1][coluna_atual] is None:
                    movimentos.append((linha_atual + 1, coluna_atual))

                    #movimento inicial - move 2 casas
                    if linha_atual == 1 and tabuleiro[linha_atual - 2][coluna_atual] is None:
                        movimentos.append((linha_atual + 2), coluna_atual)
            
            #captura na diagonal
            for d in [-1, 1]:
                nova_linha = linha_atual + 1
                nova_coluna = coluna_atual + d 

                if self.posicao_valida(tabuleiro, nova_coluna, nova_linha):
                    if tabuleiro[nova_linha][nova_coluna] is not None and tabuleiro[nova_linha][nova_coluna].cor != self.cor:
                        movimentos.append((nova_linha, nova_coluna))

            for d in [-1, 1]:
                nova_linha = linha_atual - 1 #peoes branco para cima(frente)
                nova_coluna = coluna_atual + d
                if self.posicao_valida(tabuleiro, nova_coluna, nova_linha):
                    if tabuleiro[nova_linha][nova_coluna] is not None and tabuleiro[nova_linha][nova_coluna].cor != self.cor:
                        movimentos.append((nova_linha, nova_coluna))

        return movimentos 

class Bispo(Peca):
    def movimentos_validos(self, tabuleiro):
        movimentos = []
        return movimentos

class Torre(Peca):
    def movimentos_validos(self, tabuleiro):
        movimentos = []
        return movimentos

class Cavalo(Peca):
    def movimentos_validos(self, tabuleiro):
        movimentos = []
        return movimentos

class Tabuleiro:
    def __init__(self):
        # Inicializar tabuleiro 8x8 com None
        self.tabuleiro = [[None for _ in range(8)] for _ in range(8)]
        self.inicializar_tabuleiro()

    def inicializar_tabuleiro(self):
        # Peças pretas
        self.tabuleiro[0] = [
            Torre('preto', (0, 0)), Cavalo('preto', (0, 1)), Bispo('preto', (0, 2)),
            Rainha('preto', (0, 3)), Rei('preto', (0, 4)), Bispo('preto', (0, 5)),
            Cavalo('preto', (0, 6)), Torre('preto', (0, 7))
        ]
        self.tabuleiro[1] = [Peao('preto', (1, col)) for col in range(8)]

        # Peças brancas
        self.tabuleiro[6] = [Peao('branco', (6, col)) for col in range(8)]
        self.tabuleiro[7] = [
            Torre('branco', (7, 0)), Cavalo('branco', (7, 1)), Bispo('branco', (7, 2)),
            Rainha('branco', (7, 3)), Rei('branco', (7, 4)), Bispo('branco', (7, 5)),
            Cavalo('branco', (7, 6)), Torre('branco', (7, 7))
        ]

    def mostrar_tabuleiro(self):
        for linha in self.tabuleiro:
            print([str(peca) if peca else '.' for peca in linha])


tabuleiro = Tabuleiro()
peca_selecionada = True
posicao_inicial = True


# Loop do jogo
executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
    
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            #capturar o clique do mouse e seleciona a peca
            pos = pygame.mouse.get_pos()
            linha, coluna = obter_posicao_do_mouse(pos)
            peca = tabuleiro.tabuleiro[linha][coluna]
            if peca:
                peca_selecionada = peca
                posicao_inicial = (linha, coluna)

                #verifica se a peca é um rei
                if isinstance(peca, Rei):
                    print('é o rei')

                if isinstance(peca, Peao):
                    print('é peao')
        
        elif evento.type == pygame.MOUSEBUTTONUP and peca_selecionada:
            #soltar a peca e mover para a nova posicao
            pos = pygame.mouse.get_pos()
            nova_linha, nova_coluna = obter_posicao_do_mouse(pos)

            #verificar se o movimento é valido
            movimentos_validos = peca_selecionada.movimentos_validos(tabuleiro.tabuleiro)
            if (nova_linha, nova_coluna) in movimentos_validos:
                #move nova posicao
                tabuleiro.tabuleiro[nova_linha][nova_coluna] = peca_selecionada
                tabuleiro.tabuleiro[posicao_inicial[0]][posicao_inicial[1]] = None
            #limpar a peca selecionada
            peca_selecionada = None 

    desenhar_tabuleiro()
    desenhar_pecas()
    
    # Atualizar a tela
    pygame.display.flip()

pygame.quit()


# Classe carro
ESQUERDA = 0
DIREITA = 1
FRENTE = 2
RE = 3
VERTICAL = 0
HORIZONTAL = 1

class Carro():
    def __init__(self, direção, sentido, velocidade):  # função construtora
        self.caminho = None
        self.velocidade = 0 #self é igual a this, em java
        self.direção = VERTICAL #0 - vertical, 1 - horizontal
        self.sentido = FRENTE #0 - esquerda, 1 - direita
        #print("Meu carrão está sendo rebocado.")

    def acelerar(self):
        self.velocidade += 10

    def freiar(self):
        self.velocidade = 0

    def virar_esquerda(self):
        self.sentido = ESQUERDA

    def virar_direita(self):
        self.sentido = DIREITA

    def re(self):
        self.sentido = RE

    def frente(self):
        self.sentido = FRENTE

    def carregar_imagem(self, caminho):
        return self.caminho
     
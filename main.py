from pickle import TRUE
from turtle import width
import pygame #Importanto a biblioteca de jogos do python. É necessário inatala-la. Para isso vai até prompt de comando e digite "pip install pygame"

#Definindo o tamanho da tela do jogo
width = 1200
height = 600

#Importando a classe do player no jogo
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #Toda vez que for criar uma classe tem que ter esses parâmetros, a única coisa que vai mudar é o nome da classe, no caso "Player"
        self.image = pygame.image.load ('imagens/Run_000.png') #Utilizando a imagem do personagem salva dentro das pasta do programa
        self.rect = pygame.Rect(100,100,100,100) #Definindo um box retangular para imagem e também o tamanho

    def  update(self, *args): #Sempre dentro da classe, teremos que ter o métodos update
        #self.image = pygame.transform.scale(self.imagem,[100,100])
        pass

#Inicializando o pygame
pygame.init ()

#Criando a janela do Pygame
game_windon = pygame.display.set_mode([width, height]) #Definindo o tamanho da janela do jogo

pygame.display.set_caption ('Infinity Game') #Escrevendo no título da janela o nome do jogo

#Toda vez que eu crio uma classe, eu tenho que criar um grupo para essa classe
playerGroup = pygame.sprite.Group()
player = Player()

#Todo jogo deve ter um game loop definido. Criando um game loop
gameloop = True

#Vamos criar uma função para desenharmos na tela
def draw ():
    game_windon.fill ([255,255,0]) #Fill é preencher, ou seja preencher a janela do jogo. Os número que estão ali são o código da cor em rgb

while gameloop: #Enquanto o game loop for true ele vai ficar rodando
 
    for event in pygame.event.get(): #Para poder fechar, adicionar comandos dentro da janela, preciso criar um "for event", para pegar os eventos dentro do pygame.

        if event.type == pygame.QUIT: #Se o evento for igual ao evento de SAIR
            pygame.QUIT()
            break
    
    draw() #Chamando a função criada para preencher a janela 

    pygame.display.update() #A janela vai ficar atualizando cada frame
    
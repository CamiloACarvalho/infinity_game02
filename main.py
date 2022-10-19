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

        #Mas o bonequinho não vai ficar parado, ele vai correr, logo, preciso criar uma animção pra ele. E pra isso, criarei uma lista
        self.image_run = [pygame.image.load ('imagens\Run__000.png'),
                          pygame.image.load ('imagens\Run__001.png'),
                          pygame.image.load ('imagens\Run__002.png'),
                          pygame.image.load ('imagens\Run__003.png'),
                          pygame.image.load ('imagens\Run__004.png'),
                          pygame.image.load ('imagens\Run__005.png'),
                          pygame.image.load ('imagens\Run__006.png'),
                          pygame.image.load ('imagens\Run__007.png'),
                          pygame.image.load ('imagens\Run__008.png'),
                          pygame.image.load ('imagens\Run__009.png')]
                                            
        self.image = pygame.image.load ('imagens\Run__000.png') #Utilizando a imagem do personagem salva dentro das pasta do programa

        self.rect = pygame.Rect(100,100,100,100) #Definindo um box retangular para imagem e também o tamanho

        self.current_image = 0

    def  update (self, *args): #Sempre dentro da classe, teremos que ter o métodos update

        def move_player(self): #Função criada para movimentar o personagem do jogo. Lembrando que tem que colocar o 'self' porque está dentro da classe

            self.current_image = (self.current_image + 1) % 10 #Isso fará com que rode toda a lista de imagem. E terá que ter um loop infinito gerando assim o movimento do personagem. 0 "mais um e resto da divisão por 10" porque tenho 10 imagens
            
            self.image = self.image_run [self.current_image] #

            self.image = pygame.transform.scale(self.image,[100,100])
        move_player (self)

#Inicializando o pygame
pygame.init ()

#Criando a janela do Pygame
game_window = pygame.display.set_mode([width, height]) #Definindo o tamanho da janela do jogo

pygame.display.set_caption ('Infinity Game') #Escrevendo no título da janela o nome do jogo

#Criando o background, ou seja, o fundo do jogo!
BACKGROUND = pygame.image.load('imagens/background_03.jpg') #Carregando a imagem de fundo do jogo
BACKGROUND = pygame.transform.scale(BACKGROUND, [width, height]) #Ajustando o tamanho da imagem à tela do jogo

#Toda vez que eu crio uma classe, eu tenho que criar um grupo para essa classe
playerGroup = pygame.sprite.Group()
player = Player() #Criei um objeto player para receber a classe player
playerGroup.add(player) #Agora eu adiciei o objeto player dentro do gurpo player

#Todo jogo deve ter um game loop definido. Criando um game loop
gameloop = True

#Vamos criar uma função para desenharmos na tela
def draw ():
    #game_windon.fill ([255,255,0]) #Fill é preencher, ou seja preencher a janela do jogo. Os número que estão ali são o código da cor em rgb
    playerGroup.draw(game_window) #PEu tenho que passar a janela do jogo "game_window" no draw para desenhar na tela

#Essa função vai atualizar a tela a todo o momento com a classe player criada
def update():
    playerGroup.update() #A função update vai chamar a classe player group

while gameloop: #Enquanto o game loop for true ele vai ficar rodando

    game_window.blit(BACKGROUND, (0, 0)) #Coloquei a imagem de fundo atrás de tudo, realmente para ser fundo do jogo
 
    for event in pygame.event.get(): #Para poder fechar, adicionar comandos dentro da janela, preciso criar um "for event", para pegar os eventos dentro do pygame.

        if event.type == pygame.QUIT: #Se o evento for igual ao evento de SAIR
            pygame.QUIT()
            break
    
    update()

    draw() #Chamando a função criada para preencher a janela 

    pygame.display.update() #A janela vai ficar atualizando cada frame
    
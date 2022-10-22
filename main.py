from cmath import rect
from math import fabs
from pickle import TRUE
from turtle import speed, width
import pygame #Importanto a biblioteca de jogos do python. É necessário inatala-la. Para isso vai até prompt de comando e digite "pip install pygame"

#Definindo o tamanho da tela do jogo
width = 1200
height = 600

#Definindo o tamanho do chão do jogo na tela do game
GROUND_WIDTH = 2*width
GROUND_HEIGTH = 30

#Definindo variável para movimentar o personagem
SPEED = 10
GAME_SPEED = 10

#Importando a classe do player no jogo
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #Toda vez que for criar uma classe tem que ter esses parâmetros, a única coisa que vai mudar é o nome da classe, no caso "Player"

        #Mas o bonequinho não vai ficar parado, ele vai correr, logo, preciso criar uma animção pra ele. E pra isso, criarei uma lista
        #O convert_alpha() serve para excluir, limpar os pixels da imagem que não estão sendo usados
        self.image_run = [pygame.image.load ('sprites\Run__000.png').convert_alpha(),
                          pygame.image.load ('sprites\Run__001.png').convert_alpha(),
                          pygame.image.load ('sprites\Run__002.png').convert_alpha(),
                          pygame.image.load ('sprites\Run__003.png').convert_alpha(),
                          pygame.image.load ('sprites\Run__004.png').convert_alpha(),
                          pygame.image.load ('sprites\Run__005.png').convert_alpha(),
                          pygame.image.load ('sprites\Run__006.png').convert_alpha(),
                          pygame.image.load ('sprites\Run__007.png').convert_alpha(),
                          pygame.image.load ('sprites\Run__008.png').convert_alpha(),
                          pygame.image.load ('sprites\Run__009.png').convert_alpha()]

        self.image_fall = pygame.image.load ('sprites\Fall.png').convert_alpha() #Criando uma variável para a queda do personagem
                                            
        self.image = pygame.image.load ('sprites\Run__000.png').convert_alpha() #Utilizando a imagem do personagem salva dentro das pasta do programa

        self.rect = pygame.Rect(100,100,100,100) #Definindo um box retangular para imagem e também o tamanho

        self.current_image = 0

    def  update (self, *args): #Sempre dentro da classe, teremos que ter o métodos update

        def move_player(self): #Função criada para movimentar o personagem do jogo. Lembrando que tem que colocar o 'self' porque está dentro da classe

            #Nessa parte, vou fazer o personagem movimentar na tela
            key = pygame.key.get_pressed() #Essa parte é pra "captar" alguma tecla pressionada

            if key[pygame.K_RIGHT]: #Movimentar o personagem pra frente
                self.rect[0] += GAME_SPEED
            
            if key[pygame.K_LEFT]: #Movimentar o personagem pra trás
                self.rect[0] -= GAME_SPEED

            self.current_image = (self.current_image + 1) % 10 #Isso fará com que rode toda a lista de imagem. E terá que ter um loop infinito gerando assim o movimento do personagem. 0 "mais um e resto da divisão por 10" porque tenho 10 imagens
            
            self.image = self.image_run [self.current_image] #

            self.image = pygame.transform.scale(self.image,[100,100])
        move_player (self)

        self.rect[1] += SPEED #Adicionando gravidade no jogo

        def fly (self): #Para o personagem do jogo pular
            
            key = pygame.key.get_pressed() #para reconhecer o a tecla apertada

            if key[pygame.K_UP]: #Para o personagem pular

                self.rect[1] -= 30 #Velocidade com que o personagem vai pular
                self.image = pygame.image.load('sprites/Fly.png').convert_alpha #Troca a imagem do personagem para "pulo"   
                self.image = pygame.transform.scale(self.image, [100, 100])  
        fly(self)

        def fall (self): #Para o personagem do jogo cair depois de pular
            
            key = pygame.key.get_pressed() #para reconhecer o a tecla apertada

            if not pygame.sprite.groupcollide(playerGroup,groundGroup, False,False) and not key[pygame.K_UP]: #Se não tiver colisão com o chão e tbm não tiver apertando tecla up para pular, ele não vai mudar a imagem

                self.image = self.image_fall #Troca a imagem do personagem para "queda"   
                self.image = pygame.transform.scale(self.image, [100, 100])  
        fall(self)


#Definindo o chão do jogo
class Ground(pygame.sprite.Sprite):

    def __init__(self, xpos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('sprites/ground.png').convert_alpha() #Selecionando a imagem
        self.image = pygame.transform.scale(self.image,(GROUND_WIDTH, GROUND_HEIGTH)) #Definindo o tamanho do chão do jogo
        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.rect[1] = height - GROUND_HEIGTH #Vai pegar o tamanho todo da tela e subtrair o tamanho do chão

    def update(self, *args):
        self.rect[0] -= GAME_SPEED

#Essa função é para ver se o objeto está fora da tela
def is_of_screen(sprite):
    return sprite.rect[0] < -(sprite.rect[2])

#Inicializando o pygame
pygame.init ()

#Criando a janela do Pygame
game_window = pygame.display.set_mode([width, height]) #Definindo o tamanho da janela do jogo

pygame.display.set_caption ('Infinity Game') #Escrevendo no título da janela o nome do jogo

#Criando o background, ou seja, o fundo do jogo!
BACKGROUND = pygame.image.load('sprites/background_03.jpg').convert_alpha() #Carregando a imagem de fundo do jogo
BACKGROUND = pygame.transform.scale(BACKGROUND, [width, height]) #Ajustando o tamanho da imagem à tela do jogo

#Toda vez que eu crio uma classe, eu tenho que criar um grupo para essa classe
playerGroup = pygame.sprite.Group()
player = Player() #Criei um objeto player para receber a classe player
playerGroup.add(player) #Agora eu adiciei o objeto player dentro do gurpo player

#Criando o grupo para o chão do jogo
groundGroup = pygame.sprite.Group()

for i in range(2): #Para o chão ficar "correndo" e infinito, não acabar. Para isso, vamos "destruir" e "criar" um chão novo, para não ficar um jogo muito pesado

    ground = Ground(width*i)
    groundGroup.add(ground)

#Todo jogo deve ter um game loop definido. Criando um game loop
gameloop = True

#Vamos criar uma função para desenharmos na tela
def draw ():
    #game_windon.fill ([255,255,0]) #Fill é preencher, ou seja preencher a janela do jogo. Os número que estão ali são o código da cor em rgb
    playerGroup.draw(game_window) #Eu tenho que passar a janela do jogo "game_window" no draw para desenhar na tela
    groundGroup.draw(game_window)#Eu tenho que passar a janela do jogo "game_window" no draw para desenhar na tela

#Essa função vai atualizar a tela a todo o momento com a classe player criada
def update():
    playerGroup.update() #A função update vai chamar a classe player group
    groundGroup.update() #A função update vai chamar a classe player group

clock = pygame.time.Clock() #Criamos essa variável para ajustar a corrida do personagem, pq ele esta correndo muito rápido

while gameloop: #Enquanto o game loop for true ele vai ficar rodando

    clock.tick(30) #Aqui é o ajusta da velocidade dos passos do personagem (fps)

    game_window.blit(BACKGROUND, (0, 0)) #Coloquei a imagem de fundo atrás de tudo, realmente para ser fundo do jogo
 
    for event in pygame.event.get(): #Para poder fechar, adicionar comandos dentro da janela, preciso criar um "for event", para pegar os eventos dentro do pygame.

        if event.type == pygame.QUIT: #Se o evento for igual ao evento de SAIR
            pygame.QUIT()
            break
    
    if is_of_screen (groundGroup.sprites()[0]): 
        groundGroup.remove(groundGroup.sprites()[0]) #Isso quer dizer, que se esse objeto estiver fora da tela, ele será removido
        newGround = ground(width -20) #Nova varíavel para criar um novo chão após ter sido removido. O -20 é pra não dar espaço entre chãos, porque queremos um chão contínuo
        groundGroup.add(newGround) #Aqui estamos adicionando o novo chão
    
    if pygame.sprite.groupcollide(playerGroup, groundGroup, False, False): #Criando parâmetro para colidir com o chão
        SPEED = 0
    else:
        SPEED = 10 #Velocidade com que o personagem vai cair.

    update()

    draw() #Chamando a função criada para preencher a janela 

    pygame.display.update() #A janela vai ficar atualizando cada frame
    
from time import sleep
import pygame
import random
pygame.init()

# taille de la fenetre
width = 800
height = 600
# création de la fenetre
screen = pygame.display.set_mode((width, height))
pygame.display.set_icon(pygame.image.load('pong_icon.png'))
font = pygame.image.load("pong_bg.png").convert()
# nom de la fenetre
pygame.display.set_caption('Pong')

# initialisation du joueur
player_img = pygame.image.load('pong_bar.png')
player_X = 25
player_Y = height/2 - 50

# initialisation du bot
bot_img = pygame.image.load('pong_bar.png')
bot_X = width - 50
bot_Y = height/2 - 50

# initialisation de la balle
ball_img = pygame.image.load('pong_ball.png')
ball_X = width/2 + 25
ball_Y = height/2
ball_direction_X = -1
ball_direction_Y = 1

# afficher le score
score1 = 0
score2 = 0
score1_display = 0
score2_display = 0
white = (255, 255, 255)
sysFont = pygame.font.SysFont("None", 32)


def player():
    # affichage du joueur
    screen.blit(player_img, (player_X, player_Y))


def bot():
    # affichage du bot
    screen.blit(bot_img, (bot_X, bot_Y))


def bot_mouv():
    # mouvement du bot
    global bot_Y
    bot_Y += ball_direction_Y + random.randint(0, 2) - random.randint(0, 2)
    if bot_Y < 50:
        bot_Y += 1
    if bot_Y > 450:
        bot_Y -= 1


def ball():
    # afficher l'image de la balle
    screen.blit(pygame.image.load("pong_ball.png").convert(), (ball_X, ball_Y))


def ball_mouv():
    # mouvement de la balle
    global ball_Y
    global ball_X
    global ball_direction_Y
    global ball_direction_X
    global score1
    global score2

    # si la balle touche le plafond ou le sol, elle va dans le sans inverse
    # touche le plafond
    if ball_Y == 0:
        ball_direction_Y *= -1
    # touche le sol
    elif ball_Y == height-50:
        ball_direction_Y *= -1

    # si la balle touche une barre (player ou bot) la balle ira dans le sans inverse
    # toucher par le joueur
    if ball_X <= 50 and ball_Y + 50 >= player_Y and ball_Y <= player_Y + 100:
        ball_direction_X *= -1
    # toucher par le bot
    if ball_X + 50 >= bot_X and ball_Y + 50 >= bot_Y and ball_Y <= bot_Y + 100:
        ball_direction_X *= -1

    # si le bot gagne
    if ball_X == 0:
        global running

        # remet la balle au point initial
        ball_X = width/2 + 25
        ball_Y = height/2
        ball_direction_X = -1
        ball_direction_Y = 1

        # ajout d'un point pour le bot
        score2 += 1

    # si le joueur gagne
    if ball_X == 750:
        global running

        # remet la balle au point initial
        ball_X = width/2 + 25
        ball_Y = height/2
        ball_direction_X = -1
        ball_direction_Y = 1

        # ajout d'un point pour le joueur
        score1 += 1

    # mouvement du bot
    ball_X += ball_direction_X
    ball_Y += ball_direction_Y


def score():
    global score1
    global score2
    global score1_display
    global score2_display

    score_label = sysFont.render("SCORE", 0, (255, 255, 255))
    screen.blit(score_label, (width/4 - 34, 25))
    screen.blit(score_label, (width/4*3 - 34, 25))

    score1_display = sysFont.render(str(score1), 0, (255, 255, 255))
    screen.blit(score1_display, (width/4, 50))
    score2_display = sysFont.render(str(score2), 0, (255, 255, 255))
    screen.blit(score2_display, (width/4*3, 50))


running = True

y = 100
x = 50

clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if score1 > score2:
                print("Le joueur a gagner")
            if score1 < score2:
                print("Le bot a gagner")
            if score1 == score2:
                print("Egalité")
            running = False

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_ESCAPE]:
        running = False

    if pressed[pygame.K_UP]:
        player_Y -= 1
        if player_Y == 50:
            player_Y += 1

    if pressed[pygame.K_DOWN]:
        player_Y += 1
        if player_Y == 450:
            player_Y -= 1

    screen.blit(font, (0, 0))
    player()
    bot_mouv()
    bot()
    ball_mouv()
    ball()
    score()
    pygame.display.flip()
    # fps
    clock.tick(480)


pygame.quit()

import pygame
import random
pygame.init()

# initialisation de la fenetre
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
# icon en haut a gauche
pygame.display.set_icon(pygame.image.load('pandu_icon.png'))
# nom de la fenetre
pygame.display.set_caption('Jeu du pandu')
# initialisation de l'alphabet
sysFont = pygame.font.SysFont("None", 75)
# initialisation des couleur
white = (255, 255, 255)
red = (255, 0, 0)
dark = (0, 0, 0)
# librairy de tout les mots du jeu
library = ["angle", "armoire", "bureau", "cabinet", "carreau", "chaise", "classe", "couloir", "dossier", "ecole", "ecriture", "escalier", "etagere", "etude", "exterieur", "fenetre", "interieur", "lavabo", "lecture", "marche", "matelas", "meuble", "mousse", "peluche", "placard",
           "plafond", "porte", "poubelle", "radiateur", "rampe", "rideau", "robinet", "salle", "savon", "serrure", "serviette", "siege", "sieste", "silence", "sommeil", "sonnette", "sortie", "table", "tableau", "tabouret", "tapis", "tiroir", "toilette", "vitre"]

# initialisation du mot et du mot caché
guess_word = library[random.randint(0, 51)]
guess_word_split = list(guess_word)
# taille du mot
hide_word = []
for i in range(len(guess_word)):
    hide_word += "_"

# lettre deja utiliser
use_leter = []
# input des lettres par defaut
pressed = "_"
# nombre de fois que le joueur va se tromper
fail = 0
# pour voir si le joueur a gagner ou perdu
win = ""


def leters():
    alphabets = ""
    y = 25
    x = 200
    # toute les lettre minuscule unicode
    for i in range(97, 123):
        # retour a la ligne
        if i == 110:
            x -= 100
            y -= 50*13
        # mettre le unicode en langue française
        alphabets = chr(i)
        alphabets_display = sysFont.render(str(alphabets), 0, white)
        # si la lettre une ancienne lettre a été presser, les mettre en rouge pour les différencier des non presser
        for i in range(len(use_leter)):
            if alphabets == use_leter[i]:
                # rouge si la lettre a été utiliser
                alphabets_display = sysFont.render(str(alphabets), 0, red)
                break
            else:
                # blanc si la lettre n'a pas encore été utliser
                alphabets_display = sysFont.render(str(alphabets), 0, white)
        # afficher a interval régulier
        y += 50
        screen.blit(alphabets_display, (y, height - x))


def player_input():
    global pressed
    global use_leter
    global fail
    save_leter = True
    # si une touche est presser
    if event.type == pygame.KEYUP:
        # si la touche est une lettre
        if 97 <= event.key <= 123:
            pressed = chr(event.key)
            # verifi si la lettre n'a pas déja été presser
            for i in range(len(use_leter)):
                if pressed == use_leter[i]:
                    save_leter = False
                    pass
            # enregistrer dans save_leter si la touche n'a pas encore été presser
            if save_leter == True:
                use_leter += chr(event.key)
                lens_word = 0
                for i in range(len(guess_word)):
                    if pressed == guess_word_split[i]:
                        lens_word = 0
                        break
                    else:
                        lens_word += 1
                        if lens_word == len(guess_word):
                            fail += 1
        else:
            # si la touche n'est pas une lettre, mettre "_"
            pressed = "_"
    # afficher le rendu
    pressed1 = sysFont.render(pressed, 0, white)
    screen.blit(pressed1, (150, 100))


def word():
    global hide_word
    global use_leter
    global fail
    global running
    global win
    lens = 0
    # verifi si la lettre presser fait parti du mot
    if pressed:
        for i in range(len(guess_word)):
            if pressed == guess_word_split[i]:
                # remplacer le "_" par la lettre presser
                hide_word[i] = guess_word_split[i]
    # affichage du mots caché
    for i in range(len(guess_word)):
        lens += 50
        hide_caractere = sysFont.render(hide_word[i], 0, white)
        screen.blit(hide_caractere, (lens, 275))
    # verifi si le mots est trouver en entier
    if hide_word == guess_word_split:
        win = "win"
        print(win)


def hang_stickman():
    global fail
    global running
    global win
    # création du pandu en fonction du nombre d'erreur
    if fail >= 1:
        pygame.draw.line(screen, white, (700, 300), (750, 300), 5)
    if fail >= 2:
        pygame.draw.line(screen, white, (725, 300), (725, 100), 5)
    if fail >= 3:
        pygame.draw.line(screen, white, (725, 100), (625, 100), 5)
    if fail >= 4:
        pygame.draw.line(screen, white, (625, 100), (625, 125), 5)
    if fail >= 5:
        pygame.draw.circle(screen, white, (625, 125+25), 25, 5)
    if fail >= 6:
        pygame.draw.line(screen, white, (625, 175), (625, 225), 5)
    if fail >= 7:
        pygame.draw.line(screen, white, (625, 185), (650, 225), 5)
    if fail >= 8:
        pygame.draw.line(screen, white, (625, 185), (600, 225), 5)
    if fail >= 9:
        pygame.draw.line(screen, white, (625, 225), (650, 265), 5)
    if fail >= 10:
        pygame.draw.line(screen, white, (625, 225), (600, 265), 5)
        win = "lose"
        print(win)
        running = False


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # quand on gagne, le jeu s'arrete
        if win != "win":
            screen.fill((0, 0, 51))
            player_input()
            leters()
            word()
            hang_stickman()
            pygame.display.flip()
        else:
            running = False
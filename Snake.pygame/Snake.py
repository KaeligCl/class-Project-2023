import random
import pygame
pygame.init()


# initialisation de la fenetre
width = 600
height = 640
screen = pygame.display.set_mode((width, height))
# centre de la fenetre
semi_height = height/2
semi_width = width/2
# icon en haut a gauche
pygame.display.set_icon(pygame.image.load(
    'D:\Programmation\Dossier Thonny\Snake.pygame\image\snake_icon.png'))
# nom de la fenetre
pygame.display.set_caption('Snake')
# image du fruit
apple_img = pygame.image.load(
    'D:\Programmation\Dossier Thonny\Snake.pygame\image/apple.png')
apple_img = pygame.transform.scale(apple_img, (20, 20))
# image des trophés
BestScore_img = pygame.image.load(
    'D:\Programmation\Dossier Thonny\Snake.pygame\image/BestScore.png')
BestScore_img = pygame.transform.scale(BestScore_img, (50, 50))
CurrentScore_img = pygame.image.load(
    'D:\Programmation\Dossier Thonny\Snake.pygame\image/CurrentScore.png')
CurrentScore_img = pygame.transform.scale(CurrentScore_img, (50, 50))
# initialisation de l'affichage du texte
sysFont = pygame.font.SysFont("None", 50)
# initialisation des couleur
white = (255, 255, 255)
bk_green = (0, 204, 0)
snake_green = (0, 102, 0)
score_screen_color = (0, 153, 0)


# déssiner tout le corps du serpent
def sneak_body():
    # dessiner la téte
    pygame.draw.rect(screen, snake_green,
                     pygame.Rect(snake_position[0], snake_position[1], 20, 20))
    # dessiner le reste du corps
    for pos in snake_body:
        pygame.draw.rect(screen, snake_green,
                         pygame.Rect(pos[0] + 2, pos[1] + 2, 15, 15))


def snake_direction():
    global direction
    # direction du serpent
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT]:
        if direction != "Left":
            direction = "Right"
    if pressed[pygame.K_LEFT]:
        if direction != "Right":
            direction = "Left"
    if pressed[pygame.K_DOWN]:
        if direction != "Up":
            direction = "Down"
    if pressed[pygame.K_UP]:
        if direction != "Down":
            direction = "Up"


def sneak_move():
    global apple, current_score
    # mouvement du serpent
    if direction == "Right":
        snake_position[0] += 20
    if direction == "Left":
        snake_position[0] -= 20
    if direction == "Down":
        snake_position[1] += 20
    if direction == "Up":
        snake_position[1] -= 20

    # ajoute une tête au cordonné de snake_move()
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == appleXY[0] and snake_position[1] == appleXY[1]:
        apple = False
        current_score += 1
    else:
        # supprime le dernier bout du serpent si un fruit n'est pas manger
        snake_body.pop()


def fruit():
    global apple, appleXY
    # affiche la pomme
    screen.blit(apple_img, (appleXY[0], appleXY[1]))
    # si la pomme n'est pas là, mettre des coordonée aléatoire dans le cadre de jeu
    if apple == False:
        x = random.randint(0, (width - 20)/20)*20
        y = random.randint(140/20, (height - 20)/20)*20

        # Tant que la pomme n'est toujours pas apparu
        while apple == False:
            num = 0
            # verifier si la pomme spawn sur le corps du serpent et donc recrée d'autre coordoné
            for pos in snake_body:
                if x == pos[0] and y == pos[1]:
                    x = random.randint(0, (width - 20)/20)*20
                    y = random.randint(140/20, (height - 20)/20)*20
                else:
                    # compté toute les fois que la pomme n'apparé pas dans le corps du serpent
                    num += 1
            # si la pomme n'apparait dans aucune partie du serpent, afficher la pomme au coordoné déja calculer
            if num == len(snake_body):
                appleXY = [x, y]
                apple = True


def game_over():
    global game
    # verifie si le serpent sort du cadre de jeu
    if snake_position[0] < 0 or snake_position[0] == width:
        game = "Over"
    if snake_position[1] < 140 or snake_position[1] == height:
        game = "Over"

    # verifie si le serpent entre en colision avec son corps (lis chaque coordonée du corps excépté la téte)
    x = 0
    for pos in snake_body:
        x += 1
        if snake_position[0] == pos[0] and snake_position[1] == pos[1] and x > 1:
            game = "Over"


def score_screen():
    # afficher le bandeau des score en haut du cadre
    pygame.draw.rect(screen, score_screen_color,
                     pygame.Rect(0, 0, 600, 140))


def score():
    global best_score, current_score
    # affichage de l'image du meilleur score
    screen.blit(BestScore_img, (width/5 - 60, 50))
    pygame.draw.rect(screen, snake_green,
                     pygame.Rect(width/5, 50, 100, 50))

    # affichage du meilleur score
    best_score_print = sysFont.render(str(best_score), 0, white)
    screen.blit(best_score_print, (width/5 + 30, 60))

    # remplacer le meilleur si le score actuel est plus grand
    if current_score > best_score:
        best_score = current_score
        with open('Best Score.txt', "w") as file:
            file.writelines(["\nBest Score:", "\n", str(current_score)])

    # affichage de l'image du score actuel
    screen.blit(CurrentScore_img, (width/5*3, 50))
    pygame.draw.rect(screen, snake_green,
                     pygame.Rect(width/5*3 + 60, 50, 100, 50))

    # affichage du score actuel sur cette partie
    current_score_print = sysFont.render(str(current_score), 0, white)
    screen.blit(current_score_print, (width/5*3 + 110, 60))


# position de la tête du serpent
snake_position = [semi_width, semi_height]

# position de tout le corps du serpent (y compris la tête qui se trouve à l'emplacement: snake_body[0])
snake_body = [[semi_width, semi_height], [semi_height - 20, semi_height],
              [semi_height - 40, semi_height], [semi_height - 60, semi_height]]

# coordonée aléatoire du fruit
appleXY = [random.randint(0, width), random.randint(0, height)]
apple = False

# direction de départ du jeu
direction = "Right"
game = ""

# prendre la donné 'meilleur score' sur le fichier 'Best Score.txt'
file = open('D:\Programmation\Dossier Thonny\Snake.pygame\Best Score.txt', 'r')
for line in file:
    Bestscore = line
file.close()
best_score = int(Bestscore)
# score actuel
current_score = 0

# initialisation des fps
fps = pygame.time.Clock()

# boucle de jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if game == "Over":
        running = False

    screen.fill(bk_green)

    snake_direction()
    sneak_move()
    sneak_body()

    game_over()

    fruit()
    score_screen()
    score()

    pygame.display.flip()
    # fps
    fps.tick(5)

pygame.quit()

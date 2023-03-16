import pygame
pygame.init()   #start/initialise pygame

screen = pygame.display.set_mode([600,600]) #Setup the static screen of the game
pygame.display.set_caption('Pong by Teun Jansen')
#global variables:
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
orange = (255, 165, 0)

background = blue
framerate = 60

circle_x = 300 #Ball starting coordinates
circle_y = 300 #Ball starting coordinates
circle_x_direction = 4 #Determine speed of the ball
circle_y_direction = 5 #Determine speed of the ball

#Determine player variables:
player_width = 30
player_height = 50
player_x = 300
player_y = 500
player_x_direction = 0
player_y_direction = 0
player_speed = 3

#HighScores and Fonts:
font = pygame.font.Font('freesansbold.ttf', 20)
game_over_font = pygame.font.Font('freesansbold.ttf', 60)
score = 0
previous_score = 0
high_score = 0

#Import a timer to use to control the framerate:
timer = pygame.time.Clock()

# Set initial game-status:
gameover = False


#Increase the difficulty of the game:
def check_difficulty():
    global score
    global circle_y_direction
    global circle_x_direction
    x_mod = (score//15)
    y_mod = (score//10)
    if circle_x_direction > 0:
        circle_x_direction = 4 + x_mod
    elif circle_x_direction < 0:
        circle_x_direction = -4 - x_mod
    if circle_y_direction > 0:
        circle_y_direction = 5 + y_mod
    elif circle_y_direction < 0:
        circle_y_direction = -5 - y_mod


#Check if player has collided with the ball/circle:
def check_collision(playerx, playery, ballx, bally):
    if abs(playerx - ballx) < 44 and abs(playery - bally) < 54:
        global player_x_direction
        global player_y_direction
        global circle_x_direction
        global circle_y_direction
        player_x_direction = 0
        player_y_direction = 0
        circle_x_direction = 0
        circle_y_direction = 0
        game_over()

#Game over instructions:
def game_over():
    global gameover
    display_game_over = game_over_font.render("GAME OVER!", True, red, black)
    screen.blit(display_game_over, (100, 300))
    display_restart = font.render("PRESS SPACE TO RESTART!", True, white, black)
    screen.blit(display_restart, (150, 400))
    gameover = True


#bound player within the gamescreen:
def update_player_position():
    global player_x
    global player_y
    global player_x_direction
    global player_y_direction
    if player_x_direction > 0:
        if player_x < (600 - player_width):
            player_x += player_x_direction * player_speed
    if player_x_direction < 0:
        if player_x > 0:
            player_x += player_x_direction * player_speed
    if player_y_direction > 0:
        if player_y < (600 - player_height):
            player_y += player_y_direction * player_speed
    if player_y_direction < 0:
        if player_y > 0:
            player_y += player_y_direction * player_speed


#bound ball/circle withing in the game screen:
def update_ball_position():
    global circle_x
    global circle_y
    global circle_x_direction
    global circle_y_direction
    global score
    if circle_x_direction > 0:
        if circle_x < 570:
            circle_x += circle_x_direction
        else:
           circle_x_direction *= -1
           score += 1 
    elif circle_x_direction < 0:
        if circle_x > 30:
            circle_x += circle_x_direction
        else:
           circle_x_direction *= -1
           score += 1
    if circle_y_direction > 0:
        if circle_y < 570:
            circle_y += circle_y_direction
        else:
           circle_y_direction *= -1
           score += 1 
    elif circle_y_direction < 0:
        if circle_y > 30:
            circle_y += circle_y_direction
        else:
           circle_y_direction *= -1
           score += 1

#set up game loop:
running = True
while running:
    timer.tick(framerate)   #set a 'speed'for the program to run.
    update_ball_position()
    update_player_position()
    check_difficulty()

#Check if certain keys are pressed or released:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_direction = -1
            if event.key == pygame.K_RIGHT:
                player_x_direction = 1
            if event.key == pygame.K_UP:
                player_y_direction = -1
            if event.key == pygame.K_DOWN:
                player_y_direction = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player_x_direction = 0
            if event.key == pygame.K_RIGHT:
                player_x_direction = 0
            if event.key == pygame.K_UP:
                player_y_direction = 0
            if event.key == pygame.K_DOWN:
                player_y_direction = 0
            #When space is released the game starts again collection and comparing scores:
            if event.key == pygame.K_SPACE and gameover:
                circle_x = 300
                circle_y = 300
                circle_x_direction = 4
                circle_y_direction = 5
                player_x = 300
                player_y = 500
                previous_score = score
                if score > high_score:
                    high_score = score
                #Return to intial game-state:
                score = 0
                gameover = False

        
    screen.fill((background))
    #Draw the Ball/Circle
    ball = pygame.draw.circle(screen, green, (circle_x,circle_y), 30, 5)
    pygame.draw.circle(screen, red, (circle_x,circle_y), 25)
    #Draw the player:
    gamer = pygame.draw.rect(screen, orange, [player_x, player_y, player_width, player_height])
    #Check for game-status:
    check_collision(gamer.centerx, gamer.centery, ball.centerx, ball.centery)
    #Print scores on screen:
    display_score = font.render("Score: "+ str(score), True, white, black)
    screen.blit(display_score, (10, 10))
    display_previous_score = font.render("Previous Score: "+ str(previous_score), True, white, black)
    screen.blit(display_previous_score, (10, 35))
    display_high_score = font.render("HighScore: "+ str(high_score), True, green, black)
    screen.blit(display_high_score, (10, 60))
    #"update" screen:
    pygame.display.flip()

pygame.quit()
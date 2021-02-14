import pygame
from config import Config
from helpers import getSound
from draw import displayWinner

red_bullets = Config.RED_BULLETS
yellow_bullets = Config.YELLOW_BULLETS

def updateRedSpaceship(keys_pressed, red_spaceship):
    velocity = 4.2

    can_move_right = red_spaceship.x + red_spaceship.width + velocity < Config.WIDTH
    can_move_left = red_spaceship.x - velocity > 0
    can_move_up = red_spaceship.y - velocity > 0
    can_move_down = red_spaceship.y + red_spaceship.height + velocity < Config.HEIGHT
    passed_middle_border = red_spaceship.x + red_spaceship.width + velocity > Config.MIDDLE_BORDER_POSITION[0]

    Config.RED_SPACESHIP_POSITION = red_spaceship.x, red_spaceship.y

    if keys_pressed[pygame.K_d] and can_move_right and not passed_middle_border:
        red_spaceship.x += velocity

    if keys_pressed[pygame.K_a] and can_move_left:
        red_spaceship.x -= velocity

    if keys_pressed[pygame.K_w] and can_move_up:
        red_spaceship.y -= velocity

    if keys_pressed[pygame.K_s] and can_move_down:
        red_spaceship.y += velocity

def updateYellowSpaceship(keys_pressed, yellow_spaceship):
    velocity = 4.2

    can_move_right = yellow_spaceship.x + yellow_spaceship.width + velocity < Config.WIDTH
    can_move_left = yellow_spaceship.x - velocity > 0
    can_move_up = yellow_spaceship.y - velocity > 0
    can_move_down = yellow_spaceship.y + yellow_spaceship.height + velocity < Config.HEIGHT
    passed_middle_border = yellow_spaceship.x - velocity < Config.MIDDLE_BORDER_POSITION[0] + Config.MIDDLE_BORDER_SCALE[0]
    
    Config.YELLOW_SPACESHIP_POSITION = yellow_spaceship.x, yellow_spaceship.y

    if keys_pressed[pygame.K_RIGHT] and can_move_right:
        yellow_spaceship.x += velocity

    if keys_pressed[pygame.K_LEFT] and can_move_left and not passed_middle_border:
        yellow_spaceship.x -= velocity

    if keys_pressed[pygame.K_UP] and can_move_up:
        yellow_spaceship.y -= velocity

    if keys_pressed[pygame.K_DOWN] and can_move_down:
        yellow_spaceship.y += velocity

def handleEvents(WIN, sounds, red_spaceship, yellow_spaceship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Config.RUN = False
            pygame.quit()

        # key per frame events
        if event.type == pygame.KEYDOWN:
            max_bullets = 4

            if event.key == pygame.K_LCTRL and len(red_bullets) < max_bullets:
                spaceship_scale = Config.SPACESHIP_SCALE[1], Config.SPACESHIP_SCALE[0]
                spaceship_position = Config.RED_SPACESHIP_POSITION
                
                bullet_scale = 20, 5

                bullet_position = spaceship_position[0] + spaceship_scale[0], spaceship_position[1]
                bullet_position = bullet_position[0], spaceship_position[1] + (spaceship_scale[1] / 2)
                bullet_position = bullet_position[0], bullet_position[1] - (bullet_scale[1] / 2)

                bullet = pygame.Rect(*bullet_position, *bullet_scale)
                red_bullets.append(bullet)
                
                getSound(sounds, 'gun')['sound'].play()

            if event.key == pygame.K_RCTRL and len(yellow_bullets) < max_bullets:
                spaceship_scale = Config.SPACESHIP_SCALE[1], Config.SPACESHIP_SCALE[0]
                spaceship_position = Config.YELLOW_SPACESHIP_POSITION
                
                bullet_scale = 20, 5

                bullet_position = spaceship_position[0] - bullet_scale[0], spaceship_position[1]
                bullet_position = bullet_position[0], spaceship_position[1] + (spaceship_scale[1] / 2)
                bullet_position = bullet_position[0], bullet_position[1] - (bullet_scale[1] / 2)

                bullet = pygame.Rect(*bullet_position, *bullet_scale)

                yellow_bullets.append(bullet)

                getSound(sounds, 'gun')['sound'].play()

        # user events
        if event.type == Config.RED_HIT:
            if Config.RED_HEALTH == 0:
                displayWinner(WIN, "yellow won!")
                pygame.time.delay(2500)
                pygame.quit()

            Config.RED_HEALTH -= 1
            getSound(sounds, 'grenade')['sound'].play()

        if event.type == Config.YELLOW_HIT:
            if Config.YELLOW_HEALTH == 0:
                displayWinner(WIN, "red won!")
                pygame.time.delay(2500)
                pygame.quit()

            Config.YELLOW_HEALTH -= 1
            getSound(sounds, 'grenade')['sound'].play()

    keys_pressed = pygame.key.get_pressed()

    updateRedSpaceship(keys_pressed, red_spaceship)
    updateYellowSpaceship(keys_pressed, yellow_spaceship)

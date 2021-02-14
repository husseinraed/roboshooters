import pygame
from config import Config
from helpers import rgb, getImage

red_bullets = Config.RED_BULLETS
yellow_bullets = Config.YELLOW_BULLETS

def frame(WIN, images, red_spaceship, yellow_spaceship, middle_border):
    space = getImage(images, 'space')['image']
    space = pygame.transform.scale(space, (Config.WIDTH, Config.HEIGHT))
    
    WIN.blit(space, (0,0))

    renderBullets(WIN, red_spaceship, yellow_spaceship)

    redSpaceship(WIN, images, red_spaceship)

    yellowSpaceship(WIN, images, yellow_spaceship)
    
    middleBorder(WIN, middle_border)

    red_health_text = Config.HEALTH_FONT.render(f"Health: {Config.RED_HEALTH}", 1, (255,255,255))
    yellow_health_text = Config.HEALTH_FONT.render(f"Health: {Config.YELLOW_HEALTH}", 1, (255,255,255))

    WIN.blit(red_health_text, (10, 10))
    WIN.blit(yellow_health_text, ((Config.WIDTH - yellow_health_text.get_width()) - 10, 10))

def renderBullets(WIN, red_spaceship, yellow_spaceship):
    for bullet in red_bullets:
        pygame.draw.rect(WIN, rgb("#ff0000"), bullet)

        bullet.x += 7

        if yellow_spaceship.colliderect(bullet):
            red_bullets.remove(bullet)
            pygame.event.post(pygame.event.Event(Config.YELLOW_HIT))

        if bullet.x > Config.WIDTH:
            red_bullets.remove(bullet)


    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, rgb("#f6ff00"), bullet)

        bullet.x -= 7

        if red_spaceship.colliderect(bullet):
            yellow_bullets.remove(bullet)
            pygame.event.post(pygame.event.Event(Config.RED_HIT))

        if bullet.x < 0:
            yellow_bullets.remove(bullet)

def yellowSpaceship(WIN, images, yellow_spaceship):
    image = getImage(images, 'yellow_spaceship')['image']
    image = pygame.transform.scale(image, Config.SPACESHIP_SCALE)
    image = pygame.transform.rotate(image, -90)
    
    WIN.blit(image, (yellow_spaceship.x, yellow_spaceship.y))

def redSpaceship(WIN, images, red_spaceship):
    image = getImage(images, 'red_spaceship')['image']
    image = pygame.transform.scale(image, Config.SPACESHIP_SCALE)
    image = pygame.transform.rotate(image, 90)

    WIN.blit(image, (red_spaceship.x, red_spaceship.y))

def middleBorder(WIN, middle_border):
    pygame.draw.rect(WIN, rgb("#000000"), middle_border)

def displayWinner(WIN, text):
    winner_text = Config.HEALTH_FONT.render(text, 1, (255,255,255))

    WIN.blit(winner_text, ((Config.WIDTH / 2) - (winner_text.get_width() / 2), (Config.HEIGHT / 2)))
    pygame.display.update()
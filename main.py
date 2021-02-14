import pygame
from config import Config
import events
import draw
import load

WIN = pygame.display.set_mode((Config.WIDTH, Config.HEIGHT))
pygame.display.set_caption("RoboShooters - 1v1")

images = load.images() 
sounds = load.sounds()

def main():
    Config.RUN = True
    clock = pygame.time.Clock()

    spacship_collider_scale = Config.SPACESHIP_SCALE[1], Config.SPACESHIP_SCALE[0]

    red_spaceship = pygame.Rect(*Config.RED_SPACESHIP_POSITION, *spacship_collider_scale)
    yellow_spaceship = pygame.Rect(*Config.YELLOW_SPACESHIP_POSITION, *spacship_collider_scale)
    middle_border = pygame.Rect(*Config.MIDDLE_BORDER_POSITION, *Config.MIDDLE_BORDER_SCALE)
    
    while Config.RUN:
        clock.tick(Config.FPS)

        events.handleEvents(WIN, sounds, red_spaceship, yellow_spaceship)

        draw.frame(WIN, images, red_spaceship, yellow_spaceship, middle_border)

        pygame.display.update()

if __name__ == "__main__":
    main()

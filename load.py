import pygame
import os

def images():
    path = os.path.dirname(os.path.abspath(__file__))
    images = []

    for file in os.listdir(os.path.join(path, 'Assets', 'images')):
        name = file.split('.')[0]

        images.append({'name': name, 'image': pygame.image.load(os.path.join(path, 'Assets', 'images', file))})

    return images

def sounds():
    pygame.mixer.init()

    path = os.path.dirname(os.path.abspath(__file__))
    sounds = []

    for file in os.listdir(os.path.join(path, 'Assets', 'sounds')):
        name = file.split('.')[0]

        sounds.append({'name': name, 'sound': pygame.mixer.Sound(os.path.join(path, 'Assets', 'sounds', file))})

    return sounds

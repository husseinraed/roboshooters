import errors

def rgb(h):
    h = h.lstrip('#')
    
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def getImage(images, name):
    for image in images:
        if image['name'] == name:
            return image
    else:
        raise errors.ImageNotFoundError(f"Image of name {name} was not found!")

def getSound(sounds, name):
    for sound in sounds:
        if sound['name'] == name:
            return sound
    else:
        raise errors.SoundNotFoundError(f"Sound of name {name} was not found!")



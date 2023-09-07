import settings

def height_proportion(value):
    return int(value * settings.HEIGTH / 100)

def width_proportion(value):
    return int(value * settings.WIDTH / 100)
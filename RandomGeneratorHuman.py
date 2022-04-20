# IMPORTS
from ursina import *
import random

# VARIABLES
random_generator = random.Random()
ColorEyes = color.random_color()
ColorJeans = color.random_color()
ColorShirt = color.random_color()
ColorShoes = color.random_color()

class Humano(Entity):
    cabello = Entity(model = "cube", coillider = "mesh", color = color.random_color(), position = (0, 2, -0.1), scale = (1.1, random_generator.random(), 1.1))
    cabeza = Entity(model = "cube", collider = "mesh", position = (0, 1.6, -0.1), scale = (1, 1.2, 0.9))
    ojo1 = Entity(model = "cube", color = color.white, position = (0.3, 1.6, -0.5), scale = (0.3, random_generator.random(), 0.2))
    pupila1 = Entity(model = "quad", position = (0.25,  1.62, -0.62), scale = 0.125)
    ojo2 = Entity(model = "cube", color = color.white, position = (-0.3, 1.6, -0.5), scale = (0.3, random_generator.random(), 0.2))
    pupila2 = Entity(model = "quad", color = ColorEyes, position = (-0.25,  1.62, -0.62), scale = 0.125)
    nariz = Entity(model = "cube", position = (0, 1.4, -0.6), scale = (0.2, 0.3, random_generator.random()))
    boca = Entity(model = "quad", color = color.salmon, position = (0, 1.15, -0.56), scale = (0.3, 0.05))
    cuerpo = Entity(model = "cube", collider = "mesh", color = ColorShirt)
    hombro1 = Entity(model = "cube", collider = "mesh", color = ColorShirt, position = (0.9, 0.75, 0))
    hombro2 = Entity(model = "cube", collider = "mesh", color = ColorShirt, position = (-0.9, 0.75, 0))
    brazo1 = Entity(model = "cube", collider = "mesh", position = (0.9, -0.125, 0))
    brazo2 = Entity(model = "cube", collider = "mesh", position = (-0.9, -0.125, 0))
    mano1 = Entity(model = "cube", collider = "mesh", position = (0.9, -0.875, 0), scale = (0.5, 0.25, 0.5))
    mano2 = Entity(model = "cube", collider = "mesh", position = (-0.9, -0.875, 0), scale = (0.5, 0.25, 0.5))
    cadera = Entity(model = "cube", color = ColorJeans, position = (0, -1.125, 0), scale = (1.4, 0.25, 0.6))
    shortleg1 = Entity(model = "cube", color = ColorJeans, position = (0.4, -1.5, 0), scale = 0.6)
    shortleg2 = Entity(model = "cube", color = ColorJeans, position = (-0.4, -1.5, 0), scale = 0.6)
    pierna1 = Entity(model = "cube", collider = "mesh", position = (0.4, -2.25, 0))
    pierna2 = Entity(model = "cube", collider = "mesh", position = (-0.4, -2.25, 0))
    pie1 = Entity(model = "cube", collider = "mesh", position =(0.4, -2.875, -0.125), scale = (0.5, 0.25, 0.75))
    pie2 = Entity(model = "cube", collider = "mesh", position = (-0.4, -2.875, -0.125), scale = (0.5, 0.25, 0.75))

def genes():
    Cabello = random_generator.random()
    Heterocromia = random_generator.random()
    Caucasico = random_generator.random()

    if Cabello <= 0.9:
        Humano.cabello.visible = True
    else:
        Humano.cabello.visible = False

    if Heterocromia <= 0.1:
        for i in range(1):
            Humano.pupila1.color = color.random_color()
    else:
        Humano.pupila1.color = ColorEyes

    if Caucasico <= 0.7:
        Humano.cabeza.color = color.peach
        Humano.nariz.color = color.peach
        Humano.brazo1.color = color.peach
        Humano.brazo2.color = color.peach
        Humano.mano1.color = color.peach
        Humano.mano2.color = color.peach
    else:
        Humano.cabeza.color = color.brown
        Humano.nariz.color = color.brown
        Humano.brazo1.color = color.brown
        Humano.brazo2.color = color.brown
        Humano.mano1.color = color.brown
        Humano.mano2.color = color.brown

def func():
    if Humano.cabello.scale_y <= 0.5:
        Humano.cabello.scale_y = 0.5
    if Humano.ojo1.scale_y <= 0.5:
        Humano.ojo1.scale_y = 0.2
    else:
        Humano.ojo1.scale_y = 0.225

    if Humano.ojo2.scale_y <= 0.5:
        Humano.ojo2.scale_y = 0.2
    else:
        Humano.ojo2.scale_y = 0.225

    if Humano.nariz.scale.z >= 0.5:
        Humano.nariz.scale.z = 0.35
    elif Humano.nariz.scale.z <= 0.2:
        Humano.nariz.scale.z = 0.2
    
def ropa():
    sueter = random_generator.random()
    pantalon = random_generator.random()
    tenis = random_generator.random()

    if sueter <= 0.3:
        Humano.brazo1.color = ColorShirt
        Humano.brazo1.scale = (0.6, 1.35, 0.6)
        Humano.brazo2.color = ColorShirt
        Humano.brazo2.scale = (0.6, 1.35, 0.6)
        Humano.cuerpo.scale = (1.4, 2, 0.6)
        Humano.hombro1.scale = 0.6
        Humano.hombro2.scale = 0.6
    elif sueter <= 0.6 and sueter > 0.3:
        Humano.brazo1.color = ColorShirt
        Humano.brazo1.scale = (0.5, 1.25, 0.5)
        Humano.brazo2.color = ColorShirt
        Humano.brazo2.scale = (0.5, 1.25, 0.5)
        Humano.cuerpo.scale = (1.3, 2, 0.5)
        Humano.hombro1.scale = 0.5
        Humano.hombro2.scale = 0.5
    else:
        Humano.brazo1.color = Humano.cabeza.color
        Humano.brazo1.scale = (0.5, 1.25, 0.5)
        Humano.brazo2.color = Humano.cabeza.color
        Humano.brazo2.scale = (0.5, 1.25, 0.5)
        Humano.cuerpo.scale = (1.3, 2, 0.5)
        Humano.hombro1.scale = 0.5
        Humano.hombro2.scale = 0.5
    
    if pantalon <= 0.5:
        Humano.pierna1.color = ColorJeans
        Humano.pierna1.scale = (0.6, 1.1, 0.6)
        Humano.pierna2.color = ColorJeans
        Humano.pierna2.scale = (0.6, 1.1, 0.6)
    else:
        Humano.pierna1.color = Humano.cabeza.color
        Humano.pierna1.scale = (0.5, 1, 0.5)
        Humano.pierna2.color = Humano.cabeza.color
        Humano.pierna2.scale = (0.5, 1, 0.5)
    
    if tenis <= 0.5:
        Humano.pie1.color = ColorShoes
        Humano.pie2.color = ColorShoes
    else:
        Humano.pie1.color = Humano.cabeza.color
        Humano.pie2.color = Humano.cabeza.color
        
genes()
ropa()
func()

# IMPORTS
from ursina import *
import random

# VARIABLES
random_generator = random.Random()
ColorEyes = color.random_color()
ColorLegs = color.random_color()
ColorCloth = color.random_color()

class Humano(Entity
    cabello = Entity(model = "cube", coillider = "mesh", color = color.random_color(), position = (0, 2, -0.1), scale = (1.1, random_generator.random(), 1.1))
    cabeza = Entity(model = "cube", collider = "mesh", position = (0, 1.6, -0.1), scale = (1, 1.2, 0.9))
    ojo1 = Entity(model = "cube", color = ColorEyes, position = (0.3, 1.6, -0.5), scale = random_generator.random())
    ojo2 = Entity(model = "cube", color = ColorEyes, position = (-0.3, 1.6, -0.5), scale = random_generator.random())
    nariz = Entity(model = "cube", position = (0, 1.4, -0.6), scale = (0.2, 0.3, random_generator.random()))
    cuerpo = Entity(model = "cube", collider = "mesh", color = ColorCloth, scale = (1.3, 2, 0.5))
    hombro1 = Entity(model = "cube", collider = "mesh", color = ColorCloth, position = (0.9, 0.75, 0), scale = 0.5)
    hombro2 = Entity(model = "cube", collider = "mesh", color = ColorCloth, position = (-0.9, 0.75, 0), scale = 0.5)
    brazo1 = Entity(model = "cube", collider = "mesh", position = (0.9, -0.25 , 0), scale = (0.5, 1.5, 0.5))
    brazo2 = Entity(model = "cube", collider = "mesh", position = (-0.9, -0.25, 0), scale = (0.5, 1.5, 0.5))
    pierna1 = Entity(model = "cube", collider = "mesh", color = ColorLegs, position = (0.4, -2, 0), scale = (0.5, 2, 0.5))
    pierna2 = Entity(model = "cube", collider = "mesh", color = ColorLegs, position = (-0.4, -2, 0), scale = (0.5, 2, 0.5))

def func():
    if Humano.cabello.scale_y <= 0.5:
        Humano.cabello.scale_y = 0.5

    if Humano.ojo1.scale <= 0.5:
        Humano.ojo1.scale = 0.2
    else:
        Humano.ojo1.scale = 0.225

    if Humano.ojo2.scale <= 0.5:
        Humano.ojo2.scale = 0.2
    else:
        Humano.ojo2.scale = 0.225
    
    if Humano.nariz.scale.z >= 0.5:
        Humano.nariz.scale.z = 0.35
    elif Humano.nariz.scale.z <= 0.2:
        Humano.nariz.scale.z = 0.2

    #Genes
    Cabello = random_generator.random()
    Heterocromia = random_generator.random()
    Caucasico = random_generator.random()

    if Cabello <= 0.5:
        Humano.cabello.visible = True
    else:
        Humano.cabello.visible = False

    if Heterocromia < 0.1:
        for i in range(1):
            Humano.ojo1.color = color.random_color()
    else:
        Humano.ojo1.color = ColorEyes

    if Caucasico <= 0.5:
        Humano.cabeza.color = color.peach
        Humano.nariz.color = color.peach
        Humano.brazo1.color = color.peach
        Humano.brazo2.color = color.peach
    else:
        Humano.cabeza.color = color.brown
        Humano.nariz.color = color.brown
        Humano.brazo1.color = color.brown
        Humano.brazo2.color = color.brown
        
func()

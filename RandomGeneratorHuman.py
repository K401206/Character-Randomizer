# IMPORTS

from ursina import *
from ursina.shaders import lit_with_shadows_shader
import random


app = Ursina()

#WINDOW

window.title = 'Random Character Generator'
window.borderless = True
window.fullscreen = False
window.exit_button.visible = True
window.fps_counter.enabled = False
window.size = (630, 710)
window.position = Vec2(725, 50)

#ENVIROMENT

Sky()
Entity.default_shader = lit_with_shadows_shader
sun = DirectionalLight(shadows=True)
sun.look_at(Vec3(1,-1,-1))
EditorCamera()

# VARIABLES

Cabello = True
Heterocromia = False
ColorEyes = color.random_color()
Caucasico = True
ColorLegs = color.random_color()
ColorCloth = color.random_color()

random_generator = random.Random()

# ENTITYS

class Humano(Entity):
    cabeza = Entity(
        model = "cube",
        collider = "mesh",
        position = (0, 1.6, -0.1),
        scale = (1, 1.2, 0.9)
    )
    cabello = Entity(
        model = "cube",
        color = color.random_color(),
        coillider = "mesh",
        position = (0, 2, -0.1),
        scale = (1.1, random_generator.random(), 1.1)
    )
    ojo1 = Entity(
        model = "cube",
        color = ColorEyes,
        position = (0.3, 1.6, -0.5),
        scale = 0.2
    )
    ojo2 = Entity(
        model = "cube",
        color = ColorEyes,
        position = (-0.3, 1.6, -0.5),
        scale = 0.2
    )
    nariz = Entity(
        model = "cube",
        position = (0, 1.4, -0.6),
        scale = (0.2, 0.3, random_generator.random())
    )

    cuerpo = Entity(
        model = "cube",
        color = ColorCloth,
        collider = "mesh",
        scale = (1.3, 2, 0.5)
    )
    hombro1 = Entity(
        model = "cube",
        color = ColorCloth,
        collider = "mesh",
        position = (0.9, 0.75, 0),
        scale = 0.5
    )
    hombro2 = Entity(
        model = "cube",
        color = ColorCloth,
        collider = "mesh",
        position = (-0.9, 0.75, 0),
        scale = 0.5
    )
    brazo1 = Entity(
        model = "cube",
        collider = "mesh",
        position = (0.9, -0.25 , 0),
        scale = (0.5, 1.5, 0.5)
    )
    brazo2 = Entity(
        model = "cube",
        collider = "mesh",
        position = (-0.9, -0.25, 0),
        scale = (0.5, 1.5, 0.5)
    )

    pierna1 = Entity(
        model = "cube",
        color = ColorLegs,
        collider = "mesh",
        position = (0.4, -2, 0),
        scale = (0.5, 2, 0.5)
    )
    pierna2 = Entity(
        model = "cube",
        color = ColorLegs,
        collider = "mesh",
        position = (-0.4, -2, 0),
        scale = (0.5, 2, 0.5)
    )

def func():

    for i in range(1):
        if Heterocromia:
            Humano.ojo1.color = color.random_color()
        else:
            Humano.ojo1.color = ColorEyes

    if Cabello:
        Humano.cabello.visible = True
    else:
        Humano.cabello.visible = False
    
    if Caucasico:
        Humano.cabeza.color = color.peach
        Humano.nariz.color = color.peach
        Humano.brazo1.color = color.peach
        Humano.brazo2.color = color.peach
    else:
        Humano.cabeza.color = color.brown
        Humano.nariz.color = color.brown
        Humano.brazo1.color = color.brown
        Humano.brazo2.color = color.brown

    if Humano.cabello.scale_y <= .5:
        Humano.cabello.scale_y = .5

func()

app.run()

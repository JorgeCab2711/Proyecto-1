from gl import Renderer, color, V3, V2
from texture import Texture
from shaders import *

width = 1000
height = 800

rend = Renderer(width, height)

rend.dirLight = V3(1, 0, 0)

"""
    Text
"""
# Shader 1
rend.active_shader = clearTextShader
rend.active_texture = Texture("textures/marble.bmp")
# text JOIN  model load
rend.glLoadModel("models/mine/join.obj",
                 translate=V3(-1.5, 4, -10),
                 scale=V3(4.4, 4.4, 4.4),
                 rotate=V3(100, 0, -12))
# text US model load
rend.glLoadModel("models/mine/us.obj",
                 translate=V3(0, -6, -15),
                 scale=V3(2, 2, 2),
                 rotate=V3(80, 0, -14))


"""
    Mask
"""
# Shader 2
rend.active_shader = metal
# Applying red texture to mask
rend.active_texture = Texture("textures/red.bmp")
# Mask hand model load
rend.glLoadModel("models/mine/mask.obj",
                 translate=V3(0, -2, -11.5),
                 scale=V3(4.4, 4.4, 4.4),
                 rotate=V3(0, 10, 10))


"""
    Hands
"""
# shader 3
rend.active_shader = soft
# Right hand model load
rend.active_texture = Texture("textures/marble.bmp")
rend.glLoadModel("models/mine/hand_mod.obj",
                 translate=V3(-4, -3.5, -10),
                 scale=V3(2.8, 2.8, 2.8),
                 rotate=V3(60, -130, 0)
                 )


# left hand model load
rend.glLoadModel("models/mine/left_hand.obj",
                 translate=V3(4, -3.5, -10),
                 scale=V3(2.8, 2.8, 2.8),
                 rotate=V3(60, 130, 0)
                 )

# skulls to right model load
# Skull with normal mapping
rend.active_texture = Texture("textures/Skull.bmp")
rend.active_texture2 = Texture("textures/skullNM.bmp")
# Skull number n

x = 2
z = -14

for i in range(13):
    rend.glLoadModel("models/skull.obj",
                     translate=V3(x, -1, z),
                     scale=V3(2.8, 2.8, 2.8),
                     rotate=V3(-10, 0, 0)
                     )
    x += 2
    z -= 2

# Skull number n
x = -3
z = -14

for i in range(13):
    rend.glLoadModel("models/skull.obj",
                     translate=V3(x, -1, z),
                     scale=V3(2.8, 2.8, 2.8),
                     rotate=V3(-10, 0, 0)
                     )
    x -= 2
    z -= 2


rend.glFinish("output.bmp")

import pyglet
from pyglet.window import key
import fruitloop as fruit

# Create Window and Add Keyboard State Handler to it's Event Loop
window = pyglet.window.Window()
keys = key.KeyStateHandler()
window.push_handlers(keys)

# Insert filename into WavefrontReader.
obj_filename = fruit.resources.obj_primitives
obj_reader = fruit.WavefrontReader(obj_filename)

# Create Mesh
monkey = obj_reader.get_mesh("Monkey", position=(0, 0, -1.5), scale=.6)
torus = obj_reader.get_mesh("Torus", position=(-1, 0, -1.5), scale=.4)

# Create Scene
scene = fruit.Scene(meshes=[monkey, torus])
scene.bgColor = 1, 0, 0


# Functions to Run in Event Loop
def rotate_meshes(dt):
    monkey.rotation.y += 15 * dt  # dt is the time between frames
    torus.rotation.x += 80 * dt


pyglet.clock.schedule(rotate_meshes)


def move_camera(dt):
    camera_speed = 3
    if keys[key.LEFT]:
        scene.camera.position.x -= camera_speed * dt
    if keys[key.RIGHT]:
        scene.camera.position.x += camera_speed * dt


pyglet.clock.schedule(move_camera)


shader = fruit.Shader.from_file(*fruit.resources.genShader)

@window.event
def on_draw():
    with shader:
        scene.draw()


pyglet.app.run()
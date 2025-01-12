# import pygame
import pygdk

window = pygdk.Surface(pygdk.Vector2(800.0, 600.0), "Jolly")
pygdk.drawText(window, "Hello, World!", None, None)
window.show()
import pygdk

#winsize = pygdk.Vector2(800, 600)
#window = pygdk.init(winsize.x, winsize.y)
#pygdk.draw.drawText(window, "Hello World", pygdk.font.Font(size=30))
#window.show()

window = pygdk.init(800, 600)
pygdk.draw.drawText(window, "Hello World", pygdk.font.Font(size=30))
window.show()

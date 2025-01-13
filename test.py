import pygdk

window = pygdk.init(800, 600)
pygdk.draw.drawText(window, "Hello World", pygdk.font.Font(size=30))
window.show()

import pygdk

pygdk.init(800, 600, "Example")
pygdk.drawText("Hello World", pygdk.Color(100, 100, 100))
pygdk.show()
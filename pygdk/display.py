from pygdk.constants import window

def SetTitle(title):
    if window:
        window.setWindowTitle(title)
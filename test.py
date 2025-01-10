import pygame
import pygdk

def main():
    pygdk.SetWindowSize(800, 600)
    pygdk.display.SetTitle('Hello World')
    pygdk.Show()

if __name__ == '__main__':
    main()

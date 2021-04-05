#modcolocko's PNG Generator
import pygame

#File Settings
filename = "Filename"

#Color Settings
background = (35, 39, 42)

#Image Settings
width = 100
height = 100

#Draw Window
pygame.init()
win = pygame.display.set_mode((width, height))
win.fill(background)

#Draw Objects

filename = f"{filename}.png"
pygame.image.save(win, filename)
print(f"file {filename} has been saved")
pygame.quit()

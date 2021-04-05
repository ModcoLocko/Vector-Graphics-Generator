import pygame
#File Settings
filename = "rankcard"
#Message Settings
xp = 140
xptogo = 440
username = "modcolocko"
#Color Settings
backgroundcolor = (35, 39, 42)
xpbarbackcolor = (57, 47, 100)
xpcolor = (90, 47, 217)
xptextcolor = (80, 80, 100)
textcolor = (166, 166, 200)
#Image Settings
width = 560
height = 140
#Object Settings
XBradius = 24
#XpBar
XBtopdis = 52
XBheight = 48
#XpBarBack
XBBwidth = 500
#End of object settings
#Config
xpbarposh = (width - XBBwidth)/2
xforxp = XBBwidth/xptogo
xp2 = xp*xforxp
if XBradius > XBheight/2:
    XBradius = int(XBheight/2)
if xp2 == 0:
    xp2 = 0
elif xp2 < XBradius*2:
    xp2 = XBradius*2
elif xp2 > XBBwidth:
    xp2 = XBBwidth

#Draw Window
win = pygame.display.set_mode((width, height))
win.fill(backgroundcolor)
pygame.init()
#Text
font = pygame.font.Font('FiraSans-Medium.ttf', 30)
fontsmall = pygame.font.Font('FiraSans-Medium.ttf', 20)
name = font.render(username, True, (textcolor))
xptext = fontsmall.render(f"{xp}/{xptogo} xp", True, (xptextcolor))
namewidth = int(name.get_width())
namepos = (width-namewidth)/2
xpwidth = int(xptext.get_width())
xppos = (width-xpwidth)/2
#Draw Objects
pygame.draw.rect(win, xpbarbackcolor, pygame.Rect(xpbarposh, XBtopdis, XBBwidth, XBheight), border_radius=XBradius)
pygame.draw.rect(win, xpcolor, pygame.Rect(xpbarposh, XBtopdis, xp2, XBheight), border_radius=XBradius)
win.blit(name, (namepos, 6.5))
win.blit(xptext, (xppos, 105))
#Update
pygame.display.flip()
#Save File
filename = f"{filename}.png"
pygame.image.save(win, filename)
print(f"file {filename} has been saved")
pygame.quit()

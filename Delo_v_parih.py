import pygame
import sys

pygame.init()
sirina, visina = 1400, 1050
zaslon = pygame.display.set_mode((sirina, visina))
ura = pygame.time.Clock()

mucka_sirina, mucka_visina = 50, 35
mucka_x = sirina // 4
mucka_y = visina // 2
hitrost = 5

crna = (0, 0, 0)
zelenomodra = (0, 255, 255)

while True:
    for dogodek in pygame.event.get():
        if dogodek.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    tipke = pygame.key.get_pressed()
    if tipke[pygame.K_UP]:
        mucka_y -= hitrost
    if tipke[pygame.K_DOWN]:
        mucka_y += hitrost

    zaslon.fill(crna)
    pygame.draw.rect(zaslon, zelenomodra, (mucka_x, mucka_y, mucka_sirina, mucka_visina))
    pygame.display.flip()
    ura.tick(60)

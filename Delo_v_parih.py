import pygame
import sys
import random

pygame.init()
sirina, visina = 1400, 1050
zaslon = pygame.display.set_mode((sirina, visina))
ura = pygame.time.Clock()

mucka_sirina, mucka_visina = 50, 35
mucka_x = sirina // 4
mucka_y = visina // 2

hitrost_y = 0
gravitacija = 0.5
skok_moc = -10

crna = (0, 0, 0)
zelenomodra = (0, 255, 255)
platforma_barva = (255, 105, 180)
tla_barva = (255, 140, 0)
tla_visina = 60

platforme = []
stevilo_platform = 6
platforma_sirina = 200
platforma_visina = 20
platforma_hitrost = 4

for i in range(stevilo_platform):
    x = random.randint(0, sirina)
    y = random.randint(0, visina - platforma_visina)
    platforme.append([x, y])

while True:
    for dogodek in pygame.event.get():
        if dogodek.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    tipke = pygame.key.get_pressed()

    if tipke[pygame.K_SPACE]:
        for p in platforme:
            px, py = p
            if (mucka_x + mucka_sirina > px and
                    mucka_x < px + platforma_sirina and
                    mucka_y + mucka_visina <= py + 5 and
                    mucka_y + mucka_visina >= py - 5):
                hitrost_y = skok_moc

    hitrost_y += gravitacija
    mucka_y += hitrost_y

    if mucka_y + mucka_visina >= visina - tla_visina:
        pygame.quit()
        sys.exit()

    for p in platforme:
        px, py = p
        if (mucka_x + mucka_sirina > px and
                mucka_x < px + platforma_sirina and
                mucka_y + mucka_visina >= py and
                mucka_y + mucka_visina <= py + platforma_visina and
                hitrost_y > 0):
            mucka_y = py - mucka_visina
            hitrost_y = 0

    for p in platforme:
        p[0] -= platforma_hitrost
        if p[0] + platforma_sirina < 0:
            p[0] = sirina + random.randint(50, 300)
            p[1] = random.randint(0, visina - platforma_visina)

    zaslon.fill(crna)

    for p in platforme:
        pygame.draw.rect(zaslon, platforma_barva, (p[0], p[1], platforma_sirina, platforma_visina))

    pygame.draw.rect(zaslon, zelenomodra, (mucka_x, mucka_y, mucka_sirina, mucka_visina))
    pygame.draw.rect(zaslon, tla_barva, (0, visina - tla_visina, sirina, tla_visina))

    pygame.display.flip()
    ura.tick(60)

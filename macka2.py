import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Nyan Cat Game")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLUE = (15, 15, 50)
RAINBOW = [(255,0,0),(255,127,0),(255,255,0),(0,255,0),(0,0,255),(75,0,130)]

# zvezde
stars = [[random.randint(0, WIDTH), random.randint(0, HEIGHT)] for _ in range(80)]

# maček 
cat_x = 200
cat_y = HEIGHT // 2

# kovanci
coins = []
score = 0
font = pygame.font.SysFont("Arial", 32)

def draw_cat(x, y):
    # telo 
    pygame.draw.rect(screen, (255,182,193), (x, y, 80, 50), border_radius=8)

    # pikice
    for _ in range(10):
        px = random.randint(x+5, x+75)
        py = random.randint(y+5, y+45)
        pygame.draw.circle(screen, (255,105,180), (px, py), 2)

    # glava
    pygame.draw.circle(screen, (160,160,160), (x+90, y+25), 20)

    # oči
    pygame.draw.circle(screen, (0,0,0), (x+85, y+20), 3)
    pygame.draw.circle(screen, (0,0,0), (x+95, y+20), 3)

    # ušesa
    pygame.draw.polygon(screen, (160,160,160),
        [(x+75,y+10),(x+85,y-5),(x+90,y+10)])
    pygame.draw.polygon(screen, (160,160,160),
        [(x+90,y+10),(x+100,y-5),(x+105,y+10)])

def draw_rainbow(x, y):
    for i, color in enumerate(RAINBOW):
        pygame.draw.rect(screen, color, (x-220, y+10+i*6, 220, 6))

running = True
while running:
    screen.fill(BLUE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # zvezde
    for star in stars:
        star[0] -= 2
        if star[0] < 0:
            star[0] = WIDTH
            star[1] = random.randint(0, HEIGHT)
        pygame.draw.circle(screen, WHITE, star, random.randint(1,3))

    # spawn kovancev
    if random.randint(1, 35) == 1:
        coins.append([WIDTH, random.randint(50, HEIGHT-50)])

    # kovanci
    for coin in coins[:]:
        coin[0] -= 5

        # glow efekt
        pygame.draw.circle(screen, (255,255,100), coin, 12)
        pygame.draw.circle(screen, (255,215,0), coin, 8)

        # pobiranje
        if abs(coin[0]-cat_x) < 50 and abs(coin[1]-cat_y) < 40:
            coins.remove(coin)
            score += 1
        elif coin[0] < 0:
            coins.remove(coin)

    # mavrica
    draw_rainbow(cat_x, cat_y)

    # maček
    draw_cat(cat_x, cat_y)

    # score (lepši)
    text = font.render(f" {score}", True, (255,255,0))
    screen.blit(text, (15, 15))

    pygame.display.update()
    clock.tick(60)

pygame.quit()

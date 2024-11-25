import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Movement Example")

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))

sprite1 = Sprite((255, 0, 0), 50, 50, 100, 100)
sprite2 = Sprite((0, 0, 255), 50, 50, 300, 100)

sprites = pygame.sprite.Group(sprite1, sprite2)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        sprite1.rect.x -= 5
    if keys[pygame.K_RIGHT]:
        sprite1.rect.x += 5
    if keys[pygame.K_UP]:
        sprite1.rect.y -= 5
    if keys[pygame.K_DOWN]:
        sprite1.rect.y += 5

    screen.fill((255, 255, 255))
    sprites.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
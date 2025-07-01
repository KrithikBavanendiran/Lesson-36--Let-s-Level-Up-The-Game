import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Add Custom Event")

BLACK = (0, 0, 0)

class ColorSprite(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface((100, 100))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update_color(self, new_color):
        self.color = new_color
        self.image.fill(self.color)

sprite_width = 100
gap = 10
total_width = sprite_width * 2 + gap
start_x = (WIDTH - total_width) // 2
start_y = (HEIGHT - sprite_width) // 2

red_sprite = ColorSprite((255, 0, 0), start_x, start_y)
blue_sprite = ColorSprite((0, 0, 255), start_x + sprite_width + gap, start_y)

all_sprites = pygame.sprite.Group(red_sprite, blue_sprite)

running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                red_sprite.update_color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
                blue_sprite.update_color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    all_sprites.draw(screen)
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()

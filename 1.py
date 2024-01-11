import pygame
import os
import sys
import random

FPS = 50
pygame.init()
screen = pygame.display.set_mode((600, 500))
bg = pygame.image.load("data/mainwind.jpg")

class Button():
    def __init__(self, image, pos, te_in, font, b_color, h_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.color1, self.color2 = b_color, h_color
        self.text = te_in
        self.tex = self.font.render(self.text, True, self.color1)
        if self.image is None:
            self.image = self.tex

        self.rect = self.image.get_rect(centre=(self.x_pos, self.y_pos))
        self.text_inr = self.tex(centre=(self.x_pos, self.y_pos))
    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.tex, self.text_inr)

    def inside(self, pos):
        if pos[0] in range(self.rect.left, self.rest.right) and pos[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def butcolour(self, pos):
        if pos[0] in range(self.rect.left, self.rest.right) and pos[1] in range(self.rect.top, self.rect.bottom):
            self.tex = self.font.render(self.text_inr, True, self.color2)
        else:
            self.tex = self.font.render(self.text_inr, True, self.color1)

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image

def start_screen(screen):
    clock = pygame.time.Clock()
    intro_text = ["Утка в погоне за утятами", "",
                  "Ищи люгушек для утят,"
                  " чтобы их прокормить"]
                  # "Если в правилах несколько строк,",
                  # "приходится выводить их построчно"]

    fon = pygame.transform.scale(load_image("mainwind.jpg"),
                                 (screen.get_width(), screen.get_height()))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)

def terminate():
    pygame.quit()
    sys.exit()

def main():
    running = True
    pygame.display.flip()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        start_screen(screen)
        pygame.display.flip()

    pygame.quit()



if __name__ == '__main__':
    main()

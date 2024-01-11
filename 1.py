import pygame
import os
import sys
import random

pygame.font.init()
FPS = 50
pygame.init()
screen = pygame.display.set_mode((600, 500))
bg = pygame.image.load("data/mainwind.jpg")

# def get_fonts(shr):
#     return pygame.font.get_fonts(shr)

img1 = pygame.image.load("data/img_1.png")
img1 = pygame.transform.scale(img1, (200, 70))
img2 = pygame.image.load("data/Green.jpg")
img2 = pygame.transform.scale(img1, (200, 70))
le1 = pygame.image.load("data/lev.jpg")
le1 = pygame.transform.scale(le1, (200, 200))


class Button():
    def __init__(self, image, pos, te_in, b_color, h_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.color1, self.color2 = b_color, h_color
        self.text = te_in
        self.font = pygame.font.SysFont('serif', 38)
        self.tex = self.font.render(self.text, True, self.color1)
        if self.image is None:
            self.image = self.tex

        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_inr = self.tex.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.tex, self.text_inr)

    def inside(self, pos):
        if pos[0] in range(self.rect.left, self.rect.right) and pos[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def butcolour(self, pos):
        if pos[0] in range(self.rect.left, self.rect.right) and pos[1] in range(self.rect.top, self.rect.bottom):
            self.tex = self.font.render(self.text, True, self.color2)
        else:
            self.tex = self.font.render(self.text, True, self.color1)


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


# fr = load_image("fr1.jpg", None)

lv = pygame.image.load("level1.jpg")
lv = pygame.transform.scale(lv, (600, 500))

# gr = pygame.image.load("data/Green.jpg")
# gr = pygame.transform.scale(gr, (600, 500))
walk = [
    pygame.image.load("data/fr1/frame_0.png"),
    pygame.image.load("data/fr1/frame_1.png"),
    pygame.image.load("data/fr1/frame_2.png"),
    pygame.image.load("data/fr1/frame_3.png"),
]




def level1():
    pygame.display.set_caption("Основной экран")
    clock = pygame.time.Clock()

    player_count = 0
    while True:
        screen.blit(lv, (0, 0))
        screen.blit(walk[player_count], (300, 250))
        # fon = pygame.transform.scale(load_image("playw.jpg"),
        #                              (screen.get_width(), screen.get_height()))
        # screen.blit(fon, (0, 0))
        # font = pygame.font.SysFont('arial', 48)
        if player_count == 3:
            player_count = 0
        else:
            player_count += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
        pygame.display.update()
        clock.tick(10)


def level2():
    pass


def play():
    pygame.display.set_caption("Основной экран")
    while True:
        screen.fill("black")
        fon = pygame.transform.scale(load_image("playw.jpg"),
                                     (screen.get_width(), screen.get_height()))
        screen.blit(fon, (0, 0))
        font = pygame.font.SysFont('arial', 48)
        font = font.render("Уровни", True, (255, 255, 255))
        st_t = font.get_rect(center=(300, 150))
        pos = pygame.mouse.get_pos()
        rules = Button(image=img2, pos=(300, 50), te_in="Rules"
                       , b_color=(255, 255, 255), h_color="#6495ED")
        exb = Button(image=None, pos=(500, 450), te_in="Back"
                     , b_color=(0, 0, 0), h_color="white")
        lev1 = Button(image=le1, pos=(150, 300), te_in="Level 1"
                      , b_color=(255, 255, 255), h_color="#6495ED")
        lev2 = Button(image=le1, pos=(450, 300), te_in="Level 2"
                      , b_color=(255, 255, 255), h_color="#6495ED")
        screen.blit(font, st_t)
        for button in [rules, exb, lev1, lev2]:
            button.butcolour(pos)
            button.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if rules.inside(pos):
                    rule()
                if exb.inside(pos):
                    start_screen(screen)
                if lev1.inside(pos):
                    level1()
                if lev2.inside(pos):
                    level2()
        pygame.display.update()


def rule():
    pass


def start_screen(screen):
    clock = pygame.time.Clock()
    intro_text = ["Утка в погоне за утятами"]
    # "Если в правилах несколько строк,",
    # "приходится выводить их построчно"]
    while True:
        fon = pygame.transform.scale(load_image("mainwind.jpg"),
                                     (screen.get_width(), screen.get_height()))
        screen.blit(fon, (0, 0))
        font = pygame.font.SysFont('arial', 48)
        font = font.render("Утка в погоне за утятами", True, (74, 144, 226))

        pos = pygame.mouse.get_pos()
        st_t = font.get_rect(center=(300, 100))
        playb = Button(image=img1, pos=(300, 200), te_in="Начать игру"
                       , b_color=(255, 255, 255), h_color="#f0d8a2")
        exb = Button(image=img1, pos=(300, 300), te_in="Выход"
                     , b_color=(255, 255, 255), h_color="#f1abad")
        screen.blit(font, st_t)
        for button in [playb, exb]:
            button.butcolour(pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if playb.inside(pos):
                    play()
                if exb.inside(pos):
                    terminate()
        pygame.display.update()
        clock.tick(FPS)


def terminate():
    pygame.quit()
    sys.exit()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


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

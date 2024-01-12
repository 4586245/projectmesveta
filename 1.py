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




def level1():
    pygame.display.set_caption("Основной экран")
    walk = [
        pygame.image.load("data/fr1/frame_0.png").convert_alpha(),
        pygame.image.load("data/fr1/frame_1.png").convert_alpha(),
        pygame.image.load("data/fr1/frame_2.png").convert_alpha(),
        pygame.image.load("data/fr1/frame_3.png").convert_alpha(),
    ]
    walk1 = []
    for i in walk:
        a = pygame.transform.scale(i, (140, 140))
        walk1.append(a)

    lv = pygame.image.load("data/level1.jpg").convert()
    lv = pygame.transform.scale(lv, (600, 500))

    gamep = True

    clock = pygame.time.Clock()
    bird = pygame.image.load("data/evel1.png").convert_alpha()
    bird = pygame.transform.scale(bird, (120, 120))
    bird_list = []
    bir_tim = pygame.USEREVENT + 1
    pygame.time.set_timer(bir_tim, 5000)

    player_count = 0
    lv_x = 0
    lv_sound = pygame.mixer.Sound("data/sound/music.mp3")
    lv_sound.play()
    tim = 0
    player_speed = 5
    player_x = 100
    player_y = 250

    pos = pygame.mouse.get_pos()

    font = pygame.font.SysFont("arial", 50)
    lose = font.render("You lose!", False, (193, 196, 199))
    rest = font.render("Restart", False, (115, 132, 148))
    rest_rect = rest.get_rect(topleft=(180, 250))

    i_jump = False
    junp_count = 11
    while True:
        screen.blit(lv, (lv_x, 0))
        screen.blit(lv, (lv_x + 600, 0))


        if gamep:
            player_rect = walk1[0].get_rect(topleft=(player_x, player_y))

            if bird_list:
                for (a, elem) in enumerate(bird_list):
                    screen.blit(bird, elem)
                    elem.x -= 10

                    if elem.x < - 10:
                        bird_list.pop(a)

                    if player_rect.colliderect(elem):
                        gamep = False

            screen.blit(walk[player_count], (player_x, player_y))
            # fon = pygame.transform.scale(load_image("playw.jpg"),
            #                              (screen.get_width(), screen.get_height()))
            # screen.blit(fon, (0, 0))
            # font = pygame.font.SysFont('arial', 48)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and player_x > 50:
                player_x -= player_speed
            elif keys[pygame.K_RIGHT] and player_x < 200:
                player_x += player_speed

            if not i_jump:
                if keys[pygame.K_SPACE]:
                    i_jump = True
            else:
                if junp_count >= -11:
                    if junp_count > 0:
                        player_y -= (junp_count ** 2) / 2
                    else:
                        player_y += (junp_count ** 2) / 2
                    junp_count -= 1
                else:
                    i_jump = False
                    junp_count = 11

            if player_count == 3:
                player_count = 0
            else:
                player_count += 1
            lv_x -= 5

            if lv_x == -600:
                lv_x = 0
        else:
            screen.fill((87, 88, 89))
            screen.blit(lose, (200, 100))
            screen.blit(rest, rest_rect)


            if rest_rect.collidepoint(pos) and pygame.mouse.get_pressed():
                gamep = True
                player_x = 100
                bird_list.clear()




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == bir_tim:
                bird_list.append(bird.get_rect(topleft=(620, 300)))


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

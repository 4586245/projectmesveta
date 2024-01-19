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


def print_tex(mes, x, y, font_color=(255, 255, 255), font_t="arial", font_si=30):
    font_t = pygame.font.SysFont(font_t, font_si)
    tex = font_t.render(mes, True, font_color)
    screen.blit(tex, (x, y))


def pause():
    clock = pygame.time.Clock()
    pause = True

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
        print_tex("Paused. Press enter to continue", 130, 170)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            pause = False
        pygame.display.update()
        clock.tick(15)


def level1():
    pygame.display.set_caption("Уровень 1")
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

    sn = pygame.image.load("data/snake.png").convert_alpha()
    sn = pygame.transform.scale(sn, (100, 100))
    sn_list = []
    sn_tim = pygame.USEREVENT + 1
    pygame.time.set_timer(sn_tim, 9000)

    wolf = pygame.image.load("data/wolf.png").convert_alpha()
    wolf = pygame.transform.scale(wolf, (130, 130))
    wolf_list = []
    wolf_tim = pygame.USEREVENT + 1
    pygame.time.set_timer(wolf_tim, 9000)

    frog = pygame.image.load("data/frog.png").convert_alpha()
    frog = pygame.transform.scale(frog, (60, 60))
    frog_list = []
    frog_tim = pygame.USEREVENT + 1
    f = []
    pygame.time.set_timer(frog_tim, 12000)

    player_count = 0
    lv_x = 0
    lv_sound = pygame.mixer.Sound("data/sound/music.mp3")
    lv_sound.play()
    player_speed = 5
    player_x = 100
    player_y = 250

    font = pygame.font.SysFont("arial", 50)
    lose = font.render("You lose!", False, (193, 196, 199))

    rest = font.render("Restart", False, (115, 132, 148))
    rest_rect = rest.get_rect(topleft=(220, 250))

    exb = Button(image=None, pos=(50, 20), te_in="Back"
                 , b_color=(0, 0, 0), h_color="white")

    pos = pygame.mouse.get_pos()

    scores = 0

    i_jump = False
    junp_count = 10

    run = True
    while run:
        screen.blit(lv, (lv_x, 0))
        screen.blit(lv, (lv_x + 600, 0))
        k = 0
        if gamep:
            player_rect = walk1[0].get_rect(topleft=(player_x, player_y))
            print_tex("scores:" + str(scores), 480, 10)
            exb.butcolour(pos)
            exb.update(screen)
            if frog_list:
                for (a, elem) in enumerate(frog_list):
                    screen.blit(frog, elem)
                    elem.x -= 10

                    if elem.x < - 20:
                        frog_list.pop(a)

                    if player_rect.colliderect(elem):
                        frog_list.pop(a)
                        scores += 1

            if bird_list:
                for (a, elem) in enumerate(bird_list):
                    screen.blit(bird, elem)
                    elem.x -= 10

                    if elem.x < - 20:
                        bird_list.pop(a)

                    if player_rect.colliderect(elem):
                        gamep = False

            if wolf_list:
                for (a, elem) in enumerate(wolf_list):
                    screen.blit(wolf, elem)
                    elem.x -= 10

                    if elem.x < - 20:
                        wolf_list.pop(a)

                    if player_rect.colliderect(elem):
                        gamep = False

            if sn_list:
                for (a, elem) in enumerate(sn_list):
                    screen.blit(sn, elem)
                    elem.x -= 10

                    if elem.x < - 20:
                        sn_list.pop(a)

                    if player_rect.colliderect(elem):
                        gamep = False

            screen.blit(walk1[player_count], (player_x, player_y))

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and player_x > 50:
                player_x -= player_speed
            elif keys[pygame.K_DOWN] and player_y < 300:
                player_y += player_speed
            elif keys[pygame.K_RIGHT] and player_x < 200:
                player_x += player_speed
            elif keys[pygame.K_UP] and player_y > 150:
                player_y -= player_speed
            if keys[pygame.K_ESCAPE]:
                pause()

            if not i_jump:
                if keys[pygame.K_SPACE]:
                    i_jump = True
            else:
                if junp_count >= -10:
                    if junp_count > 0:
                        player_y -= (junp_count ** 2) / 2
                    else:
                        player_y += (junp_count ** 2) / 2
                    junp_count -= 1
                else:
                    i_jump = False
                    junp_count = 10

            if player_count == 3:
                player_count = 0
            else:
                player_count += 1
            lv_x -= 10

            pos = pygame.mouse.get_pos()

            if lv_x == -600:
                lv_x = 0


        else:
            pos = pygame.mouse.get_pos()
            screen.fill((87, 88, 89))
            screen.blit(lose, (220, 100))
            screen.blit(rest, rest_rect)

            if rest_rect.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
                gamep = True
                player_x = 100
                player_y = 250
                i_jump = False
                bird_list.clear()
                scores = 0
                frog_list.clear()
                wolf_list.clear()
                sn_list.clear()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
                lv_sound.stop()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exb.inside(pos):
                    lv_sound.stop()
                    play()

            if event.type == wolf_tim:
                if k % 3 == 0:
                    wolf_list.append(wolf.get_rect(topleft=(500, random.randint(250, 350))))
                    k += 1
                elif k % 3 == 1:
                    wolf_list.append(wolf.get_rect(topleft=(1000, random.randint(250, 350))))
                    k += 1
                else:
                    wolf_list.append(wolf.get_rect(topleft=(1500, random.randint(250, 350))))
                    k += 1

            if event.type == bir_tim:
                if k % 3 == 0:
                    bird_list.append(bird.get_rect(topleft=(500, random.randint(250, 350))))
                    k += 1
                elif k % 3 == 1:
                    bird_list.append(bird.get_rect(topleft=(1000, random.randint(250, 350))))
                    k += 1
                else:
                    bird_list.append(bird.get_rect(topleft=(1500, random.randint(250, 350))))
                    k += 1

            if event.type == sn_tim:
                if k % 3 == 0:
                    sn_list.append(sn.get_rect(topleft=(500, random.randint(250, 350))))
                    k += 1
                elif k % 3 == 1:
                    sn_list.append(sn.get_rect(topleft=(1000, random.randint(250, 350))))
                    k += 1
                else:
                    sn_list.append(sn.get_rect(topleft=(1500, random.randint(250, 350))))
                    k += 1

            if event.type == frog_tim:
                frog_list.append(frog.get_rect(topleft=(2000, random.randint(300, 400))))

        pygame.display.update()
        clock.tick(10)


def level2():
    RUNNING = [pygame.image.load(os.path.join('data/fr1', 'frame_0.png')),
               pygame.image.load(os.path.join('data/fr1', 'frame_1.png')), ]

    jumping = pygame.image.load(os.path.join('data/fr1', 'frame_3.png'))

    bird = pygame.image.load("data/evel1.png").convert_alpha()
    bird = pygame.transform.scale(bird, (100, 100))

    sn = pygame.image.load("data/snake.png").convert_alpha()
    sn = pygame.transform.scale(sn, (100, 100))

    wolf = pygame.image.load("data/wolf.png").convert_alpha()
    wolf = pygame.transform.scale(wolf, (100, 100))

    frog = pygame.image.load("data/frog.png").convert_alpha()
    frog = pygame.transform.scale(frog, (60, 60))

    DIFFICULTY = [bird, sn, wolf]
    FROG = [frog]

    lv = pygame.image.load("data/level1.jpg").convert()
    lv = pygame.transform.scale(lv, (600, 500))

    class Duck:
        x_pos = 100
        y_pos = 230
        jump_speed = 20

        def __init__(self):
            self.run_img = RUNNING
            self.jump_img = jumping

            self.duck_run = True
            self.duck_jump = False

            self.step = 0
            self.jump_s = self.jump_speed
            self.image = self.run_img[0]
            self.duck_rect = self.image.get_rect()
            self.duck_rect.x = self.x_pos
            self.duck_rect.y = self.y_pos

        def update(self, user):
            if self.duck_run:
                self.run()
            if self.duck_jump:
                self.jump()

            if self.step >= 10:
                self.step = 0

            if user[pygame.K_UP] and not self.duck_jump:
                self.duck_run = False
                self.duck_jump = True
            elif not (self.duck_jump or user[pygame.K_DOWN]):
                self.duck_run = True
                self.duck_jump = False

        def run(self):
            self.image = self.run_img[self.step // 5]
            self.duck_rect = self.image.get_rect()
            self.duck_rect.x = self.x_pos
            self.duck_rect.y = self.y_pos
            self.step += 1

        def jump(self):
            self.image = self.jump_img
            if self.duck_jump:
                self.duck_rect.y -= self.jump_s * 1
                self.jump_s -= 0.8
            if self.jump_s < - self.jump_speed:
                self.duck_jump = False
                self.jump_s = self.jump_speed

        def draw(self, screen):
            screen.blit(self.image, self.duck_rect)

    class Obstacle(pygame.sprite.Sprite):
        def __init__(self, image, type):
            super().__init__()
            self.image = image
            self.type = type
            self.rect = self.image[self.type].get_rect()
            self.rect.x = 600

        def update(self):
            self.rect.x -= games
            if self.rect.x < -self.rect.width:
                difficulty.pop()

        def draw(self, screen):
            screen.blit(self.image[self.type], self.rect)

    class Difficult(Obstacle):
        def __init__(self, image):
            self.type = random.randint(0, 2)
            super().__init__(image, self.type)
            self.rect.y = 325

    class Frog(Obstacle):
        def __init__(self, image):
            self.type = 0
            super().__init__(image, self.type)
            self.rect.y = 325

    def main():
        global games, x_pos_lv, y_pos_lv, difficulty, points
        running = True
        games = 7
        x_pos_lv = 0
        y_pos_lv = 0
        difficulty = []
        points = 0
        death_count = 0
        clock = pygame.time.Clock()
        duck = Duck()

        def score():
            global points, games

            font = pygame.font.SysFont("arial", 50)
            text = font.render("Score: " + str(points), True, (0, 0, 0))
            textRect = text.get_rect()
            textRect.center = (480, 10)
            screen.blit(text, textRect)

        def background():
            global x_pos_lv, y_pos_lv
            image_width = lv.get_width()
            screen.blit(lv, (x_pos_lv, y_pos_lv))
            screen.blit(lv, (image_width + x_pos_lv, y_pos_lv))
            if x_pos_lv <= -image_width:
                screen.blit(lv, (image_width + x_pos_lv, y_pos_lv))
                x_pos_lv = 0
            x_pos_lv -= games

        exb = Button(image=None, pos=(50, 20), te_in="Back"
                     , b_color=(0, 0, 0), h_color="white")
        pos = pygame.mouse.get_pos()
        exb.butcolour(pos)
        exb.update(screen)

        pygame.display.flip()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if exb.inside(pos):
                        play()

            screen.fill((0, 0, 0))
            user = pygame.key.get_pressed()

            background()
            duck.draw(screen)
            duck.update(user)
            exb.butcolour(pos)
            exb.update(screen)
            score()

            if len(difficulty) == 0:
                if random.randint(0, 1) == 0:
                    difficulty.append(Difficult(DIFFICULTY))
                elif random.randint(0, 1) == 1:
                    difficulty.append(Frog(FROG))

            for i in difficulty:
                i.draw(screen)
                i.update()
                if duck.duck_rect.colliderect(i.rect):
                    if i.rect == frog:
                        points += 1
                    else:
                        pygame.time.delay(500)
                        screen.fill((255, 255, 255))

                        font = pygame.font.SysFont("arial", 50)
                        text = font.render("You lose!", True, (110, 210, 255))
                        textRect = text.get_rect()
                        textRect.center = (600 // 2, 100)
                        screen.blit(text, textRect)
                        screen.blit(RUNNING[0], (600 // 2 - 20, 500 // 2 - 140))
                        rest = Button(image=img2, pos=(300, 350), te_in="Restart"
                                      , b_color=(255, 255, 255), h_color="#6495ED")
                        pos = pygame.mouse.get_pos()
                        rest.butcolour(pos)
                        rest.update(screen)
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                running = False
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if rest.inside(pos):
                                    main()

            clock.tick(30)
            pygame.display.update()

    main()


def play():
    screen = pygame.display.set_mode((600, 500))
    pygame.display.set_caption("Главное меню")
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
    pygame.display.set_caption("Правила")
    screen1 = pygame.display.set_mode((800, 500))
    while True:
        fon = pygame.transform.scale(load_image("Green.jpg"),
                                     (1000, 1000))
        screen1.blit(fon, (0, 0))
        pos = pygame.mouse.get_pos()
        clock = pygame.time.Clock()

        font1 = pygame.font.SysFont('arial', 48)
        fontr = font1.render("Правила", True, (255, 255, 255))
        fontrr = fontr.get_rect(center=(400, 20))

        font2 = pygame.font.SysFont('arial', 28)
        fontr1 = font2.render("Ваша задача помочь маме утке прокормить своих утят", True, "#1E5945")
        fontrr1 = fontr1.get_rect(center=(400, 200))

        osnf = font2.render("По пути вам встретятся враги, которые будут мешать собирать еду", True, "#1E5945")
        fontrr2 = osnf.get_rect(center=(400, 230))

        osnf1 = font2.render("Не дайте монстрам вам помешать!", True, "#1E5945")
        fontrr3 = osnf1.get_rect(center=(400, 380))

        osnf2 = font2.render("Ваша главное преимущество в том, чьл вы очень высоко прыгаете", True, "#1E5945")
        fontrr4 = osnf1.get_rect(center=(230, 260))

        osnf3 = font2.render("Тебе нужно перепрыгивать монстров, чтобы избежать проигрыша", True, "#1E5945")
        fontrr5 = osnf1.get_rect(center=(230, 290))

        osnf4 = font2.render("В первом уровне перемешай утку стрелками 'вверх' и 'вниз' ", True, "#1E5945")
        fontrr6 = osnf1.get_rect(center=(230, 320))

        osnf5 = font2.render("Во втором уровне помогай утке подпрыгнуть стрелкой 'вверх'", True, "#1E5945")
        fontrr7 = osnf1.get_rect(center=(230, 350))

        exb = Button(image=None, pos=(700, 450), te_in="Back"
                     , b_color=(0, 0, 0), h_color="white")
        screen1.blit(fontr, fontrr)
        screen1.blit(fontr1, fontrr1)
        screen1.blit(osnf, fontrr2)
        screen1.blit(osnf1, fontrr3)
        screen1.blit(osnf2, fontrr4)
        screen1.blit(osnf3, fontrr5)
        screen1.blit(osnf4, fontrr6)
        screen1.blit(osnf5, fontrr7)

        exb.butcolour(pos)
        exb.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if exb.inside(pos):
                    play()
            pygame.display.update()
            clock.tick(FPS)


def start_screen(screen):
    clock = pygame.time.Clock()
    while True:
        fon = pygame.transform.scale(load_image("mainwind.jpg"),
                                     (screen.get_width(), screen.get_height()))
        screen.blit(fon, (0, 0))

        font = pygame.font.SysFont('arial', 48)
        font = font.render("Утка Сью", True, (74, 144, 226))

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
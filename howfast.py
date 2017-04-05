import time, pygame, random, sys

pygame.init()
GameDisplay = pygame.display.set_mode((1280, 920))
pygame.display.set_caption('F*CKING TYPE')  # title ba
clock = pygame.time.Clock()  # ========
center = (640, 420)
#=========COLOR==============
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 200, 0)
red = (200, 0, 0)
blue = (0, 0, 200)
yellow = (200, 200, 0)
purple = (150, 0, 200)

#===========================


# i = color out of range  / a = color in range
def botton(msg, x, y, w, h, fontsize, i, a, order=None):
    click = pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(GameDisplay, a, (x, y, w, h))
        if click[0] == 1 and order is not None:
            if order == "start":
                how_fast_a_to_z_mode()
            elif order == "quit":
                pygame.quit()
                quit()
            elif order == "mini_game":
                list_word = ["CAT", "ZZZ",
                             "JAZZ", "THUNDER"]
                mini_game(list_word)
            elif order == "rand_mode":
                prepare()

    else:
        pygame.draw.rect(GameDisplay, i, (x, y, w, h))
    sizetext = pygame.font.Font(
        "Baby Blocks.ttf", fontsize)
    textsurface, textrec = text_objects(msg, sizetext)
    textrec.center = (x + (w / 2), y + (h / 2))
    GameDisplay.blit(textsurface, textrec)


def text_objects(text, font, color=None):
    if not color:
        color = black
    textsurface = font.render(text, True, color)
    return textsurface, textsurface.get_rect()


def message_dis(text, size, position, color=None):
    if not color:
        color = black
    # parameter is family , font size
    sizetext = pygame.font.Font("Baby Blocks.ttf", size)
# www.WebpagePublicity.com/free-fonts/b/Baby Blocks.ttf
    textsurface, textrec = text_objects(text, sizetext, color)
    textrec.center = position
    GameDisplay.blit(textsurface, textrec)
    # pygame.display.update()


#=========Random AtoZ=====================================================
def random_a_to_z(keycap):
    last = len(keycap) - 1
    index_random = random.randrange(0, last)
    return index_random


def prepare():
    set_AtoZ = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", ""]
    keycap = [pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d, pygame.K_e, pygame.K_f, pygame.K_g, pygame.K_h, pygame.K_i, pygame.K_j, pygame.K_k, pygame.K_l, pygame.K_m,
              pygame.K_n, pygame.K_o, pygame.K_p, pygame.K_q, pygame.K_r, pygame.K_s, pygame.K_t, pygame.K_u, pygame.K_v, pygame.K_w, pygame.K_x, pygame.K_y, pygame.K_z, ""]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    time_start = time.time()
                    index_random = random_a_to_z(keycap)
                    random_a_to_z_mode(
                        set_AtoZ, keycap, index_random, time_start)
        GameDisplay.fill(green)
        message_dis("Press Space Bar To Start", 40,center, red)
        pygame.display.update()
        clock.tick(30)


def random_a_to_z_mode(set_AtoZ, keycap, index_random, time_start):
    while True:  # main game loop
        text = set_AtoZ[index_random]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    prepare()
                if len(set_AtoZ) == 2:
                    finish_time = time.time()
                    total_time = round((finish_time - time_start), 4)
                    while True:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                    prepare()
                            GameDisplay.fill(black)
                            botton(str(total_time), 270, 280, 540,
                                   360, 50, red, (255, 0, 50))
                            pygame.display.update()
                if event.key == keycap[index_random]:
                    set_AtoZ.pop(index_random)
                    keycap.pop(index_random)
                    new_index = random_a_to_z(keycap)
                    random_a_to_z_mode(set_AtoZ, keycap, new_index, time_start)
                else:
                    continue
        GameDisplay.fill(red)
        message_dis(text, 300, center, white)
        message_dis("PRESS SPACE BAR TO RESTART", 30, (640, 800), black)
        pygame.display.update()
        clock.tick(60)

#================how fast you can type====================================


def how_fast_a_to_z_mode():
    i = 0
    while True:  # main game loop
        if i == 0:
            time_start = time.time()
        set_AtoZ = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                    "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        keycap = [pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d, pygame.K_e, pygame.K_f, pygame.K_g, pygame.K_h, pygame.K_i, pygame.K_j, pygame.K_k, pygame.K_l, pygame.K_m,
                  pygame.K_n, pygame.K_o, pygame.K_p, pygame.K_q, pygame.K_r, pygame.K_s, pygame.K_t, pygame.K_u, pygame.K_v, pygame.K_w, pygame.K_x, pygame.K_y, pygame.K_z]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    how_fast_a_to_z_mode()
                if event.key == keycap[i]:
                    i += 1
                else:
                    continue
        if i == 26:
            finish_time = time.time()
            total_time = round((finish_time - time_start), 4)
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            how_fast_a_to_z_mode()
                    GameDisplay.fill(white)
                    botton(str(total_time), 470, 280, 540,
                           360, 70, red, (255, 0, 50))
                    pygame.display.update()
        text = set_AtoZ[i]
        GameDisplay.fill(red)
        message_dis(text, 300, center, white)
        message_dis("PRESS SPACE BAR TO RESTART", 30, (640, 800), black)
        pygame.display.update()
        clock.tick(90)
#===============================================


#=========Mini Game================================

def mini_game(list_word):
    perfect = pygame.mixer.Sound('ding.wav')
    bad = pygame.mixer.Sound('wrong.wav')  # too long, make it short than this
    time_count = 120 #time in seconds
    pygame.time.set_timer(pygame.USEREVENT+1, 1000)
    i = 0
    life = 3
    speed = 2
    score = 0
    word = ""
    word_check = ""
    show_input = ""
    x = 640
    y = 40
    set_AtoZ = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    keycap = [pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d, pygame.K_e, pygame.K_f, pygame.K_g, pygame.K_h, pygame.K_i, pygame.K_j, pygame.K_k, pygame.K_l, pygame.K_m,
              pygame.K_n, pygame.K_o, pygame.K_p, pygame.K_q, pygame.K_r, pygame.K_s, pygame.K_t, pygame.K_u, pygame.K_v, pygame.K_w, pygame.K_x, pygame.K_y, pygame.K_z, 13, pygame.K_SPACE , pygame.K_BACKSPACE]
    while True:
        GameDisplay.fill(black)
        botton("          ", 125, 600, 980, 130, 30, red, red)
        botton("1st", 1040, 50, 200, 70, 10, (0,255,0),(0,255,0))
        botton("2nd", 1040, 100, 200, 50, 10,  green,green)
        botton("3rd", 1040, 150, 200, 50, 10, (200,0,250), (200,0,250))
        botton("4th", 1040, 200, 200, 50, 10, purple, purple)
        botton("5th", 1040, 250, 200, 50, 10, red, red)
        message_dis(str(score), 20, (105, 55), white)
        message_dis(str(time_count), 30, (640, 850), white)
        message_dis(list_word[i], 100, (x, y), white)
        if word == "":
                for j in range(len(list_word[i])):
                    index = set_AtoZ.index(list_word[i][j])
                    if j == 0:
                        word += str(keycap[index])
                    else:
                        word += "." + str(keycap[index])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.USEREVENT+1:
                time_count -= 1
        
            if event.type == pygame.KEYDOWN and event.key in keycap:
                if event.key == pygame.K_BACKSPACE:
                    word_check = word_check.split(".")
                    del word_check[-1]
                    word_check = ".".join(word_check)
                    continue
                elif event.key == pygame.K_SPACE or event.key == 13:
                    if word == word_check and abs(680 - y) < 100:
                        if abs(680 - y) < 25:
                            color = purple
                            message_dis("PERFECT x 2", 50, (640, 300), purple)
                            bonus = 2
                        elif abs(680 - y) < 60:
                            color = blue
                            message_dis("GREAT x 1.5", 50, (640, 300), blue)
                            bonus = 1.5
                        else:
                            color = green
                            message_dis("GOOD x 1.5", 50, (640, 300), green)
                            bonus = 1
                        score += int(len(word.split(".")) * 1500 * bonus)
                        if word_check != "":
                            output = word_check.split(".")
                            for z in output:
                                z = int(z) - 97
                                show_input += set_AtoZ[z]
                            perfect.play()
                            show_input = ""
                        word = ""
                        word_check = ""
                        y = 0
                        i += 1
                        if i % 3 == 0:
                            speed += 1
                    else:
                        speed = 2
                        if word_check != "":
                            if abs(700 - y) < 200:
                                bonus = 1
                            else:
                                bonus = 0.5
                            score += int(len(word.split(".")) * 100)
                            output = word_check.split(".")
                            for z in output:
                                z = int(z) - 97
                                show_input += set_AtoZ[z]
                            message_dis("BAD", 50, (640, 300), white)
                            show_input = ""
                            bad.play()
                            time.sleep(0.3)
                        word = ""
                        word_check = ""
                        y = 0
                        i += 1
                else:
                    if word_check == "":
                        word_check += str(event.key)
                    else:
                        word_check += "." + str(event.key)

        if len(word_check) > 0:
            output = word_check.split(".")
            for z in output:
                z = int(z) - 97
                show_input += set_AtoZ[z]

        if y > 800:
            life -= 1
            x = 640
            y = 40
            i += 1

        if time_count == 0:
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            mini_game()
                GameDisplay.fill(black)
                message_dis("GAME OVER", 100, (640, 460), red)
                pygame.display.update()
        
        message_dis(show_input, 100, (640, 665), yellow)
        show_input = ""
        y += speed
        pygame.display.update()
        clock.tick(60)

#================================================


def game_intro():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        GameDisplay.fill(black)
        botton("HOW FAST YOU CAN TYPE", 850, 400, 400,
               70, 15, green, (0, 255, 0), "start")
        botton("RANDOM TYPE", 850, 470, 400, 70,
               30, green, (0, 255, 0), "rand_mode")
        botton("Mini Game", 850, 540, 400, 70, 20,
               green, (0, 255, 0), "mini_game")
        botton("QUIT", 950, 610, 200, 70, 20, red, (255, 0, 0), "quit")

        pygame.display.update()
        clock.tick(30)
game_intro()

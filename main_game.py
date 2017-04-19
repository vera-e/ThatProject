import time, pygame, random
from p import word_list
GameDisplay = pygame.display.set_mode((1280, 920))
clock = pygame.time.Clock()
center = (640, 420)
pause = True
#===========================
keyboard1 = pygame.image.load("1.png")
keyboard2 = pygame.image.load("2.png")
keyboard3 = pygame.image.load("3.png")
keyboard4 = pygame.image.load("4.png")
mt1 = pygame.image.load("meteor0001.png")
mt2 = pygame.image.load("meteor0002.png")
mt3 = pygame.image.load("meteor0003.png")
mt4 = pygame.image.load("meteor0004.png")
mt5 = pygame.image.load("meteor0005.png")
mt6 = pygame.image.load("meteor0006.png")
mt7 = pygame.image.load("meteor0007.png")
mt8 = pygame.image.load("meteor0008.png")
mt9 = pygame.image.load("meteor0009.png")
mt10 = pygame.image.load("meteor0010.png")
mt11 = pygame.image.load("meteor0011.png")
start = pygame.image.load("start_icon.png")
start_light  = pygame.image.load("start_icon_lighter.png")
exit_light = pygame.image.load("exit_icon_lighter.png")
exit = pygame.image.load("exit_icon.png")
highscore =  pygame.image.load("high_score_icon.png")
highscore_light = pygame.image.load("high_score_icon_lighter.png")
howto = pygame.image.load("how_icon .png")
howto_light = pygame.image.load("how_icon_lighter.png")
credit = pygame.image.load("credit_icon.png")
credit_light = pygame.image.load("credit_icon_lighter.png")
resume =  pygame.image.load("resume_button.png")
resume_light =  pygame.image.load("resume_button_lighter.png")
main_menu = pygame.image.load("main_manu_button.png")
main_menu_light = pygame.image.load("main_manu_button_lighter.png")
exitp = pygame.image.load("exit_button.png")
exitp_light = pygame.image.load("exit_button_lighter.png")
heart = pygame.image.load("Hearts_01_128x128_025.png")
#===========================
list_word = word_list()
#=========COLOR==============
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 200, 0)
red = (200, 0, 0)
blue = (0, 0, 200)
yellow = (200, 200, 0)
purple = (150, 0, 200)

#============helper function==========================
# i = color out of range  / a = color in range
def botton(msg, x, y, w, h, fontsize, i, a, order=None):
    global list_word
    click = pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(GameDisplay, a, (x, y, w, h))
        if click[0] == 1 and order is not None:

            if order == "start":
                how_fast_a_to_z_mode()
            if order == "quit":
                pygame.quit()
                quit()
            if order == "mini_game":
                mini_game_mode()
            if order == "high_score":
                high_score()
            # if order == "rand_mode":
            #     prepare()
            if order == "main_menu":
                game_intro()
            if order == "unpause":
                unpaused()
    else:
        pygame.draw.rect(GameDisplay, i, (x, y, w, h))
    sizetext = pygame.font.Font(
        "Baby Blocks.ttf", fontsize)
    textsurface, textrec = text_objects(msg, sizetext)
    textrec.center = (x + (w / 2), y + (h / 2))
    GameDisplay.blit(textsurface, textrec)


def botton_im(icon, icon_light, x, y, w, h, order=None, p=None):
    global list_word
    click = pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()
    if x + w + 30 > mouse[0] > x and y + h + 30 > mouse[1] > y:
        GameDisplay.blit(icon_light, (x - (w / 2), y - (h / 2)))
        # pygame.draw.rect(GameDisplay, a, (x, y, w, h))
        if click[0] == 1 and order is not None:
            if order == "quit":
                pygame.quit()
                quit()
            if order == "mini_game":
                mini_game_mode()
            if order == "high_score":
                high_score()
            # if order == "rand_mode":
            #     prepare()
            if order == "main_menu":
                game_intro()
            if order == "unpause":
                unpaused()
    else:
        if p:
            GameDisplay.blit(icon, (x - (w / 2), y - (h / 2)))
        else:
            GameDisplay.blit(icon, (x - (w / 2)+20, y - (h / 2)+20))
        # pygame.draw.rect(GameDisplay, i, (x, y, w, h))
    # sizetext = pygame.font.Font(
    #     "Baby Blocks.ttf", fontsize)
    # textsurface, textrec = text_objects(msg, sizetext)
    # textrec.center = (x + (w / 2), y + (h / 2))


def text_objects(text, font, color=None):
    if not color:
        color = black
    textsurface = font.render(text, True, color)
    return textsurface, textsurface.get_rect()


def message_dis(text, size, position, color=None, fontfam=None):
    if not color:
        color = black
    if not fontfam:
        fontfam = "Baby Blocks.ttf"
    # parameter is family , font size
    sizetext = pygame.font.Font(fontfam, size)
# www.WebpagePublicity.com/free-fonts/b/Baby Blocks.ttf
# www.WebpagePublicity.com/free-fonts/b/Billboard.ttf
    textsurface, textrec = text_objects(text, sizetext, color)
    textrec.center = position
    GameDisplay.blit(textsurface, textrec)


def unpaused():
    global pause
    pause = False
    return


def paused():
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        GameDisplay.fill(black)
        message_dis("PAUSE", 50, (645,200), white)
        # botton("RESUME", 440, 300, 400,100, 25, green, (0, 255, 0), "unpause")
        botton_im(resume_light, resume, 561, 320, 180, 60, "unpause", True)
        # botton("MIAN MENU", 440, 400, 400,100, 25, green, (0, 255, 0), "main_menu")
        botton_im(main_menu_light, main_menu, 561, 415, 180, 60, "main_menu", True)
        # botton("QUIT", 540, 500, 200,100, 25, red, (255, 0, 0), "quit")
        botton_im(exitp_light, exitp, 586, 510, 180, 60, "quit", True)
        pygame.display.update()
    return


def input_name():
    end = True
    ip_check = ""
    set_num = [i for i in "0123456789"]
    set_AtoZ = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    keycap = [pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d, pygame.K_e, pygame.K_f, pygame.K_g, pygame.K_h, pygame.K_i, pygame.K_j, pygame.K_k, pygame.K_l, pygame.K_m,
              pygame.K_n, pygame.K_o, pygame.K_p, pygame.K_q, pygame.K_r, pygame.K_s, pygame.K_t, pygame.K_u, pygame.K_v, pygame.K_w, pygame.K_x, pygame.K_y, pygame.K_z, 13 , pygame.K_BACKSPACE, pygame.K_ESCAPE, pygame.K_SPACE]
    keypad = [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9,
                        pygame.K_KP0, pygame.K_KP1, pygame.K_KP2, pygame.K_KP3, pygame.K_KP4, pygame.K_KP5,
                        pygame.K_KP6, pygame.K_KP7, pygame.K_KP8, pygame.K_KP9, 13, pygame.K_BACKSPACE, pygame.K_PERIOD , pygame.K_KP_PERIOD, pygame.K_ESCAPE ]
    while True:
        show_input = ""
        GameDisplay.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:                   
                if event.key == 13:
                        return name
            if event.type == pygame.KEYDOWN and (event.key in keypad or event.key in keycap) :
                if event.key == pygame.K_SPACE:
                    continue
                if event.key == pygame.K_ESCAPE:
                    game_intro()
                if event.key == pygame.K_BACKSPACE:
                    ip_check = ip_check.split(" ")
                    del ip_check[-1]
                    ip_check = " ".join(ip_check)
                    continue
                if event.key == pygame.K_PERIOD or event.key == pygame.K_KP_PERIOD:
                    ip_check +=" ." 
                else:
                    if len(ip_check.split(" ")) > 6:
                        continue
                    if ip_check == "":
                        ip_check += str(event.key)
                    else:
                        ip_check += " " + str(event.key)
                    continue
        if ip_check != "":
            output = ip_check.split(" ")
            try:
                for z in output:
                    if z == ".":
                        show_input += z
                    elif int(z) >= 97:
                        z = int(z) - 97
                        show_input += set_AtoZ[z]
                            
                    elif int(z) > 9:
                        z = keypad.index(int(z))
                        z =z-10
                        show_input += set_num[z]
            except:
                continue
        message_dis("New High Score", 70, (640, 200),white, "Billboard.ttf")
        message_dis("Submit your name", 70, (640, 400),white, "Billboard.ttf")
        message_dis(show_input, 50, (640, 465), yellow, "Billboard.ttf")
        if show_input != "":
            name = show_input
        pygame.display.update()
        clock.tick(30)


def high_score():
    file = open("high_score.txt", "r")
    file = file.read()
    score_list = []
    for i in file.split(";"):
        score_list += [i.split()]
    while True:
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_intro()
         GameDisplay.fill(black)
         message_dis(score_list[0][1], 70, (500, 155), white)
         message_dis(score_list[0][0], 70, (150, 155), white)
         message_dis(score_list[0][2], 70, (920, 155), white)
         message_dis(score_list[1][1], 70, (500, 255), white)
         message_dis(score_list[1][0], 70, (150, 255), white)
         message_dis(score_list[1][2], 70, (920, 255), white)
         message_dis(score_list[2][1], 70, (500, 355), white)
         message_dis(score_list[2][0], 70, (150, 355), white)
         message_dis(score_list[2][2], 70, (920, 355), white)
         message_dis(score_list[3][1], 70, (500, 455), white)
         message_dis(score_list[3][0], 70, (150, 455), white)
         message_dis(score_list[3][2], 70, (920, 455), white)
         message_dis(score_list[4][1], 70, (500, 555), white)
         message_dis(score_list[4][0], 70, (150, 555), white)
         message_dis(score_list[4][2], 70, (920, 555), white)
         pygame.display.update()

def write(score):
    file = open("high_score.txt", "r")
    data = file.read()
    data = data.split(";")
    score_list = []
    write = True
    for i in data:
        i = i.split()
        if score > int(i[2]) and write:
            name = input_name()
            new = [i[0], name, str(score)]
            score_list += [new]
            score_list += [[str(int(i[0])+1), i[1], i[2]]]
            write = False
        else:
            if write:
                score_list += [i]
            else:
                score_list += [[str(int(i[0])+1), i[1], i[2]]]
    score_data1 = " ".join(score_list[0])
    score_data2 = " ".join(score_list[1])
    score_data3 = " ".join(score_list[2])
    score_data4 = " ".join(score_list[3])
    score_data5 = " ".join(score_list[4])
    file = open("high_score.txt", "w")
    score_data = ";".join([score_data1, score_data2, score_data3, score_data4, score_data5])
    file.write(score_data)
    file.close()


def keyboard(m):
    # if m < 1:
    #     GameDisplay.blit(keyboard1, (0, 0))
    #     m += 0.4
    # elif m < 2:
    #     GameDisplay.blit(keyboard1, (0, 0))
    #     m += 0.4
    # elif m < 3:
    #     GameDisplay.blit(keyboard1, (0, 0))
    #     m += 0.4
    # elif m < 4:
    #     GameDisplay.blit(keyboard1, (0, 0))
    #     m += 0.4
    #     if m > 4:
    #         m = 0
    return m

def meteor(x, y, n):
    if n < 1:
        GameDisplay.blit(mt1, (x, y-140))
        n += 0.4
    elif n < 2:
        GameDisplay.blit(mt2, (x, y-140))
        n += 0.4
    elif n < 3:
        GameDisplay.blit(mt3, (x, y-140))
        n += 0.4
    elif n < 4:
        GameDisplay.blit(mt4, (x, y-140))
        n += 0.4
    elif n < 5:
        GameDisplay.blit(mt5, (x, y-140))
        n += 0.4
    elif n < 6:
        GameDisplay.blit(mt6, (x, y-140))
        n += 0.4
    elif n < 7:
        GameDisplay.blit(mt7, (x, y-140))
        n += 0.4
    elif n < 8:
        GameDisplay.blit(mt8, (x, y-140))
        n += 0.4
    elif n < 9:
        GameDisplay.blit(mt9, (x, y-140))
        n += 0.4
    elif n < 10:
        GameDisplay.blit(mt10, (x, y-140))
        n += 0.4
    elif n < 11:
        GameDisplay.blit(mt11, (x, y-140))
        n += 0.4
        if n > 11:
            n = 0
    return  n
#=========Mini Game================================

def mini_game_mode():
    #A mash up of some graphics from the Glitch assets by Tiny Speck.
    bg = pygame.image.load("Grid2.png")
    global pause, list_word
    perfect = pygame.mixer.Sound('ding.wav')
    bad = pygame.mixer.Sound('wrong.wav')  # too long, make it short than this
    time_count = 0 #time in seconds
    pygame.time.set_timer(pygame.USEREVENT+1, 1000)
    life = 5
    unpause = True
    score = 0
    speedmax = 3
    speedmin = 1
    speed1, speed2, speed3, speed4, speed5 = random.randrange(speedmin,speedmax), random.randrange(speedmin,speedmax), random.randrange(speedmin,speedmax), random.randrange(speedmin,speedmax), random.randrange(speedmin,speedmax)
    n1, n2, n3, n4, n5, m = 0, 0, 0, 0, 0, 0
    word1, word2, word3, word4, word5 = "", "", "", "", ""
    word_check = ""
    show_input = ""
    x1, x2, x3, x4, x5 = random.randrange(100,233), random.randrange(333,433), random.randrange(533,633), random.randrange(733,833), random.randrange(933,1100)
    y1, y2, y3, y4, y5 = 0, 0, 0, 0, 0
    set_AtoZ = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    keycap = [pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d, pygame.K_e, pygame.K_f, pygame.K_g, pygame.K_h, pygame.K_i, pygame.K_j, pygame.K_k, pygame.K_l, pygame.K_m,
              pygame.K_n, pygame.K_o, pygame.K_p, pygame.K_q, pygame.K_r, pygame.K_s, pygame.K_t, pygame.K_u, pygame.K_v, pygame.K_w, pygame.K_x, pygame.K_y, pygame.K_z, 13 , pygame.K_BACKSPACE, pygame.K_ESCAPE, pygame.K_SPACE]
    while True:
        if m <= 1:
            GameDisplay.blit(keyboard1, (0, 0))
        elif m <= 2:
            GameDisplay.blit(keyboard2, (0, 0))
        elif m <= 3:
            GameDisplay.blit(keyboard3, (0, 0))
        elif m <= 4:
            GameDisplay.blit(keyboard4, (0, 0))
            if m >= 4:
                m = 0
        # botton("            ", 125, 600, 980, 130, 30, red, red)
        GameDisplay.blit(heart, (45, 730))
        message_dis(" x "+str(life), 30, (155, 755), white)
        message_dis("score "+str(score), 40, (1055, 655), white)
        n1 = meteor(x1-50, y1, n1)
        n2 = meteor(x2-50, y2, n2)
        n3 = meteor(x3-50, y3, n3)
        n4 = meteor(x4-50, y4, n4)
        n5 = meteor(x5-50, y5, n5)
        if word1 == "":
            show_word1 = list_word.pop(0)
            i = 0
            for j in show_word1:
                index = set_AtoZ.index(j)
                if word1 == "":
                    word1 += str(keycap[index])
                    i = 1
                else:
                    word1 += "." + str(keycap[index])
        if word2 == "":
            i = 0
            show_word2 = list_word.pop(0)
            for j in show_word2:
                index = set_AtoZ.index(j)
                if word2 == "":
                    word2 += str(keycap[index])
                    i = 1
                else:
                    word2 += "." + str(keycap[index])
        if word3 == "":
            i = 0
            show_word3 = list_word.pop(0)
            for j in show_word3:
                index = set_AtoZ.index(j)
                if word3 == "":
                    word3 += str(keycap[index])
                    i = 1
                else:
                    word3 += "." + str(keycap[index])
        if word4 == "":
            show_word4 = list_word.pop(0)
            for j in show_word4:
                index = set_AtoZ.index(j)
                if word4 == "":
                    word4 += str(keycap[index])
                    i = 1
                else:
                    word4 += "." + str(keycap[index])
        if word5 == "":
            i = 0
            show_word5 = list_word.pop(0)
            for j in show_word5:
                index = set_AtoZ.index(j)
                if word5 == "" :
                    word5 += str(keycap[index])
                    i = 1
                else:
                    word5 += "." + str(keycap[index])
        message_dis(show_word1, 35, (x1, y1), white, "Billboard.ttf")
        message_dis(show_word2, 35, (x2, y2), white, "Billboard.ttf")
        message_dis(show_word3, 35, (x3, y3), white, "Billboard.ttf")
        message_dis(show_word4, 35, (x4, y4), white, "Billboard.ttf")
        message_dis(show_word5, 35, (x5, y5), white, "Billboard.ttf")
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.USEREVENT+1:
                time_count += 1
            if event.type == pygame.KEYDOWN and event.key in keycap:
                if len(word_check) > 60:
                    continue
                pygame.display.update() 
                m += 1
                if event.key == pygame.K_ESCAPE:
                    pause = True
                    paused()
                    continue
                if event.key == pygame.K_BACKSPACE:
                    word_check = word_check.split(".")
                    del word_check[-1]
                    word_check = ".".join(word_check)
                    continue
                elif event.key == pygame.K_SPACE or event.key == 13:
                    if (word1 == word_check or word2 == word_check or word3 == word_check or word4 == word_check or word5 == word_check):
                        if score % 50 == 0:
                            speedmax += 1
                        if score % 200 == 0:
                            speedmin += 1
                        score += 1
                        if word_check != "":
                            output = word_check.split(".")
                            for z in output:
                                z = int(z) - 97
                                show_input += set_AtoZ[z]
                            perfect.play()
                            show_input = ""
                        if word1 == word_check:
                            word1 = ""
                            y1 = 0
                            x1 = random.randrange(100,233)
                            speed1 = 0
                            speed1 = random.randrange(speedmin, speedmax)
                        elif word2 == word_check:
                            word2 = ""
                            y2 = 0
                            x2 = random.randrange(333,433)
                            speed2 = 0
                            speed2 = random.randrange(speedmin, speedmax)
                        elif word3 == word_check:
                            word3 = ""
                            y3 = 0
                            x3 = random.randrange(533,633)
                            speed3 = 0
                            speed3 = random.randrange(speedmin, speedmax)
                        elif word4 == word_check:
                            word4 = ""
                            y4 = 0
                            x4 = random.randrange(733,833)
                            speed4 = 0
                            speed4 = random.randrange(speedmin, speedmax)
                        elif word5 == word_check:
                            word5 = ""
                            y5 = 0
                            x5 = random.randrange(933,1100)
                            speed5 = 0
                            speed5 = random.randrange(speedmin, speedmax)
                        word_check = ""
                    else:
                        bad.play()
                        pygame.display.update()
                        word_check = ""
                else:
                    if word_check == "":
                        word_check += str(event.key)
                    else:
                        word_check += "." + str(event.key)

        if word_check != "":
            output = word_check.split(".")
            for z in output:
                z = int(z) - 97
                show_input += set_AtoZ[z]
        if y1 > 720:
            word1 = ""
            life -= 1
            x1 = random.randrange(100,233)
            y1 = 0
            speed1 = 0
            speed1 = random.randrange(speedmin, speedmax)
        if y2 > 650:
            word2 = ""
            life -= 1
            x2 = random.randrange(333,433)
            y2 = 0
            speed2 = 0
            speed2 = random.randrange(speedmin, speedmax)
        if y3 > 630:
            word3 = ""
            life -= 1
            x3 = random.randrange(533,633)
            y3 = 0
            speed3 = 0
            speed3 = random.randrange(speedmin, speedmax)
        if y4 > 650:
            word4 = ""
            life -= 1
            x4 = random.randrange(733,833)
            y4 = 0
            speed4 = 0
            speed4 = random.randrange(speedmin, speedmax)
        if y5 > 720:
            word5 = ""
            life -= 1
            x5 = random.randrange(933,1100)
            y5 = 0
            speed5 = 0
            speed5 = random.randrange(speedmin, speedmax)
        if life <1:
            check = 1
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.KEYDOWN:
                         if event.key == pygame.K_ESCAPE:
                            game_intro()
                         if event.key == pygame.K_SPACE:
                            mini_game_mode()
                GameDisplay.fill(black)
                output = "Game Over"
                message_dis(output, 100, (640, 360), red)
                message_dis("Your Score", 80, (640, 460))
                message_dis(str(score), 80, (640, 560), red)
                message_dis("Press 'SPACE' To Restart", 40, (640, 660), red)
                pygame.display.update()
                if check ==1 :
                    time.sleep(2)
                    write(score)
                    check = 2
        message_dis(show_input, 150, (640, 665), yellow, "Billboard.ttf")
        show_input = ""
        y1 += speed1*0.45
        y2 += speed2*0.45
        y3 += speed3*0.45
        y4 += speed4*0.45
        y5 += speed5*0.45
        pygame.display.update() 
        clock.tick(30)

#================================================

def game_intro():
    bg = pygame.image.load("mainmenu-1.jpg")
    pygame.init()
    pygame.display.set_caption("METEOTYPE")  # title ba
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        GameDisplay.blit(bg,(0,0))
        botton_im(start_light, start, 920, 245, 300, 250, "mini_game")
        botton_im(howto_light, howto, 930, 510, 300, 300, "howtoplay")
        botton_im(highscore_light, highscore, 120, 245, 200, 200, "high_score")
        botton_im(credit_light, credit, 105, 475, 200, 200, "credit")
        botton_im(exit_light, exit, 540, 750, 200, 200, "quit")
        pygame.display.update()
        clock.tick(30)
game_intro()

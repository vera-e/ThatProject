import time, pygame, random
from p import word_list
GameDisplay = pygame.display.set_mode((1280, 920))
clock = pygame.time.Clock()
center = (640, 420)
pause = True
#===========================
keyboard1 = pygame.image.load("Pics/BG_main/1.png")
keyboard2 = pygame.image.load("Pics/BG_main/2.png")
keyboard3 = pygame.image.load("Pics/BG_main/3.png")
keyboard4 = pygame.image.load("Pics/BG_main/4.png")
mt1 = pygame.image.load("Pics/Meteor/meteor0001.png")
mt2 = pygame.image.load("Pics/Meteor/meteor0002.png")
mt3 = pygame.image.load("Pics/Meteor/meteor0003.png")
mt4 = pygame.image.load("Pics/Meteor/meteor0004.png")
mt5 = pygame.image.load("Pics/Meteor/meteor0005.png")
mt6 = pygame.image.load("Pics/Meteor/meteor0006.png")
mt7 = pygame.image.load("Pics/Meteor/meteor0007.png")
mt8 = pygame.image.load("Pics/Meteor/meteor0008.png")
mt9 = pygame.image.load("Pics/Meteor/meteor0009.png")
mt10 = pygame.image.load("Pics/Meteor/meteor0010.png")
mt11 = pygame.image.load("Pics/Meteor/meteor0011.png")
start = pygame.image.load("Pics/Icon/start_icon.png")
start_light  = pygame.image.load("Pics/Icon/start_icon_lighter.png")
exit_light = pygame.image.load("Pics/Icon/exit_icon_lighter.png")
exit = pygame.image.load("Pics/Icon/exit_icon.png")
highscore =  pygame.image.load("Pics/Icon/high_score_icon.png")
highscore_light = pygame.image.load("Pics/Icon/high_score_icon_lighter.png")
howto = pygame.image.load("Pics/Icon/how_icon .png")
howto_light = pygame.image.load("Pics/Icon/how_icon_lighter.png")
credit = pygame.image.load("Pics/Icon/credit_icon.png")
credit_light = pygame.image.load("Pics/Icon/credit_icon_lighter.png")
resume =  pygame.image.load("Pics/Icon/resume_button.png")
resume_light =  pygame.image.load("Pics/Icon/resume_button_lighter.png")
main_menu = pygame.image.load("Pics/Icon/main_manu_button.png")
main_menu_light = pygame.image.load("Pics/Icon/main_manu_button_lighter.png")
exitp = pygame.image.load("Pics/Icon/exit_button.png")
exitp_light = pygame.image.load("Pics/Icon/exit_button_lighter.png")
heart = pygame.image.load("Pics/BG_main/Hearts_01_128x128_025.png")
damscreen = pygame.image.load("Pics/BG_main/red.png")
#========================
#=========COLOR==============
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 200, 0)
red = (200, 0, 0)
blue = (0, 0, 200)
yellow = (200, 200, 0)
purple = (150, 0, 200)

#============helper function==========================
def prepare():
     countdown = pygame.mixer.Sound('sounds/countdown.wav')
     m = 0
     life = 5
     score = 0
     time_count = 3 #time in seconds
     pygame.time.set_timer(pygame.USEREVENT+1, 1000)
     countdown.play()
     while time_count >=0:
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
        GameDisplay.blit(heart, (45, 780))
        message_dis(" x "+str(life), 30, (155, 805), white)
        message_dis("score "+str(score), 40, (1055, 655), white)
        message_dis(str(time_count), 300, center, white)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN  :
                if m < 4:
                    m += 1
                else:
                    m =0
            if event.type == pygame.USEREVENT+1:
                time_count -= 1
        pygame.display.update()

     return


def botton_im(icon, icon_light, x, y, w, h, order=None, p=None):
    click = pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()
    if p:
        x1 = x + w+ 70
        x2 = x - 80
        y1 = y + h
        y2 = y -30
    else:
        x1 = x + w +50
        x2 = x - 40
        y1 = y + h-30
        y2 = y - 40

    if (x1 > mouse[0] > x2) and (y1 > mouse[1] > y2)  :
        GameDisplay.blit(icon_light, (x - (w / 2), y - (h / 2)))
        if click[0] == 1 and order is not None:
            if order == "quit":
                pygame.quit()
                quit()
            if order == "mini_game":
                mini_game_mode()
            if order == "high_score":
                high_score()
            if order == "main_menu":
                game_intro()
            if order == "unpause":
                unpaused()
    else:
        if p:
            GameDisplay.blit(icon, (x - (w / 2), y - (h / 2)))
        else:
            GameDisplay.blit(icon, (x - (w / 2)+20, y - (h / 2)+20))



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
        botton_im(resume_light, resume, 561, 320, 180, 60, "unpause", True)
        botton_im(main_menu_light, main_menu, 561, 415, 180, 60, "main_menu", True)
        botton_im(exitp_light, exitp, 547, 510, 150, 60, "quit", True)
        pygame.display.update()
    return


def input_name():
    end = True
    name = ""
    ip_check = ""
    set_num = [i for i in "0123456789"]
    set_AtoZ = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    keycap = [pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d, pygame.K_e, pygame.K_f, pygame.K_g, pygame.K_h, pygame.K_i, pygame.K_j, pygame.K_k, pygame.K_l, pygame.K_m,
              pygame.K_n, pygame.K_o, pygame.K_p, pygame.K_q, pygame.K_r, pygame.K_s, pygame.K_t, pygame.K_u, pygame.K_v, pygame.K_w, pygame.K_x, pygame.K_y, pygame.K_z, 13 , pygame.K_BACKSPACE, pygame.K_ESCAPE, pygame.K_SPACE]
    while True:
        show_input = ""
        GameDisplay.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:                   
                if event.key == 13:
                    if name == "":
                        name = "USER"
                    return name
            if event.type == pygame.KEYDOWN and (event.key in keycap) :
                if event.key == pygame.K_SPACE:
                    continue
                if event.key == pygame.K_ESCAPE:
                    game_intro()
                if event.key == pygame.K_BACKSPACE:
                    ip_check = ip_check.split(" ")
                    del ip_check[-1]
                    ip_check = " ".join(ip_check)
                    continue

                if len(ip_check.split(" ")) > 5:
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
    list_word = word_list()
    #A mash up of some graphics from the Glitch assets by Tiny Speck.
    prepare()
    global pause
    perfect = pygame.mixer.Sound('sounds/ding.wav')
    perfect.set_volume(.2)
    bad = pygame.mixer.Sound('sounds/wrong.wav')  # too long, make it short than this
    bad.set_volume(.2)
    alarm = pygame.mixer.Sound('sounds/Alarm Siren.wav') # Audio Productions on youtube
    alarm.set_volume(.25)
    explode = pygame.mixer.Sound('sounds/Explosion Sound effect.wav')
    explode.set_volume(.2)
    speed_reduce = 0.60
    life = 5
    damage = False
    unpause = True
    score = 0
    speedmax = 3
    speedmin = 1
    speed1, speed2, speed3, speed4, speed5 = random.randrange(speedmin,speedmax), random.randrange(speedmin,speedmax), random.randrange(speedmin,speedmax), random.randrange(speedmin,speedmax), random.randrange(speedmin,speedmax)
    n1, n2, n3, n4, n5, m, l = 0, 0, 0, 0, 0, 0, 0
    word1, word2, word3, word4, word5 = "", "", "", "", ""
    word_check = ""
    show_input = ""
    x1, x2, x3, x4, x5 = random.randrange(150,233), random.randrange(353,483), random.randrange(583,683), random.randrange(803,883), random.randrange(983,1100)
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
        GameDisplay.blit(heart, (45, 780))
        message_dis(" x "+str(life), 30, (155, 805), white)
        message_dis("score "+str(score), 40, (1055, 655), white)
        n2 = meteor(x2-50, y2, n2)
        n3 = meteor(x3-50, y3, n3)
        n4 = meteor(x4-50, y4, n4)
        if score >= 30:           
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
            n1 = meteor(x1-50, y1, n1)
            message_dis(show_word1, 35, (x1, y1), white, "Billboard.ttf")
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
        if score >= 30:
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
            n5 = meteor(x5-50, y5, n5)
            message_dis(show_word5, 35, (x5, y5), white, "Billboard.ttf")
        message_dis(show_word2, 35, (x2, y2), white, "Billboard.ttf")
        message_dis(show_word3, 35, (x3, y3), white, "Billboard.ttf")
        message_dis(show_word4, 35, (x4, y4), white, "Billboard.ttf")
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if (event.type == pygame.KEYDOWN and event.key in keycap) :
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
                    if ((word1 == word_check and score >=30) or word2 == word_check or word3 == word_check or word4 == word_check or (word5 == word_check and score >=30)):
                        if score % 45 == 0:
                            speedmax += 1
                            if speed_reduce < 1:
                                speed_reduce += 0.05
                        if score % 100 == 0:
                            speedmin += 1
                        score += 1
                        if word_check != "":
                            output = word_check.split(".")
                            for z in output:
                                z = int(z) - 97
                                show_input += set_AtoZ[z]
                            perfect.play()
                            show_input = ""
                        if word1 == word_check :
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
                        elif word4 == word_check :
                            word4 = ""
                            y4 = 0
                            x4 = random.randrange(803,833)
                            speed4 = 0
                            speed4 = random.randrange(speedmin, speedmax)
                        elif word5 == word_check :
                            word5 = ""
                            y5 = 0
                            x5 = random.randrange(983,1100)
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
                if m < 4:
                    m += 1
                else:
                    m =0

        if word_check != "":
            output = word_check.split(".")
            for z in output:
                z = int(z) - 97
                show_input += set_AtoZ[z]
        if y1 > 530 or y2 > 480 or y3 > 460 or y4 > 480 or y5 > 480:
            alarm_check = True
        else:
            alarm_check = False
            a = True
        if alarm_check and a:
            alarm.play()
            a = False
        if a:
            alarm.fadeout(1)
            a = True
        if y1 > 700:
            damage = True
            word1 = ""
            life -= 1
            x1 = random.randrange(100,233)
            y1 = 0
            speed1 = 0
            speed1 = random.randrange(speedmin, speedmax)
        if y2 > 650:
            damage = True
            word2 = ""
            life -= 1
            x2 = random.randrange(333,433)
            y2 = 0
            speed2 = 0
            speed2 = random.randrange(speedmin, speedmax)
        if y3 > 630:
            damage = True
            word3 = ""
            life -= 1
            x3 = random.randrange(533,633)
            y3 = 0
            speed3 = 0
            speed3 = random.randrange(speedmin, speedmax)
        if y4 > 650:
            damage = True
            word4 = ""
            life -= 1
            x4 = random.randrange(803,883)
            y4 = 0
            speed4 = 0
            speed4 = random.randrange(speedmin, speedmax)
        if y5 > 700:
            damage = True
            word5 = ""
            life -= 1
            x5 = random.randrange(983,1100)
            y5 = 0
            speed5 = 0
            speed5 = random.randrange(speedmin, speedmax)
        if damage:
            explode.play()
            GameDisplay.blit(damscreen, (0,0))
            l += 1
            if l > 4:
                damage = False
                l = 0
        if life <1:
            explode.play()
            pygame.mixer.fadeout(1)
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
        if score >= 30:
            y1 += speed1*speed_reduce
        y2 += speed2*speed_reduce
        y3 += speed3*speed_reduce
        y4 += speed4*speed_reduce
        if score >= 30:
            y5 += speed5*speed_reduce
        pygame.display.update()
        clock.tick(30)

#================================================

def game_intro():
    bg = pygame.image.load("Pics/BG_intro/mainmenu-1.jpg")
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

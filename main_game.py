import time, pygame, random
from p import word_list
GameDisplay = pygame.display.set_mode((1080, 720))
clock = pygame.time.Clock()
center = (540, 360)
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
bg_highscore = pygame.image.load("Pics/BG_intro/bg_highscore.png")
siren = pygame.image.load("Pics/BG_main/siren.png")
siren_light = pygame.image.load("Pics/BG_main/sirenlight.png")
back1 = pygame.image.load("Pics/Icon/back1.png")
back2 = pygame.image.load("Pics/Icon/back2.png")
restart1 = pygame.image.load("Pics/Icon/restart.png")
restart2 = pygame.image.load("Pics/Icon/restart2.png")
pause1 = pygame.image.load("Pics/Icon/pause.png")
pause2 = pygame.image.load("Pics/Icon/pause2.png")
#========================
bgsound = False
bgsound_intro = False
first = True
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
     k = 1
     s = 0
     key_sound1 = pygame.mixer.Sound('sounds/t1.wav')
     key_sound1.set_volume(3)
     key_sound2 = pygame.mixer.Sound('sounds/t2.wav')
     key_sound2.set_volume(3)
     key_sound3 = pygame.mixer.Sound('sounds/enter.wav')
     key_sound3.set_volume(3)
     time_count = 3 #time in seconds
     pygame.time.set_timer(pygame.USEREVENT+1, 1000)
     countdown.play()
     t = 40
     while time_count >=0:
        if t < 255:
            t += 12
            keyboard1.set_alpha(t)
            GameDisplay.blit(keyboard1,(0,0))
            pygame.time.delay(100)
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
        GameDisplay.blit(siren, (235, 455)) 
        GameDisplay.blit(siren, (760, 455))   
        GameDisplay.blit(heart, (15, 30))
        message_dis("X "+str(life), 20, (105, 50), white)
        message_dis(str(score), 40, (1005, 55), white)
        message_dis(str(time_count), 200,  (540, 300), white)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN  :
                if m < 4:
                    m += 1
                else:
                    m =0
                if k == 1:
                    key_sound1.play()
                    k = 2
                elif k == 2:
                    key_sound2.play()
                    k = 1
                if s == 0:
                    GameDisplay.blit(siren_light, (235,455))
                    GameDisplay.blit(siren_light, (760,455))
                    s = 1
                elif s == 1:
                    GameDisplay.blit(siren, (235, 455)) 
                    GameDisplay.blit(siren, (760, 455))   
                    s = 0  
                if event.key == pygame.K_SPACE or event.key == 13:
                    key_sound3.play()
            if event.type == pygame.USEREVENT+1:
                time_count -= 1
        pygame.display.update()


def botton_im(icon, icon_light, x, y, w, h, order=None, p=None):
    global pause
    click = pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()
    click_sound = pygame.mixer.Sound('sounds/click_sound.wav')
    click_sound.set_volume(.5)
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
            click_sound.play()
            if order == "quit":
                pygame.quit()
                quit()
            if order== "pause":
                pause = True
                paused()
            if order == "howtoplay":
                how_to_play()
            if order == "back":
                game_intro()
            if order == "mini_game":
                mini_game_mode()
            if order == "high_score":
                high_score()
            if order == "main_menu":
                game_intro()
            if order == "unpause":
                unpaused()
            if order == "credit":
                credit_()
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
        fontfam = "fonts/Baby Blocks.ttf"
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
        message_dis("PAUSE", 50, (545,130), white)
        botton_im(resume_light, resume, 513, 250, 180, 60, "unpause", True)
        botton_im(main_menu_light, main_menu, 513, 317, 180, 60, "main_menu", True)
        botton_im(exitp_light, exitp, 498, 384, 150, 60, "quit", True)
        pygame.display.update()
    return



def input_name(score):
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
        message_dis("NEW HIGH SCORE", 70, (540, 150),white, "fonts/Billboard.ttf")
        message_dis(str(score), 70, (530, 250),white, "fonts/Billboard.ttf")
        message_dis("SUBMIT YOUR NAME", 70, (540, 350),white, "fonts/Billboard.ttf")
        message_dis(show_input, 50, (540, 475), yellow, "fonts/Billboard.ttf")
        if show_input != "":
            message_dis("PRESS ENTER TO SUBMIT", 30, (540, 530),white, "fonts/Billboard.ttf")
            name = show_input
        pygame.display.update()
        clock.tick(30)


def high_score():
    file = open("high_score.txt", "r")
    file = file.read()
    score_list = []
    show = bg_highscore
    t = 40
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
         if t < 255:
            t += 10
            show.set_alpha(t)
            GameDisplay.blit(show,(0,0))
            pygame.time.delay(100)
         GameDisplay.blit(show, (0,0))
         back()
         message_dis(score_list[0][1], 60, (500, 155), white)
         message_dis(score_list[0][0], 60, (150, 155), white)
         message_dis(score_list[0][2], 60, (920, 155), white)
         message_dis(score_list[1][1], 60, (500, 245), white)
         message_dis(score_list[1][0], 60, (150, 245), white)
         message_dis(score_list[1][2], 60, (920, 245), white)
         message_dis(score_list[2][1], 60, (500, 345), white)
         message_dis(score_list[2][0], 60, (150, 345), white)
         message_dis(score_list[2][2], 60, (920, 345), white)
         message_dis(score_list[3][1], 60, (500, 445), white)
         message_dis(score_list[3][0], 60, (150, 445), white)
         message_dis(score_list[3][2], 60, (920, 445), white)
         message_dis(score_list[4][1], 60, (500, 545), white)
         message_dis(score_list[4][0], 60, (150, 545), white)
         message_dis(score_list[4][2], 60, (920, 545), white)
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
            name = input_name(score)
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

def credit_():
    t = 40
    show = pygame.image.load("Pics/BG_intro/credit.jpg")  # title ba
    while True:
        click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_intro()
        if t < 255:
            t += 15
            show.set_alpha(t)
            GameDisplay.blit(show,(0,0))
            pygame.time.delay(100)
        GameDisplay.blit(show, (0,0))
        back()
        pygame.display.update()
        clock.tick(30)


def how_to_play():
    t = 40
    show = pygame.image.load("Pics/BG_intro/howtoplay.jpg").convert()  # title ba
    while True:
        click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_intro()
        if t < 255:
            t += 15
            show.set_alpha(t)
            GameDisplay.blit(show,(0,0))
            pygame.time.delay(100)
        GameDisplay.blit(show, (0,0))
        back()
        pygame.display.update()
        clock.tick(30)



def back():
     botton_im(back1, back2, 990, 650, 100, 80, "back", True)
#=========Mini Game================================

def mini_game_mode():
    list_word = word_list()
    #A mash up of some graphics from the Glitch assets by Tiny Speck.
    global pause, bgsound, bgsound_intro
    if bgsound_intro:
        bgsound_intro.fadeout(500)
        bgsound_intro = False
    bgsound = pygame.mixer.Sound('sounds/soundbg.wav')
    bgsound.set_volume(.2)
    perfect = pygame.mixer.Sound('sounds/ding.wav')
    perfect.set_volume(.5)
    bad = pygame.mixer.Sound('sounds/wrong.wav')  # too long, make it short than this
    bad.set_volume(.3)
    alarm = pygame.mixer.Sound('sounds/Alarm Siren.wav') # Audio Productions on youtube
    alarm.set_volume(.5)
    explode = pygame.mixer.Sound('sounds/Explosion Sound effect.wav')
    explode.set_volume(.5)
    key_sound1 = pygame.mixer.Sound('sounds/t1.wav')
    key_sound1.set_volume(4)
    key_sound2 = pygame.mixer.Sound('sounds/t2.wav')
    key_sound2.set_volume(4)
    key_sound3 = pygame.mixer.Sound('sounds/enter.wav')
    key_sound3.set_volume(4)
    prepare()
    speed_reduce = 0.60
    life = 5
    damage = False
    unpause = True
    bgsound_check = True
    score = 0
    speedmax = 3
    speedmin = 1
    speed1, speed2, speed3, speed4, speed5 = random.randrange(speedmin,speedmax), random.randrange(speedmin,speedmax), random.randrange(speedmin,speedmax), random.randrange(speedmin,speedmax), random.randrange(speedmin,speedmax)
    n1, n2, n3, n4, n5, m, s, l, k, i = 0, 0, 0, 0, 0, 0, 0, 0, 1, 0
    word1, word2, word3, word4, word5 = "", "", "", "", ""
    word_check = ""
    show_input = ""
    x1, x2, x3, x4, x5 = random.randrange(83,183), random.randrange(283,383), random.randrange(483,583), random.randrange(683,783), random.randrange(883,983)
    y1, y2, y3, y4, y5 = 0, 0, 0, 0, 0
    set_AtoZ = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    keycap = [pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d, pygame.K_e, pygame.K_f, pygame.K_g, pygame.K_h, pygame.K_i, pygame.K_j, pygame.K_k, pygame.K_l, pygame.K_m,
              pygame.K_n, pygame.K_o, pygame.K_p, pygame.K_q, pygame.K_r, pygame.K_s, pygame.K_t, pygame.K_u, pygame.K_v, pygame.K_w, pygame.K_x, pygame.K_y, pygame.K_z, 13 , pygame.K_BACKSPACE, pygame.K_ESCAPE, pygame.K_SPACE]
    while True:
        if list_word  == []:
            list_word = word_list()
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
        if y1 > 490 or y2 > 460 or y3 > 440 or y4 > 460 or y5 > 490:
            alarm_check = True
            if s == 0:
                GameDisplay.blit(siren_light, (235,455))
                GameDisplay.blit(siren_light, (760, 455))
                s = 1
            elif s == 1:
                GameDisplay.blit(siren, (235, 455)) 
                GameDisplay.blit(siren, (760,455))   
                s = 0  
        else:
            GameDisplay.blit(siren, (235, 455))
            GameDisplay.blit(siren, (760, 455))   
            alarm_check = False
            a = True
        GameDisplay.blit(heart, (15, 30))
        message_dis("X "+str(life), 20, (105, 50), white)
        message_dis(str(score), 40, (1005, 55), white)
        n2 = meteor(x2-50, y2, n2)
        n3 = meteor(x3-50, y3, n3)
        n4 = meteor(x4-50, y4, n4)
        if bgsound_check:
            bgsound.play(loops=-1)
            bgsound_check = False
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
            message_dis(show_word1, 30, (x1, y1), white, "fonts//theboldfont.ttf")
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
            message_dis(show_word5, 30, (x5, y5), white, "fonts/theboldfont.ttf")
        message_dis(show_word2, 30, (x2, y2), white,  "fonts/theboldfont.ttf")
        message_dis(show_word3, 30, (x3, y3), white, "fonts/theboldfont.ttf") 
        message_dis(show_word4, 30, (x4, y4), white,  "fonts/theboldfont.ttf")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if (event.type == pygame.KEYDOWN and event.key in keycap) :
                if k == 1:
                    key_sound1.play()
                    k = 2
                elif k == 2:
                    key_sound2.play()
                    k = 1
                if m < 4:
                    m += 1
                else:
                    m =0
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
                    key_sound3.play()
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
                            x1 = random.randrange(83,183)
                            speed1 = 0
                            speed1 = random.randrange(speedmin, speedmax)
                        elif word2 == word_check:
                            word2 = ""
                            y2 = 0
                            x2 = random.randrange(283,383)
                            speed2 = 0
                            speed2 = random.randrange(speedmin, speedmax)
                        elif word3 == word_check:
                            word3 = ""
                            y3 = 0
                            x3 = random.randrange(483,583)
                            speed3 = 0
                            speed3 = random.randrange(speedmin, speedmax)
                        elif word4 == word_check :
                            word4 = ""
                            y4 = 0
                            x4 = random.randrange(683,783)
                            speed4 = 0
                            speed4 = random.randrange(speedmin, speedmax)
                        elif word5 == word_check :
                            word5 = ""
                            y5 = 0
                            x5 = random.randrange(883, 983)
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

        if alarm_check and a:
            alarm.play()
            a = False
        if a:
            alarm.fadeout(500)
            a = True
        if y1 > 650:
            damage = True
            word1 = ""
            life -= 1
            x1 = random.randrange(83,183)
            y1 = 0
            speed1 = 0
            speed1 = random.randrange(speedmin, speedmax)
        if y2 > 590:
            damage = True
            word2 = ""
            life -= 1
            x2 = random.randrange(283,383)
            y2 = 0
            speed2 = 0
            speed2 = random.randrange(speedmin, speedmax)
        if y3 > 560:
            damage = True
            word3 = ""
            life -= 1
            x3 = random.randrange(483,583)
            y3 = 0
            speed3 = 0
            speed3 = random.randrange(speedmin, speedmax)
        if y4 > 590:
            damage = True
            word4 = ""
            life -= 1
            x4 = random.randrange(683,783)
            y4 = 0
            speed4 = 0
            speed4 = random.randrange(speedmin, speedmax)
        if y5 > 650:
            damage = True
            word5 = ""
            life -= 1
            x5 = random.randrange(883,983)
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
            pygame.mixer.fadeout(1000)
            gameover = pygame.mixer.Sound('sounds/gameover_sound.wav')
            time.sleep(1.2)
            gameover.set_volume(5)
            gameover.play()
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
                back()
                output = "GAME OVER"
                botton_im(restart2, restart1, 990, 560, 100, 80, "mini_game", True)
                message_dis(output, 80, (540, 150), red, "fonts/Scary Halloween Font.ttf")
                message_dis("Your Score", 80, (540, 300), red, "fonts/Scary Halloween Font.ttf")
                message_dis(str(score), 80, (540, 460), red, "fonts/Scary Halloween Font.ttf")
                pygame.display.update()
                if check ==1 :
                    time.sleep(2)
                    write(score)
                    check = 2
        message_dis(show_input, 75, (540, 540), yellow,  "fonts/theboldfont.ttf")
        botton_im(pause1, pause2, 1020, 630, 100, 80, "pause", True)
        show_input = ""
        if score >= 30:
            y1 += speed1*0.35
        y2 += speed2*0.35
        y3 += speed3*0.35
        y4 += speed4*0.35
        if score >= 30:
            y5 += speed5*0.5
        pygame.display.update()
        clock.tick(30)

#================================================

def game_intro():
    global bgsound, bgsound_intro, first
    story_list = False
    if not bgsound and first:
        story_list = []
        for i in range(1, 5):
            if i == 1:
                j = 3
            if i == 2:
                j = 3
            if i == 3:
                j = 2
            if i == 4:
                j = 2
            for x in range(1, j+1):
                story_list += [pygame.image.load("Pics/BG_intro/Story/"+str(i)+"/"+str(i)+"-"+str(x)+".png").convert()]
        first = False
    else:
        story = False
    if not bgsound_intro:
        bgsound_intro = pygame.mixer.Sound('sounds/intro.wav')
        bgsound_intro.set_volume(.2)
        bgsound_intro.play(loops=-1)
    first_scene = True
    break_loop = True
    last = False
    if story_list:
        while break_loop:
            t = 40
            if not bgsound:
                try:
                    if first_scene:
                        story = story_list.pop(0)
                        first_scene = False
                    else:
                        story = story_list.pop(0)
                except:
                    last = True
            while t < 255:
                t += 17
                story.set_alpha(t)
                GameDisplay.blit(story, (0,0))
                pygame.time.delay(100)
                pygame.display.update()
            GameDisplay.blit(story, (0,0))
            if last:
                break_loop = False
            pygame.display.update()
    bg = pygame.image.load("Pics/BG_intro/mainmenu-1.jpg").convert()
    i = 40
    while True:
        if i < 100:
            i += 4
            pygame.time.delay(100)
            bg.set_alpha(i)
        for event in pygame.event.get():
            if bgsound:
                pygame.mixer.fadeout(1500)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        GameDisplay.blit(bg,(0,0))
        botton_im(start_light, start, 840, 245, 300, 250, "mini_game")
        botton_im(howto_light, howto, 830, 490, 300, 300, "howtoplay")
        botton_im(highscore_light, highscore, 120, 245, 200, 200, "high_score")
        botton_im(credit_light, credit, 105, 445, 200, 200, "credit")
        botton_im(exit_light, exit, 500, 590, 100, 100, "quit")
        pygame.display.update()
        clock.tick(30)
pygame.init()
pygame.display.set_caption("METEORTYPE")  # title ba
game_intro()

import pygame, time, random
from main_game import mini_game_mode, random_a_to_z_mode, how_fast_a_to_z_mode
# pygame.init()
# pygame.display.set_caption('F*CKING TYPE')
GameDisplay = pygame.display.set_mode((1280, 920))
center = (640, 420)
#=========COLOR==============
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 200, 0)
red = (200, 0, 0)
blue = (0, 0, 200)
yellow = (200, 200, 0)
purple = (150, 0, 200)

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
                mini_game_mode(list_word)
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

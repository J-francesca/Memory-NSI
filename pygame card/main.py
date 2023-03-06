import pygame

pygame.init()


BACK_CARD_IMG = pygame.image.load("back.png")
FRONT_CARD_IMG = pygame.image.load("front.png")

CARD_WIDTH = FRONT_CARD_IMG.get_width()
CARD_HEIGHT = FRONT_CARD_IMG.get_height()


SCREEN_WIDTH = CARD_WIDTH + 20
SCREEN_HEIGHT = CARD_HEIGHT + 20
SPEED = 7
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

BG_IMAGE = pygame.transform.smoothscale(pygame.image.load("bg.png"),(SCREEN_WIDTH,SCREEN_HEIGHT))

clock = pygame.time.Clock()

current_width = CARD_WIDTH
go_on = True
decrease = True

show_img = FRONT_CARD_IMG
while go_on:
    screen.blit(BG_IMAGE,(0,0))
    go_on = all(event.type != pygame.QUIT for event in pygame.event.get())
    if decrease:

        current_width -= SPEED
        if current_width <= 2:
            current_width = 2
            decrease = False
            if show_img == FRONT_CARD_IMG:
                show_img = BACK_CARD_IMG
            else:
                show_img = FRONT_CARD_IMG
        image = pygame.transform.smoothscale(show_img, (current_width, CARD_HEIGHT))
    else:
        current_width += SPEED
        if current_width > CARD_WIDTH:
            current_width = CARD_WIDTH
            decrease = True
        image = pygame.transform.smoothscale(show_img, (current_width, CARD_HEIGHT))
    screen.blit(image, ((SCREEN_WIDTH - current_width) // 2, 5))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()

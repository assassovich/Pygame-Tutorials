import pygame
pygame.init()

win = pygame.display.set_mode((500,480))

pygame.display.set_caption("First Game")
path = r'H:/python/pygame/tutorrials/Pygame-Tutorials/Game/'
walkRight = [pygame.image.load(path + f'R{i}.png') for i in range(1, 10)]
walkLeft = [pygame.image.load(path + f'L{i}.png') for i in range(1, 10)]

bg = pygame.image.load(path + 'bg.jpg')
char = pygame.image.load(path + 'standing.png')

clock = pygame.time.Clock()

x, y = 50, 400
width, height = 64, 64
vel, jumpCount, walkCount = 5, 10, 0
isJump, left, right = False, False, False


def redrawGameWindow():
    global walkCount
    win.blit(bg, (0,0))

    if walkCount + 1 >= 27: walkCount = 0

    if left:
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount +=1
    else:
        win.blit(char, (x,y))
    
    pygame.display.update()


#mainloop
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left, right = True, False
    elif keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel
        right, left = True, False
    else:
        right, left, walkCount = False, False, 0
        
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump, right, left, walkCount = True, False, False, 0
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0: neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump, jumpCount = False, 10
            
    redrawGameWindow()

pygame.quit()



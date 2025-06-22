import pygame
import time
import random

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((500,500))

score = 0

font = pygame.font.SysFont("Calibri", 35, False)

class Slider(pygame.sprite.Sprite):
    def __init__(self,x):
        super().__init__()
        self.x = x
        self.speed = 10
        self.image = pygame.image.load("C:/Pygame2/images/alienship.png")
        self.rect = self.image.get_rect()
    def draw(self):
        screen.blit(self.image,(self.x,410))
    def right(self):
        self.x = self.x + self.speed
    def left(self):
        self.x = self.x - self.speed

 
class astronauts(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load("C:/Pygame2/images/astronaut.png")
        self.rect = self.image.get_rect()
    def draw(self):
        screen.blit(self.image,(self.x,500))
    def update(self):
        self.rect.y = self.rect.y + 10

        


slider = Slider(0)
run = True

astronautgroup = pygame.sprite.Group()

for i in range(20):
    astronaut = astronauts(0,0)
    astronaut.rect.x = random.randint(0,500)
    astronaut.rect.y = 0
    
    astronautgroup.add(astronaut)


bg = pygame.image.load("C:/Pygame2/images/spacebg3.png")

while run:
    screen.blit(bg,(0,0))
    clock.tick(60)
    

    txt = font.render("Score:  "+str(score), True, "white")
    screen.blit(txt,(0,0))
    
    
    
    astronautgroup.update()
    pygame.display.update()
        
    astronautgroup.draw(screen)

    for astronaut in astronautgroup:
        if astronaut.rect.colliderect(slider.rect):
            astronautgroup.remove(astronaut)
            score = score + 1

        
    key  = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        slider.left()
        pygame.display.update()
    if key[pygame.K_RIGHT]:
        slider.right()
        pygame.display.update()


    slider.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        

    pygame.display.update()
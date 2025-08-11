
import pygame
import time
import random
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((1000,700))
pygame.display.set_caption('Spac Vadré')
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
img1=pygame.image.load("vaderb2.png")
img2=pygame.image.load("vaderb2.png")
img3=pygame.image.load("vaderc1.png")
img=pygame.image.load("space.png")
img4=pygame.image.load('bullet.png')
##img = pygame.transform.scale(img,(100,100))
##img4=pygame.image.load('bullet.png')
##img4 = pygame.transform.scale(img4,(10,35))
##img5=pygame.image.load('shoot.png')
##img5 = pygame.transform.scale(img5,(10,35))

class Character:
    def __init__(self,x,y,w,h,img):
        self.x= x
        self.y =y
        self.w=w
        self.h=h
        self.image=img
    def draw (self):
        pygame.draw.circle(screen,(255,0,255), (self.x, self.y), 20)
        #self.image = pygame.transform.scale(self.image,(self.w,self.h))
        #screen.blit(self.image,(self.x,self.y))
                    
class Alien(Character):
    def __init__(self,x,y,w,h,img, level):
        super().__init__(x,y,w,h,img)
        self.min = self.x-5
        self.max = self.x+45
        self.speed  = random.randint(1,3)
        self.level = level
        
    def move(self):
        self.x += self.speed
        if self.x < self.min:
            self.speed = random.randint(1,3)
        if self.x >self.max:
            self.speed = - random.randint(1,3)
##        if movex == 'right':
##            self.x += 1
##        if movex == 'left':
##            self.x -= 1
##    def movedown(self,movey,row):
##        #print(self.y,movey,row-self.row)
##        self.y = movey * (row-self.row)

    def moverow(self,movex, movey):
        if movex == 'right':
            self.x += 1
        if movex == 'left':
            self.x -= 1
        self.y = movey + self.level


class Bullet(Character):
    def __init__(self,x,y,w,h,img):
        super().__init__(x,y,w,h,img)
        self.m='up'

    def move(self):
        self.y -= 3

class Player(Character):
    def __init__(self,x,y,w,h,img):
        super().__init__(x,y,w,h,img)
        self.speed = 0
        

    def move(self):
        self.x += self.speed 
    
step =1        
        
        
##class player:
##    def __init__(self,img):
##        self.x=500
##        self.y=600
##        self.img=img
##        self.movex = 0
##    def draw(self):
##        screen.blit(self.img,(self.x,self.y))
##    def move(self):
##        self.x += self.movex
##        
##class bullet:
##    def __init__(self, x,y,img, m):
##        self.x= x
##        self.y= y
##        self.img=img
##        self.m =m
##    def draw(self):
##        screen.blit(self.img,(self.x+43,self.y))
##    def move(self):
##        if self.m == 'up':
##            self.y -= 1
##        if self.m == 'down':
##            self.y += 1
invader=[]

bullet_list=[]
row =2

space = Player(500, 620, 75,75,img)

for i in range(10):
    for j in range(5):
        invader.append(Alien(100*i+50,10+j*50,60,60,img1,j*50))

##    invader2.append(invaders(i,80,img2))
##    invader3.append(invaders(i,140,img3))

##shoot1=random.choice(invader1)
##shoot2=random.choice(invader2)
##shoot3=random.choice(invader3)
     
signal =0
movey=50

##movex1=movex2=movex3='left'
##movey1=20
##movey2=80
##movey3=140
##space=player(img)

clock = pygame.time.Clock()
start = time.time()

movex='left'
movey=10
while True:
    pygame.time.wait(10)
    pygame.display.update()
    screen.fill(black)

    space.move()
    space.draw()
    

    for i in invader:
        i.moverow(movex, movey)
        i.draw()
        if i.x <0:
            movey += 20
            movex='right'

        if i.x >1000:
            movey += 20
            movex='left'

##    space.move()
##    space.draw()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type==KEYDOWN:
            if event.key==K_LEFT:
                space.speed = -1
            if event.key==K_RIGHT:
                space.speed = 1
            if event.key==K_SPACE:
                bullet_list.append(Bullet(space.x+32,570,10,50,img4))
        if event.type==KEYUP:
            if event.key==K_LEFT:
                space.speed = 0
            if event.key==K_RIGHT:
                space.speed = 0
    
    second = time.time() -start
    #print(second, start)       
##    if second > 3:
##        movey = 50
##        row +=1
##        step +=.8
##        print(step,movey,step*movey)
##        start = time.time()
##        for i in range(0,1000,100):
##            invader1.append(Alien(i,0,60,60,img3,row))
##        

 
            
        
        
##    for x in invader:
## 
##        x.move()
##      
##        x.movedown(movey,step)
##        x.draw()
##
##        if random.randint(1,3000)==1:
##            bullet_list.append(bullet(x.x-20,x.y+40,pygame.transform.flip(img4,False,True),'down'))
##        
##        #x.draw()
        
            
    

        
    for b in bullet_list:
        if b.m=='down' and b.x in range(space.x-50,space.x+50) and b.y in range(space.y,space.y+50):
            print('collision')
        
        if b.m=='down' and b.y <0:
            bullet_list.remove(b)
        b.move()
        b.draw()
        for a in invader:
            if b.m=='up' and b.x in range(a.x,a.x+20) and b.y in range(a.y,a.y+50):
                if b in bullet_list:
                    bullet_list.remove(b)
                if a in invader:
                    invader.remove(a)
##        for a in invader2:
##            if b.m=='up' and b.x in range(a.x-20,a.x+20) and b.y in range(a.y,a.y+50):
##                if b in bullet_list:
##                    bullet_list.remove(b)
##                if a in invader2:
##                    invader2.remove(a)
##        for a in invader3:
##            if b.m=='up' and b.x in range(a.x-20,a.x+20) and b.y in range(a.y,a.y+50):
##                if b in bullet_list:
##                    bullet_list.remove(b)
##                if a in invader3:
##                    invader3.remove(a)
##
##



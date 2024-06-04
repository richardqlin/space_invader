import pygame
import time
pygame.init()
screen=pygame.display.set_mode((900,700))
pygame.display.set_caption('space invaders')
Ship1=pygame.image.load('Ship.png')
Alien1=pygame.image.load('Alien1.png')
Alien2=pygame.image.load('Alien2.png')
Alien3=pygame.image.load('Alien3.png')
Bullets=pygame.image.load('Bullet.png')
class Character:
    def __init__(self,x,y,image,height,width):
        self.x=x
        self.y=y
        self.image=image
        self.height=height
        self.width=width
class Alien(Character):
    def __init__(self,x,y,image,height,width,level):
        super().__init__(x,y,image,height,width)
        self.x=x
        self.y=y
        self.image=pygame.transform.scale(Alien1,(self.width,self.height))
        self.height=height
        self.width=width
        self.level=level
        self.direction = 1
        self.count = 0
    def draw(self):
        screen.blit(self.image,(self.x,self.y))
    def move_alien(self,movex,movey):
        if movex=='right':
            self.x=self.x+1
        if movex=='left':
            self.x=self.x-1
        self.y=movey+self.level
    def move_update(self):
        self.x += self.direction
        self.count += 1
        if abs(self.count) > 75:
            self.direction *= -1
            self.count *= self.direction
            self.y += 20
class PlayerShip(Character):
    def __init__(self,x,y,image,height,width):
        super().__init__(x,y,image,height,width)
        self.x=x
        self.y=y
        self.image=pygame.transform.scale(Ship1,(self.width,self.height))
        self.height=height
        self.width=width
        self.speed=0
    def draw(self):
        screen.blit(self.image,(self.x,self.y))
    def move_ship(self):
        self.x=self.x+self.speed
class Bullet(Character):
    def __init__(self,x,y,image,height,width):
        super().__init__(x,y,image,height,width)
        self.x=x
        self.y=y
        self.image=pygame.transform.scale(Bullets,(self.width,self.height))
        self.height=height
        self.width=width
    def draw(self):
        screen.blit(self.image,(self.x,self.y))
    def bullet_move(self):
        self.y=self.y-5
class SuperAlien(Character):
    def __init__(self,x,y,image,height,width):
        super().__init__(x,y,image,height,width)
        self.x=x
        self.y=y
        self.image=pygame.transform.scale(Alien2,(self.width,self.height))
        self.height=height
        self.width=width
        self.speed=1
        self.count=3
    def draw(self):
        screen.blit(self.image,(self.x,self.y))
    def move_alien(self):
        self.x=self.x+self.speed
        if self.x>=900:
            self.y=self.y+50
            self.speed=-self.speed
        if self.x<=0:
            self.y=self.y+50
            self.speed=-self.speed
class ShooterAlien(SuperAlien):
    def __init__(self,x,y,image,height,width):
        super().__init__(x,y,image,height,width)
        self.x=x
        self.y=y
        self.image=pygame.transform.scale(Alien3,(self.width,self.height))
        self.height=height
        self.width=width
        self.count = 0
        self.direction = 1
        
 
    def draw(self):
        screen.blit(self.image,(self.x,self.y))
    def move_update(self):
        self.x += self.direction
        self.count += 1
        if abs(self.count) > 225:
            self.direction *= -1
            self.count *= self.direction
            self.y += 20
        
SuperAlienList=[]   
Alienlist=[]
bulletlist=[]
Alienlist2=[]
for j in range(0,10,1):
    for w in range(0,5,1):
        alien2=ShooterAlien(j*85+50,w*55+35,Alien,45,45)
        Alienlist2.append(alien2)
for n in range(0,10,1):
    for b in range(0,5,1):
        alien=Alien(n*85+50,b*55+30,Alien2,45,45,b*55)
        Alienlist.append(alien)
ship=PlayerShip(440,610,Ship1,70,70)
movex='left'
movey=15
level=1
levels=1
count=0
star=time.time()
while True:
    screen.fill((0,0,0))
    ship.draw()
    ship.move_ship()
    for s in Alienlist:
        s.draw()
        s.move_update()
##        s.move_alien(movex,movey)
##        if s.x<0:
##            movey=movey+15
##            movex='right'
##        if s.x>900:
##            movey=movey+15
##            movex='left'
    for a in Alienlist:
          for b in bulletlist:
            if b.x in range(a.x,a.x+a.width) and b.y in range(a.y-a.height,a.y):
                if a in Alienlist:
                    Alienlist.remove(a)
                if b in bulletlist:
                    bulletlist.remove(b)
            if b.y<0:
                bulletlist.remove(b)
    for l in SuperAlienList:
        for k in bulletlist:
            if k.x in range(l.x,l.x+l.width) and k.y in range(l.y-l.height,l.y):
                l.count=l.count-1
            if l.count<=0:
                if l in SuperAlienList:
                    SuperAlienList.remove(l)
                if k in bulletlist:
                    bulletlist.remove(k)
            if k.y<0:
                if k in bulletlist:
                    bulletlist.remove(k)
    for b in bulletlist:
        b.draw()
        b.bullet_move()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                ship.speed=1
            if event.key==pygame.K_LEFT:
                ship.speed=-1
            if event.key==pygame.K_SPACE:
                bullet=Bullet(ship.x-45,ship.y,Bullets,90,100)
                bullet2=Bullet(ship.x+15,ship.y,Bullets,90,100)
                bulletlist.append(bullet)
                bulletlist.append(bullet2)               
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT:
                ship.speed=0
            if event.key==pygame.K_LEFT:
                ship.speed=0
    for l in Alienlist:
        if ship.x in range(l.x,l.x+l.width) and ship.y in range(l.y-l.height,l.y):
            print('Game Over')
            exit
            break
    if len(Alienlist)==0 and level==1:
        level=2
    if level==2:
        if time.time()-star>3:
            Superalien=SuperAlien(0,0,Alien1,100,100)
            SuperAlienList.append(Superalien)
            count=count+1
            star=time.time()
        for o in SuperAlienList:
            o.draw()
            o.move_alien()
        if count==2:
            level=3
            for j in range(0,3,1):
                for w in range(0,5,1):
                    alien2=Alien(j*85+30,w*55-35,Alien,45,45,w*55)
                    Alienlist.append(alien2)
            
        for e in SuperAlienList:
            for g in bulletlist:
                if g.x in range(g.x,g.x+g.width) and g.y in range(g.y-g.height,g.y):
                    if e in Alienlist:
                        SuperAlienList.remove(e)
                    if g in bulletlist:
                        bulletlist.remove(g)

          
    if level==3:
        screen.fill((0,0,0))
        movey=15
        movex='right'
        
        for lo in Alienlist2:
            lo.draw()
            lo.move_update()
            #print(movex, movey)
##            if lo.x<0:
##                
##                movey+=15
##                movex='right'
##            elif lo.x>900:
##                movey+=15
##                movex='left'
##        for ye in Bullet:
##            ye.draw()
##            ye.bullet_move()
##            bullet=Bullet(alien2.x-45,alien2.y,Bullets,90,100)            
        for ae in Alienlist2:  
            for be in bulletlist:
                if be.x in range(ae.x,ae.x+ae.width) and be.y in range(ae.y-ae.height,ae.y):
                    if ae in Alienlist:
                        Alienlist2.remove(ae)
                    if be in bulletlist:
                        bulletlist.remove(be)
                if be.y<0:
                    bulletlist.remove(be)
        pygame.display.update()   
    pygame.display.update()





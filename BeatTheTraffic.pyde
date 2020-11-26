add_library('minim')
import random, os

path = os.getcwd()
musicplayer = Minim(this)

WIDTH = 720
HEIGHT = 720
objcnt = 0
score = 0
W = 70 #car's width
H = 140 #car's height
XL = 150
XR = 570
backgroundmusicplaying = False
highscores = []
LANEWIDTH = 140
DIVIDERWIDTH = 5

class Car:
    def __init__(self,x,y,img):
        self.x = x
        self.y = y
        self.img = loadImage(path+ "/image/" + img)


class Player(Car):
    def __init__(self,x,y,img):
        Car.__init__(self, x,y,img)
        self.crash = False
        self.key_handler = {LEFT:False,RIGHT:False}

class Game:
    def __init__(self):
        global backgroundmusicplaying
        
        self.speed = 0
        self.player = Player(0,0,"car1.png")
        self.bg_music = musicplayer.loadFile(path+"/sound/background.mp3")
        if backgroundmusicplaying == False:
            self.bg_music.loop()
            backgroundmusicplaying = True

    def display(self):
        if self.player.crash == True:
            textSize(15)
            text("GAME OVER", 600, 350)
            return
            
        global highscores
        leftimg = loadImage(path+"/image/left.png")
        image(leftimg,0,0,LANEWIDTH,HEIGHT)
        rightimg = loadImage(path+"/image/right.png")
        image(rightimg,580,0,LANEWIDTH,HEIGHT)
        
        scoredisplay = "Score: "+str(score)            
        highscoredisplay = "High Score: \n"+ "     "+str(max(highscores))
        fill(255,255,0)
        textSize(HEIGHT/25)
        text(scoredisplay,(XR+12),(HEIGHT/20))
        textSize(HEIGHT/30)
        text(highscoredisplay,(12),(HEIGHT/20))
        
        fill (255,255,255)
        rect(LANEWIDTH,0,DIVIDERWIDTH,HEIGHT)
        rect((LANEWIDTH+DIVIDERWIDTH+LANEWIDTH),0,DIVIDERWIDTH,HEIGHT)
        rect((LANEWIDTH+DIVIDERWIDTH+LANEWIDTH+DIVIDERWIDTH+LANEWIDTH),0,DIVIDERWIDTH,HEIGHT)
        rect((LANEWIDTH+DIVIDERWIDTH+LANEWIDTH+DIVIDERWIDTH+LANEWIDTH+DIVIDERWIDTH+LANEWIDTH),0,DIVIDERWIDTH,HEIGHT)


game = Game()



def setup():
    global highscores
    size(WIDTH,HEIGHT)
    fileread = open('highscores.txt','r')
    for line in fileread:
        highscores.append(int(line.strip())) 
    
def draw():
    if frameCount %(max(1, int(8 - game.speed)))==0 or frameCount==1:
        background(0)
        game.display()
        
def keyPressed():
    if keyCode == LEFT:
        game.player.key_handler[LEFT] = True
    elif keyCode == RIGHT:
        game.player.key_handler[RIGHT] = True
            
def keyReleased():
    if keyCode == LEFT:
        game.player.key_handler[LEFT] = False
    elif keyCode == RIGHT:
        game.player.key_handler[RIGHT] = False
        
def mouseClicked():
    global game, score, objcnt, highscores
    if game.player.crash == True: #reseting and starting the game again
        highscores.append(score)
        writeobj = open('highscores.txt','w')
        s = ''
        for i in highscores:
            s += str(i)+"\n"
        writeobj.write(s)
        score = 0
        objcnt = 0
        game = Game()

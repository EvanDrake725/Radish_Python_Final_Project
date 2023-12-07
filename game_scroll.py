# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 09:33:18 2023

@author: evand
audio made in BeepBox
"""

import pygame, simpleGE

class StartScreen(simpleGE.SuperSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("EndScreen.png")
        self.setSize(640, 480)
        self.x=640
        self.y=480
        self.hide()
        
class Player(simpleGE.SuperSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.images = {
            "idol": pygame.image.load("Player_Radish_f.png"),
            "left": pygame.image.load("Player_Radish_l.png"),
            "right": pygame.image.load("Player_Radish_r.png"),
            "up": pygame.image.load("Player_Radish_b.png")}
        self.imageMaster = self.images["idol"]
        self.x=320
        self.y=240
        self.moveSpeedxa=5
        self.moveSpeedxb=5
        self.moveSpeedya=5
        self.moveSpeedyb=5
        self.something=0
        self.phone=0
        self.salt=0
        self.tasks=0
        
    def checkEvents(self):
        self.imageMaster = self.images["idol"]  
        if self.scene.isKeyPressed(pygame.K_LEFT):
            self.x-=self.moveSpeedxa
            if self.x<=10:
                self.moveSpeedxa=0
            else:
                self.moveSpeedxa=5
            self.imageMaster = self.images["left"]
                
        if self.scene.isKeyPressed(pygame.K_RIGHT):
            self.x+=self.moveSpeedxb
            if self.x>=630:
                self.moveSpeedxb=0
            else:
                self.moveSpeedxb=5
            self.imageMaster = self.images["right"]
                
        if self.scene.isKeyPressed(pygame.K_UP):
            self.y-=self.moveSpeedya
            if self.y<=10:
                self.moveSpeedya=0
            else:
                self.moveSpeedya=5
            self.imageMaster = self.images["up"]
                
        if self.scene.isKeyPressed(pygame.K_DOWN):
            self.y+=self.moveSpeedyb
            if self.y>=470:
                self.scene.moveSpeedyb=0
            else:
                self.moveSpeedyb=5
            self.imageMaster = self.images["idol"]  
        elif self.tileState == 5:
            self.something=5
        elif self.tileState == 7:
            self.something=7
        elif self.tileState == 8:
            self.something=8
            if self.salt==1:
                self.tasks=1
        elif self.tileState == 10:
            self.something=10
        elif self.tileState==6:
            self.phone+=1
        elif self.tileState==9:
            self.salt+=1
        else:
            self.something=0

class Tile(simpleGE.BasicSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.images = [
            pygame.image.load("Grass-1.png.png"),
            pygame.image.load("Grass-2.png.png"),
            pygame.image.load("Grass-3.png.png"),
            pygame.image.load("Dirt-6.png.png"),
            pygame.image.load("empty.png"),
            pygame.image.load("Goth_Radish.png"),
            pygame.image.load("Skibity.png"),
            pygame.image.load("Carrot.png"),
            pygame.image.load("Snail.png"),
            pygame.image.load("Salt.png"),
            pygame.image.load("Turnip.png")]
        
        self.setSize(32, 32)
        self.GRASS = 0
        self.YELLOWFLOWER = 1
        self.REDFLOWER = 2
        self.DIRT=3
        self.EMPTY=4
        self.GOTH=5
        self.PHONE=6
        self.CARROT=7
        self.SNAIL=8
        self.SALT=9
        self.TURNIP=10

        self.state = self.GRASS
        
    def setState(self, state):
        self.state = state
        self.image = self.images[state]

    def checkEvents(self):

        if self.collidesWith(self.scene.player):

            self.scene.player.tileOver = self.tilePos
            self.scene.player.tileState = self.state
            if self.scene.player.phone==1:
                if self.state==6:
                    newState=self.GRASS
                    self.setState(newState)
                    self.scene.player.tileState=self.setState
            if self.scene.player.salt==1:
                if self.state==9:
                    newState=self.GRASS
                    self.setState(newState)
                    self.scene.player.tileState=self.setState
             
class Intro (simpleGE.MultiLabel):
    def __init__(self):
        super().__init__()
        self.textLines = [
            "It seems my firends stole the keys to my house!",
            "Why would they do that? Who knows?",
            "I should ask around and try to get them back!"]
        self.fgColor = "black"
        self.bgColor = "aqua"
        self.center = ((320, 240))
        self.size = ((500, 200))

class Carrotcomment (simpleGE.MultiLabel):
    def __init__(self):
        super().__init__()
        self.textLines= ["Carrot:",
                         "I dont know about Turnip",
                         "Have you tried the snails?",
                         "They may still work for him."]
        self.size = ((345, 125))
        self.fgColor = "black"
        self.bgColor = "aqua"
        self.hide()
        
class PhoneQuest (simpleGE.MultiLabel):
    def __init__(self):
        super().__init__()
        self.textLines= ["Woman Radish:",
                         "Can you find my phone?"]
        self.size = ((320, 70))
        self.fgColor = "black"
        self.bgColor = "aqua"
        self.hide()
        
class PhoneQuestDone (simpleGE.MultiLabel):
    def __init__(self):
        super().__init__()
        self.textLines= ["Woman Radish:",
                         "Thank you!",
                         "Carrot Might be able to help you."]
        self.size = ((345, 100))
        self.fgColor = "black"
        self.bgColor = "aqua"
        self.hide()
        
class MainQuest (simpleGE.MultiLabel):
    def __init__(self):
        super().__init__()
        self.textLines= ["Wild Turnip:",
                         "I STOLE YOUR KEYS!!",
                         "I WONT TELL YOU HOW TO GET THEM"]
        self.size = ((400, 100))
        self.fgColor = "black"
        self.bgColor = "aqua"
        self.hide()
        
class MainQuestDone (simpleGE.MultiLabel):
    def __init__(self):
        super().__init__()
        self.textLines= ["Wild Turnip:",
                         "YOU HAVE PEROGIS!?",
                         "FINE YOU CAN HAVE YOUR KEYS BACK!",
                         "BUT ILL HAVE MY VENGANCE ONE DAY!"]
        self.size = ((400, 165))
        self.fgColor = "black"
        self.bgColor = "aqua"
        self.hide()
        
class SaltQuest (simpleGE.MultiLabel):
    def __init__(self):
        super().__init__()
        self.textLines= ["Snail:",
                         "Oh Ol Turnip?",
                         "We can help you get your keys if you can get us something",
                         "Apparently salt tastes really good"
                         , "Can you get us some?"]
        self.size = ((575, 165))
        self.fgColor = "black"
        self.bgColor = "aqua"
        self.hide()
        
class SaltQuestDone (simpleGE.MultiLabel):
    def __init__(self):
        super().__init__()
        self.textLines= ["Snail:",
                         "Thanks, hopefully the salt tastes good!",
                         "Heres some perogis",
                         "Boss loves them."]
        self.size = ((375, 125))
        self.fgColor = "black"
        self.bgColor = "aqua"
        self.hide()
        
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setCaption("RAD RADISH")

        self.tileset = []
        
        self.ROWS = 20
        self.COLS = 40
        
        self.SCREEN_ROWS = 15
        self.SCREEN_COLS = 20
        
        self.offRow = 0
        self.offCol = 0
        self.startScreen=StartScreen(self)
        self.player=Player(self)
        self.intro=Intro()
        self.phoneQuest=PhoneQuest()
        self.phonequestDone=PhoneQuestDone()
        self.mainQuest=MainQuest()
        self.mainquestDone=MainQuestDone()
        self.saltQuest=SaltQuest()
        self.saltquestDone=SaltQuestDone()
        self.carrotComment=Carrotcomment()
        self.playable=True
        self.coolSong = simpleGE.Sound("Cool_Song.wav")
        self.timer = simpleGE.Timer()
        self.loadMap()
        self.sprites = [self.tileset,self.player, self.phoneQuest,
                        self.phonequestDone, self.mainQuest, self.mainquestDone,
                        self.saltQuest, self.saltquestDone, self.carrotComment, self.intro
                        , self.startScreen]
    def endScreen(self):
        self.startScreen.show()
        self.startScreen.x=320
        self.startScreen.y=240
    
    def startText(self):
        self.intro
        self.playable=False
    
    def phoneNpc(self):
        self.phoneQuest.show((320, 200)) 
        self.playable=False

    def phoneDone(self):
        self.phonequestDone.show((320, 200))
        self.playable=False
        
    def mainNpc(self):
        self.mainQuest.show((320, 200)) 
        self.playable=False

    def mainDone(self):
        self.mainquestDone.show((320, 200))
        self.playable=False
        
    def saltNpc(self):
        self.saltQuest.show((320, 200)) 
        self.playable=False

    def saltDone(self):
        self.saltquestDone.show((320, 200))
        self.playable=False
        
    def carrotTalk(self):
        self.carrotComment.show((320,200))
        self.playable=False
    
    def playGame(self):
            self.intro.hide()
            self.phoneQuest.hide()
            self.phonequestDone.hide()
            self.mainQuest.hide()
            self.mainquestDone.hide()
            self.saltQuest.hide()
            self.saltquestDone.hide()
            self.carrotComment.hide()
            self.playable=True

    def loadMap(self):
        
      self.map = [
          
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,0,0],  
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,7,3,0,0],  
          [0,0,10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,0,0],  
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0],  
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0],  
          [0,0,0,0,0,0,0,0,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0],  
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,0,0],  
          [0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,0],  
          [0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,3],  
          [0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  
          [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  
          [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  
          [0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,0,0,0,0,0,0,0],  
          [0,0,0,0,0,0,0,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

      ]
    
      for row in range(self.SCREEN_ROWS):
          self.tileset.append([])
          for col in range(self.SCREEN_COLS):
            currentVal = self.map[row][col]
            newTile = Tile(self)
            newTile.setState(currentVal)
            newTile.tilePos = (row, col)
            xPos = 12 + (32 * col)
            yPos = 12 + (32 * row)
            newTile.x = xPos
            newTile.y = yPos
            self.tileset[row].append(newTile)
            
    def showMap(self):
        for row in range(self.SCREEN_ROWS):
            for col in range(self.SCREEN_COLS):
                currentVal = self.map[row + self.offRow][col + self.offCol]
                if currentVal==6:
                    if self.player.phone>=1:
                        currentVal=0
                if currentVal==9:
                    if self.player.salt>=1:
                        currentVal=0
                self.tileset[row][col].setState(currentVal)
                
    def update(self):
        timeLeft = 0 + self.timer.getElapsedTime()
        if timeLeft>=45:
            timeLeft=0
            self.coolSong.play()


        if self.isKeyPressed(pygame.K_LEFT):
            if self.player.x<=330:
                if self.offCol > 0:
                    self.offCol -= 1
            else:
                self.offCol=20
                
        if self.isKeyPressed(pygame.K_RIGHT):
            if self.player.x>=331:
                if self.offCol < self.COLS - self.SCREEN_COLS:
                    self.offCol += 1
            else:
                self.offCol=0
                
        if self.isKeyPressed(pygame.K_UP):
            if self.player.y<=250:
                if self.offRow > 0:
                    self.offRow -= 1
            else:
                self.offRow=5
                
        if self.isKeyPressed(pygame.K_DOWN):
            if self.player.y>=251:
                if self.offRow < (self.ROWS - self.SCREEN_ROWS):
                    self.offRow += 1
            else:
                self.offRow=0 
                    
        if self.isKeyPressed(pygame.K_a): 
            if self.player.something==5:
                if self.player.phone==0:
                    self.phoneNpc()
                else:
                    self.phoneDone()
            elif self.player.something==8:
                if self.player.salt==0:
                    self.saltNpc()
                else:
                    self.saltDone()
            elif self.player.something==10:
                if self.player.tasks==0:
                    self.mainNpc()
                else:
                    self.mainDone()
            elif self.player.something==7:
                self.carrotTalk()
                    
        if self.phoneQuest.clicked:
            self.playGame()
        if self.phonequestDone.clicked:
            self.playGame()
        if self.mainQuest.clicked:
            self.playGame()
        if self.mainquestDone.clicked:
            self.endScreen()
        if self.saltQuest.clicked:
            self.playGame()
        if self.saltquestDone.clicked:
            self.playGame()
        if self.carrotComment.clicked:
            self.playGame()
        if self.intro.clicked:
            self.playGame()
            self.coolSong.play()
                
        if self.playable==False:
            self.player.moveSpeedxa=0
            self.player.moveSpeedxb=0
            self.player.moveSpeedya=0
            self.player.moveSpeedyb=0
            
        self.showMap()
        
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()
import pygame
import time
import random
import ctypes
import sys

pygame.init()

ctypes.windll.user32.SetProcessDPIAware() #Automatic scaling - Makes game windows only

#McMaster University - Materials Properties Battleship Education Game
#Developed by Dr. Bosco Yu and Muhammad Arshad
#2022 McMaster University - All Rights Reserved
#Please see copyrightbox.png, or load game and see copyright sceen

#Setup

display_width = 1600 #Window default width
display_height = 896 #Window default height

black = (0,0,0)
white = (255,255,255)
grey = (166,162,162)
darkgrey = (80,77,77)
lightdarkgrey = (128,128,128)

light_red = (255,151,151)
red = (200,0,0)
teal = (109,158,255)

light_green = (66,212,61)
green = (74,179,71)

yellow = (227,197,66)
light_yellow = (250,211,37)

lime = (125,161,90)
light_lime = (168,224,112)

#randship1 = random.randint(1,3) Old variables, not needed
#randship2 = random.randint(4,6)
#randship3 = random.randint(7,9)

#Tracking variables below
randship1 = 0
randship2 = 0
randship3 = 0

randship4 = 0
randship5 = 0
randship6 = 0

randship7 = 0
randship8 = 0
randship9 = 0

hits = 0
miss = 0

hits2 = 0
miss2 = 0

hits3 = 0
miss3 = 0

countme = 0
countme2 = 0
countme3 = 0
lock1 = False
lock2 = False
lock3 = False

#Tracking Button Color Definition--------------------------
color1 = darkgrey
color2 = darkgrey
color3 = darkgrey
color4 = darkgrey
color5 = darkgrey
color6 = darkgrey
color7 = darkgrey
color8 = darkgrey
color9 = darkgrey
color10 = darkgrey
color11 = darkgrey
color12 = darkgrey
color13 = darkgrey
color14 = darkgrey
color15 = darkgrey
color16 = darkgrey
color17 = darkgrey
color18 = darkgrey
color19 = darkgrey
color20 = darkgrey
color21 = darkgrey
color22 = darkgrey
color23 = darkgrey
color24 = darkgrey
color25 = darkgrey
color26 = darkgrey
color27 = darkgrey
color28 = darkgrey
color29 = darkgrey
color30 = darkgrey
color31 = darkgrey
color32 = darkgrey
color33 = darkgrey
color34 = darkgrey
color35 = darkgrey
color36 = darkgrey
color37 = darkgrey
color38 = darkgrey
color39 = darkgrey
color40 = darkgrey
color41 = darkgrey
color42 = darkgrey
color43 = darkgrey
color44 = darkgrey
color45 = darkgrey
color46 = darkgrey
color47 = darkgrey
color48 = darkgrey
color49 = darkgrey

color56 = darkgrey
color57 = darkgrey
color58 = darkgrey
color59 = darkgrey
color60 = darkgrey
color61 = darkgrey
color62 = darkgrey
color63 = darkgrey
color64 = darkgrey
color65 = darkgrey
color66 = darkgrey
color67 = darkgrey
color68 = darkgrey
color69 = darkgrey
color70 = darkgrey
color71 = darkgrey
color72 = darkgrey
color73 = darkgrey
color74 = darkgrey
color75 = darkgrey
color76 = darkgrey
color77 = darkgrey
color78 = darkgrey
color79 = darkgrey
color80 = darkgrey
color81 = darkgrey
color82 = darkgrey
color83 = darkgrey
color84 = darkgrey
color85 = darkgrey
color86 = darkgrey
color87 = darkgrey
color88 = darkgrey
color89 = darkgrey
color90 = darkgrey
color91 = darkgrey
color92 = darkgrey
color93 = darkgrey
color94 = darkgrey
color95 = darkgrey
color96 = darkgrey
color97 = darkgrey
color98 = darkgrey
color99 = darkgrey
color100 = darkgrey
color101 = darkgrey
color102 = darkgrey
color103 = darkgrey
color104 = darkgrey

color111 = darkgrey
color112 = darkgrey
color113 = darkgrey
color114 = darkgrey
color115 = darkgrey
color116 = darkgrey
color117 = darkgrey
color118 = darkgrey
color119 = darkgrey
color120 = darkgrey
color121 = darkgrey
color122 = darkgrey
color123 = darkgrey
color124 = darkgrey
color125 = darkgrey
color126 = darkgrey
color127 = darkgrey
color128 = darkgrey
color129 = darkgrey
color130 = darkgrey
color131 = darkgrey
color132 = darkgrey
color133 = darkgrey
color134 = darkgrey
color135 = darkgrey
color136 = darkgrey
color137 = darkgrey
color138 = darkgrey
color139 = darkgrey
color140 = darkgrey
color141 = darkgrey
color142 = darkgrey
color143 = darkgrey
color144 = darkgrey
color145 = darkgrey
color146 = darkgrey
color147 = darkgrey
color148 = darkgrey
color149 = darkgrey
color150 = darkgrey
color151 = darkgrey
color152 = darkgrey
color153 = darkgrey
color154 = darkgrey
color155 = darkgrey
color156 = darkgrey
color157 = darkgrey
color158 = darkgrey
color159 = darkgrey

#Tracking Button Color Definition--------------------------


#Hit Button Color Definition--------------------------
color50 = green
color51 = green
color52 = green
color53 = green
color54 = green
color55 = green

color105 = green
color106 = green
color107 = green
color108 = green
color109 = green
color110 = green

color160 = green
color161 = green
color162 = green
color163 = green
color164 = green
color165 = green

#Hit Button Color Definition--------------------------

gameDisplay = pygame.display.set_mode((display_width,display_height)) #Width Height Tuple
pygame.display.set_caption('McMaster University Materials Properties Battleship') #Changes caption of game
clock = pygame.time.Clock() #game clock


#Image Loading--------------------------

#Board

bg = pygame.image.load("paperback.png")
sidearrow = pygame.image.load("sidearrow.png")
uparrow = pygame.image.load("uparrow.png")

#Ships images

#Level1 (Mass vs Stiffness)
cardship = pygame.image.load("Level1/Sm2cardship.png")
concreteship = pygame.image.load("Level1/Sm2concreteship.png")
goldship = pygame.image.load("Level1/Sm2goldship.png")
leathership1 = pygame.image.load("Level1/Sm2leathership.png")
silvership = pygame.image.load("Level1/Sm2silvership.png")
tungship1 = pygame.image.load("Level1/Sm2tungship.png")

#Level 2 (Mass vs Price)
styroship = pygame.image.load("Level2/Smstyroship.png")
corkship = pygame.image.load("Level2/Smcorkship.png")
rubbership = pygame.image.load("Level2/Smrubbership.png")

leathership = pygame.image.load("Level2/Smleathership.png")
woodship = pygame.image.load("Level2/Smwoodship.png")
bambooship = pygame.image.load("Level2/Smbambooship.png")

alumship = pygame.image.load("Level2/Smalumship.png")
steelship = pygame.image.load("Level2/Smsteelship.png")
tungship = pygame.image.load("Level2/Smtungship.png")

#Level3(Thermal Conductivity vs Yield Strength)

alumship2 = pygame.image.load("Level3/Sm3alumship.png")
bambooship2 = pygame.image.load("Level3/Sm3bambooship.png")
rubbership2 = pygame.image.load("Level3/Sm3rubbership.png")
brickship = pygame.image.load("Level3/Sm3brickship.png")
leadship = pygame.image.load("Level3/Sm3leadship.png")
titanship = pygame.image.load("Level3/Sm3titaniumship.png")
tinship = pygame.image.load("Level3/Sm3tinship.png")

#Other (Win tables)

wintable = pygame.image.load("wintable.png")
wintable = wintable.convert()

wintable2 = pygame.image.load("wintable2.png")
wintable2 = wintable2.convert()

wintable3 = pygame.image.load("wintable3.png")
wintable3 = wintable3.convert()



mcmasterlogo = pygame.image.load("mcmasterlogo300.png") #Logo large
mcmasterlogo180x = pygame.image.load("mcmasterlogo180.png") #Logo small
mcmasterlogo64x = pygame.image.load("icon64x.png") #Game Icon
copyrightbox = pygame.image.load("copyrightbox.png")

#How to play images
how2playvar = pygame.image.load("How2Play.png")
how2play2var = pygame.image.load("How2Play2.png")
how2play3var = pygame.image.load("How2Play3.png")

#Hint and Solution Images
hintimage1 = pygame.image.load("Source/_bin/_recompiled/_del/level1hint.png")
hintimage2 = pygame.image.load("Source/_bin/_recompiled/_del/level2hint.png")
hintimage3 = pygame.image.load("Source/_bin/_recompiled/_del/level3hint.png")

solimage1 = pygame.image.load("Source/_bin/_lmty/_remove/_Filesave/S1Pic.png")
solimage2 = pygame.image.load("Source/_bin/_dist/_recompiled/_Filesave/S2Pic.png")
solimage3 = pygame.image.load("Source/_bin/_cache/_remove/_Save/S3Pic.png")

pygame.display.set_icon(mcmasterlogo64x) #Setting Icon

#Image Loading--------------------------

#Drawing right grid
def drawTrack():
    blockwidth = 64
    blockheight = 64
    for x in range(1024,1472,blockwidth):
        for y in range(192,640,blockheight):
            rect = pygame.Rect(x,y,blockwidth,blockheight)
            pygame.draw.rect(gameDisplay,black,rect,4)

#Drawing left grid
def drawGrid():
    blockwidth = 64
    blockheight = 64
    for x in range(128,576,blockwidth):
        for y in range(192,640,blockheight):
            rect = pygame.Rect(x,y,blockwidth,blockheight)
            pygame.draw.rect(gameDisplay,black,rect,3)

def text_objects(text, font):
    textSurface = font.render(text, True, black) #second parameter antialiasing
    return textSurface,textSurface.get_rect()

def text_objects_color(text, font,color):
    textSurface = font.render(text, True, color) #second parameter antialiasing
    return textSurface,textSurface.get_rect()

#Left and right axis's
def drawXaxis(x,y,msg):
    gameDisplay.blit(sidearrow,(x,y))
    smallText = pygame.font.SysFont("calibri",20)
    textSurf,textRect = text_objects(msg, smallText)
    textRect.center = ((x+(224)),y+(30))
    gameDisplay.blit(textSurf,textRect)

def drawYaxis1(x,y,msg):
    gameDisplay.blit(uparrow,(x,y))
    font = pygame.font.SysFont('calibri', 20)
    smallText = font.render(msg,True,black)
    smallText = pygame.transform.rotate(smallText, 90)
    gameDisplay.blit(smallText,(x+30,y+189))

def drawYaxis2(x,y,msg):
    gameDisplay.blit(uparrow,(x,y))
    font = pygame.font.SysFont('calibri', 20)

    smallText = font.render(msg,True,black)
    smallText = pygame.transform.rotate(smallText, 90)
    gameDisplay.blit(smallText,(x-15,y+189))

#GUI Drawing
def drawShipBox(x,y):
    pygame.draw.rect(gameDisplay, (183,174,245), pygame.Rect(131, 704, 442, 26),0,5)
    pygame.draw.rect(gameDisplay, (56,53,78), pygame.Rect(128, 700, 448, 180),5,5)
    smallText = pygame.font.SysFont("calibri",20)
    textSurf,textRect = text_objects('Your Ships', smallText)
    textRect.center = ((x//2),(y))
    gameDisplay.blit(textSurf,textRect)

def drawInfoBox(x,y,w,h,msg,color):
    pygame.draw.rect(gameDisplay, color, pygame.Rect(x, y, w, h),0,5)
    smallText = pygame.font.SysFont("calibri",15)
    textSurf,textRect = text_objects(msg, smallText)
    textRect.center = ((w-90),(y+25))
    gameDisplay.blit(textSurf,textRect)

def drawInfoBox2(x,y,w,h,msg,color):
    pygame.draw.rect(gameDisplay, color, pygame.Rect(x, y, w, h),0,5)
    smallText = pygame.font.SysFont("calibri",14)
    textSurf,textRect = text_objects(msg, smallText)
    textRect.center = ((w-90),(y+25))
    gameDisplay.blit(textSurf,textRect)

def drawInfoBox3(x,y,w,h,msg,color):
    pygame.draw.rect(gameDisplay, color, pygame.Rect(x, y, w, h),0,5)
    smallText = pygame.font.SysFont("calibri",13)
    textSurf,textRect = text_objects(msg, smallText)
    textRect.center = ((w-90),(y+25))
    gameDisplay.blit(textSurf,textRect)

def drawHitBox(x,y):
    pygame.draw.rect(gameDisplay, (56,53,78), pygame.Rect(51, 700, 80, 180),5,5)
    smallText = pygame.font.SysFont("calibri",20)
    textSurf,textRect = text_objects('Hits', smallText)
    textRect.center = ((x//2),(y))
    gameDisplay.blit(textSurf,textRect)

def drawMarkerBox(x,y):
    pygame.draw.rect(gameDisplay, (56,53,78), pygame.Rect(1024, 700, 448, 180),5,5)
    smallText = pygame.font.SysFont("calibri",20)
    textSurf,textRect = text_objects('', smallText)
    textRect.center = ((x//2),(y))
    gameDisplay.blit(textSurf,textRect)

def drawTitle(x,y,msg,color,size):
    font = pygame.font.SysFont("calibri",size)
    text = font.render(msg,True,color)
    gameDisplay.blit(text,(x,y))
    

def missCounter(count):
    font = pygame.font.SysFont('calibri',25)
    text = font.render("Hits Missed: " + str(count),True,black)
    gameDisplay.blit(text,(1070,718))
    pygame.draw.rect(gameDisplay,teal,(1040,714,20,20),0,10)


def hitCounter(count):
    font = pygame.font.SysFont('calibri',25)
    text = font.render("Hits Landed: " + str(count),True,black)
    gameDisplay.blit(text,(1070,759))
    pygame.draw.rect(gameDisplay,red,(1040,755,20,20),0,10)


#Generating random ships for Mass vs Stiffness
def loadships():
    if randship1 == 1:
        gameDisplay.blit(styroship,(150,512))
        drawInfoBox(128,730,448,50,'A6 A7: Very Light, Very Elastic, Styrofoam Cruiser',(170,156,255))

    elif randship1 == 2:
        gameDisplay.blit(woodship,(256,406))
        drawInfoBox(128,730,448,50,'C4 D4: Medium Weight, Medium Stiffness, Wood Cruiser',(170,156,255))

    elif randship1 == 3:
        gameDisplay.blit(tungship,(448,214))
        drawInfoBox(128,730,448,50,'F1 G1: Very Heavy, Very Stiff, Tungsten Cruiser',(170,156,255))

    if randship2 == 4:
        gameDisplay.blit(corkship,(214,512))
        drawInfoBox(128,780,448,50,'B6 B7: Light, Elastic, Cork Destroyer',(157,145,235))
        
    elif randship2 == 5:
        gameDisplay.blit(leathership,(278,448))
        drawInfoBox(128,780,448,50,'C5 C6: Light, Slightly Elastic, Leather Destroyer',(157,145,235))

    elif randship2 == 6:
        gameDisplay.blit(alumship,(406,320))
        drawInfoBox(128,780,448,50,'E3 E4: Slightly Heavy, Stiff, Aluminum Destroyer',(157,145,235))

    if randship3 == 7:
        gameDisplay.blit(rubbership,(320,598))
        drawInfoBox(128,830,448,50,'D7 E7: Medium Weight, Very Elastic, Rubber Battleship',(157,145,235))

    elif randship3 == 8:
        gameDisplay.blit(bambooship,(256,342))
        drawInfoBox(128,830,448,50,'C3 D3: Medium Weight, Stiff, Bamboo Battleship',(157,145,235))

    elif randship3 == 9:
        gameDisplay.blit(steelship,(384,278))
        drawInfoBox(128,830,448,50,'E2 F2: Heavy, Stiff, Steel Battleship',(157,145,235))

#Genertaing random ships for Mass vs Price
def loadships2():
    if randship4 == 1:
        gameDisplay.blit(styroship,(150,448))
        drawInfoBox(128,730,448,50,'A5 A6: Very Light, Cheap, Styrofoam Cruiser',(170,156,255))

    elif randship4 == 2:
        gameDisplay.blit(leathership1,(256,405))
        drawInfoBox(128,730,448,50,'C4 D4: Light, Medium Price, Leather Cruiser',(170,156,255))

    elif randship4 == 3:
        gameDisplay.blit(silvership,(470,256))
        drawInfoBox(128,730,448,50,'F2 F3: Heavy, Expensive, Silver Cruiser',(170,156,255))

    if randship5 == 4:
        gameDisplay.blit(corkship,(214,448))
        drawInfoBox(128,780,448,50,'B5 B6: Light, Cheap, Cork Destroyer',(157,145,235))

    elif randship5 == 5:
        gameDisplay.blit(concreteship,(320,597))
        drawInfoBox(128,780,448,50,'D7 E7: Medium Weight, Very Cheap, Concrete Destroyer',(157,145,235))

    elif randship5 == 6:
        gameDisplay.blit(goldship,(534,192))
        drawInfoBox(128,780,448,50,'G1 G2: Very Heavy, Very Expensive, Gold Destroyer',(157,145,235))

    if randship6 == 7:
        gameDisplay.blit(cardship,(256,530))
        drawInfoBox(128,830,448,50,'C6 D6: Light, Cheap, Cardboard Battleship',(157,145,235))

    elif randship6 == 8:
        gameDisplay.blit(steelship,(384,469))
        drawInfoBox(128,830,448,50,'E5 F5: Heavy, Slightly Expensive, Steel Battleship',(157,145,235))

    elif randship6 == 9:
        gameDisplay.blit(tungship1,(534,320))
        drawInfoBox(128,830,448,50,'G3 G4: Very Heavy, Expensive, Tungsten Battleship',(157,145,235))

#Generating random ships for Thermal Conductivity vs Yield Strength
def loadships3():
    if randship7 == 1:
        gameDisplay.blit(styroship,(150,512))
        drawInfoBox3(128,730,448,50,'A6 A7: Very Low Heat Conductivity and Yield Strength, Styrofoam Cruiser',(170,156,255))

    elif randship7 == 2:
        gameDisplay.blit(concreteship,(320,533))
        drawInfoBox3(128,730,448,50,'D6 E6: Medium Heat Conductivity, Fairly Low Yield Strength, Concrete Cruiser',(170,156,255))

    elif randship7 == 3:
        gameDisplay.blit(alumship2,(448,277))
        drawInfoBox3(128,730,448,50,'F2 G2: Very High Heat Conductivity, High Yield Strength, Aluminum Destroyer',(170,156,255))

    if randship8 == 4:
        gameDisplay.blit(rubbership2,(214,448))
        drawInfoBox3(128,780,448,50,'B5 B6: Low Heat Conductivity, Low Yield Strength, Rubber Destroyer',(157,145,235))

    elif randship8 == 5:
        gameDisplay.blit(brickship,(256,469))
        drawInfoBox3(128,780,448,50,'C5 D5: Medium Heat Conductivity, Medium Yield Strength, Brick Cruiser',(157,145,235))

    elif randship8 == 6:
        gameDisplay.blit(leadship,(406,320))
        drawInfoBox3(128,780,448,50,'E3 E4: Slightly High Heat Conductivity, Medium Yield Strength, Lead Destroyer',(157,145,235))

    if randship9 == 7:
        gameDisplay.blit(bambooship2,(192,405))
        drawInfoBox3(128,830,448,50,'B4 C4: Low Heat Conductivity, Slightly High Yield Strength, Bamboo Battleship',(157,145,235))

    elif randship9 == 8:
        gameDisplay.blit(titanship,(320,213))
        drawInfoBox3(128,830,448,50,'D1 E1: Medium Heat Conductivity, Very High Yield Strength, Titanium Battleship',(157,145,235))

    elif randship9 == 9:
        gameDisplay.blit(tinship,(470,320))
        drawInfoBox3(128,830,448,50,'F3 F4: Fairly High Heat Conductivity, Medium Yield Strength, Tin Battleship',(157,145,235))

def newshipB(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h),0,5)
        if click[0] == 1 and action != None:
            action()
        
    else:
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h),0,5)

    smallText = pygame.font.SysFont("calibri",20)
    textSurf,textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)),y+(h/2))
    gameDisplay.blit(textSurf,textRect)

#Random ship generator functions
def generateNewrand():
    global randship1
    global randship2
    global randship3

    global color50
    global color51
    global color52
    global color53
    global color54
    global color55
    
    randship1 = random.randint(1,3)
    randship2 = random.randint(4,6)
    randship3 = random.randint(7,9)


    color50 = green
    color51 = green
    color52 = green
    color53 = green
    color54 = green
    color55 = green
    
    time.sleep(0.3)

def generateNewrand2():
    global randship4
    global randship5
    global randship6

    global color105
    global color106
    global color107
    global color108
    global color109
    global color110
    
    randship4 = random.randint(1,3)
    randship5 = random.randint(4,6)
    randship6 = random.randint(7,9)

    color105 = green
    color106 = green
    color107 = green
    color108 = green
    color109 = green
    color110 = green
    
    time.sleep(0.3)

def generateNewrand3():
    global randship7
    global randship8
    global randship9

    global color160
    global color161
    global color162
    global color163
    global color164
    global color165
    
    randship7 = random.randint(1,3)
    randship8 = random.randint(4,6)
    randship9 = random.randint(7,9)

    color160 = green
    color161 = green
    color162 = green
    color163 = green
    color164 = green
    color165 = green
    
    time.sleep(0.3)

def clearBoard():

    global hits
    global miss

    hits = 0
    miss = 0

    global color1 
    global color2
    global color3 
    global color4 
    global color5 
    global color6
    global color7
    global color8
    global color9 
    global color10
    global color11
    global color12
    global color13 
    global color14
    global color15
    global color16 
    global color17
    global color18
    global color19
    global color20
    global color21
    global color22 
    global color23 
    global color24 
    global color25 
    global color26 
    global color27 
    global color28 
    global color29 
    global color30 
    global color31 
    global color32 
    global color33 
    global color34
    global color35 
    global color36 
    global color37
    global color38
    global color39 
    global color40 
    global color41 
    global color42 
    global color43
    global color44
    global color45 
    global color46
    global color47 
    global color48 
    global color49 
    
    color1 = darkgrey
    color2 = darkgrey
    color3 = darkgrey
    color4 = darkgrey
    color5 = darkgrey
    color6 = darkgrey
    color7 = darkgrey
    color8 = darkgrey
    color9 = darkgrey
    color10 = darkgrey
    color11 = darkgrey
    color12 = darkgrey
    color13 = darkgrey
    color14 = darkgrey
    color15 = darkgrey
    color16 = darkgrey
    color17 = darkgrey
    color18 = darkgrey
    color19 = darkgrey
    color20 = darkgrey
    color21 = darkgrey
    color22 = darkgrey
    color23 = darkgrey
    color24 = darkgrey
    color25 = darkgrey
    color26 = darkgrey
    color27 = darkgrey
    color28 = darkgrey
    color29 = darkgrey
    color30 = darkgrey
    color31 = darkgrey
    color32 = darkgrey
    color33 = darkgrey
    color34 = darkgrey
    color35 = darkgrey
    color36 = darkgrey
    color37 = darkgrey
    color38 = darkgrey
    color39 = darkgrey
    color40 = darkgrey
    color41 = darkgrey
    color42 = darkgrey
    color43 = darkgrey
    color44 = darkgrey
    color45 = darkgrey
    color46 = darkgrey
    color47 = darkgrey
    color48 = darkgrey
    color49 = darkgrey

def clearBoard2():

    global hits2
    global miss2

    hits2 = 0
    miss2 = 0

    global color56
    global color57
    global color58
    global color59
    global color60
    global color61
    global color62
    global color63
    global color64
    global color65
    global color66
    global color67
    global color68
    global color69
    global color70
    global color71
    global color72
    global color73
    global color74
    global color75
    global color76
    global color77
    global color78
    global color79
    global color80
    global color81
    global color82
    global color83
    global color84
    global color85
    global color86
    global color87
    global color88
    global color89
    global color90
    global color91
    global color92
    global color93
    global color94 
    global color95
    global color96
    global color97
    global color98
    global color99
    global color100
    global color101
    global color102
    global color103
    global color104
    
    color56 = darkgrey
    color57 = darkgrey
    color58 = darkgrey
    color59 = darkgrey
    color60 = darkgrey
    color61 = darkgrey
    color62 = darkgrey
    color63 = darkgrey
    color64 = darkgrey
    color65 = darkgrey
    color66 = darkgrey
    color67 = darkgrey
    color68 = darkgrey
    color69 = darkgrey
    color70 = darkgrey
    color71 = darkgrey
    color72 = darkgrey
    color73 = darkgrey
    color74 = darkgrey
    color75 = darkgrey
    color76 = darkgrey
    color77 = darkgrey
    color78 = darkgrey
    color79 = darkgrey
    color80 = darkgrey
    color81 = darkgrey
    color82 = darkgrey
    color83 = darkgrey
    color84 = darkgrey
    color85 = darkgrey
    color86 = darkgrey
    color87 = darkgrey
    color88 = darkgrey
    color89 = darkgrey
    color90 = darkgrey
    color91 = darkgrey
    color92 = darkgrey
    color93 = darkgrey
    color94 = darkgrey
    color95 = darkgrey
    color96 = darkgrey
    color97 = darkgrey
    color98 = darkgrey
    color99 = darkgrey
    color100 = darkgrey
    color101 = darkgrey
    color102 = darkgrey
    color103 = darkgrey
    color104 = darkgrey

def clearBoard3():

    global hits3
    global miss3

    hits3 = 0
    miss3 = 0

    global color111
    global color112
    global color113
    global color114
    global color115
    global color116
    global color117
    global color118
    global color119
    global color120
    global color121
    global color122
    global color123
    global color124
    global color125
    global color126
    global color127
    global color128
    global color129
    global color130
    global color131
    global color132
    global color133
    global color134
    global color135
    global color136
    global color137
    global color138
    global color139
    global color140
    global color141
    global color142
    global color143
    global color144
    global color145
    global color146
    global color147
    global color148
    global color149 
    global color150
    global color151
    global color152
    global color153
    global color154
    global color155
    global color156
    global color157
    global color158
    global color159
    
    color111 = darkgrey
    color112 = darkgrey
    color113 = darkgrey
    color114 = darkgrey
    color115 = darkgrey
    color116 = darkgrey
    color117 = darkgrey
    color118 = darkgrey
    color119 = darkgrey
    color120 = darkgrey
    color121 = darkgrey
    color122 = darkgrey
    color123 = darkgrey
    color124 = darkgrey
    color125 = darkgrey
    color126 = darkgrey
    color127 = darkgrey
    color128 = darkgrey
    color129 = darkgrey
    color130 = darkgrey
    color131 = darkgrey
    color132 = darkgrey
    color133 = darkgrey
    color134 = darkgrey
    color135 = darkgrey
    color136 = darkgrey
    color137 = darkgrey
    color138 = darkgrey
    color139 = darkgrey
    color140 = darkgrey
    color141 = darkgrey
    color142 = darkgrey
    color143 = darkgrey
    color144 = darkgrey
    color145 = darkgrey
    color146 = darkgrey
    color147 = darkgrey
    color148 = darkgrey
    color149 = darkgrey
    color150 = darkgrey
    color151 = darkgrey
    color152 = darkgrey
    color153 = darkgrey
    color154 = darkgrey
    color155 = darkgrey
    color156 = darkgrey
    color157 = darkgrey
    color158 = darkgrey
    color159 = darkgrey

def doNothing():
    pass

    
#Tracking Buttons Function Definition--------------------------
#NOTE: The above list of colors and below functions are for EACH button
#This can be EASILY converted into a Button CLASS for much more simple code
#What is shown above and below is the manual approach to this game

def HMbutton1(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color1
    global hits
    global miss
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color1 == teal:
                pass

            elif color1 == red:
                color1 = teal
                hits-=1
                miss+=1
            
            else:
                color1 = teal
                miss+=1
               
            
        elif click[2] == 1:
            if color1 == red:
                pass

            elif color1 == teal:
                color1 = red
                miss-=1
                hits+=1
            
            else:
                color1 = red
                hits+=1
                
    else:
        pygame.draw.rect(gameDisplay,color1,(x,y,w,h))

def HMbutton2(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color2
    global hits
    global miss
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color2 == teal:
                pass

            elif color2 == red:
                color2 = teal
                hits-=1
                miss+=1
            
            else:
                color2 = teal
                miss+=1
                
            
        elif click[2] == 1:
            if color2 == red:
                pass

            elif color2 == teal:
                color2 = red
                miss-=1
                hits+=1
            
            else:
                color2 = red
                hits+=1
                
    else:
        pygame.draw.rect(gameDisplay,color2,(x,y,w,h))

def HMbutton3(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color3
    global hits
    global miss
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color3 == teal:
                pass

            elif color3 == red:
                color3 = teal
                hits-=1
                miss+=1
            
            else:
                color3 = teal
                miss+=1
                
            
        elif click[2] == 1:
            if color3 == red:
                pass

            elif color3 == teal:
                color3 = red
                miss-=1
                hits+=1
            
            else:
                color3 = red
                hits+=1
                
    else:
        pygame.draw.rect(gameDisplay,color3,(x,y,w,h))

def HMbutton4(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color4
    global hits
    global miss
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color4 == teal:
                pass

            elif color4 == red:
                color4 = teal
                hits-=1
                miss+=1
            
            else:
                color4 = teal
                miss+=1
                
            
        elif click[2] == 1:
            if color4 == red:
                pass

            elif color4 == teal:
                color4 = red
                miss-=1
                hits+=1
            
            else:
                color4 = red
                hits+=1
                
    else:
        pygame.draw.rect(gameDisplay,color4,(x,y,w,h))
        
def HMbutton5(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color5
    global hits
    global miss
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color5 == teal:
                pass

            elif color5 == red:
                color5 = teal
                hits-=1
                miss+=1
            
            else:
                color5 = teal
                miss+=1
                
            
        elif click[2] == 1:
            if color5 == red:
                pass

            elif color5 == teal:
                color5 = red
                miss-=1
                hits+=1
            
            else:
                color5 = red
                hits+=1
                
    else:
        pygame.draw.rect(gameDisplay,color5,(x,y,w,h))

def HMbutton6(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color6
    global hits
    global miss
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color6 == teal:
                pass

            elif color6 == red:
                color6 = teal
                hits-=1
                miss+=1
            
            else:
                color6 = teal
                miss+=1
                
            
        elif click[2] == 1:
            if color6 == red:
                pass

            elif color6 == teal:
                color6 = red
                miss-=1
                hits+=1
            
            else:
                color6 = red
                hits+=1
                
    else:
        pygame.draw.rect(gameDisplay,color6,(x,y,w,h))

def HMbutton7(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color7
    global hits
    global miss
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color7 == teal:
                pass

            elif color7 == red:
                color7 = teal
                hits-=1
                miss+=1
            
            else:
                color7 = teal
                miss+=1
                
            
        elif click[2] == 1:
            if color7 == red:
                pass

            elif color7 == teal:
                color7 = red
                miss-=1
                hits+=1
            
            else:
                color7 = red
                hits+=1
                
    else:
        pygame.draw.rect(gameDisplay,color7,(x,y,w,h))

def HMbutton8(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color8
    global hits
    global miss
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color8 == teal:
                pass

            elif color8 == red:
                color8 = teal
                hits-=1
                miss+=1
            
            else:
                color8 = teal
                miss+=1
                
            
        elif click[2] == 1:
            if color8 == red:
                pass

            elif color8 == teal:
                color8 = red
                miss-=1
                hits+=1
            
            else:
                color8 = red
                hits+=1
                
    else:
        pygame.draw.rect(gameDisplay,color8,(x,y,w,h))

def HMbutton9(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color9
    global hits
    global miss
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color9 == teal:
                pass

            elif color9 == red:
                color9 = teal
                hits-=1
                miss+=1
            
            else:
                color9 = teal
                miss+=1
                
            
        elif click[2] == 1:
            if color9 == red:
                pass

            elif color9 == teal:
                color9 = red
                miss-=1
                hits+=1
            
            else:
                color9 = red
                hits+=1
                
    else:
        pygame.draw.rect(gameDisplay,color9,(x,y,w,h))

def HMbutton10(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color10
    global hits
    global miss
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color10 == teal:
                pass

            elif color10 == red:
                color10 = teal
                hits-=1
                miss+=1
            
            else:
                color10 = teal
                miss+=1
                
            
        elif click[2] == 1:
            if color10 == red:
                pass

            elif color10 == teal:
                color10 = red
                miss-=1
                hits+=1
            
            else:
                color10 = red
                hits+=1
                
    else:
        pygame.draw.rect(gameDisplay,color10,(x,y,w,h))

def HMbutton11(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color11
    global hits
    global miss
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color11 == teal:
                pass

            elif color11 == red:
                color11 = teal
                hits-=1
                miss+=1
            
            else:
                color11 = teal
                miss+=1
                
            
        elif click[2] == 1:
            if color11 == red:
                pass

            elif color11 == teal:
                color11 = red
                miss-=1
                hits+=1
            
            else:
                color11 = red
                hits+=1
                
    else:
        pygame.draw.rect(gameDisplay,color11,(x,y,w,h))

def HMbutton12(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color12
    global hits
    global miss
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color12 == teal:
                pass

            elif color12 == red:
                color12 = teal
                hits-=1
                miss+=1
            
            else:
                color12 = teal
                miss+=1
                
            
        elif click[2] == 1:
            if color12 == red:
                pass

            elif color12 == teal:
                color12 = red
                miss-=1
                hits+=1
            
            else:
                color12 = red
                hits+=1
                
    else:
        pygame.draw.rect(gameDisplay,color12,(x,y,w,h))

def HMbutton13(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color13
    global hits
    global miss
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color13 == teal:
                pass

            elif color13 == red:
                color13 = teal
                hits-=1
                miss+=1
            
            else:
                color13 = teal
                miss+=1
                
            
        elif click[2] == 1:
            if color13 == red:
                pass

            elif color13 == teal:
                color13 = red
                miss-=1
                hits+=1
            
            else:
                color13 = red
                hits+=1
                
    else:
        pygame.draw.rect(gameDisplay,color13,(x,y,w,h))

def HMbutton14(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color14
    global hits
    global miss
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color14 == teal:
                pass

            elif color14 == red:
                color14 = teal
                hits-=1
                miss+=1
            
            else:
                color14 = teal
                miss+=1
                
            
        elif click[2] == 1:
            if color14 == red:
                pass

            elif color14 == teal:
                color14 = red
                miss-=1
                hits+=1
            
            else:
                color14 = red
                hits+=1
                
    else:
        pygame.draw.rect(gameDisplay,color14,(x,y,w,h))

def HMbutton15(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color15
    global hits
    global miss
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color15 == teal:
                pass

            elif color15 == red:
                color15 = teal
                hits-=1
                miss+=1
            
            else:
                color15 = teal
                miss+=1
                
            
        elif click[2] == 1:
            if color15 == red:
                pass

            elif color15 == teal:
                color15 = red
                miss-=1
                hits+=1
            
            else:
                color15 = red
                hits+=1
                
    else:
        pygame.draw.rect(gameDisplay,color15,(x,y,w,h))

def HMbutton16(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color16
    global hits
    global miss
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color16 == teal:
                pass

            elif color16 == red:
                color16 = teal
                hits-=1
                miss+=1
            
            else:
                color16 = teal
                miss+=1
                
            
        elif click[2] == 1:
            if color16 == red:
                pass

            elif color16 == teal:
                color16 = red
                miss-=1
                hits+=1
            
            else:
                color16 = red
                hits+=1
                
    else:
        pygame.draw.rect(gameDisplay,color16,(x,y,w,h))


def HMbutton17(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color17
    global hits
    global miss
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color17 == teal:
                pass

            elif color17 == red:
                color17 = teal
                hits-=1
                miss+=1
            
            else:
                color17 = teal
                miss+=1
                
            
        elif click[2] == 1:
            if color17 == red:
                pass

            elif color17 == teal:
                color17 = red
                miss-=1
                hits+=1
            
            else:
                color17 = red
                hits+=1
                
    else:
        pygame.draw.rect(gameDisplay,color17,(x,y,w,h))

def HMbutton18(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color18
    global hits
    global miss
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color18 == teal:
                pass

            elif color18 == red:
                color18 = teal
                hits-=1
                miss+=1
            
            else:
                color18 = teal
                miss+=1
                
            
        elif click[2] == 1:
            if color18 == red:
                pass

            elif color18 == teal:
                color18 = red
                miss-=1
                hits+=1
            
            else:
                color18 = red
                hits+=1
                
    else:
        pygame.draw.rect(gameDisplay,color18,(x,y,w,h))

def HMbutton19(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color19
    global hits
    global miss
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color19 == teal:
                pass

            elif color19 == red:
                color19 = teal
                hits-=1
                miss+=1
            
            else:
                color19 = teal
                miss+=1
                
            
        elif click[2] == 1:
            if color19 == red:
                pass

            elif color19 == teal:
                color19 = red
                miss-=1
                hits+=1
            
            else:
                color19 = red
                hits+=1
                
    else:
        pygame.draw.rect(gameDisplay,color19,(x,y,w,h))
        
def HMbutton20(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color20
    global hits
    global miss
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color20 == teal:
                pass

            elif color20 == red:
                color20 = teal
                hits-=1
                miss+=1
            
            else:
                color20 = teal
                miss+=1
                
            
        elif click[2] == 1:
            if color20 == red:
                pass

            elif color20 == teal:
                color20 = red
                miss-=1
                hits+=1
            
            else:
                color20 = red
                hits+=1
                
    else:
        pygame.draw.rect(gameDisplay,color20,(x,y,w,h))

def HMbutton21(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color21
    global hits
    global miss
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color21 == teal:
                pass

            elif color21 == red:
                color21 = teal
                hits-=1
                miss+=1
            
            else:
                color21 = teal
                miss+=1
                
            
        elif click[2] == 1:
            if color21 == red:
                pass

            elif color21 == teal:
                color21 = red
                miss-=1
                hits+=1
            
            else:
                color21 = red
                hits+=1
                
    else:
        pygame.draw.rect(gameDisplay,color21,(x,y,w,h))

def HMbutton22(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color22
    global hits
    global miss
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color22 == teal:
                pass

            elif color22 == red:
                color22 = teal
                hits-=1
                miss+=1
            
            else:
                color22 = teal
                miss+=1
                
            
        elif click[2] == 1:
            if color22 == red:
                pass

            elif color22 == teal:
                color22 = red
                miss-=1
                hits+=1
            
            else:
                color22 = red
                hits+=1
                
    else:
        pygame.draw.rect(gameDisplay,color22,(x,y,w,h))
        
def HMbutton23(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color23
    global hits
    global miss
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color23 == teal:
                pass

            elif color23 == red:
                color23 = teal
                hits-=1
                miss+=1
            
            else:
                color23 = teal
                miss+=1
                
            
        elif click[2] == 1:
            if color23 == red:
                pass

            elif color23 == teal:
                color23 = red
                miss-=1
                hits+=1
            
            else:
                color23 = red
                hits+=1
                
    else:
        pygame.draw.rect(gameDisplay,color23,(x,y,w,h))
        

def HMbutton24(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color24
    global hits
    global miss
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color24 == teal:
                pass

            elif color24 == red:
                color24 = teal
                hits-=1
                miss+=1
            
            else:
                color24 = teal
                miss+=1
                
            
        elif click[2] == 1:
            if color24 == red:
                pass

            elif color24 == teal:
                color24 = red
                miss-=1
                hits+=1
            
            else:
                color24 = red
                hits+=1
                
    else:
        pygame.draw.rect(gameDisplay,color24,(x,y,w,h))

def HMbutton25(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color25
    global hits
    global miss
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color25 == teal:
                pass

            elif color25 == red:
                color25 = teal
                hits-=1
                miss+=1
            
            else:
                color25 = teal
                miss+=1
                
            
        elif click[2] == 1:
            if color25 == red:
                pass

            elif color25 == teal:
                color25 = red
                miss-=1
                hits+=1
            
            else:
                color25 = red
                hits+=1
                
    else:
        pygame.draw.rect(gameDisplay,color25,(x,y,w,h))

def HMbutton26(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color26
    global hits
    global miss
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color26 == teal:
                pass

            elif color26 == red:
                color26 = teal
                hits-=1
                miss+=1
            
            else:
                color26 = teal
                miss+=1
                
            
        elif click[2] == 1:
            if color26 == red:
                pass

            elif color26 == teal:
                color26 = red
                miss-=1
                hits+=1
            
            else:
                color26 = red
                hits+=1
                
    else:
        pygame.draw.rect(gameDisplay,color26,(x,y,w,h))
        
def HMbutton27(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color27
    global hits
    global miss
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color27 == teal:
                pass

            elif color27 == red:
                color27 = teal
                hits-=1
                miss+=1
            
            else:
                color27 = teal
                miss+=1
                
            
        elif click[2] == 1:
            if color27 == red:
                pass

            elif color27 == teal:
                color27 = red
                miss-=1
                hits+=1
            
            else:
                color27 = red
                hits+=1
                
    else:
        pygame.draw.rect(gameDisplay,color27,(x,y,w,h))

def HMbutton28(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color28
    global hits
    global miss
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color28 == teal:
                pass

            elif color28 == red:
                color28 = teal
                hits-=1
                miss+=1
            
            else:
                color28 = teal
                miss+=1
                
            
        elif click[2] == 1:
            if color28 == red:
                pass

            elif color28 == teal:
                color28 = red
                miss-=1
                hits+=1
            
            else:
                color28 = red
                hits+=1
                
    else:
        pygame.draw.rect(gameDisplay,color28,(x,y,w,h))

def HMbutton29(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color29
    global hits
    global miss
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color29 == teal:
                pass

            elif color29 == red:
                color29 = teal
                hits-=1
                miss+=1
            
            else:
                color29 = teal
                miss+=1
                
            
        elif click[2] == 1:
            if color29 == red:
                pass

            elif color29 == teal:
                color29 = red
                miss-=1
                hits+=1
            
            else:
                color29 = red
                hits+=1
                
    else:
        pygame.draw.rect(gameDisplay,color29,(x,y,w,h))


def HMbutton30(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color30
    global hits
    global miss
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color30 == teal:
                pass

            elif color30 == red:
                color30 = teal
                hits-=1
                miss+=1
            
            else:
                color30 = teal
                miss+=1
                
            
        elif click[2] == 1:
            if color30 == red:
                pass

            elif color30 == teal:
                color30 = red
                miss-=1
                hits+=1
            
            else:
                color30 = red
                hits+=1
                
    else:
        pygame.draw.rect(gameDisplay,color30,(x,y,w,h))

def HMbutton31(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color31
    global hits
    global miss
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color31 == teal:
                pass

            elif color31 == red:
                color31 = teal
                hits-=1
                miss+=1
            
            else:
                color31 = teal
                miss+=1
                
            
        elif click[2] == 1:
            if color31 == red:
                pass

            elif color31 == teal:
                color31 = red
                miss-=1
                hits+=1
            
            else:
                color31 = red
                hits+=1
                
    else:
        pygame.draw.rect(gameDisplay,color31,(x,y,w,h))

def HMbutton32(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color32
    global hits
    global miss
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color32 == teal:
                pass

            elif color32 == red:
                color32 = teal
                hits-=1
                miss+=1
            
            else:
                color32 = teal
                miss+=1
                
            
        elif click[2] == 1:
            if color32 == red:
                pass

            elif color32 == teal:
                color32 = red
                miss-=1
                hits+=1
            
            else:
                color32 = red
                hits+=1
                
    else:
        pygame.draw.rect(gameDisplay,color32,(x,y,w,h))

def HMbutton33(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color33
    global hits
    global miss
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color33 == teal:
                pass

            elif color33 == red:
                color33 = teal
                hits-=1
                miss+=1
            
            else:
                color33 = teal
                miss+=1
                
            
        elif click[2] == 1:
            if color33 == red:
                pass

            elif color33 == teal:
                color33 = red
                miss-=1
                hits+=1
            
            else:
                color33 = red
                hits+=1
                
    else:
        pygame.draw.rect(gameDisplay,color33,(x,y,w,h))
        
def HMbutton34(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color34
    global hits
    global miss
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color34 == teal:
                pass

            elif color34 == red:
                color34 = teal
                hits-=1
                miss+=1
            
            else:
                color34 = teal
                miss+=1
                
            
        elif click[2] == 1:
            if color34 == red:
                pass

            elif color34 == teal:
                color34 = red
                miss-=1
                hits+=1
            
            else:
                color34 = red
                hits+=1
                
    else:
        pygame.draw.rect(gameDisplay,color34,(x,y,w,h))

def HMbutton35(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color35
    global hits
    global miss
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color35 == teal:
                pass

            elif color35 == red:
                color35 = teal
                hits-=1
                miss+=1
            
            else:
                color35 = teal
                miss+=1
                
            
        elif click[2] == 1:
            if color35 == red:
                pass

            elif color35 == teal:
                color35 = red
                miss-=1
                hits+=1
            
            else:
                color35 = red
                hits+=1
                
    else:
        pygame.draw.rect(gameDisplay,color35,(x,y,w,h))

def HMbutton36(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color36
    global hits
    global miss
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color36 == teal:
                pass

            elif color36 == red:
                color36 = teal
                hits-=1
                miss+=1
            
            else:
                color36 = teal
                miss+=1
                
            
        elif click[2] == 1:
            if color36 == red:
                pass

            elif color36 == teal:
                color36 = red
                miss-=1
                hits+=1
            
            else:
                color36 = red
                hits+=1
                
    else:
        pygame.draw.rect(gameDisplay,color36,(x,y,w,h))


def HMbutton37(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color37
    global hits
    global miss
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color37 == teal:
                pass

            elif color37 == red:
                color37 = teal
                hits-=1
                miss+=1
            
            else:
                color37 = teal
                miss+=1
                
            
        elif click[2] == 1:
            if color37 == red:
                pass

            elif color37 == teal:
                color37 = red
                miss-=1
                hits+=1
            
            else:
                color37 = red
                hits+=1
                
    else:
        pygame.draw.rect(gameDisplay,color37,(x,y,w,h))

def HMbutton38(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color38
    global hits
    global miss
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color38 == teal:
                pass

            elif color38 == red:
                color38 = teal
                hits-=1
                miss+=1
            
            else:
                color38 = teal
                miss+=1
                
            
        elif click[2] == 1:
            if color38 == red:
                pass

            elif color38 == teal:
                color38 = red
                miss-=1
                hits+=1
            
            else:
                color38 = red
                hits+=1
                
    else:
        pygame.draw.rect(gameDisplay,color38,(x,y,w,h))


def HMbutton39(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color39
    global hits
    global miss
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color39 == teal:
                pass

            elif color39 == red:
                color39 = teal
                hits-=1
                miss+=1
            
            else:
                color39 = teal
                miss+=1
                
            
        elif click[2] == 1:
            if color39 == red:
                pass

            elif color39 == teal:
                color39 = red
                miss-=1
                hits+=1
            
            else:
                color39 = red
                hits+=1
                
    else:
        pygame.draw.rect(gameDisplay,color39,(x,y,w,h))
        
def HMbutton40(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color40
    global hits
    global miss
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color40 == teal:
                pass

            elif color40 == red:
                color40 = teal
                hits-=1
                miss+=1
            
            else:
                color40 = teal
                miss+=1
                
            
        elif click[2] == 1:
            if color40 == red:
                pass

            elif color40 == teal:
                color40 = red
                miss-=1
                hits+=1
            
            else:
                color40 = red
                hits+=1
                
    else:
        pygame.draw.rect(gameDisplay,color40,(x,y,w,h))
        
def HMbutton41(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color41
    global hits
    global miss
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color41 == teal:
                pass

            elif color41 == red:
                color41 = teal
                hits-=1
                miss+=1
            
            else:
                color41 = teal
                miss+=1
                
            
        elif click[2] == 1:
            if color41 == red:
                pass

            elif color41 == teal:
                color41 = red
                miss-=1
                hits+=1
            
            else:
                color41 = red
                hits+=1
                
    else:
        pygame.draw.rect(gameDisplay,color41,(x,y,w,h))
        
def HMbutton42(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color42
    global hits
    global miss
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color42 == teal:
                pass

            elif color42 == red:
                color42 = teal
                hits-=1
                miss+=1
            
            else:
                color42 = teal
                miss+=1
                
            
        elif click[2] == 1:
            if color42 == red:
                pass

            elif color42 == teal:
                color42 = red
                miss-=1
                hits+=1
            
            else:
                color42 = red
                hits+=1
                
    else:
        pygame.draw.rect(gameDisplay,color42,(x,y,w,h))

def HMbutton43(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color43
    global hits
    global miss
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color43 == teal:
                pass

            elif color43 == red:
                color43 = teal
                hits-=1
                miss+=1
            
            else:
                color43 = teal
                miss+=1
                
            
        elif click[2] == 1:
            if color43 == red:
                pass

            elif color43 == teal:
                color43 = red
                miss-=1
                hits+=1
            
            else:
                color43 = red
                hits+=1
                
    else:
        pygame.draw.rect(gameDisplay,color43,(x,y,w,h))


def HMbutton44(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color44
    global hits
    global miss
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color44 == teal:
                pass

            elif color44 == red:
                color44 = teal
                hits-=1
                miss+=1
            
            else:
                color44 = teal
                miss+=1
                
            
        elif click[2] == 1:
            if color44 == red:
                pass

            elif color44 == teal:
                color44 = red
                miss-=1
                hits+=1
            
            else:
                color44 = red
                hits+=1
                
    else:
        pygame.draw.rect(gameDisplay,color44,(x,y,w,h))

def HMbutton45(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color45
    global hits
    global miss
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color45 == teal:
                pass

            elif color45 == red:
                color45 = teal
                hits-=1
                miss+=1
            
            else:
                color45 = teal
                miss+=1
                
            
        elif click[2] == 1:
            if color45 == red:
                pass

            elif color45 == teal:
                color45 = red
                miss-=1
                hits+=1
            
            else:
                color45 = red
                hits+=1
                
    else:
        pygame.draw.rect(gameDisplay,color45,(x,y,w,h))

def HMbutton46(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color46
    global hits
    global miss
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color46 == teal:
                pass

            elif color46 == red:
                color46 = teal
                hits-=1
                miss+=1
            
            else:
                color46 = teal
                miss+=1
                
            
        elif click[2] == 1:
            if color46 == red:
                pass

            elif color46 == teal:
                color46 = red
                miss-=1
                hits+=1
            
            else:
                color46 = red
                hits+=1
                
    else:
        pygame.draw.rect(gameDisplay,color46,(x,y,w,h))


def HMbutton47(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color47
    global hits
    global miss
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color47 == teal:
                pass

            elif color47 == red:
                color47 = teal
                hits-=1
                miss+=1
            
            else:
                color47 = teal
                miss+=1
                
            
        elif click[2] == 1:
            if color47 == red:
                pass

            elif color47 == teal:
                color47 = red
                miss-=1
                hits+=1
            
            else:
                color47 = red
                hits+=1
                
    else:
        pygame.draw.rect(gameDisplay,color47,(x,y,w,h))

def HMbutton48(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color48
    global hits
    global miss
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color48 == teal:
                pass

            elif color48 == red:
                color48 = teal
                hits-=1
                miss+=1
            
            else:
                color48 = teal
                miss+=1
                
            
        elif click[2] == 1:
            if color48 == red:
                pass

            elif color48 == teal:
                color48 = red
                miss-=1
                hits+=1
            
            else:
                color48 = red
                hits+=1
                
    else:
        pygame.draw.rect(gameDisplay,color48,(x,y,w,h))

def HMbutton49(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color49
    global hits
    global miss
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color49 == teal:
                pass

            elif color49 == red:
                color49 = teal
                hits-=1
                miss+=1
            
            else:
                color49 = teal
                miss+=1
                
            
        elif click[2] == 1:
            if color49 == red:
                pass

            elif color49 == teal:
                color49 = red
                miss-=1
                hits+=1
            
            else:
                color49 = red
                hits+=1
                
    else:
        pygame.draw.rect(gameDisplay,color49,(x,y,w,h))

#Tracking Buttons Function Definition--------------------------
        

#Hit Button Defintion--------------------------
def Hbutton1(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color50
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,light_red,(x,y,w,h),0,10)
        if click[0] == 1:
            color50 = red

        elif click[2] == 1:
            color50 = green
        
    else:
        pygame.draw.rect(gameDisplay,color50,(x,y,w,h),0,10)

def Hbutton2(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color51
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,light_red,(x,y,w,h),0,10)
        if click[0] == 1:
            color51 = red

        elif click[2] == 1:
            color51 = green
        
    else:
        pygame.draw.rect(gameDisplay,color51,(x,y,w,h),0,10)


def Hbutton3(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color52
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,light_red,(x,y,w,h),0,10)
        if click[0] == 1:
            color52 = red

        elif click[2] == 1:
            color52 = green
        
    else:
        pygame.draw.rect(gameDisplay,color52,(x,y,w,h),0,10)

def Hbutton4(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color53
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,light_red,(x,y,w,h),0,10)
        if click[0] == 1:
            color53 = red

        elif click[2] == 1:
            color53 = green
        
    else:
        pygame.draw.rect(gameDisplay,color53,(x,y,w,h),0,10)

def Hbutton5(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color54
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,light_red,(x,y,w,h),0,10)
        if click[0] == 1:
            color54 = red

        elif click[2] == 1:
            color54 = green
        
    else:
        pygame.draw.rect(gameDisplay,color54,(x,y,w,h),0,10)

def Hbutton6(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color55
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,light_red,(x,y,w,h),0,10)
        if click[0] == 1:
            color55 = red

        elif click[2] == 1:
            color55 = green
        
    else:
        pygame.draw.rect(gameDisplay,color55,(x,y,w,h),0,10)

#Level 1

def Hbutton7(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color105
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,light_red,(x,y,w,h),0,10)
        if click[0] == 1:
            color105 = red

        elif click[2] == 1:
            color105 = green
        
    else:
        pygame.draw.rect(gameDisplay,color105,(x,y,w,h),0,10)


def Hbutton8(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color106
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,light_red,(x,y,w,h),0,10)
        if click[0] == 1:
            color106 = red

        elif click[2] == 1:
            color106 = green
        
    else:
        pygame.draw.rect(gameDisplay,color106,(x,y,w,h),0,10)

def Hbutton9(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color107
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,light_red,(x,y,w,h),0,10)
        if click[0] == 1:
            color107 = red

        elif click[2] == 1:
            color107 = green
        
    else:
        pygame.draw.rect(gameDisplay,color107,(x,y,w,h),0,10)

def Hbutton10(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color108
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,light_red,(x,y,w,h),0,10)
        if click[0] == 1:
            color108 = red

        elif click[2] == 1:
            color108 = green
        
    else:
        pygame.draw.rect(gameDisplay,color108,(x,y,w,h),0,10)

def Hbutton11(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color109
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,light_red,(x,y,w,h),0,10)
        if click[0] == 1:
            color109 = red

        elif click[2] == 1:
            color109 = green
        
    else:
        pygame.draw.rect(gameDisplay,color109,(x,y,w,h),0,10)

def Hbutton12(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color110
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,light_red,(x,y,w,h),0,10)
        if click[0] == 1:
            color110 = red

        elif click[2] == 1:
            color110 = green
        
    else:
        pygame.draw.rect(gameDisplay,color110,(x,y,w,h),0,10)

#Level 3

def Hbutton13(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color160
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,light_red,(x,y,w,h),0,10)
        if click[0] == 1:
            color160 = red

        elif click[2] == 1:
            color160 = green
        
    else:
        pygame.draw.rect(gameDisplay,color160,(x,y,w,h),0,10)


def Hbutton14(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color161
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,light_red,(x,y,w,h),0,10)
        if click[0] == 1:
            color161 = red

        elif click[2] == 1:
            color161 = green
        
    else:
        pygame.draw.rect(gameDisplay,color161,(x,y,w,h),0,10)

def Hbutton15(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color162
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,light_red,(x,y,w,h),0,10)
        if click[0] == 1:
            color162 = red

        elif click[2] == 1:
            color162 = green
        
    else:
        pygame.draw.rect(gameDisplay,color162,(x,y,w,h),0,10)

def Hbutton16(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color163
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,light_red,(x,y,w,h),0,10)
        if click[0] == 1:
            color163 = red

        elif click[2] == 1:
            color163 = green
        
    else:
        pygame.draw.rect(gameDisplay,color163,(x,y,w,h),0,10)

def Hbutton17(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color164
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,light_red,(x,y,w,h),0,10)
        if click[0] == 1:
            color164 = red

        elif click[2] == 1:
            color164 = green
        
    else:
        pygame.draw.rect(gameDisplay,color164,(x,y,w,h),0,10)

def Hbutton18(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color165
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,light_red,(x,y,w,h),0,10)
        if click[0] == 1:
            color165 = red

        elif click[2] == 1:
            color165 = green
        
    else:
        pygame.draw.rect(gameDisplay,color165,(x,y,w,h),0,10)

#Hit Button Defintion--------------------------

#Level 2 Technically Level 1 HM Buttons

def HMbutton50(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color56
    global hits2
    global miss2
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color56 == teal:
                pass

            elif color56 == red:
                color56 = teal
                hits2-=1
                miss2+=1
            
            else:
                color56 = teal
                miss2+=1
               
            
        elif click[2] == 1:
            if color56 == red:
                pass

            elif color56 == teal:
                color56 = red
                miss2-=1
                hits2+=1
            
            else:
                color56 = red
                hits2+=1
                
    else:
        pygame.draw.rect(gameDisplay,color56,(x,y,w,h))

def HMbutton51(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color57
    global hits2
    global miss2
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color57 == teal:
                pass

            elif color57 == red:
                color57 = teal
                hits2-=1
                miss2+=1
            
            else:
                color57 = teal
                miss2+=1
                
            
        elif click[2] == 1:
            if color57 == red:
                pass

            elif color57 == teal:
                color57 = red
                miss2-=1
                hits2+=1
            
            else:
                color57 = red
                hits2+=1
                
    else:
        pygame.draw.rect(gameDisplay,color57,(x,y,w,h))

def HMbutton52(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color58
    global hits2
    global miss2
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color58 == teal:
                pass

            elif color58 == red:
                color58 = teal
                hits2-=1
                miss2+=1
            
            else:
                color58 = teal
                miss2+=1
                
            
        elif click[2] == 1:
            if color58 == red:
                pass

            elif color58 == teal:
                color58 = red
                miss2-=1
                hits2+=1
            
            else:
                color58 = red
                hits2+=1
                
    else:
        pygame.draw.rect(gameDisplay,color58,(x,y,w,h))

def HMbutton53(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color59
    global hits2
    global miss2
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color59 == teal:
                pass

            elif color59 == red:
                color59 = teal
                hits2-=1
                miss2+=1
            
            else:
                color59 = teal
                miss2+=1
                
            
        elif click[2] == 1:
            if color59 == red:
                pass

            elif color59 == teal:
                color59 = red
                miss2-=1
                hits2+=1
            
            else:
                color59 = red
                hits2+=1
                
    else:
        pygame.draw.rect(gameDisplay,color59,(x,y,w,h))
        
def HMbutton54(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color60
    global hits2
    global miss2
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color60 == teal:
                pass

            elif color60 == red:
                color60 = teal
                hits2-=1
                miss2+=1
            
            else:
                color60 = teal
                miss2+=1
                
            
        elif click[2] == 1:
            if color60 == red:
                pass

            elif color60 == teal:
                color60 = red
                miss2-=1
                hits2+=1
            
            else:
                color60 = red
                hits2+=1
                
    else:
        pygame.draw.rect(gameDisplay,color60,(x,y,w,h))

def HMbutton55(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color61
    global hits2
    global miss2
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color61 == teal:
                pass

            elif color61 == red:
                color61 = teal
                hits2-=1
                miss2+=1
            
            else:
                color61 = teal
                miss2+=1
                
            
        elif click[2] == 1:
            if color61 == red:
                pass

            elif color61 == teal:
                color61 = red
                miss2-=1
                hits2+=1
            
            else:
                color61 = red
                hits2+=1
                
    else:
        pygame.draw.rect(gameDisplay,color61,(x,y,w,h))

def HMbutton56(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color62
    global hits2
    global miss2
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color62 == teal:
                pass

            elif color62 == red:
                color62 = teal
                hits2-=1
                miss2+=1
            
            else:
                color62 = teal
                miss2+=1
                
            
        elif click[2] == 1:
            if color62 == red:
                pass

            elif color62 == teal:
                color62 = red
                miss2-=1
                hits2+=1
            
            else:
                color62 = red
                hits2+=1
                
    else:
        pygame.draw.rect(gameDisplay,color62,(x,y,w,h))

def HMbutton57(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color63
    global hits2
    global miss2
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color63 == teal:
                pass

            elif color63 == red:
                color63 = teal
                hits2-=1
                miss2+=1
            
            else:
                color63 = teal
                miss2+=1
                
            
        elif click[2] == 1:
            if color63 == red:
                pass

            elif color63 == teal:
                color63 = red
                miss2-=1
                hits2+=1
            
            else:
                color63 = red
                hits2+=1
                
    else:
        pygame.draw.rect(gameDisplay,color63,(x,y,w,h))

def HMbutton58(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color64
    global hits2
    global miss2
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color64 == teal:
                pass

            elif color64 == red:
                color64 = teal
                hits2-=1
                miss2+=1
            
            else:
                color64 = teal
                miss2+=1
                
            
        elif click[2] == 1:
            if color64 == red:
                pass

            elif color64 == teal:
                color64 = red
                miss2-=1
                hits2+=1
            
            else:
                color64 = red
                hits2+=1
                
    else:
        pygame.draw.rect(gameDisplay,color64,(x,y,w,h))

def HMbutton59(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color65
    global hits2
    global miss2
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color65 == teal:
                pass

            elif color65 == red:
                color65 = teal
                hits2-=1
                miss2+=1
            
            else:
                color65 = teal
                miss2+=1
                
            
        elif click[2] == 1:
            if color65 == red:
                pass

            elif color65 == teal:
                color65 = red
                miss2-=1
                hits2+=1
            
            else:
                color65 = red
                hits2+=1
                
    else:
        pygame.draw.rect(gameDisplay,color65,(x,y,w,h))

def HMbutton60(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color66
    global hits2
    global miss2
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color66 == teal:
                pass

            elif color66 == red:
                color66 = teal
                hits2-=1
                miss2+=1
            
            else:
                color66 = teal
                miss2+=1
                
            
        elif click[2] == 1:
            if color66 == red:
                pass

            elif color66 == teal:
                color66 = red
                miss2-=1
                hits2+=1
            
            else:
                color66 = red
                hits2+=1
                
    else:
        pygame.draw.rect(gameDisplay,color66,(x,y,w,h))

def HMbutton61(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color67
    global hits2
    global miss2
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color67 == teal:
                pass

            elif color67 == red:
                color67 = teal
                hits2-=1
                miss2+=1
            
            else:
                color67 = teal
                miss2+=1
                
            
        elif click[2] == 1:
            if color67 == red:
                pass

            elif color67 == teal:
                color67 = red
                miss2-=1
                hits2+=1
            
            else:
                color67 = red
                hits2+=1
                
    else:
        pygame.draw.rect(gameDisplay,color67,(x,y,w,h))

def HMbutton62(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color68
    global hits2
    global miss2
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color68 == teal:
                pass

            elif color68 == red:
                color68 = teal
                hits2-=1
                miss2+=1
            
            else:
                color68 = teal
                miss2+=1
                
            
        elif click[2] == 1:
            if color68 == red:
                pass

            elif color68 == teal:
                color68 = red
                miss2-=1
                hits2+=1
            
            else:
                color68 = red
                hits2+=1
                
    else:
        pygame.draw.rect(gameDisplay,color68,(x,y,w,h))

def HMbutton63(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color69
    global hits2
    global miss2
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color69 == teal:
                pass

            elif color69 == red:
                color69 = teal
                hits2-=1
                miss2+=1
            
            else:
                color69 = teal
                miss2+=1
                
            
        elif click[2] == 1:
            if color69 == red:
                pass

            elif color69 == teal:
                color69 = red
                miss2-=1
                hits2+=1
            
            else:
                color69 = red
                hits2+=1
                
    else:
        pygame.draw.rect(gameDisplay,color69,(x,y,w,h))

def HMbutton64(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color70
    global hits2
    global miss2
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color70 == teal:
                pass

            elif color70 == red:
                color70 = teal
                hits2-=1
                miss2+=1
            
            else:
                color70 = teal
                miss2+=1
                
            
        elif click[2] == 1:
            if color70 == red:
                pass

            elif color70 == teal:
                color70 = red
                miss2-=1
                hits2+=1
            
            else:
                color70 = red
                hits2+=1
                
    else:
        pygame.draw.rect(gameDisplay,color70,(x,y,w,h))

def HMbutton65(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color71
    global hits2
    global miss2
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color71 == teal:
                pass

            elif color71 == red:
                color71 = teal
                hits2-=1
                miss2+=1
            
            else:
                color71 = teal
                miss2+=1
                
            
        elif click[2] == 1:
            if color71 == red:
                pass

            elif color71 == teal:
                color71 = red
                miss2-=1
                hits2+=1
            
            else:
                color71 = red
                hits2+=1
                
    else:
        pygame.draw.rect(gameDisplay,color71,(x,y,w,h))


def HMbutton66(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color72
    global hits2
    global miss2
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color72 == teal:
                pass

            elif color72 == red:
                color72 = teal
                hits2-=1
                miss2+=1
            
            else:
                color72 = teal
                miss2+=1
                
            
        elif click[2] == 1:
            if color72 == red:
                pass

            elif color72 == teal:
                color72 = red
                miss2-=1
                hits2+=1
            
            else:
                color72 = red
                hits2+=1
                
    else:
        pygame.draw.rect(gameDisplay,color72,(x,y,w,h))

def HMbutton67(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color73
    global hits2
    global miss2
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color73 == teal:
                pass

            elif color73 == red:
                color73 = teal
                hits2-=1
                miss2+=1
            
            else:
                color73 = teal
                miss2+=1
                
            
        elif click[2] == 1:
            if color73 == red:
                pass

            elif color73 == teal:
                color73 = red
                miss2-=1
                hits2+=1
            
            else:
                color73 = red
                hits2+=1
                
    else:
        pygame.draw.rect(gameDisplay,color73,(x,y,w,h))

def HMbutton68(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color74
    global hits2
    global miss2
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color74 == teal:
                pass

            elif color74 == red:
                color74 = teal
                hits2-=1
                miss2+=1
            
            else:
                color74 = teal
                miss2+=1
                
            
        elif click[2] == 1:
            if color74 == red:
                pass

            elif color74 == teal:
                color74 = red
                miss2-=1
                hits2+=1
            
            else:
                color74 = red
                hits2+=1
                
    else:
        pygame.draw.rect(gameDisplay,color74,(x,y,w,h))
        
def HMbutton69(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color75
    global hits2
    global miss2
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color75 == teal:
                pass

            elif color75 == red:
                color75 = teal
                hits2-=1
                miss2+=1
            
            else:
                color75 = teal
                miss2+=1
                
            
        elif click[2] == 1:
            if color75 == red:
                pass

            elif color75 == teal:
                color75 = red
                miss2-=1
                hits2+=1
            
            else:
                color75 = red
                hits2+=1
                
    else:
        pygame.draw.rect(gameDisplay,color75,(x,y,w,h))

def HMbutton70(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color76
    global hits2
    global miss2
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color76 == teal:
                pass

            elif color76 == red:
                color76 = teal
                hits2-=1
                miss2+=1
            
            else:
                color76 = teal
                miss2+=1
                
            
        elif click[2] == 1:
            if color76 == red:
                pass

            elif color76 == teal:
                color76 = red
                miss2-=1
                hits2+=1
            
            else:
                color76 = red
                hits2+=1
                
    else:
        pygame.draw.rect(gameDisplay,color76,(x,y,w,h))

def HMbutton71(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color77
    global hits2
    global miss2
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color77 == teal:
                pass

            elif color77 == red:
                color77 = teal
                hits2-=1
                miss2+=1
            
            else:
                color77 = teal
                miss2+=1
                
            
        elif click[2] == 1:
            if color77 == red:
                pass

            elif color77 == teal:
                color77 = red
                miss2-=1
                hits2+=1
            
            else:
                color77 = red
                hits2+=1
                
    else:
        pygame.draw.rect(gameDisplay,color77,(x,y,w,h))
        
def HMbutton72(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color78
    global hits2
    global miss2
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color78 == teal:
                pass

            elif color78 == red:
                color78 = teal
                hits2-=1
                miss2+=1
            
            else:
                color78 = teal
                miss2+=1
                
            
        elif click[2] == 1:
            if color78 == red:
                pass

            elif color78 == teal:
                color78 = red
                miss2-=1
                hits2+=1
            
            else:
                color78 = red
                hits2+=1
                
    else:
        pygame.draw.rect(gameDisplay,color78,(x,y,w,h))
        

def HMbutton73(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color79
    global hits2
    global miss2
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color79 == teal:
                pass

            elif color79 == red:
                color79 = teal
                hits2-=1
                miss2+=1
            
            else:
                color79 = teal
                miss2+=1
                
            
        elif click[2] == 1:
            if color79 == red:
                pass

            elif color79 == teal:
                color79 = red
                miss2-=1
                hits2+=1
            
            else:
                color79 = red
                hits2+=1
                
    else:
        pygame.draw.rect(gameDisplay,color79,(x,y,w,h))

def HMbutton74(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color80
    global hits2
    global miss2
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color80 == teal:
                pass

            elif color80 == red:
                color80 = teal
                hits2-=1
                miss2+=1
            
            else:
                color80 = teal
                miss2+=1
                
            
        elif click[2] == 1:
            if color80 == red:
                pass

            elif color80 == teal:
                color80 = red
                miss2-=1
                hits2+=1
            
            else:
                color80 = red
                hits2+=1
                
    else:
        pygame.draw.rect(gameDisplay,color80,(x,y,w,h))

def HMbutton75(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color81
    global hits2
    global miss2
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color81 == teal:
                pass

            elif color81 == red:
                color81 = teal
                hits2-=1
                miss2+=1
            
            else:
                color81 = teal
                miss2+=1
                
            
        elif click[2] == 1:
            if color81 == red:
                pass

            elif color81 == teal:
                color81 = red
                miss2-=1
                hits2+=1
            
            else:
                color81 = red
                hits2+=1
                
    else:
        pygame.draw.rect(gameDisplay,color81,(x,y,w,h))
        
def HMbutton76(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color82
    global hits2
    global miss2
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color82 == teal:
                pass

            elif color82 == red:
                color82 = teal
                hits2-=1
                miss2+=1
            
            else:
                color82 = teal
                miss2+=1
                
            
        elif click[2] == 1:
            if color82 == red:
                pass

            elif color82 == teal:
                color82 = red
                miss2-=1
                hits2+=1
            
            else:
                color82 = red
                hits2+=1
                
    else:
        pygame.draw.rect(gameDisplay,color82,(x,y,w,h))

def HMbutton77(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color83
    global hits2
    global miss2
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color83 == teal:
                pass

            elif color83 == red:
                color83 = teal
                hits2-=1
                miss2+=1
            
            else:
                color83 = teal
                miss2+=1
                
            
        elif click[2] == 1:
            if color83 == red:
                pass

            elif color83 == teal:
                color83 = red
                miss2-=1
                hits2+=1
            
            else:
                color83 = red
                hits2+=1
                
    else:
        pygame.draw.rect(gameDisplay,color83,(x,y,w,h))

def HMbutton78(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color84
    global hits2
    global miss2
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color84 == teal:
                pass

            elif color84 == red:
                color84 = teal
                hits2-=1
                miss2+=1
            
            else:
                color84 = teal
                miss2+=1
                
            
        elif click[2] == 1:
            if color84 == red:
                pass

            elif color84 == teal:
                color84 = red
                miss2-=1
                hits2+=1
            
            else:
                color84 = red
                hits2+=1
                
    else:
        pygame.draw.rect(gameDisplay,color84,(x,y,w,h))


def HMbutton79(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color85
    global hits2
    global miss2
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color85 == teal:
                pass

            elif color85 == red:
                color85 = teal
                hits2-=1
                miss2+=1
            
            else:
                color85 = teal
                miss2+=1
                
            
        elif click[2] == 1:
            if color85 == red:
                pass

            elif color85 == teal:
                color85 = red
                miss2-=1
                hits2+=1
            
            else:
                color85 = red
                hits2+=1
                
    else:
        pygame.draw.rect(gameDisplay,color85,(x,y,w,h))

def HMbutton80(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color86
    global hits2
    global miss2
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color86 == teal:
                pass

            elif color86 == red:
                color86 = teal
                hits2-=1
                miss2+=1
            
            else:
                color86 = teal
                miss2+=1
                
            
        elif click[2] == 1:
            if color86 == red:
                pass

            elif color86 == teal:
                color86 = red
                miss2-=1
                hits2+=1
            
            else:
                color86 = red
                hits2+=1
                
    else:
        pygame.draw.rect(gameDisplay,color86,(x,y,w,h))

def HMbutton81(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color87
    global hits2
    global miss2
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color87 == teal:
                pass

            elif color87 == red:
                color87 = teal
                hits2-=1
                miss2+=1
            
            else:
                color87 = teal
                miss2+=1
                
            
        elif click[2] == 1:
            if color87 == red:
                pass

            elif color87 == teal:
                color87 = red
                miss2-=1
                hits2+=1
            
            else:
                color87 = red
                hits2+=1
                
    else:
        pygame.draw.rect(gameDisplay,color87,(x,y,w,h))

def HMbutton82(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color88
    global hits2
    global miss2
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color88 == teal:
                pass

            elif color88 == red:
                color88 = teal
                hits2-=1
                miss2+=1
            
            else:
                color88 = teal
                miss2+=1
                
            
        elif click[2] == 1:
            if color88 == red:
                pass

            elif color88 == teal:
                color88 = red
                miss2-=1
                hits2+=1
            
            else:
                color88 = red
                hits2+=1
                
    else:
        pygame.draw.rect(gameDisplay,color88,(x,y,w,h))
        
def HMbutton83(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color89
    global hits2
    global miss2
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color89 == teal:
                pass

            elif color89 == red:
                color89 = teal
                hits2-=1
                miss2+=1
            
            else:
                color89 = teal
                miss2+=1
                
            
        elif click[2] == 1:
            if color89 == red:
                pass

            elif color89 == teal:
                color89 = red
                miss2-=1
                hits2+=1
            
            else:
                color89 = red
                hits2+=1
                
    else:
        pygame.draw.rect(gameDisplay,color89,(x,y,w,h))

def HMbutton84(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color90
    global hits2
    global miss2
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color90 == teal:
                pass

            elif color90 == red:
                color90 = teal
                hits2-=1
                miss2+=1
            
            else:
                color90 = teal
                miss2+=1
                
            
        elif click[2] == 1:
            if color90 == red:
                pass

            elif color90 == teal:
                color90 = red
                miss2-=1
                hits2+=1
            
            else:
                color90 = red
                hits2+=1
                
    else:
        pygame.draw.rect(gameDisplay,color90,(x,y,w,h))

def HMbutton85(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color91
    global hits2
    global miss2
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color91 == teal:
                pass

            elif color91 == red:
                color91 = teal
                hits2-=1
                miss2+=1
            
            else:
                color91 = teal
                miss2+=1
                
            
        elif click[2] == 1:
            if color91 == red:
                pass

            elif color91 == teal:
                color91 = red
                miss2-=1
                hits2+=1
            
            else:
                color91 = red
                hits2+=1
                
    else:
        pygame.draw.rect(gameDisplay,color91,(x,y,w,h))


def HMbutton86(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color92
    global hits2
    global miss2
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color92 == teal:
                pass

            elif color92 == red:
                color92 = teal
                hits2-=1
                miss2+=1
            
            else:
                color92 = teal
                miss2+=1
                
            
        elif click[2] == 1:
            if color92 == red:
                pass

            elif color92 == teal:
                color92 = red
                miss2-=1
                hits2+=1
            
            else:
                color92 = red
                hits2+=1
                
    else:
        pygame.draw.rect(gameDisplay,color92,(x,y,w,h))

def HMbutton87(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color93
    global hits2
    global miss2
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color93 == teal:
                pass

            elif color93 == red:
                color93 = teal
                hits2-=1
                miss2+=1
            
            else:
                color93 = teal
                miss2+=1
                
            
        elif click[2] == 1:
            if color93 == red:
                pass

            elif color93 == teal:
                color93 = red
                miss2-=1
                hits2+=1
            
            else:
                color93 = red
                hits2+=1
                
    else:
        pygame.draw.rect(gameDisplay,color93,(x,y,w,h))


def HMbutton88(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color94
    global hits2
    global miss2
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color94 == teal:
                pass

            elif color94 == red:
                color94 = teal
                hits2-=1
                miss2+=1
            
            else:
                color94 = teal
                miss2+=1
                
            
        elif click[2] == 1:
            if color94 == red:
                pass

            elif color94 == teal:
                color94 = red
                miss2-=1
                hits2+=1
            
            else:
                color94 = red
                hits2+=1
                
    else:
        pygame.draw.rect(gameDisplay,color94,(x,y,w,h))
        
def HMbutton89(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color95
    global hits2
    global miss2
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color95 == teal:
                pass

            elif color95 == red:
                color95 = teal
                hits2-=1
                miss2+=1
            
            else:
                color95 = teal
                miss2+=1
                
            
        elif click[2] == 1:
            if color95 == red:
                pass

            elif color95 == teal:
                color95 = red
                miss2-=1
                hits2+=1
            
            else:
                color95 = red
                hits2+=1
                
    else:
        pygame.draw.rect(gameDisplay,color95,(x,y,w,h))
        
def HMbutton90(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color96
    global hits2
    global miss2
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color96 == teal:
                pass

            elif color96 == red:
                color96 = teal
                hits2-=1
                miss2+=1
            
            else:
                color96 = teal
                miss2+=1
                
            
        elif click[2] == 1:
            if color96 == red:
                pass

            elif color96 == teal:
                color96 = red
                miss2-=1
                hits2+=1
            
            else:
                color96 = red
                hits2+=1
                
    else:
        pygame.draw.rect(gameDisplay,color96,(x,y,w,h))
        
def HMbutton91(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color97
    global hits2
    global miss2
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color97 == teal:
                pass

            elif color97 == red:
                color97 = teal
                hits2-=1
                miss2+=1
            
            else:
                color97 = teal
                miss2+=1
                
            
        elif click[2] == 1:
            if color97 == red:
                pass

            elif color97 == teal:
                color97 = red
                miss2-=1
                hits2+=1
            
            else:
                color97 = red
                hits2+=1
                
    else:
        pygame.draw.rect(gameDisplay,color97,(x,y,w,h))

def HMbutton92(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color98
    global hits2
    global miss2
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color98 == teal:
                pass

            elif color98 == red:
                color98 = teal
                hits2-=1
                miss2+=1
            
            else:
                color98 = teal
                miss2+=1
                
            
        elif click[2] == 1:
            if color98 == red:
                pass

            elif color98 == teal:
                color98 = red
                miss2-=1
                hits2+=1
            
            else:
                color98 = red
                hits2+=1
                
    else:
        pygame.draw.rect(gameDisplay,color98,(x,y,w,h))


def HMbutton93(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color99
    global hits2
    global miss2
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color99 == teal:
                pass

            elif color99 == red:
                color99 = teal
                hits2-=1
                miss2+=1
            
            else:
                color99 = teal
                miss2+=1
                
            
        elif click[2] == 1:
            if color99 == red:
                pass

            elif color99 == teal:
                color99 = red
                miss2-=1
                hits2+=1
            
            else:
                color99 = red
                hits2+=1
                
    else:
        pygame.draw.rect(gameDisplay,color99,(x,y,w,h))

def HMbutton94(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color100
    global hits2
    global miss2
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color100 == teal:
                pass

            elif color100 == red:
                color100 = teal
                hits2-=1
                miss2+=1
            
            else:
                color100 = teal
                miss2+=1
                
            
        elif click[2] == 1:
            if color100 == red:
                pass

            elif color100 == teal:
                color100 = red
                miss2-=1
                hits2+=1
            
            else:
                color100 = red
                hits2+=1
                
    else:
        pygame.draw.rect(gameDisplay,color100,(x,y,w,h))

def HMbutton95(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color101
    global hits2
    global miss2
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color101 == teal:
                pass

            elif color101 == red:
                color101 = teal
                hits2-=1
                miss2+=1
            
            else:
                color101 = teal
                miss2+=1
                
            
        elif click[2] == 1:
            if color101 == red:
                pass

            elif color101 == teal:
                color101 = red
                miss2-=1
                hits2+=1
            
            else:
                color101 = red
                hits2+=1
                
    else:
        pygame.draw.rect(gameDisplay,color101,(x,y,w,h))


def HMbutton96(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color102
    global hits2
    global miss2
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color102 == teal:
                pass

            elif color102 == red:
                color102 = teal
                hits2-=1
                miss2+=1
            
            else:
                color102 = teal
                miss2+=1
                
            
        elif click[2] == 1:
            if color102 == red:
                pass

            elif color102 == teal:
                color102 = red
                miss2-=1
                hits2+=1
            
            else:
                color102 = red
                hits2+=1
                
    else:
        pygame.draw.rect(gameDisplay,color102,(x,y,w,h))

def HMbutton97(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color103
    global hits2
    global miss2
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color103 == teal:
                pass

            elif color103 == red:
                color103 = teal
                hits2-=1
                miss2+=1
            
            else:
                color103 = teal
                miss2+=1
                
            
        elif click[2] == 1:
            if color103 == red:
                pass

            elif color103 == teal:
                color103 = red
                miss2-=1
                hits2+=1
            
            else:
                color103 = red
                hits2+=1
                
    else:
        pygame.draw.rect(gameDisplay,color103,(x,y,w,h))

def HMbutton98(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color104
    global hits2
    global miss2
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color104 == teal:
                pass

            elif color104 == red:
                color104 = teal
                hits2-=1
                miss2+=1
            
            else:
                color104 = teal
                miss2+=1
                
            
        elif click[2] == 1:
            if color104 == red:
                pass

            elif color104 == teal:
                color104 = red
                miss2-=1
                hits2+=1
            
            else:
                color104 = red
                hits2+=1
                
    else:
        pygame.draw.rect(gameDisplay,color104,(x,y,w,h))

def HMbutton99(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color111
    global hits3
    global miss3
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color111 == teal:
                pass

            elif color111 == red:
                color111 = teal
                hits3-=1
                miss3+=1
            
            else:
                color111 = teal
                miss3+=1
               
            
        elif click[2] == 1:
            if color111 == red:
                pass

            elif color111 == teal:
                color111 = red
                miss3-=1
                hits3+=1
            
            else:
                color111 = red
                hits3+=1
                
    else:
        pygame.draw.rect(gameDisplay,color111,(x,y,w,h))

def HMbutton100(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color112
    global hits3
    global miss3
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color112 == teal:
                pass

            elif color112 == red:
                color112 = teal
                hits3-=1
                miss3+=1
            
            else:
                color112 = teal
                miss3+=1
                
            
        elif click[2] == 1:
            if color112 == red:
                pass

            elif color112 == teal:
                color112 = red
                miss3-=1
                hits3+=1
            
            else:
                color112 = red
                hits3+=1
                
    else:
        pygame.draw.rect(gameDisplay,color112,(x,y,w,h))

def HMbutton101(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color113
    global hits3
    global miss3
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color113 == teal:
                pass

            elif color113 == red:
                color113 = teal
                hits3-=1
                miss3+=1
            
            else:
                color113 = teal
                miss3+=1
                
            
        elif click[2] == 1:
            if color113 == red:
                pass

            elif color113 == teal:
                color113 = red
                miss3-=1
                hits3+=1
            
            else:
                color113 = red
                hits3+=1
                
    else:
        pygame.draw.rect(gameDisplay,color113,(x,y,w,h))

def HMbutton102(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color114
    global hits3
    global miss3
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color114 == teal:
                pass

            elif color114 == red:
                color114 = teal
                hits3-=1
                miss3+=1
            
            else:
                color114 = teal
                miss3+=1
                
            
        elif click[2] == 1:
            if color114 == red:
                pass

            elif color114 == teal:
                color114 = red
                miss3-=1
                hits3+=1
            
            else:
                color114 = red
                hits3+=1
                
    else:
        pygame.draw.rect(gameDisplay,color114,(x,y,w,h))
        
def HMbutton103(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color115
    global hits3
    global miss3
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color115 == teal:
                pass

            elif color115 == red:
                color115 = teal
                hits3-=1
                miss3+=1
            
            else:
                color115 = teal
                miss3+=1
                
            
        elif click[2] == 1:
            if color115 == red:
                pass

            elif color115 == teal:
                color115 = red
                miss3-=1
                hits3+=1
            
            else:
                color115 = red
                hits3+=1
                
    else:
        pygame.draw.rect(gameDisplay,color115,(x,y,w,h))

def HMbutton104(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color116
    global hits3
    global miss3
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color116 == teal:
                pass

            elif color116 == red:
                color116 = teal
                hits3-=1
                miss3+=1
            
            else:
                color116 = teal
                miss3+=1
                
            
        elif click[2] == 1:
            if color116 == red:
                pass

            elif color116 == teal:
                color116 = red
                miss3-=1
                hits3+=1
            
            else:
                color116 = red
                hits3+=1
                
    else:
        pygame.draw.rect(gameDisplay,color116,(x,y,w,h))

def HMbutton105(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color117
    global hits3
    global miss3
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color117 == teal:
                pass

            elif color117 == red:
                color117 = teal
                hits3-=1
                miss3+=1
            
            else:
                color117 = teal
                miss3+=1
                
            
        elif click[2] == 1:
            if color117 == red:
                pass

            elif color117 == teal:
                color117 = red
                miss3-=1
                hits3+=1
            
            else:
                color117 = red
                hits3+=1
                
    else:
        pygame.draw.rect(gameDisplay,color117,(x,y,w,h))

def HMbutton106(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color118
    global hits3
    global miss3
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color118 == teal:
                pass

            elif color118 == red:
                color118 = teal
                hits3-=1
                miss3+=1
            
            else:
                color118 = teal
                miss3+=1
                
            
        elif click[2] == 1:
            if color118 == red:
                pass

            elif color118 == teal:
                color118 = red
                miss3-=1
                hits3+=1
            
            else:
                color118 = red
                hits3+=1
                
    else:
        pygame.draw.rect(gameDisplay,color118,(x,y,w,h))

def HMbutton107(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color119
    global hits3
    global miss3
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color119 == teal:
                pass

            elif color119 == red:
                color119 = teal
                hits3-=1
                miss3+=1
            
            else:
                color119 = teal
                miss3+=1
                
            
        elif click[2] == 1:
            if color119 == red:
                pass

            elif color119 == teal:
                color119 = red
                miss3-=1
                hits3+=1
            
            else:
                color119 = red
                hits3+=1
                
    else:
        pygame.draw.rect(gameDisplay,color119,(x,y,w,h))

def HMbutton108(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color120
    global hits3
    global miss3
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color120 == teal:
                pass

            elif color120 == red:
                color120 = teal
                hits3-=1
                miss3+=1
            
            else:
                color120 = teal
                miss3+=1
                
            
        elif click[2] == 1:
            if color120 == red:
                pass

            elif color120 == teal:
                color120 = red
                miss3-=1
                hits3+=1
            
            else:
                color120 = red
                hits3+=1
                
    else:
        pygame.draw.rect(gameDisplay,color120,(x,y,w,h))

def HMbutton109(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color121
    global hits3
    global miss3
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color121 == teal:
                pass

            elif color121 == red:
                color121 = teal
                hits3-=1
                miss3+=1
            
            else:
                color121 = teal
                miss3+=1
                
            
        elif click[2] == 1:
            if color121 == red:
                pass

            elif color121 == teal:
                color121 = red
                miss3-=1
                hits3+=1
            
            else:
                color121 = red
                hits3+=1
                
    else:
        pygame.draw.rect(gameDisplay,color121,(x,y,w,h))

def HMbutton110(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color122
    global hits3
    global miss3
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color122 == teal:
                pass

            elif color122 == red:
                color122 = teal
                hits3-=1
                miss3+=1
            
            else:
                color122 = teal
                miss3+=1
                
            
        elif click[2] == 1:
            if color122 == red:
                pass

            elif color122 == teal:
                color122 = red
                miss3-=1
                hits3+=1
            
            else:
                color122 = red
                hits3+=1
                
    else:
        pygame.draw.rect(gameDisplay,color122,(x,y,w,h))

def HMbutton111(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color123
    global hits3
    global miss3
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color123 == teal:
                pass

            elif color123 == red:
                color123 = teal
                hits3-=1
                miss3+=1
            
            else:
                color123 = teal
                miss3+=1
                
            
        elif click[2] == 1:
            if color123 == red:
                pass

            elif color123 == teal:
                color123 = red
                miss3-=1
                hits3+=1
            
            else:
                color123 = red
                hits3+=1
                
    else:
        pygame.draw.rect(gameDisplay,color123,(x,y,w,h))

def HMbutton112(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color124
    global hits3
    global miss3
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color124 == teal:
                pass

            elif color124 == red:
                color124 = teal
                hits3-=1
                miss3+=1
            
            else:
                color124 = teal
                miss3+=1
                
            
        elif click[2] == 1:
            if color124 == red:
                pass

            elif color124 == teal:
                color124 = red
                miss3-=1
                hits3+=1
            
            else:
                color124 = red
                hits3+=1
                
    else:
        pygame.draw.rect(gameDisplay,color124,(x,y,w,h))

def HMbutton113(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color125
    global hits3
    global miss3
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color125 == teal:
                pass

            elif color125 == red:
                color125 = teal
                hits3-=1
                miss3+=1
            
            else:
                color125 = teal
                miss3+=1
                
            
        elif click[2] == 1:
            if color125 == red:
                pass

            elif color125 == teal:
                color125 = red
                miss3-=1
                hits3+=1
            
            else:
                color125 = red
                hits3+=1
                
    else:
        pygame.draw.rect(gameDisplay,color125,(x,y,w,h))

def HMbutton114(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color126
    global hits3
    global miss3
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color126 == teal:
                pass

            elif color126 == red:
                color126 = teal
                hits3-=1
                miss3+=1
            
            else:
                color126 = teal
                miss3+=1
                
            
        elif click[2] == 1:
            if color126 == red:
                pass

            elif color126 == teal:
                color126 = red
                miss3-=1
                hits3+=1
            
            else:
                color126 = red
                hits3+=1
                
    else:
        pygame.draw.rect(gameDisplay,color126,(x,y,w,h))


def HMbutton115(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color127
    global hits3
    global miss3
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color127 == teal:
                pass

            elif color127 == red:
                color127 = teal
                hits3-=1
                miss3+=1
            
            else:
                color127 = teal
                miss3+=1
                
            
        elif click[2] == 1:
            if color127 == red:
                pass

            elif color127 == teal:
                color127 = red
                miss3-=1
                hits3+=1
            
            else:
                color127 = red
                hits3+=1
                
    else:
        pygame.draw.rect(gameDisplay,color127,(x,y,w,h))

def HMbutton116(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color128
    global hits3
    global miss3
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color128 == teal:
                pass

            elif color128 == red:
                color128 = teal
                hits3-=1
                miss3+=1
            
            else:
                color128 = teal
                miss3+=1
                
            
        elif click[2] == 1:
            if color128 == red:
                pass

            elif color128 == teal:
                color128 = red
                miss3-=1
                hits3+=1
            
            else:
                color128 = red
                hits3+=1
                
    else:
        pygame.draw.rect(gameDisplay,color128,(x,y,w,h))

def HMbutton117(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color129
    global hits3
    global miss3
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color129 == teal:
                pass

            elif color129 == red:
                color129 = teal
                hits3-=1
                miss3+=1
            
            else:
                color129 = teal
                miss3+=1
                
            
        elif click[2] == 1:
            if color129 == red:
                pass

            elif color129 == teal:
                color129 = red
                miss3-=1
                hits3+=1
            
            else:
                color129 = red
                hits3+=1
                
    else:
        pygame.draw.rect(gameDisplay,color129,(x,y,w,h))
        
def HMbutton118(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color130
    global hits3
    global miss3
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color130 == teal:
                pass

            elif color130 == red:
                color130 = teal
                hits3-=1
                miss3+=1
            
            else:
                color130 = teal
                miss3+=1
                
            
        elif click[2] == 1:
            if color130 == red:
                pass

            elif color130 == teal:
                color130 = red
                miss3-=1
                hits3+=1
            
            else:
                color130 = red
                hits3+=1
                
    else:
        pygame.draw.rect(gameDisplay,color130,(x,y,w,h))

def HMbutton119(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color131
    global hits3
    global miss3
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color131 == teal:
                pass

            elif color131 == red:
                color131 = teal
                hits3-=1
                miss3+=1
            
            else:
                color131 = teal
                miss3+=1
                
            
        elif click[2] == 1:
            if color131 == red:
                pass

            elif color131 == teal:
                color131 = red
                miss3-=1
                hits3+=1
            
            else:
                color131 = red
                hits3+=1
                
    else:
        pygame.draw.rect(gameDisplay,color131,(x,y,w,h))

def HMbutton120(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color132
    global hits3
    global miss3
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color132 == teal:
                pass

            elif color132 == red:
                color132 = teal
                hits3-=1
                miss3+=1
            
            else:
                color132 = teal
                miss3+=1
                
            
        elif click[2] == 1:
            if color132 == red:
                pass

            elif color132 == teal:
                color132 = red
                miss3-=1
                hits3+=1
            
            else:
                color132 = red
                hits3+=1
                
    else:
        pygame.draw.rect(gameDisplay,color132,(x,y,w,h))
        
def HMbutton121(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color133
    global hits3
    global miss3
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color133 == teal:
                pass

            elif color133 == red:
                color133 = teal
                hits3-=1
                miss3+=1
            
            else:
                color133 = teal
                miss3+=1
                
            
        elif click[2] == 1:
            if color133 == red:
                pass

            elif color133 == teal:
                color133 = red
                miss3-=1
                hits3+=1
            
            else:
                color133 = red
                hits3+=1
                
    else:
        pygame.draw.rect(gameDisplay,color133,(x,y,w,h))
        

def HMbutton122(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color134
    global hits3
    global miss3
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color134 == teal:
                pass

            elif color134 == red:
                color134 = teal
                hits3-=1
                miss3+=1
            
            else:
                color134 = teal
                miss3+=1
                
            
        elif click[2] == 1:
            if color134 == red:
                pass

            elif color134 == teal:
                color134 = red
                miss3-=1
                hits3+=1
            
            else:
                color134 = red
                hits3+=1
                
    else:
        pygame.draw.rect(gameDisplay,color134,(x,y,w,h))

def HMbutton123(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color135
    global hits3
    global miss3
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color135 == teal:
                pass

            elif color135 == red:
                color135 = teal
                hits3-=1
                miss3+=1
            
            else:
                color135 = teal
                miss3+=1
                
            
        elif click[2] == 1:
            if color135 == red:
                pass

            elif color135 == teal:
                color135 = red
                miss3-=1
                hits3+=1
            
            else:
                color135 = red
                hits3+=1
                
    else:
        pygame.draw.rect(gameDisplay,color135,(x,y,w,h))

def HMbutton124(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color136
    global hits3
    global miss3
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color136 == teal:
                pass

            elif color136 == red:
                color136 = teal
                hits3-=1
                miss3+=1
            
            else:
                color136 = teal
                miss3+=1
                
            
        elif click[2] == 1:
            if color136 == red:
                pass

            elif color136 == teal:
                color136 = red
                miss3-=1
                hits3+=1
            
            else:
                color136 = red
                hits3+=1
                
    else:
        pygame.draw.rect(gameDisplay,color136,(x,y,w,h))
        
def HMbutton125(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color137
    global hits3
    global miss3
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color137 == teal:
                pass

            elif color137 == red:
                color137 = teal
                hits3-=1
                miss3+=1
            
            else:
                color137 = teal
                miss3+=1
                
            
        elif click[2] == 1:
            if color137 == red:
                pass

            elif color137 == teal:
                color137 = red
                miss3-=1
                hits3+=1
            
            else:
                color137 = red
                hits3+=1
                
    else:
        pygame.draw.rect(gameDisplay,color137,(x,y,w,h))

def HMbutton126(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color138
    global hits3
    global miss3
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color138 == teal:
                pass

            elif color138 == red:
                color138 = teal
                hits3-=1
                miss3+=1
            
            else:
                color138 = teal
                miss3+=1
                
            
        elif click[2] == 1:
            if color138 == red:
                pass

            elif color138 == teal:
                color138 = red
                miss3-=1
                hits3+=1
            
            else:
                color138 = red
                hits3+=1
                
    else:
        pygame.draw.rect(gameDisplay,color138,(x,y,w,h))

def HMbutton127(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color139
    global hits3
    global miss3
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color139 == teal:
                pass

            elif color139 == red:
                color139 = teal
                hits3-=1
                miss3+=1
            
            else:
                color139 = teal
                miss3+=1
                
            
        elif click[2] == 1:
            if color139 == red:
                pass

            elif color139 == teal:
                color139 = red
                miss3-=1
                hits3+=1
            
            else:
                color139 = red
                hits3+=1
                
    else:
        pygame.draw.rect(gameDisplay,color139,(x,y,w,h))


def HMbutton128(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color140
    global hits3
    global miss3
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color140 == teal:
                pass

            elif color140 == red:
                color140 = teal
                hits3-=1
                miss3+=1
            
            else:
                color140 = teal
                miss3+=1
                
            
        elif click[2] == 1:
            if color140 == red:
                pass

            elif color140 == teal:
                color140 = red
                miss3-=1
                hits3+=1
            
            else:
                color140 = red
                hits3+=1
                
    else:
        pygame.draw.rect(gameDisplay,color140,(x,y,w,h))

def HMbutton129(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color141
    global hits3
    global miss3
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color141 == teal:
                pass

            elif color141 == red:
                color141 = teal
                hits3-=1
                miss3+=1
            
            else:
                color141 = teal
                miss3+=1
                
            
        elif click[2] == 1:
            if color141 == red:
                pass

            elif color141 == teal:
                color141 = red
                miss3-=1
                hits3+=1
            
            else:
                color141 = red
                hits3+=1
                
    else:
        pygame.draw.rect(gameDisplay,color141,(x,y,w,h))

def HMbutton130(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color142
    global hits3
    global miss3
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color142 == teal:
                pass

            elif color142 == red:
                color142 = teal
                hits3-=1
                miss3+=1
            
            else:
                color142 = teal
                miss3+=1
                
            
        elif click[2] == 1:
            if color142 == red:
                pass

            elif color142 == teal:
                color142 = red
                miss3-=1
                hits3+=1
            
            else:
                color142 = red
                hits3+=1
                
    else:
        pygame.draw.rect(gameDisplay,color142,(x,y,w,h))

def HMbutton131(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color143
    global hits3
    global miss3
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color143 == teal:
                pass

            elif color143 == red:
                color143 = teal
                hits3-=1
                miss3+=1
            
            else:
                color143 = teal
                miss3+=1
                
            
        elif click[2] == 1:
            if color143 == red:
                pass

            elif color143 == teal:
                color143 = red
                miss3-=1
                hits3+=1
            
            else:
                color143 = red
                hits3+=1
                
    else:
        pygame.draw.rect(gameDisplay,color143,(x,y,w,h))
        
def HMbutton132(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color144
    global hits3
    global miss3
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color144 == teal:
                pass

            elif color144 == red:
                color144 = teal
                hits3-=1
                miss3+=1
            
            else:
                color144 = teal
                miss3+=1
                
            
        elif click[2] == 1:
            if color144 == red:
                pass

            elif color144 == teal:
                color144 = red
                miss3-=1
                hits3+=1
            
            else:
                color144 = red
                hits3+=1
                
    else:
        pygame.draw.rect(gameDisplay,color144,(x,y,w,h))

def HMbutton133(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color145
    global hits3
    global miss3
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color145 == teal:
                pass

            elif color145 == red:
                color145 = teal
                hits3-=1
                miss3+=1
            
            else:
                color145 = teal
                miss3+=1
                
            
        elif click[2] == 1:
            if color145 == red:
                pass

            elif color145 == teal:
                color145 = red
                miss3-=1
                hits3+=1
            
            else:
                color145 = red
                hits3+=1
                
    else:
        pygame.draw.rect(gameDisplay,color145,(x,y,w,h))

def HMbutton134(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color146
    global hits3
    global miss3
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color146 == teal:
                pass

            elif color146 == red:
                color146 = teal
                hits3-=1
                miss3+=1
            
            else:
                color146 = teal
                miss3+=1
                
            
        elif click[2] == 1:
            if color146 == red:
                pass

            elif color146 == teal:
                color146 = red
                miss3-=1
                hits3+=1
            
            else:
                color146 = red
                hits3+=1
                
    else:
        pygame.draw.rect(gameDisplay,color146,(x,y,w,h))


def HMbutton135(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color147
    global hits3
    global miss3
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color147 == teal:
                pass

            elif color147 == red:
                color147 = teal
                hits3-=1
                miss3+=1
            
            else:
                color147 = teal
                miss3+=1
                
            
        elif click[2] == 1:
            if color147 == red:
                pass

            elif color147 == teal:
                color147 = red
                miss3-=1
                hits3+=1
            
            else:
                color147 = red
                hits3+=1
                
    else:
        pygame.draw.rect(gameDisplay,color147,(x,y,w,h))

def HMbutton136(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color148
    global hits3
    global miss3
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color148 == teal:
                pass

            elif color148 == red:
                color148 = teal
                hits3-=1
                miss3+=1
            
            else:
                color148 = teal
                miss3+=1
                
            
        elif click[2] == 1:
            if color148 == red:
                pass

            elif color148 == teal:
                color148 = red
                miss3-=1
                hits3+=1
            
            else:
                color148 = red
                hits3+=1
                
    else:
        pygame.draw.rect(gameDisplay,color148,(x,y,w,h))


def HMbutton137(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color149
    global hits3
    global miss3
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color149 == teal:
                pass

            elif color149 == red:
                color149 = teal
                hits3-=1
                miss3+=1
            
            else:
                color149 = teal
                miss3+=1
                
            
        elif click[2] == 1:
            if color149 == red:
                pass

            elif color149 == teal:
                color149 = red
                miss3-=1
                hits3+=1
            
            else:
                color149 = red
                hits3+=1
                
    else:
        pygame.draw.rect(gameDisplay,color149,(x,y,w,h))
        
def HMbutton138(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color150
    global hits3
    global miss3
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color150 == teal:
                pass

            elif color150 == red:
                color150 = teal
                hits3-=1
                miss3+=1
            
            else:
                color150 = teal
                miss3+=1
                
            
        elif click[2] == 1:
            if color150 == red:
                pass

            elif color150 == teal:
                color150 = red
                miss3-=1
                hits3+=1
            
            else:
                color150 = red
                hits3+=1
                
    else:
        pygame.draw.rect(gameDisplay,color150,(x,y,w,h))
        
def HMbutton139(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color151
    global hits3
    global miss3
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color151 == teal:
                pass

            elif color151 == red:
                color151 = teal
                hits3-=1
                miss3+=1
            
            else:
                color151 = teal
                miss3+=1
                
            
        elif click[2] == 1:
            if color151 == red:
                pass

            elif color151 == teal:
                color151 = red
                miss3-=1
                hits3+=1
            
            else:
                color151 = red
                hits3+=1
                
    else:
        pygame.draw.rect(gameDisplay,color151,(x,y,w,h))
        
def HMbutton140(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color152
    global hits3
    global miss3
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color152 == teal:
                pass

            elif color152 == red:
                color152 = teal
                hits3-=1
                miss3+=1
            
            else:
                color152 = teal
                miss3+=1
                
            
        elif click[2] == 1:
            if color152 == red:
                pass

            elif color152 == teal:
                color152 = red
                miss3-=1
                hits3+=1
            
            else:
                color152 = red
                hits3+=1
                
    else:
        pygame.draw.rect(gameDisplay,color152,(x,y,w,h))

def HMbutton141(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color153
    global hits3
    global miss3
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color153 == teal:
                pass

            elif color153 == red:
                color153 = teal
                hits3-=1
                miss3+=1
            
            else:
                color153 = teal
                miss3+=1
                
            
        elif click[2] == 1:
            if color153 == red:
                pass

            elif color153 == teal:
                color153 = red
                miss3-=1
                hits3+=1
            
            else:
                color153 = red
                hits3+=1
                
    else:
        pygame.draw.rect(gameDisplay,color153,(x,y,w,h))


def HMbutton142(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color154
    global hits3
    global miss3
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color154 == teal:
                pass

            elif color154 == red:
                color154 = teal
                hits3-=1
                miss3+=1
            
            else:
                color154 = teal
                miss3+=1
                
            
        elif click[2] == 1:
            if color154 == red:
                pass

            elif color154 == teal:
                color154 = red
                miss3-=1
                hits3+=1
            
            else:
                color154 = red
                hits3+=1
                
    else:
        pygame.draw.rect(gameDisplay,color154,(x,y,w,h))

def HMbutton143(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color155
    global hits3
    global miss3
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color155 == teal:
                pass

            elif color155 == red:
                color155 = teal
                hits3-=1
                miss3+=1
            
            else:
                color155 = teal
                miss3+=1
                
            
        elif click[2] == 1:
            if color155 == red:
                pass

            elif color155 == teal:
                color155 = red
                miss3-=1
                hits3+=1
            
            else:
                color155 = red
                hits3+=1
                
    else:
        pygame.draw.rect(gameDisplay,color155,(x,y,w,h))

def HMbutton144(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color156
    global hits3
    global miss3
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color156 == teal:
                pass

            elif color156 == red:
                color156 = teal
                hits3-=1
                miss3+=1
            
            else:
                color156 = teal
                miss3+=1
                
            
        elif click[2] == 1:
            if color156 == red:
                pass

            elif color156 == teal:
                color156 = red
                miss3-=1
                hits3+=1
            
            else:
                color156 = red
                hits3+=1
                
    else:
        pygame.draw.rect(gameDisplay,color156,(x,y,w,h))


def HMbutton145(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color157
    global hits3
    global miss3
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color157 == teal:
                pass

            elif color157 == red:
                color157 = teal
                hits3-=1
                miss3+=1
            
            else:
                color157 = teal
                miss3+=1
                
            
        elif click[2] == 1:
            if color157 == red:
                pass

            elif color157 == teal:
                color157 = red
                miss3-=1
                hits3+=1
            
            else:
                color157 = red
                hits3+=1
                
    else:
        pygame.draw.rect(gameDisplay,color157,(x,y,w,h))

def HMbutton146(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color158
    global hits3
    global miss3
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color158 == teal:
                pass

            elif color158 == red:
                color158 = teal
                hits3-=1
                miss3+=1
            
            else:
                color158 = teal
                miss3+=1
                
            
        elif click[2] == 1:
            if color158 == red:
                pass

            elif color158 == teal:
                color158 = red
                miss3-=1
                hits3+=1
            
            else:
                color158 = red
                hits3+=1
                
    else:
        pygame.draw.rect(gameDisplay,color158,(x,y,w,h))

def HMbutton147(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global color159
    global hits3
    global miss3
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,grey,(x,y,w,h))
        if click[0] == 1:
            if color159 == teal:
                pass

            elif color159 == red:
                color159 = teal
                hits3-=1
                miss3+=1
            
            else:
                color159 = teal
                miss3+=1
                
            
        elif click[2] == 1:
            if color159 == red:
                pass

            elif color159 == teal:
                color159 = red
                miss3-=1
                hits3+=1
            
            else:
                color159 = red
                hits3+=1
                
    else:
        pygame.draw.rect(gameDisplay,color159,(x,y,w,h))


##Main Menu Button Definition -----------------

def startButton(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h),0,5)
        if click[0] == 1 and action != None:
            action()
        
    else:
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h),0,5)

    smallText = pygame.font.SysFont("calibri",20)
    textSurf,textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)),y+(h/2))
    gameDisplay.blit(textSurf,textRect)

#Additional sleep timer here (0.4 to prevent double clicks)
def startButton2(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h),0,5)
        if click[0] == 1 and action != None:
            time.sleep(0.4)
            action()
        
    else:
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h),0,5)

    smallText = pygame.font.SysFont("calibri",20)
    textSurf,textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)),y+(h/2))
    gameDisplay.blit(textSurf,textRect)

#Additional sleep timer and smaller inner text - In the future, just make text size a parameter variable as well
def startButton3(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h),0,5)
        if click[0] == 1 and action != None:
            time.sleep(0.4)
            action()
        
    else:
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h),0,5)

    smallText = pygame.font.SysFont("calibri",18)
    textSurf,textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)),y+(h/2))
    gameDisplay.blit(textSurf,textRect)

#No sleep timer but smaller text
def startButton4(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h),0,5)
        if click[0] == 1 and action != None:
            action()
        
    else:
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h),0,5)

    smallText = pygame.font.SysFont("calibri",18)
    textSurf,textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)),y+(h/2))
    gameDisplay.blit(textSurf,textRect)


##Main Menu Button Definition -----------------

#Quit game ----------------

def quitgame():
    pygame.quit()
    sys.exit()

#Quit game ----------------

#Intro Screen ===============

def intro_screen():
    
    intro = False
    start_time = time.time()
    while not intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
        gameDisplay.blit(bg,(0,0))

        smallTitleText = pygame.font.SysFont('calibri',45)
        TextSurf1, TextRect1 = text_objects_color('McMaster University - Materials Properties Battleship Educational Game',smallTitleText,(179,89,0))
        TextRect1.center = (((display_width/2)+30,(display_height/2)-170))
        gameDisplay.blit(TextSurf1,TextRect1)

        smallTitleText1 = pygame.font.SysFont('calibri',35)
        TextSurf4, TextRect4 = text_objects_color('Developed for Windows',smallTitleText1,(179,89,0))
        TextRect4.center = (((display_width/2)+30,(display_height/2)-50))
        gameDisplay.blit(TextSurf4,TextRect4)

        TextSurf5, TextRect5 = text_objects_color('Ashby Charts From ANSYS Granta Edupack 2021 R2 Software',smallTitleText1,(179,89,0))
        TextRect5.center = (((display_width/2)+30,(display_height/2)-100))
        gameDisplay.blit(TextSurf5,TextRect5)

        copyrighttext = pygame.font.SysFont('calibri',25)
        copyrighttext2 = pygame.font.SysFont('calibri',22)

        TextSurf2, TextRect2 = text_objects_color('Developed by Dr. Bosco Yu and Muhammad Arshad',copyrighttext,(darkgrey))
        TextRect2.center = (((display_width/2)+30,(display_height/2)+350))
        gameDisplay.blit(TextSurf2,TextRect2)

        TextSurf3, TextRect3 = text_objects_color('©2022 McMaster University. All rights reserved',copyrighttext2,(darkgrey))
        TextRect3.center = (((display_width/2)+30,(display_height/2)+380))
        gameDisplay.blit(TextSurf3,TextRect3)

        new_rect = mcmasterlogo.get_rect(center = mcmasterlogo.get_rect(topleft = ((display_width//2)-150,20)).center)
        gameDisplay.blit(mcmasterlogo,new_rect)
        
        

        current_time = time.time()

        #Fade screen after 1.5 seconds
        if current_time - start_time > 1.5:
            fade(display_width,display_height)
        
        pygame.display.update()
        clock.tick(60)
#Intro Screen ===============

#Fade =======================
def fade(width,height):

    fade = pygame.Surface((width,height))
    fade.fill((255,255,255))

    for alpha in range(0,250):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        fade.set_alpha(alpha)
        redrawWindow()
        gameDisplay.blit(fade,(0,0))
        pygame.display.update()
        pygame.time.delay(5)
        
    game_intro()


def redrawWindow():
    gameDisplay.blit(bg,(0,0))

    smallTitleText = pygame.font.SysFont('calibri',45)
    TextSurf1, TextRect1 = text_objects_color('McMaster University - Materials Properties Battleship Educational Game',smallTitleText,(179,89,0))
    TextRect1.center = (((display_width/2)+30,(display_height/2)-170))
    gameDisplay.blit(TextSurf1,TextRect1)

    smallTitleText1 = pygame.font.SysFont('calibri',35)
    TextSurf4, TextRect4 = text_objects_color('Developed for Windows',smallTitleText1,(179,89,0))
    TextRect4.center = (((display_width/2)+30,(display_height/2)-50))
    gameDisplay.blit(TextSurf4,TextRect4)

    TextSurf5, TextRect5 = text_objects_color('Ashby Charts From ANSYS Granta Edupack 2021 R2 Software',smallTitleText1,(179,89,0))
    TextRect5.center = (((display_width/2)+30,(display_height/2)-100))
    gameDisplay.blit(TextSurf5,TextRect5)

    copyrighttext = pygame.font.SysFont('calibri',25)
    copyrighttext2 = pygame.font.SysFont('calibri',22)

    TextSurf2, TextRect2 = text_objects_color('Developed by Dr. Bosco Yu and Muhammad Arshad',copyrighttext,(darkgrey))
    TextRect2.center = (((display_width/2)+30,(display_height/2)+350))
    gameDisplay.blit(TextSurf2,TextRect2)

    TextSurf3, TextRect3 = text_objects_color('©2022 McMaster University. All rights reserved',copyrighttext2,(darkgrey))
    TextRect3.center = (((display_width/2)+30,(display_height/2)+380))
    gameDisplay.blit(TextSurf3,TextRect3)

    new_rect = mcmasterlogo.get_rect(center = mcmasterlogo.get_rect(topleft = ((display_width//2)-150,20)).center)
    gameDisplay.blit(mcmasterlogo,new_rect)
#Fade =======================

#Main Menu =========================================================

def game_intro():
    intro = False

    while not intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
        gameDisplay.blit(bg,(0,0))

        #Title ---------------------
        largeText = pygame.font.SysFont('calibri',60)
        TextSurf, TextRect = text_objects_color('Materials Science Educational Game',largeText,(179,89,0))
        TextRect.center = (((display_width/2)+30,(display_height/2)-230))
        gameDisplay.blit(TextSurf,TextRect)

        smallTitleText = pygame.font.SysFont('calibri',35)
        TextSurf1, TextRect1 = text_objects_color('McMaster University - Materials Properties Battleship',smallTitleText,(179,89,0))
        TextRect1.center = (((display_width/2)+30,(display_height/2)-170))
        gameDisplay.blit(TextSurf1,TextRect1)

        copyrighttext = pygame.font.SysFont('calibri',25)
        copyrighttext2 = pygame.font.SysFont('calibri',22)
        
        TextSurf2, TextRect2 = text_objects_color('Developed by Dr. Bosco Yu and Muhammad Arshad',copyrighttext,(darkgrey))
        TextRect2.center = (((display_width/2)+30,(display_height/2)+350))
        gameDisplay.blit(TextSurf2,TextRect2)

        TextSurf3, TextRect3 = text_objects_color('©2022 McMaster University. All rights reserved',copyrighttext2,(darkgrey))
        TextRect3.center = (((display_width/2)+30,(display_height/2)+380))
        gameDisplay.blit(TextSurf3,TextRect3)

        new_rect = mcmasterlogo.get_rect(center = mcmasterlogo.get_rect(topleft = ((display_width//2)-150,20)).center)
        gameDisplay.blit(mcmasterlogo,new_rect)
        #Title ---------------------

        #Buttons -------------------

        startButton2('Launch Game!',(display_width//2)-80,320,200,100,green,light_green,level_select)
        startButton('How To Play',(display_width//2)-80,480,200,100,yellow,light_yellow,how2play)
        startButton('Quit!',(display_width//2)-80,650,200,100,red,light_red,quitgame)

        startButton4('Copyright',(display_width//2)+680,20,100,50,lightdarkgrey,grey,copyright_screen)
        #Buttons -------------------
        
        pygame.display.update()
        clock.tick(60)

#Main Menu =========================================================

#Copyright Screen ==================================================
def copyright_screen():
    
    menuplay = False

    while not menuplay:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(bg,(0,0))
        gameDisplay.blit(copyrightbox,(100,30))


        startButton('Back to Menu',(display_width//2)-50,750,150,90,green,light_green,game_intro)

        pygame.display.update()
        clock.tick(60)

#Copyright Screen ==================================================

        
#How to Play Menu ==================================================

def how2play():

    menuplay = False

    while not menuplay:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(bg,(0,0))

        gameDisplay.blit(how2playvar,(306,0))

        startButton('Back to Menu',(display_width//2)-200,800,150,40,green,light_green,game_intro)
        startButton('Page 1/3',(display_width//2)+50,800,150,40,yellow,light_yellow,how2play2)
        
        pygame.display.update()
        clock.tick(60)

def how2play2():

    menuplay2 = False

    while not menuplay2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(bg,(0,0))

        gameDisplay.blit(how2play2var,(306,0))

        startButton('Back to Menu',(display_width//2)-400,800,150,40,green,light_green,game_intro)
        startButton('Page 2/3',(display_width//2)+250,800,150,40,yellow,light_yellow,how2play3)
        
        pygame.display.update()
        clock.tick(60)

def how2play3():

    menuplay3 = False

    while not menuplay3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(bg,(0,0))

        gameDisplay.blit(how2play3var,((display_width//2)-397,40))

        startButton2('Back to Menu',(display_width//2)-200,800,150,40,green,light_green,game_intro)
        startButton2('Page 3/3',(display_width//2)+50,800,150,40,yellow,light_yellow,how2play)
        
        pygame.display.update()
        clock.tick(60)

#Level Select ======================================================

def level_select():

    levels = False

    while not levels:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        gameDisplay.blit(bg,(0,0))

        drawTitle(450,60,'Choose a Difficulty Level',red,80)
        drawTitle(450,150,'Solutions For a Level Are Unlocked Once a Game Is Completed',lime,30)
        
        startButton('Back to Menu',(display_width//2)-50,800,150,90,green,light_green,game_intro)

        startButton3('Easy: Mass vs Price',(display_width//2)-600,400,330,150,lime,light_lime,game_loop2)
        startButton3('Medium: Mass vs Stiffness',(display_width//2)-135,400,330,150,yellow,light_yellow,game_loop)
        startButton3('Hard: Thermal Conductivity vs Yield Strength',(display_width//2)+320,400,330,150,red,light_red,game_loop3)

        if lock1 == False:
            startButton('Solution: LOCKED',(display_width//2)-600,570,330,30,darkgrey,grey,doNothing)
        elif lock1 == True:
            startButton('Solution: UNLOCKED',(display_width//2)-600,570,330,30,green,light_green,solution1)

        if lock2 == False:
            startButton('Solution: LOCKED',(display_width//2)-135,570,330,30,darkgrey,grey,doNothing)
        elif lock2 == True:
            startButton('Solution: UNLOCKED',(display_width//2)-135,570,330,30,green,light_green,solution2)

        if lock3 == False:
            startButton('Solution: LOCKED',(display_width//2)+320,570,330,30,darkgrey,grey,doNothing)

        elif lock3 == True:
            startButton('Solution: UNLOCKED',(display_width//2)+320,570,330,30,green,light_green,solution3)

        pygame.display.update()
        clock.tick(60)

#Level Select ======================================================

def solution1():
    solscreen = False

    while not solscreen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(bg,(0,0))

        drawTitle((display_width)//2 - 390,10,'Level 1: Density (Mass) vs Price Solution',(11,112,8),50)

        startButton('Level Select',(display_width//2)-75,760,150,40,green,light_green,level_select)
        gameDisplay.blit(solimage1,((display_width//2)-600,80))

        pygame.display.update()
        clock.tick(60)

def solution2():
    solscreen = False

    while not solscreen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(bg,(0,0))

        drawTitle((display_width)//2 - 620,10,"Level 2: Density (Mass) vs Young's Modulus (Stiffness) Solution",(11,112,8),50)

        startButton('Level Select',(display_width//2)-75,760,150,40,green,light_green,level_select)
        gameDisplay.blit(solimage2,((display_width//2)-600,80))

        pygame.display.update()
        clock.tick(60)

def solution3():
    solscreen = False

    while not solscreen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(bg,(0,0))

        drawTitle((display_width)//2 - 550,10,"Level 3: Thermal Conductivity vs Yield Strength Solution",(11,112,8),50)

        startButton('Level Select',(display_width//2)-75,760,150,40,green,light_green,level_select)
        gameDisplay.blit(solimage3,((display_width//2)-600,80))

        pygame.display.update()
        clock.tick(60)

#Maing game loop (First developed level hence referred to as level 1 when compared to other game_loops)===================================================
        
def game_loop():

    gameExit = False
    global countme
    global lock2

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        gameDisplay.blit(bg,(0,0))
        loadships()

        #Track Draw ---------------------------
        drawTrack()
        drawGrid()

        drawTitle(200,60,'Your Ship Board',(11,112,8),50)
        drawTitle(1050,60,'Your Tracking Board',(112,24,8),50)
        drawTitle(575,120,'Materials Properties Battleship',(212,159,15),36)

        drawXaxis(128,650,'Mass')
        drawXaxis(1024,650,'Mass')
        drawYaxis1(590,192,'Stiffness')
        drawYaxis2(940,192,'Stiffness')

        drawShipBox(700,720)
        drawHitBox(185,720)
        drawMarkerBox(300,300)

        drawTitle(1035,800,'Reminder: Left click to track a MISS in blue',(56,43,110),18)
        drawTitle(1032,830,'                    Right click to track a HIT in red',(110,43,43),18)

        newshipB('Get New Ships!',653,800,300,64,green,light_green,generateNewrand)
        gameDisplay.blit(mcmasterlogo180x,(690,20))

        newshipB('CLEAR BOARD!!',1250,730,190,30,red,light_red,clearBoard)

        newshipB('Back',30,15,140,30,green,light_green,level_select)
        newshipB('Exit Game',1430,15,140,30,red,light_red,quitgame)
        
        #Track Draw ---------------------------


        #Grid Fonts ---------------------------
        font = pygame.font.SysFont('calibri',64)
        text = font.render(" A  B  C  D  E  F  G",True,black)
        gameDisplay.blit(text,(128,136))
        text1 = font.render("1",True,black)
        gameDisplay.blit(text1,(91,199))
        text2 = font.render("2",True,black)
        gameDisplay.blit(text2,(91,263))
        text3 = font.render("3",True,black)
        gameDisplay.blit(text3,(91,326))
        text4 = font.render("4",True,black)
        gameDisplay.blit(text4,(91,392))
        text5 = font.render("5",True,black)
        gameDisplay.blit(text5,(91,455))
        text6 = font.render("6",True,black)
        gameDisplay.blit(text6,(91,521))
        text7 = font.render("7",True,black)
        gameDisplay.blit(text7,(91,585))
        #Grid Fonts ---------------------------

        #Track Fonts --------------------------
        texttrack = font.render(" A  B  C  D  E  F  G",True,black)
        gameDisplay.blit(texttrack,(1024,136))
        text11 = font.render("1",True,black)
        gameDisplay.blit(text11,(985,199))
        text22 = font.render("2",True,black)
        gameDisplay.blit(text22,(985,263))
        text33 = font.render("3",True,black)
        gameDisplay.blit(text33,(985,326))
        text44 = font.render("4",True,black)
        gameDisplay.blit(text44,(985,392))
        text55 = font.render("5",True,black)
        gameDisplay.blit(text55,(985,455))
        text66 = font.render("6",True,black)
        gameDisplay.blit(text66,(985,521))
        text77 = font.render("7",True,black)
        gameDisplay.blit(text77,(985,585))
        #Track Fonts --------------------------

        #Hit Buttons --------------------------
        Hbutton1(64,745,20,20)
        Hbutton2(99,745,20,20)

        Hbutton3(64,795,20,20)
        Hbutton4(99,795,20,20)

        Hbutton5(64,845,20,20)
        Hbutton6(99,845,20,20)
        #Hit Buttons --------------------------

        #H/M tracking ------------------------
        hitCounter(hits)
        missCounter(miss)

        #Fade in wintable ---------------------
        
        if hits >= 6:
            lock2 = True
            if countme == 255:
                gameDisplay.blit(wintable,(650,170))
                startButton('Hint',(display_width//2)-85,720,150,40,yellow,light_yellow,hintscreen1)
                pass

            elif countme != 255 :
                wintable.set_alpha(countme)
                countme += 17
                gameDisplay.blit(wintable,(650,170))

        #Fade in wintable ---------------------
                                   
        #-------------------------------------

        #Tracking Buttons ---------------------
        HMbutton37(1027,194,60,60)
        HMbutton38(1091,194,60,60)
        HMbutton39(1155,194,60,60)
        HMbutton40(1219,194,60,60)
        HMbutton41(1283,194,60,60)
        HMbutton42(1347,194,60,60)
        HMbutton43(1411,194,60,60)

        HMbutton44(1411,258,60,60)
        HMbutton45(1411,322,60,60)
        HMbutton46(1411,386,60,60)
        HMbutton47(1411,450,60,60)
        HMbutton48(1411,514,60,60)
        HMbutton49(1411,578,60,60)
        
        HMbutton1(1027,258,60,60)
        HMbutton2(1091,258,60,60)
        HMbutton3(1155,258,60,60)
        HMbutton4(1219,258,60,60)
        HMbutton5(1283,258,60,60)
        HMbutton6(1347,258,60,60)

        HMbutton7(1027,322,60,60)
        HMbutton8(1091,322,60,60)
        HMbutton9(1155,322,60,60)
        HMbutton10(1219,322,60,60)
        HMbutton11(1283,322,60,60)
        HMbutton12(1347,322,60,60)

        HMbutton13(1027,386,60,60)
        HMbutton14(1091,386,60,60)
        HMbutton15(1155,386,60,60)
        HMbutton16(1219,386,60,60)
        HMbutton17(1283,386,60,60)
        HMbutton18(1347,386,60,60)

        HMbutton19(1027,450,60,60)
        HMbutton20(1091,450,60,60)
        HMbutton21(1155,450,60,60)
        HMbutton22(1219,450,60,60)
        HMbutton23(1283,450,60,60)
        HMbutton24(1347,450,60,60)

        HMbutton25(1027,514,60,60)
        HMbutton26(1091,514,60,60)
        HMbutton27(1155,514,60,60)
        HMbutton28(1219,514,60,60)
        HMbutton29(1283,514,60,60)
        HMbutton30(1347,514,60,60)

        HMbutton31(1027,578,60,60)
        HMbutton32(1091,578,60,60)
        HMbutton33(1155,578,60,60)
        HMbutton34(1219,578,60,60)
        HMbutton35(1283,578,60,60)
        HMbutton36(1347,578,60,60)
        #Tracking Buttons ---------------------
        
        pygame.display.update()
        clock.tick(60)

#Maing game loop ===================================================


#Hint Screen 1 ===================================================

def hintscreen1():

    hint1 = False

    while not hint1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(bg,(0,0))

        drawTitle((display_width)//2 - 590,10,"Level 2: Density (Mass) vs Young's Modulus (Stiffness) Hint",(11,112,8),50)

        startButton('Back',(display_width//2)-75,760,150,40,green,light_green,game_loop)
        gameDisplay.blit(hintimage2,((display_width//2)-600,80))
                

        pygame.display.update()
        clock.tick(60)
    

#Hint Screen 1 ===================================================


#Making game 2 =====================================================

def game_loop2():

    gameExit2 = False
    global countme2
    global lock1

    while not gameExit2:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        gameDisplay.blit(bg,(0,0))
        loadships2()

        drawTrack()
        drawGrid()

        drawTitle(200,60,'Your Ship Board',(11,112,8),50)
        drawTitle(1050,60,'Your Tracking Board',(112,24,8),50)
        drawTitle(575,120,'Materials Properties Battleship',(212,159,15),36)

        drawXaxis(128,650,'Mass')
        drawXaxis(1024,650,'Mass')
        drawYaxis1(590,192,'Price in Dollars')
        drawYaxis2(940,192,'Price in Dollars')

        drawShipBox(700,720)
        drawHitBox(185,720)
        drawMarkerBox(300,300)

        drawTitle(1035,800,'Reminder: Left click to track a MISS in blue',(56,43,110),18)
        drawTitle(1032,830,'                    Right click to track a HIT in red',(110,43,43),18)

        newshipB('Get New Ships!',653,800,300,64,green,light_green,generateNewrand2)
        gameDisplay.blit(mcmasterlogo180x,(690,20))

        newshipB('CLEAR BOARD!!',1250,730,190,30,red,light_red,clearBoard2)

        newshipB('Back',30,15,140,30,green,light_green,level_select)
        newshipB('Exit Game',1430,15,140,30,red,light_red,quitgame)

        #Track Draw ---------------------------


        #Grid Fonts ---------------------------
        font = pygame.font.SysFont('calibri',64)
        text = font.render(" A  B  C  D  E  F  G",True,black)
        gameDisplay.blit(text,(128,136))
        text1 = font.render("1",True,black)
        gameDisplay.blit(text1,(91,199))
        text2 = font.render("2",True,black)
        gameDisplay.blit(text2,(91,263))
        text3 = font.render("3",True,black)
        gameDisplay.blit(text3,(91,326))
        text4 = font.render("4",True,black)
        gameDisplay.blit(text4,(91,392))
        text5 = font.render("5",True,black)
        gameDisplay.blit(text5,(91,455))
        text6 = font.render("6",True,black)
        gameDisplay.blit(text6,(91,521))
        text7 = font.render("7",True,black)
        gameDisplay.blit(text7,(91,585))
        #Grid Fonts ---------------------------

        #Track Fonts --------------------------
        texttrack = font.render(" A  B  C  D  E  F  G",True,black)
        gameDisplay.blit(texttrack,(1024,136))
        text11 = font.render("1",True,black)
        gameDisplay.blit(text11,(985,199))
        text22 = font.render("2",True,black)
        gameDisplay.blit(text22,(985,263))
        text33 = font.render("3",True,black)
        gameDisplay.blit(text33,(985,326))
        text44 = font.render("4",True,black)
        gameDisplay.blit(text44,(985,392))
        text55 = font.render("5",True,black)
        gameDisplay.blit(text55,(985,455))
        text66 = font.render("6",True,black)
        gameDisplay.blit(text66,(985,521))
        text77 = font.render("7",True,black)
        gameDisplay.blit(text77,(985,585))
        #Track Fonts --------------------------

        #Hit Buttons --------------------------
        Hbutton7(64,745,20,20)
        Hbutton8(99,745,20,20)

        Hbutton9(64,795,20,20)
        Hbutton10(99,795,20,20)

        Hbutton11(64,845,20,20)
        Hbutton12(99,845,20,20)
        #Hit Buttons --------------------------

        #H/M tracking ------------------------
        hitCounter(hits2)
        missCounter(miss2)

        #Fade in wintable ---------------------
        
        if hits2 >= 6:
            lock1 = True
            if countme2 == 255:
                gameDisplay.blit(wintable2,(650,170))
                startButton('Hint',(display_width//2)-85,720,150,40,yellow,light_yellow,hintscreen2)
                pass

            elif countme2 != 255 :
                wintable2.set_alpha(countme2)
                countme2 += 17
                gameDisplay.blit(wintable2,(650,170))

        #Fade in wintable ---------------------

         #Tracking Buttons ---------------------
        HMbutton86(1027,194,60,60)
        HMbutton87(1091,194,60,60)
        HMbutton88(1155,194,60,60)
        HMbutton89(1219,194,60,60)
        HMbutton90(1283,194,60,60)
        HMbutton91(1347,194,60,60)
        HMbutton92(1411,194,60,60)

        HMbutton93(1411,258,60,60)
        HMbutton94(1411,322,60,60)
        HMbutton95(1411,386,60,60)
        HMbutton96(1411,450,60,60)
        HMbutton97(1411,514,60,60)
        HMbutton98(1411,578,60,60)
        
        HMbutton50(1027,258,60,60)
        HMbutton51(1091,258,60,60)
        HMbutton52(1155,258,60,60)
        HMbutton53(1219,258,60,60)
        HMbutton54(1283,258,60,60)
        HMbutton55(1347,258,60,60)

        HMbutton56(1027,322,60,60)
        HMbutton57(1091,322,60,60)
        HMbutton58(1155,322,60,60)
        HMbutton59(1219,322,60,60)
        HMbutton60(1283,322,60,60)
        HMbutton61(1347,322,60,60)

        HMbutton62(1027,386,60,60)
        HMbutton63(1091,386,60,60)
        HMbutton64(1155,386,60,60)
        HMbutton65(1219,386,60,60)
        HMbutton66(1283,386,60,60)
        HMbutton67(1347,386,60,60)

        HMbutton68(1027,450,60,60)
        HMbutton69(1091,450,60,60)
        HMbutton70(1155,450,60,60)
        HMbutton71(1219,450,60,60)
        HMbutton72(1283,450,60,60)
        HMbutton73(1347,450,60,60)

        HMbutton74(1027,514,60,60)
        HMbutton75(1091,514,60,60)
        HMbutton76(1155,514,60,60)
        HMbutton77(1219,514,60,60)
        HMbutton78(1283,514,60,60)
        HMbutton79(1347,514,60,60)

        HMbutton80(1027,578,60,60)
        HMbutton81(1091,578,60,60)
        HMbutton82(1155,578,60,60)
        HMbutton83(1219,578,60,60)
        HMbutton84(1283,578,60,60)
        HMbutton85(1347,578,60,60)
        #Tracking Buttons ---------------------

        

        pygame.display.update()
        clock.tick(60)

#Hint Screen 2 ===================================================

def hintscreen2():

    hint1 = False

    while not hint1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(bg,(0,0))

        drawTitle((display_width)//2 - 300,10,"Level 1: Density (Mass) vs Price Hint",(11,112,8),50)

        startButton('Back',(display_width//2)-75,760,150,40,green,light_green,game_loop2)
        gameDisplay.blit(hintimage1,((display_width//2)-600,80))
                

        pygame.display.update()
        clock.tick(60)
    

#Hint Screen 2 ===================================================

#Making final level =============================================
def game_loop3():
    gameExit3 = False
    global countme3
    global lock3

    while not gameExit3:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        gameDisplay.blit(bg,(0,0))
        loadships3()
        
        drawTrack()
        drawGrid()

        drawTitle(200,60,'Your Ship Board',(11,112,8),50)
        drawTitle(1050,60,'Your Tracking Board',(112,24,8),50)
        drawTitle(575,120,'Materials Properties Battleship',(212,159,15),36)

        drawXaxis(128,650,'Thermal Conductivity')
        drawXaxis(1024,650,'Thermal Conductivity')
        drawYaxis1(590,192,'Yield Strength')
        drawYaxis2(940,192,'Yield Strength')

        

        drawShipBox(700,720)
        drawHitBox(185,720)
        drawMarkerBox(300,300)

        drawTitle(1035,800,'Reminder: Left click to track a MISS in blue',(56,43,110),18)
        drawTitle(1032,830,'                    Right click to track a HIT in red',(110,43,43),18)

        newshipB('Get New Ships!',653,800,300,64,green,light_green,generateNewrand3)
        gameDisplay.blit(mcmasterlogo180x,(690,20))

        newshipB('CLEAR BOARD!!',1250,730,190,30,red,light_red,clearBoard3)

        newshipB('Back',30,15,140,30,green,light_green,level_select)
        newshipB('Exit Game',1430,15,140,30,red,light_red,quitgame)

        #Track Draw ---------------------------


        #Grid Fonts ---------------------------
        font = pygame.font.SysFont('calibri',64)
        text = font.render(" A  B  C  D  E  F  G",True,black)
        gameDisplay.blit(text,(128,136))
        text1 = font.render("1",True,black)
        gameDisplay.blit(text1,(91,199))
        text2 = font.render("2",True,black)
        gameDisplay.blit(text2,(91,263))
        text3 = font.render("3",True,black)
        gameDisplay.blit(text3,(91,326))
        text4 = font.render("4",True,black)
        gameDisplay.blit(text4,(91,392))
        text5 = font.render("5",True,black)
        gameDisplay.blit(text5,(91,455))
        text6 = font.render("6",True,black)
        gameDisplay.blit(text6,(91,521))
        text7 = font.render("7",True,black)
        gameDisplay.blit(text7,(91,585))
        #Grid Fonts ---------------------------

        #Track Fonts --------------------------
        texttrack = font.render(" A  B  C  D  E  F  G",True,black)
        gameDisplay.blit(texttrack,(1024,136))
        text11 = font.render("1",True,black)
        gameDisplay.blit(text11,(985,199))
        text22 = font.render("2",True,black)
        gameDisplay.blit(text22,(985,263))
        text33 = font.render("3",True,black)
        gameDisplay.blit(text33,(985,326))
        text44 = font.render("4",True,black)
        gameDisplay.blit(text44,(985,392))
        text55 = font.render("5",True,black)
        gameDisplay.blit(text55,(985,455))
        text66 = font.render("6",True,black)
        gameDisplay.blit(text66,(985,521))
        text77 = font.render("7",True,black)
        gameDisplay.blit(text77,(985,585))
        #Track Fonts --------------------------

        #Hit Buttons --------------------------
        Hbutton13(64,745,20,20)
        Hbutton14(99,745,20,20)

        Hbutton15(64,795,20,20)
        Hbutton16(99,795,20,20)

        Hbutton17(64,845,20,20)
        Hbutton18(99,845,20,20)
        #Hit Buttons --------------------------


        #H/M tracking ------------------------
        hitCounter(hits3)
        missCounter(miss3)

        #Fade in wintable ---------------------

        if hits3 >= 6:
            lock3 = True
            if countme3 == 255:
                gameDisplay.blit(wintable3,(639,170))
                startButton('Hint',(display_width//2)-85,720,150,40,yellow,light_yellow,hintscreen3)
                pass

            elif countme3 != 255 :
                wintable3.set_alpha(countme3)
                countme3 += 17
                gameDisplay.blit(wintable3,(639,170))

        #Fade in wintable ---------------------

        #Tracking Buttons ---------------------
        HMbutton135(1027,194,60,60)
        HMbutton136(1091,194,60,60)
        HMbutton137(1155,194,60,60)
        HMbutton138(1219,194,60,60)
        HMbutton139(1283,194,60,60)
        HMbutton140(1347,194,60,60)
        HMbutton141(1411,194,60,60)

        HMbutton142(1411,258,60,60)
        HMbutton143(1411,322,60,60)
        HMbutton144(1411,386,60,60)
        HMbutton145(1411,450,60,60)
        HMbutton146(1411,514,60,60)
        HMbutton147(1411,578,60,60)
        
        HMbutton99(1027,258,60,60)
        HMbutton100(1091,258,60,60)
        HMbutton101(1155,258,60,60)
        HMbutton102(1219,258,60,60)
        HMbutton103(1283,258,60,60)
        HMbutton104(1347,258,60,60)

        HMbutton105(1027,322,60,60)
        HMbutton106(1091,322,60,60)
        HMbutton107(1155,322,60,60)
        HMbutton108(1219,322,60,60)
        HMbutton109(1283,322,60,60)
        HMbutton110(1347,322,60,60)

        HMbutton111(1027,386,60,60)
        HMbutton112(1091,386,60,60)
        HMbutton113(1155,386,60,60)
        HMbutton114(1219,386,60,60)
        HMbutton115(1283,386,60,60)
        HMbutton116(1347,386,60,60)

        HMbutton117(1027,450,60,60)
        HMbutton118(1091,450,60,60)
        HMbutton119(1155,450,60,60)
        HMbutton120(1219,450,60,60)
        HMbutton121(1283,450,60,60)
        HMbutton122(1347,450,60,60)

        HMbutton123(1027,514,60,60)
        HMbutton124(1091,514,60,60)
        HMbutton125(1155,514,60,60)
        HMbutton126(1219,514,60,60)
        HMbutton127(1283,514,60,60)
        HMbutton128(1347,514,60,60)

        HMbutton129(1027,578,60,60)
        HMbutton130(1091,578,60,60)
        HMbutton131(1155,578,60,60)
        HMbutton132(1219,578,60,60)
        HMbutton133(1283,578,60,60)
        HMbutton134(1347,578,60,60)
        


        pygame.display.update()
        clock.tick(60)
    

#Making game 2 =====================================================


#Hint Screen 3 ===================================================

def hintscreen3():

    hint1 = False

    while not hint1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(bg,(0,0))

        drawTitle((display_width)//2 - 510,10,"Level 3: Thermal Conductivity vs Yield Strength Hint",(11,112,8),50)

        startButton('Back',(display_width//2)-75,760,150,40,green,light_green,game_loop3)
        gameDisplay.blit(hintimage3,((display_width//2)-600,80))
                

        pygame.display.update()
        clock.tick(60)
    

#Hint Screen 3 ===================================================

intro_screen()
#game_intro()
#how2play3()
#game_loop()
#game_loop2()
#game_loop3()

#level_select()

#solution3()

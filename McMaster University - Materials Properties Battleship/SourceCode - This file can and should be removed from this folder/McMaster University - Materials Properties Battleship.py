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
white = (255,255,255) #screen fill colour
grey = (166,162,162) # mouse hover colour
darkgrey = (80,77,77) # default button tracking colour
lightdarkgrey = (128,128,128) # copyright button
orange = (179,89,0) #start screen font color

light_red = (255,151,151)
red = (200,0,0)
teal = (109,158,255)

light_green = (66,212,61)
green = (74,179,71)

yellow = (227,197,66)
light_yellow = (250,211,37)

lime = (125,161,90)
light_lime = (168,224,112)

#Tracking variables below

# Ships
randships = [0] * 9  # Creates a list with 9 zeros: randships[0] to randships[8]

# Hits and misses
hits = [0] * 3       # hits[0], hits[1], hits[2]
misses = [0] * 3     # misses[0], misses[1], misses[2]

# Counters
counts = [0] * 3     # counts[0], counts[1], counts[2]

lock1 = False
lock2 = False
lock3 = False

# Button Color Definition--------------------------
grid_colors = {}
# Button Color Definition--------------------------

gameDisplay = pygame.display.set_mode((display_width,display_height)) #Width Height Tuple
pygame.display.set_caption('McMaster University Materials Properties Battleship') #Changes caption of game
clock = pygame.time.Clock() #game clock


##Image Loading--------------------------

#Board
bg = pygame.image.load("paperback.png")
sidearrow = pygame.image.load("sidearrow.png")
uparrow = pygame.image.load("uparrow.png")

#Level1 (Mass vs Stiffness) ships
cardship = pygame.image.load("Level1/Sm2cardship.png")
concreteship = pygame.image.load("Level1/Sm2concreteship.png")
goldship = pygame.image.load("Level1/Sm2goldship.png")
leathership1 = pygame.image.load("Level1/Sm2leathership.png")
silvership = pygame.image.load("Level1/Sm2silvership.png")
tungship1 = pygame.image.load("Level1/Sm2tungship.png")

#Level 2 (Mass vs Price) ships
styroship = pygame.image.load("Level2/Smstyroship.png")
corkship = pygame.image.load("Level2/Smcorkship.png")
rubbership = pygame.image.load("Level2/Smrubbership.png")

leathership = pygame.image.load("Level2/Smleathership.png")
woodship = pygame.image.load("Level2/Smwoodship.png")
bambooship = pygame.image.load("Level2/Smbambooship.png")

alumship = pygame.image.load("Level2/Smalumship.png")
steelship = pygame.image.load("Level2/Smsteelship.png")
tungship = pygame.image.load("Level2/Smtungship.png")

#Level3(Thermal Conductivity vs Yield Strength) ships
alumship2 = pygame.image.load("Level3/Sm3alumship.png")
bambooship2 = pygame.image.load("Level3/Sm3bambooship.png")
rubbership2 = pygame.image.load("Level3/Sm3rubbership.png")
brickship = pygame.image.load("Level3/Sm3brickship.png")
leadship = pygame.image.load("Level3/Sm3leadship.png")
titanship = pygame.image.load("Level3/Sm3titaniumship.png")
tinship = pygame.image.load("Level3/Sm3tinship.png")

#Win tables
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

#Hint Images
hintimage1 = pygame.image.load("Source/_bin/_recompiled/_del/level1hint.png")
hintimage2 = pygame.image.load("Source/_bin/_recompiled/_del/level2hint.png")
hintimage3 = pygame.image.load("Source/_bin/_recompiled/_del/level3hint.png")

#Solution Images
solimage1 = pygame.image.load("Source/_bin/_lmty/_remove/_Filesave/S1Pic.png")
solimage2 = pygame.image.load("Source/_bin/_dist/_recompiled/_Filesave/S2Pic.png")
solimage3 = pygame.image.load("Source/_bin/_cache/_remove/_Save/S3Pic.png")

pygame.display.set_icon(mcmasterlogo64x)

##Image Loading--------------------------

def actionButton(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h),0)
        if click[0] == 1 and action != None:
            action()
        
    else:
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h),0)

    smallText = pygame.font.SysFont("calibri",20)
    textSurf,textRect = text_objects(msg, smallText, black)
    textRect.center = (int(x+(w/2)),int(y+(h/2)))
    gameDisplay.blit(textSurf,textRect)

# Drawing right grid
def drawTrack():
    blockwidth = 64
    blockheight = 64
    for x in range(1024,1472,blockwidth):
        for y in range(192,640,blockheight):
            rect = pygame.Rect(x,y,blockwidth,blockheight)
            pygame.draw.rect(gameDisplay,black,rect,4) # black outlines around each square

# Drawing left grid
def drawGrid():
    blockwidth = 64
    blockheight = 64
    for x in range(128,576,blockwidth):
        for y in range(192,640,blockheight):
            rect = pygame.Rect(x,y,blockwidth,blockheight)
            pygame.draw.rect(gameDisplay,black,rect,3)


def text_objects(text, font,color):
    textSurface = font.render(text, True, color) #second parameter antialiasing
    return textSurface,textSurface.get_rect()


# Left and right grid axes arrows and labels
def drawXaxis(x,y,msg):
    gameDisplay.blit(sidearrow,(x,y))
    smallText = pygame.font.SysFont("calibri",20)
    textSurf,textRect = text_objects(msg, smallText, black)
    textRect.center = (int(x+(224)),int(y+(30)))
    gameDisplay.blit(textSurf,textRect)

def drawYaxis(side,x,y,msg):
    gameDisplay.blit(uparrow,(x,y))
    font = pygame.font.SysFont('calibri', 20)
    
    smallText = font.render(msg,True,black)
    smallText = pygame.transform.rotate(smallText, 90)
    if side==1:
        gameDisplay.blit(smallText,(x+30,y+189))
    elif side==2:
        gameDisplay.blit(smallText,(x-15,y+189))
# Left and right grid axes arrows and labels


#GUI Drawing
def drawShipBox(x,y):
    pygame.draw.rect(gameDisplay, (183,174,245), pygame.Rect(131, 704, 442, 26), 0)
    pygame.draw.rect(gameDisplay, (56,53,78), pygame.Rect(128, 700, 448, 180),5)
    smallText = pygame.font.SysFont("calibri",20)
    textSurf,textRect = text_objects('Your Ships', smallText, black)
    textRect.center = (int(x//2),int(y))
    gameDisplay.blit(textSurf,textRect)

def drawInfoBox(x,y,w,h,msg,color):
    pygame.draw.rect(gameDisplay, color, pygame.Rect(x, y, w, h),0)
    smallText = pygame.font.SysFont("calibri",15)
    textSurf,textRect = text_objects(msg, smallText, black)
    textRect.center = (int(w-90),int(y+25))
    gameDisplay.blit(textSurf,textRect)

def drawInfoBox2(x,y,w,h,msg,color):
    pygame.draw.rect(gameDisplay, color, pygame.Rect(x, y, w, h),0)
    smallText = pygame.font.SysFont("calibri",14)
    textSurf,textRect = text_objects(msg, smallText, black)
    textRect.center = (int(w-90),int(y+25))
    gameDisplay.blit(textSurf,textRect)

def drawInfoBox3(x,y,w,h,msg,color):
    pygame.draw.rect(gameDisplay, color, pygame.Rect(x, y, w, h),0)
    smallText = pygame.font.SysFont("calibri",13)
    textSurf,textRect = text_objects(msg, smallText, black)
    textRect.center = (int(w-90),int(y+25))
    gameDisplay.blit(textSurf,textRect)

def drawHitBox(x,y):
    pygame.draw.rect(gameDisplay, (56,53,78), pygame.Rect(51, 700, 80, 180),5)
    smallText = pygame.font.SysFont("calibri",20)
    textSurf,textRect = text_objects('Hits', smallText, black)
    textRect.center = (int(x//2),int(y))
    gameDisplay.blit(textSurf,textRect)

def drawMarkerBox(x,y):
    pygame.draw.rect(gameDisplay, (56,53,78), pygame.Rect(1024, 700, 448, 180),5)
    smallText = pygame.font.SysFont("calibri",20)
    textSurf,textRect = text_objects('', smallText, black)
    textRect.center = (int(x//2),int(y))
    gameDisplay.blit(textSurf,textRect)

def drawTitle(x,y,msg,color,size):
    font = pygame.font.SysFont("calibri",size)
    text = font.render(msg,True,color)
    gameDisplay.blit(text,(x,y))
    
def missCounter(count):
    font = pygame.font.SysFont('calibri',25)
    text = font.render("Hits Missed: " + str(count),True,black)
    gameDisplay.blit(text,(1070,718))
    pygame.draw.rect(gameDisplay,teal,(1040,714,20,20),0)

def hitCounter(count):
    font = pygame.font.SysFont('calibri',25)
    text = font.render("Hits Landed: " + str(count),True,black)
    gameDisplay.blit(text,(1070,759))
    pygame.draw.rect(gameDisplay,red,(1040,755,20,20),0)

# Generating random ships for Mass vs Price
def loadships():
    if randships[0] == 1:
        gameDisplay.blit(styroship,(150,448))
        drawInfoBox(128,730,448,50,'A5 A6: Very Light, Cheap, Styrofoam Cruiser',(170,156,255))

    elif randships[0] == 2:
        gameDisplay.blit(leathership1,(256,405))
        drawInfoBox(128,730,448,50,'C4 D4: Light, Medium Price, Leather Cruiser',(170,156,255))

    elif randships[0] == 3:
        gameDisplay.blit(silvership,(470,256))
        drawInfoBox(128,730,448,50,'F2 F3: Heavy, Expensive, Silver Cruiser',(170,156,255))

    if randships[1] == 4:
        gameDisplay.blit(corkship,(214,448))
        drawInfoBox(128,780,448,50,'B5 B6: Light, Cheap, Cork Destroyer',(157,145,235))

    elif randships[1] == 5:
        gameDisplay.blit(concreteship,(320,597))
        drawInfoBox(128,780,448,50,'D7 E7: Medium Weight, Very Cheap, Concrete Destroyer',(157,145,235))

    elif randships[1] == 6:
        gameDisplay.blit(goldship,(534,192))
        drawInfoBox(128,780,448,50,'G1 G2: Very Heavy, Very Expensive, Gold Destroyer',(157,145,235))

    if randships[2] == 7:
        gameDisplay.blit(cardship,(256,530))
        drawInfoBox(128,830,448,50,'C6 D6: Light, Cheap, Cardboard Battleship',(157,145,235))

    elif randships[2] == 8:
        gameDisplay.blit(steelship,(384,469))
        drawInfoBox(128,830,448,50,'E5 F5: Heavy, Slightly Expensive, Steel Battleship',(157,145,235))

    elif randships[2] == 9:
        gameDisplay.blit(tungship1,(534,320))
        drawInfoBox(128,830,448,50,'G3 G4: Very Heavy, Expensive, Tungsten Battleship',(157,145,235))

# Generating random ships for Mass vs Stiffness
def loadships2():
    if randships[3] == 1:
        gameDisplay.blit(styroship,(150,512))
        drawInfoBox(128,730,448,50,'A6 A7: Very Light, Very Elastic, Styrofoam Cruiser',(170,156,255))

    elif randships[3] == 2:
        gameDisplay.blit(woodship,(256,406))
        drawInfoBox(128,730,448,50,'C4 D4: Medium Weight, Medium Stiffness, Wood Cruiser',(170,156,255))

    elif randships[3] == 3:
        gameDisplay.blit(tungship,(448,214))
        drawInfoBox(128,730,448,50,'F1 G1: Very Heavy, Very Stiff, Tungsten Cruiser',(170,156,255))

    if randships[4] == 4:
        gameDisplay.blit(corkship,(214,512))
        drawInfoBox(128,780,448,50,'B6 B7: Light, Elastic, Cork Destroyer',(157,145,235))
        
    elif randships[4] == 5:
        gameDisplay.blit(leathership,(278,448))
        drawInfoBox(128,780,448,50,'C5 C6: Light, Slightly Elastic, Leather Destroyer',(157,145,235))

    elif randships[4] == 6:
        gameDisplay.blit(alumship,(406,320))
        drawInfoBox(128,780,448,50,'E3 E4: Slightly Heavy, Stiff, Aluminum Destroyer',(157,145,235))

    if randships[5] == 7:
        gameDisplay.blit(rubbership,(320,598))
        drawInfoBox(128,830,448,50,'D7 E7: Medium Weight, Very Elastic, Rubber Battleship',(157,145,235))

    elif randships[5] == 8:
        gameDisplay.blit(bambooship,(256,342))
        drawInfoBox(128,830,448,50,'C3 D3: Medium Weight, Stiff, Bamboo Battleship',(157,145,235))

    elif randships[5] == 9:
        gameDisplay.blit(steelship,(384,278))
        drawInfoBox(128,830,448,50,'E2 F2: Heavy, Stiff, Steel Battleship',(157,145,235))

# Generating random ships for Thermal Conductivity vs Yield Strength
def loadships3():
    if randships[6] == 1:
        gameDisplay.blit(styroship,(150,512))
        drawInfoBox3(128,730,448,50,'A6 A7: Very Low Heat Conductivity and Yield Strength, Styrofoam Cruiser',(170,156,255))

    elif randships[6] == 2:
        gameDisplay.blit(concreteship,(320,533))
        drawInfoBox3(128,730,448,50,'D6 E6: Medium Heat Conductivity, Fairly Low Yield Strength, Concrete Cruiser',(170,156,255))

    elif randships[6] == 3:
        gameDisplay.blit(alumship2,(448,277))
        drawInfoBox3(128,730,448,50,'F2 G2: Very High Heat Conductivity, High Yield Strength, Aluminum Destroyer',(170,156,255))

    if randships[7] == 4:
        gameDisplay.blit(rubbership2,(214,448))
        drawInfoBox3(128,780,448,50,'B5 B6: Low Heat Conductivity, Low Yield Strength, Rubber Destroyer',(157,145,235))

    elif randships[7] == 5:
        gameDisplay.blit(brickship,(256,469))
        drawInfoBox3(128,780,448,50,'C5 D5: Medium Heat Conductivity, Medium Yield Strength, Brick Cruiser',(157,145,235))

    elif randships[7] == 6:
        gameDisplay.blit(leadship,(406,320))
        drawInfoBox3(128,780,448,50,'E3 E4: Slightly High Heat Conductivity, Medium Yield Strength, Lead Destroyer',(157,145,235))

    if randships[8] == 7:
        gameDisplay.blit(bambooship2,(192,405))
        drawInfoBox3(128,830,448,50,'B4 C4: Low Heat Conductivity, Slightly High Yield Strength, Bamboo Battleship',(157,145,235))

    elif randships[8] == 8:
        gameDisplay.blit(titanship,(320,213))
        drawInfoBox3(128,830,448,50,'D1 E1: Medium Heat Conductivity, Very High Yield Strength, Titanium Battleship',(157,145,235))

    elif randships[8] == 9:
        gameDisplay.blit(tinship,(470,320))
        drawInfoBox3(128,830,448,50,'F3 F4: Fairly High Heat Conductivity, Medium Yield Strength, Tin Battleship',(157,145,235))


def generateNewrand1():
    global randships

    randships[0] = random.randint(1,3)
    randships[1] = random.randint(4,6)
    randships[2] = random.randint(7,9)

    time.sleep(0.3)

def generateNewRand2():
    global randships

    randships[3] = random.randint(1,3) # 1=styrofoam, 2=wood, 3=tungsten
    randships[4] = random.randint(4,6) # 4=cork 5=leather 6=aluminum
    randships[5] = random.randint(7,9) # 7=rubber 8=bamboo 9=steel
    
    time.sleep(0.3)

def generateNewrand3():
    global randships
    
    randships[6] = random.randint(1,3)
    randships[7] = random.randint(4,6)
    randships[8] = random.randint(7,9)
    
    time.sleep(0.3)


def clearBoard():

    global hits,misses

    hits[0] = 0
    misses[0] = 0

    # Second block: 56–104
    for i in range(55, 103):
        grid_colors[i] = darkgrey

def clearBoard2():

    global hits, misses
    hits[1] = 0
    misses[1] = 0

    for i in range(1, 50):
        grid_colors[i] = darkgrey

def clearBoard3():

    global hits,misses

    hits[2] = 0
    misses[2] = 0

    # Third block: 111–148
    for i in range(111, 159):
        grid_colors[i] = darkgrey

def doNothing():
    pass


#Tracking Buttons Function Definition--------------------------
def HMbutton(level, index, x, y, w, h):
    # Make the correct global variables available for modification
    global hits, misses

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    current_color = grid_colors.get(index, darkgrey)

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, grey, (x, y, w, h))
        if click[0] == 1:  # Left click (miss)
            if current_color == teal:
                pass
            elif current_color == red:
                grid_colors[index] = teal
                if level == 1:
                    hits[0] -= 1
                    misses[0] += 1
                elif level == 2:
                    hits[1] -= 1
                    misses[1] += 1
                elif level == 3:
                    hits[2] -= 1
                    misses[2] += 1
            else:
                grid_colors[index] = teal
                if level == 1:
                    misses[0] += 1
                elif level == 2:
                    misses[1] += 1
                elif level == 3:
                    misses[2] += 1
        elif click[2] == 1:  # Right click (hit)
            if current_color == red:
                pass
            elif current_color == teal:
                grid_colors[index] = red
                if level == 1:
                    misses[0] -= 1
                    hits[0] += 1
                elif level == 2:
                    misses[1] -= 1
                    hits[1] += 1
                elif level == 3:
                    misses[2] -= 1
                    hits[2] += 1
            else:
                grid_colors[index] = red
                if level == 1:
                    hits[0] += 1
                elif level == 2:
                    hits[1] += 1
                elif level == 3:
                    hits[2] += 1
    else:
        pygame.draw.rect(gameDisplay, current_color, (x, y, w, h))


#Tracking Buttons Function Definition--------------------------


## Hit Button Definition--------------------------

# Personal record located below left grid to indicate status of your ships (green=unharmed, red=hit)
def Hbutton(index, x, y, w, h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    current_color = grid_colors.get(index, green)  # default color is green to unharmed status

    # if within personal scoring box range
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, light_red, (x, y, w, h), 0) # hover colour
        if click[0] == 1: # left click (hit)
            grid_colors[index] = red
        elif click[2] == 1: # right click (unharmed)
            grid_colors[index] = green
    else:
        pygame.draw.rect(gameDisplay, current_color, (x, y, w, h), 0)
## Hit Button Definition--------------------------


## Main Menu Button Definition -----------------
def startButton(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h),0)
        if click[0] == 1 and action != None:
            action()
        
    else:
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h),0)

    smallText = pygame.font.SysFont("calibri",20)
    textSurf,textRect = text_objects(msg, smallText, black)
    textRect.center = (int(x+(w/2)),int(y+(h/2)))
    gameDisplay.blit(textSurf,textRect)

#Additional sleep timer here (0.4 to prevent double clicks)
def startButton2(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Highlight the button if hovering
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h), 0)
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h), 0)

    smallText = pygame.font.SysFont("calibri", 20)
    textSurf, textRect = text_objects(msg, smallText, black)
    textRect.center = (int(x + (w / 2)), int(y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)

    # Check if a mouse click happened in the event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if x + w > event.pos[0] > x and y + h > event.pos[1] > y:
                if action is not None:
                    action()

#Additional sleep timer and smaller inner text - In the future, just make text size a parameter variable as well
def startButton3(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h),0)
        if click[0] == 1 and action != None:
            time.sleep(0.4)
            action()
        
    else:
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h),0)

    smallText = pygame.font.SysFont("calibri",18)
    textSurf,textRect = text_objects(msg, smallText, black)
    textRect.center = (int(x+(w/2)),int(y+(h/2)))
    gameDisplay.blit(textSurf,textRect)

# No sleep timer but smaller text
def startButton4(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h),0)
        if click[0] == 1 and action != None:
            action()
        
    else:
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h),0)

    smallText = pygame.font.SysFont("calibri",18)
    textSurf,textRect = text_objects(msg, smallText, black)
    textRect.center = (int(x+(w/2)),int(y+(h/2)))
    gameDisplay.blit(textSurf,textRect)

## Main Menu Button Definition -----------------

#Level Solutions ======================================================
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
#Level Solutions ======================================================

#Level 1===================================================
def game_loop():
    
    generateNewrand1()
    gameExit = False
    global counts
    global lock1

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        gameDisplay.blit(bg,(0,0))
        loadships()

        drawTrack()
        drawGrid()

        drawTitle(200,60,'Your Ship Board',(11,112,8),50)
        drawTitle(1050,60,'Your Tracking Board',(112,24,8),50)
        drawTitle(575,120,'Materials Properties Battleship',(212,159,15),36)

        drawXaxis(128,650,'Mass')
        drawXaxis(1024,650,'Mass')
        drawYaxis(1,590,192,'Price in Dollars')
        drawYaxis(2,940,192,'Price in Dollars')

        drawShipBox(700,720)
        drawHitBox(185,720)
        drawMarkerBox(300,300)

        drawTitle(1035,800,'Reminder: Left click to track a MISS in blue',(56,43,110),18)
        drawTitle(1032,830,'                    Right click to track a HIT in red',(110,43,43),18)

        actionButton('Get New Ships!',653,800,300,64,green,light_green,generateNewrand1)
        gameDisplay.blit(mcmasterlogo180x,(690,20))

        actionButton('CLEAR BOARD!!',1250,730,190,30,red,light_red,clearBoard)

        actionButton('Back',30,15,140,30,green,light_green,level_select)
        actionButton('Exit Game',1430,15,140,30,red,light_red,quitgame)

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

        #Hit Buttons 105-110--------------------------
        Hbutton(105,64,745,20,20)
        Hbutton(106,99,745,20,20)

        Hbutton(107,64,795,20,20)
        Hbutton(108,99,795,20,20)

        Hbutton(109,64,845,20,20)
        Hbutton(110,99,845,20,20)
        #Hit Buttons --------------------------

        #H/M tracking ------------------------
        hitCounter(hits[0])
        missCounter(misses[0])

        #Fade in wintable ---------------------
        
        if hits[0] >= 6:
            lock1 = True
            if counts[0] == 255:
                gameDisplay.blit(wintable2,(650,170))
                startButton('Hint',(display_width//2)-85,720,150,40,yellow,light_yellow,hintscreen1)
                pass

            elif counts[0] != 255 :
                wintable2.set_alpha(counts[0])
                counts[0] += 17
                gameDisplay.blit(wintable2,(650,170))

        #Fade in wintable ---------------------

        #Tracking Buttons 55-102---------------------

        # Top row (A1–G1) — indices 91–96
        for i, x in enumerate(range(1027, 1412, 64), start=91):
            HMbutton(1,i, x, 194, 60, 60)

        # Rightmost column (G2–G7) — indices 97–102
        for i, y in enumerate(range(258, 579, 64), start=97):
            HMbutton(1,i, 1411, y, 60, 60)

        # Main 6×6 tracking grid (B2–F7) — indices 55-90
        index = 55
        for y in range(258, 579, 64):
            for x in range(1027, 1348, 64):
                HMbutton(1,index, x, y, 60, 60)
                index += 1

        #Tracking Buttons ---------------------

        pygame.display.update()
        clock.tick(60)

def hintscreen1():

    hint1 = False

    while not hint1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(bg,(0,0))

        drawTitle((display_width)//2 - 300,10,"Level 1: Density (Mass) vs Price Hint",(11,112,8),50)

        startButton('Back',(display_width//2)-75,760,150,40,green,light_green,game_loop)
        gameDisplay.blit(hintimage1,((display_width//2)-600,80))
                

        pygame.display.update()
        clock.tick(60)
#Level 1 ===================================================    

#Level 2 ===================================================    
def game_loop2():
    
    generateNewRand2()
    gameExit2 = False
    global counts
    global lock2

    while not gameExit2:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        gameDisplay.blit(bg,(0,0))
        loadships2()

        #Track Draw ---------------------------
        drawTrack()
        drawGrid()

        drawTitle(200,60,'Your Ship Board',(11,112,8),50)
        drawTitle(1050,60,'Your Tracking Board',(112,24,8),50)
        drawTitle(575,120,'Materials Properties Battleship',(212,159,15),36)

        drawXaxis(128,650,'Mass')
        drawXaxis(1024,650,'Mass')
        drawYaxis(1,590,192,'Stiffness')
        drawYaxis(2,940,192,'Stiffness')

        drawShipBox(700,720)
        drawHitBox(185,720)
        drawMarkerBox(300,300)

        drawTitle(1035,800,'Reminder: Left click to track a MISS in blue',(56,43,110),18)
        drawTitle(1032,830,'                    Right click to track a HIT in red',(110,43,43),18)

        actionButton('Get New Ships!',653,800,300,64,green,light_green,generateNewRand2)
        gameDisplay.blit(mcmasterlogo180x,(690,20))

        actionButton('CLEAR BOARD!!',1250,730,190,30,red,light_red,clearBoard2)

        actionButton('Back',30,15,140,30,green,light_green,level_select)
        actionButton('Exit Game',1430,15,140,30,red,light_red,quitgame)
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

        #Hit Buttons 50-55--------------------------
        Hbutton(50,64,745,20,20)
        Hbutton(51,99,745,20,20)

        Hbutton(52,64,795,20,20)
        Hbutton(53,99,795,20,20)

        Hbutton(54,64,845,20,20)
        Hbutton(55,99,845,20,20)
        #Hit Buttons --------------------------

        #H/M tracking ------------------------
        hitCounter(hits[1])
        missCounter(misses[1])

        #Fade in wintable ---------------------
        
        if hits[1] >= 6:
            lock2 = True
            if counts[1] == 255:
                gameDisplay.blit(wintable,(650,170))
                startButton('Hint',(display_width//2)-85,720,150,40,yellow,light_yellow,hintscreen2)
                pass

            elif counts[1] != 255 :
                wintable.set_alpha(counts[1])
                counts[1] += 17
                gameDisplay.blit(wintable,(650,170))

        #Fade in wintable ---------------------
                                   
        #Tracking Buttons 1-49 ---------------------
        
        # Top row (indices 37–43) Row 1 (A1–G1)
        for i, x in enumerate(range(1027, 1412, 64), start=37):
            HMbutton(2,i, x, 194, 60, 60)

        # Rightmost column (indices 44–49) Column G (G2–G7)
        for i, y in enumerate(range(258, 579, 64), start=44):
            HMbutton(2,i, 1411, y, 60, 60)

        # Main 6x6 grid (indices 1–36) Rows 2–7, Columns A–F
        index = 1
        for y in range(258, 579, 64):
            for x in range(1027, 1348, 64):
                HMbutton(2,index, x, y, 60, 60)
                index += 1

        #Tracking Buttons ---------------------
        
        pygame.display.update()
        clock.tick(60)

def hintscreen2():

    hint1 = False

    while not hint1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(bg,(0,0))

        drawTitle((display_width)//2 - 590,10,"Level 2: Density (Mass) vs Young's Modulus (Stiffness) Hint",(11,112,8),50)

        startButton('Back',(display_width//2)-75,760,150,40,green,light_green,game_loop2)
        gameDisplay.blit(hintimage2,((display_width//2)-600,80))

        pygame.display.update()
        clock.tick(60)
#Level 2===================================================

#Level 3 ===================================================    
def game_loop3():
    
    generateNewrand3()
    gameExit3 = False
    global counts
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
        drawYaxis(1,590,192,'Yield Strength')
        drawYaxis(2,940,192,'Yield Strength')

        drawShipBox(700,720)
        drawHitBox(185,720)
        drawMarkerBox(300,300)

        drawTitle(1035,800,'Reminder: Left click to track a MISS in blue',(56,43,110),18)
        drawTitle(1032,830,'                    Right click to track a HIT in red',(110,43,43),18)

        actionButton('Get New Ships!',653,800,300,64,green,light_green,generateNewrand3)
        gameDisplay.blit(mcmasterlogo180x,(690,20))

        actionButton('CLEAR BOARD!!',1250,730,190,30,red,light_red,clearBoard3)

        actionButton('Back',30,15,140,30,green,light_green,level_select)
        actionButton('Exit Game',1430,15,140,30,red,light_red,quitgame)

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

        #Hit Buttons 160-165 --------------------------
        Hbutton(160,64,745,20,20)
        Hbutton(161,99,745,20,20)

        Hbutton(162,64,795,20,20)
        Hbutton(163,99,795,20,20)

        Hbutton(164,64,845,20,20)
        Hbutton(165,99,845,20,20)
        #Hit Buttons --------------------------

        #H/M tracking ------------------------
        hitCounter(hits[2])
        missCounter(misses[2])

        #Fade in wintable ---------------------

        if hits[2] >= 6:
            lock3 = True
            if counts[2] == 255:
                gameDisplay.blit(wintable3,(639,170))
                startButton('Hint',(display_width//2)-85,720,150,40,yellow,light_yellow,hintscreen3)
                pass

            elif counts[2] != 255 :
                wintable3.set_alpha(counts[2])
                counts[2] += 17
                gameDisplay.blit(wintable3,(639,170))

        #Fade in wintable ---------------------

        #Tracking Buttons ---------------------

        # Top row (A1–G1) — indices 147–153
        for i, x in enumerate(range(1027, 1412, 64), start=147):
            HMbutton(3,i, x, 194, 60, 60)

        # Rightmost column (G2–G7) — indices 153–159
        for i, y in enumerate(range(258, 579, 64), start=153):
            HMbutton(3,i, 1411, y, 60, 60)

        # Main 6×6 tracking grid (B2–F7) — indices 111–146
        index = 111
        for y in range(258, 579, 64):
            for x in range(1027, 1348, 64):
                HMbutton(3,index, x, y, 60, 60)
                index += 1

        #Tracking Buttons ---------------------
        
        pygame.display.update()
        clock.tick(60)
    
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

#Level 3 ===================================================    


#Fade =======================
def fade(width,height):

    fade = pygame.Surface((width,height))
    fade.fill(white)

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
    TextSurf1, TextRect1 = text_objects('McMaster University - Materials Properties Battleship Educational Game',smallTitleText,orange)
    TextRect1.center = (int((display_width/2)+30), int((display_height/2)-170))
    gameDisplay.blit(TextSurf1,TextRect1)

    smallTitleText1 = pygame.font.SysFont('calibri',35)
    TextSurf4, TextRect4 = text_objects('Developed for Windows',smallTitleText1,orange)
    TextRect4.center = ((int((display_width/2)+30),int((display_height/2)-50)))
    gameDisplay.blit(TextSurf4,TextRect4)

    TextSurf5, TextRect5 = text_objects('Ashby Charts From ANSYS Granta Edupack 2021 R2 Software',smallTitleText1,orange)
    TextRect5.center = ((int((display_width/2)+30),int((display_height/2)-100)))
    gameDisplay.blit(TextSurf5,TextRect5)

    copyrighttext = pygame.font.SysFont('calibri',25)
    copyrighttext2 = pygame.font.SysFont('calibri',22)

    TextSurf2, TextRect2 = text_objects('Developed by Dr. Bosco Yu and Muhammad Arshad',copyrighttext,(darkgrey))
    TextRect2.center = ((int((display_width/2)+30),int((display_height/2)+350)))
    gameDisplay.blit(TextSurf2,TextRect2)

    TextSurf3, TextRect3 = text_objects('©2022 McMaster University. All rights reserved',copyrighttext2,(darkgrey))
    TextRect3.center = ((int((display_width/2)+30),int((display_height/2)+380)))
    gameDisplay.blit(TextSurf3,TextRect3)

    new_rect = mcmasterlogo.get_rect(center = mcmasterlogo.get_rect(topleft = ((display_width//2)-150,20)).center)
    gameDisplay.blit(mcmasterlogo,new_rect)
#Fade =======================

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
        TextSurf, TextRect = text_objects('Materials Science Educational Game',largeText,orange)
        TextRect.center = ((int((display_width/2)+30),int((display_height/2)-230)))
        gameDisplay.blit(TextSurf,TextRect)

        smallTitleText = pygame.font.SysFont('calibri',35)
        TextSurf1, TextRect1 = text_objects('McMaster University - Materials Properties Battleship',smallTitleText,orange)
        TextRect1.center = (int((display_width/2)+30), int((display_height/2)-170))
        gameDisplay.blit(TextSurf1,TextRect1)

        copyrighttext = pygame.font.SysFont('calibri',25)
        copyrighttext2 = pygame.font.SysFont('calibri',22)
        
        TextSurf2, TextRect2 = text_objects('Developed by Dr. Bosco Yu and Muhammad Arshad',copyrighttext,(darkgrey))
        TextRect2.center = (int((display_width/2)+30), int((display_height/2)+350))
        gameDisplay.blit(TextSurf2,TextRect2)

        TextSurf3, TextRect3 = text_objects('©2022 McMaster University. All rights reserved',copyrighttext2,(darkgrey))
        TextRect3.center = (int((display_width/2)+30), int((display_height/2)+380))
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

        startButton3('Easy: Mass vs Price',(display_width//2)-600,400,330,150,lime,light_lime,game_loop)
        startButton3('Medium: Mass vs Stiffness',(display_width//2)-135,400,330,150,yellow,light_yellow,game_loop2)
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

## Intro Screen ------------------
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
        TextSurf1, TextRect1 = text_objects('McMaster University - Materials Properties Battleship Educational Game',smallTitleText,orange)
        TextRect1.center = (int((display_width/2)+30), int((display_height/2)-170))
        gameDisplay.blit(TextSurf1,TextRect1)

        smallTitleText1 = pygame.font.SysFont('calibri',35)
        TextSurf4, TextRect4 = text_objects('Developed for Windows',smallTitleText1,orange)
        TextRect4.center = ((int((display_width/2)+30),int((display_height/2)-50)))
        gameDisplay.blit(TextSurf4,TextRect4)

        TextSurf5, TextRect5 = text_objects('Ashby Charts From ANSYS Granta Edupack 2021 R2 Software',smallTitleText1,orange)
        TextRect5.center = ((int((display_width/2)+30),int((display_height/2)-100)))
        gameDisplay.blit(TextSurf5,TextRect5)

        copyrighttext = pygame.font.SysFont('calibri',25)
        copyrighttext2 = pygame.font.SysFont('calibri',22)

        TextSurf2, TextRect2 = text_objects('Developed by Dr. Bosco Yu and Muhammad Arshad',copyrighttext,(darkgrey))
        TextRect2.center = ((int((display_width/2)+30),int((display_height/2)+350)))
        gameDisplay.blit(TextSurf2,TextRect2)

        TextSurf3, TextRect3 = text_objects('©2022 McMaster University. All rights reserved',copyrighttext2,(darkgrey))
        TextRect3.center = ((int((display_width/2)+30),int((display_height/2)+380)))
        gameDisplay.blit(TextSurf3,TextRect3)

        new_rect = mcmasterlogo.get_rect(center = mcmasterlogo.get_rect(topleft = ((display_width//2)-150,20)).center)
        gameDisplay.blit(mcmasterlogo,new_rect)

        current_time = time.time()

        #Fade screen after 1.5 seconds
        if current_time - start_time > 1:
            fade(display_width,display_height)
        
        pygame.display.update()
        clock.tick(60)
## Intro Screen ---------------------

def quitgame():
    pygame.quit()
    sys.exit()


intro_screen()

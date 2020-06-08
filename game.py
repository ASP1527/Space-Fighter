import pygame, os #importing the pygame module
import random

pygame.init() #initialising the game

screenwidth = 800
screenheight = 600

win = pygame.display.set_mode((screenwidth,screenheight)) #creating the box that the game will be in

pygame.display.set_caption("Game")

s1 = pygame.image.load('starfighter.png')
s2 = pygame.image.load('tiefighter.png')
s3 = pygame.image.load('rocketup.png')
s4 = pygame.image.load('general.png')

runall = True #variable that runs the game
normalmode = False
starwars1 = False
starwars2 = False
starwars3 = False

displayinstruction = 0

while runall:
  class button(): #creates a button
    def __init__(self, color, x,y,width,height, text=''):
      self.color = color #button colour
      self.x = x #button x xoordinate
      self.y = y #button y coordinate
      self.width = width #button width
      self.height = height #button height
      self.text = text #text inside the button

    def drawbutton(self,win): #draws the button
      pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0) #button is a rectangle
      #next bit of code loads a font and centres the text inside the button
      font = pygame.font.SysFont('comicsans', 28)
      text = font.render(self.text, 1, (255,255,255))
      win.blit(text, (self.x + (round(self.width/2) - round(text.get_width()/2)), self.y + (round(self.height/2) - round(text.get_height()/2))))

    def isOver(self, pos): #checks if the mouse is over the button
      if pos[0] > self.x and pos[0] < self.x + self.width:
        if pos[1] > self.y and pos[1] < self.y + self.height:
          return True
              
      return False

  def redrawbutton(): #drawing all of the buttons
    win.fill((0,0,0))
    greenbutton.drawbutton(win)
    bluebutton.drawbutton(win)
    redbutton.drawbutton(win)
    whitebutton.drawbutton(win)
    quitbutton.drawbutton(win)
    win.blit(s1, (100,5))
    win.blit(s2, (453,5))
    win.blit(s3, (458,445))
    win.blit(s4, (100,445))
    

  choice = True #variable that is true until you pick a button
  #defining the button, (colour, x, y, width, height, text)
  greenbutton = button((0,0,0), 50,50,150,50,'Jedi Starfighter')
  bluebutton = button((0,0,0), 400,50,150,50,'Death Star')
  redbutton = button((0,0,0), 50,500,150,50,'Cough Cough')
  whitebutton = button((0,0,0), 400,500,150,50,'Rocket')
  quitbutton = button((0,0,0), 725,0,75,50,'Quit')
  while choice: #while you have not chosen a button
    redrawbutton() #calls the function to draw the button
    pygame.display.update() #refreshes the display

    for event in pygame.event.get(): #gets the position of the mouse
      pos = pygame.mouse.get_pos()

      if event.type == pygame.QUIT: #if you quit the game it stops running
        choice = False
        pygame.quit()

      #checks which button you click and loads in the sprites for that option
      if event.type == pygame.MOUSEBUTTONDOWN: 
        if greenbutton.isOver(pos):
          #print ("clicked")
          rocketup = pygame.image.load('starfighter.png')
          bg1 = pygame.image.load('corusant.png')
          comet = pygame.image.load('droid.png')
          comet1 = pygame.image.load('droid.png')
          comet2 = pygame.image.load('droid.png')
          comet3 = pygame.image.load('droid.png')
          comet4 = pygame.image.load('droid.png')
          choice = False #chosen a button
          starwars1 = True
          starwars2 = False
          normalmode = False
          starwars3 = False
          displayinstruction += 1
        if bluebutton.isOver(pos):
          #print ("clicked")
          rocketup = pygame.image.load('tiefighter.png')
          bg1 = pygame.image.load('deathstar.png')
          comet = pygame.image.load('x-wing.png')
          comet1 = pygame.image.load('x-wing.png')
          comet2 = pygame.image.load('x-wing.png')
          comet3 = pygame.image.load('x-wing.png')
          comet4 = pygame.image.load('x-wing.png')
          choice = False #chosen a button
          starwars2 = True
          starwars1 = False
          normalmode = False
          starwars3 = False
          displayinstruction += 1
        if redbutton.isOver(pos):
          #print ("clicked")
          rocketup = pygame.image.load('general.png')
          bg1 = pygame.image.load('corusant.png')
          comet = pygame.image.load('pod.png')
          comet1 = pygame.image.load('pod.png')
          comet2 = pygame.image.load('pod.png')
          comet3 = pygame.image.load('pod.png')
          comet4 = pygame.image.load('pod.png')
          choice = False #chosen a button
          normalmode = False
          starwars1 = False
          starwars2 = False
          starwars3 = True
          displayinstruction += 1
        if whitebutton.isOver(pos):
          #print ("clicked")
          rocketup = pygame.image.load('rocketup.png')
          bg1 = pygame.image.load('spacebg.png')
          comet = pygame.image.load('comet.png')
          comet1 = pygame.image.load('comet.png')
          comet2 = pygame.image.load('comet.png')
          comet3 = pygame.image.load('comet.png')
          comet4 = pygame.image.load('comet.png')
          choice = False #chosen a button
          normalmode = True
          starwars1 = False
          starwars2 = False
          starwars3 = False
          displayinstruction += 1
        if quitbutton.isOver(pos): #if you press the quit button, the game quits
          #print ("clicked")
          choice = False #chosen a button
          runall = False #stops everything and quits

  x = 360 #defines x coordinate of character
  y = 480 #defines y coordinate
  width = 50 #width of character
  height = 50 #height of character
  vel = 7 #speed of character

  #defining the x & y coordinates and velocity of the "comets" 
  #it is all random
  cometx = random.randint(50,750)
  comety = random.randint(-300,-100)
  cometvel = random.randint(1,3)

  cometx1 = random.randint(50,750)
  comety1 = random.randint(-300,-100)
  cometvel1 = random.randint(1,3)

  cometx2 = random.randint(50,750)
  comety2 = random.randint(-300,-100)
  cometvel2 = random.randint(1,3)

  cometx3 = random.randint(50,750)
  comety3 = random.randint(-300,-100)
  cometvel3 = random.randint(1,3)

  cometx4 = random.randint(50,750)
  comety4 = random.randint(-300,-100)
  cometvel4 = random.randint(1,3)

  #creates a class for the bullets
  class projectile(object):
    def __init__(self,x,y,radius,colour,facing):
      self.x = x #x coordinate
      self.y = y - 25 #y coordinate (top of sprite) 
      self.radius = radius #radius of the bullet
      self.colour = (0,0,255) #colour of the bullet
      self.facing = facing #direction of the bullet(only straight)
      self.vel = 10 #bullet speed
    
    def draw(self, win): #draws the bullet
      pygame.draw.circle(win, self.colour, (self.x,self.y), self.radius)

  up = True #direction of sprite
  upshoot = True
  score = 0 #score

  def redrawbg(background, sprite): #function
    win.blit(background, (0,0)) #draws background
    text1 = font.render("Score: " + str(score), True, (100, 200, 255))
    win.blit(text1, (10,10))
    pygame.display.update() #refreshes the screen
    global hitbox #creates boxes around everything to check if the bullt hits the "comet"
    hitbox = (x - 5, y, 50, 50)
    global cometbox
    cometbox = (cometx, comety, 50, 50)
    global cometbox1
    cometbox1 = (cometx1, comety1, 50, 50)
    global cometbox2
    cometbox2 = (cometx2, comety2, 50, 50)
    global cometbox3
    cometbox3 = (cometx3, comety3, 50, 50)
    global cometbox4
    cometbox4 = (cometx4, comety4, 50, 50)
    #if right:
    #  win.blit(rocketright, (x, y))
    #elif left:
    #  win.blit(rocketleft, (x, y))
    if up:
      win.blit(rocketup, (x, y))
    #pygame.draw.rect(win, (255,0,0), hitbox, 2)
    for bullet in bullets: #draws the bullets
      bullet.draw(win)
      
    #draws the comets
    win.blit(comet, (cometx, comety))
    #pygame.draw.rect(win, (255,0,0), cometbox, 2)
    win.blit(comet1, (cometx1, comety1))
    #pygame.draw.rect(win, (255,0,0), cometbox1, 2)
    win.blit(comet2, (cometx2, comety2))
    #pygame.draw.rect(win, (255,0,0), cometbox2, 2)
    win.blit(comet3, (cometx3, comety3))
    #pygame.draw.rect(win, (255,0,0), cometbox3, 2)
    win.blit(comet4, (cometx4, comety4))
    #pygame.draw.rect(win, (255,0,0), cometbox4, 2)

  font = pygame.font.SysFont('ActionIsShaded', 36) #loads a font

  startscreen = True
  instructionnumber = 1

  #x and y coordinates for all of the text
  t1x = (200)
  t2x = (200)
  t3x = (200)
  t4x = (200)
  t5x = (200)
  t6x = (200)

  t1y = (150)
  t2y = (200)
  t3y = (250)
  t4y = (300)
  t5y = (350)
  t6y = (400)

  while startscreen and starwars1 and runall and displayinstruction == 1: #creates an instruction screen where you click to move on
    #insert sprites
    for event in pygame.event.get(): #quits the game
      if event.type == pygame.QUIT:
        startscreen = False
        runall = False
      if event.type == pygame.MOUSEBUTTONDOWN: #cycles through the instructions
        instructionnumber += 1
        if instructionnumber == 3: #ends instructions when all of the pages have been shown
          startscreen = False
    
    win.fill((0,0,0)) #fills the screen black

    if instructionnumber == 1:

      text = font.render("Instructions:", True, (100, 200, 255)) #creates text
      win.blit(text, (10, 10)) #displays text
      text = font.render("A long time ago in a galaxy far, far away...", True, (100, 200, 255)) #repeats the displaying of text
      win.blit(text, (100, 282))

    if instructionnumber == 2: #displays text again

      text = font.render("Trapped between the the sepratists,", True, (150, 150, 50))
      win.blit(text, (t1x-40, t1y))
      text = font.render("You are the last hope of the Republic", True, (150, 150, 50))
      win.blit(text, (t2x-50, t2y))
      text = font.render("Use the left arrow key to go left.", True, (150, 150, 50))
      win.blit(text, (t3x-13, t3y))
      text = font.render("Use the right arrow key to go right.", True, (150, 150, 50))
      win.blit(text, (t4x-27, t4y))
      text = font.render("Press the spacebar to shoot.", True, (150, 150, 50))
      win.blit(text, (t5x-2, t5y))
      text = font.render("May the force be with you!", True, (150, 150, 50))
      win.blit(text, (t6x+7, t6y-10))
    pygame.display.update() #refreshes the screen
  #repeats the above steps
  while startscreen and starwars2 and runall and displayinstruction == 1: #creates an instruction screen where you click to move on
    #insert sprites
    for event in pygame.event.get(): #quits the game
      if event.type == pygame.QUIT:
        startscreen = False
        runall = False
      if event.type == pygame.MOUSEBUTTONDOWN: #cycles through the instructions
        instructionnumber += 1
        if instructionnumber == 3: #ends instructions when all of the pages have been shown
          startscreen = False
    
    win.fill((0,0,0))

    if instructionnumber == 1:

      text = font.render("Instructions:", True, (100, 200, 255))
      win.blit(text, (10, 10))
      text = font.render("A long time ago in a galaxy far, far away...", True, (100, 200, 255))
      win.blit(text, (100, 282))

    if instructionnumber == 2:

      text = font.render("The Rebels have attacked", True, (150, 150, 50))
      win.blit(text, (t1x+5, t1y))
      text = font.render("You are the last hope of the Empire", True, (150, 150, 50))
      win.blit(text, (t2x-40, t2y))
      text = font.render("Use the left arrow key to go left.", True, (150, 150, 50))
      win.blit(text, (t3x-13, t3y))
      text = font.render("Use the right arrow key to go right.", True, (150, 150, 50))
      win.blit(text, (t4x-27, t4y))
      text = font.render("Press the spacebar to shoot.", True, (150, 150, 50))
      win.blit(text, (t5x-2, t5y))
      text = font.render("Shoot to kill!", True, (150, 150, 50))
      win.blit(text, (t6x+80, t6y-10))
    pygame.display.update()
  #repeats steps
  while startscreen and starwars3 and runall and displayinstruction == 1: #creates an instruction screen where you click to move on
    #insert sprites
    for event in pygame.event.get(): #quits the game
      if event.type == pygame.QUIT:
        startscreen = False
        runall = False
      if event.type == pygame.MOUSEBUTTONDOWN: #cycles through the instructions
        instructionnumber += 1
        if instructionnumber == 3: #ends instructions when all of the pages have been shown
          startscreen = False
    
    win.fill((0,0,0))

    if instructionnumber == 1:

      text = font.render("Instructions:", True, (100, 200, 255))
      win.blit(text, (10, 10))
      text = font.render("A long time ago in a galaxy far, far away...", True, (100, 200, 255))
      win.blit(text, (100, 282))

    if instructionnumber == 2:

      text = font.render("Cough Cough Cough", True, (150, 150, 50))
      win.blit(text, (t1x+42, t1y))
      text = font.render("I need to escape", True, (150, 150, 50))
      win.blit(text, (t2x+65, t2y))
      text = font.render("Use the left arrow key to go left.", True, (150, 150, 50))
      win.blit(text, (t3x-13, t3y))
      text = font.render("Use the right arrow key to go right.", True, (150, 150, 50))
      win.blit(text, (t4x-27, t4y))
      text = font.render("Press the spacebar to shoot.", True, (150, 150, 50))
      win.blit(text, (t5x-2, t5y))
      text = font.render("Cough Cough!", True, (150, 150, 50))
      win.blit(text, (t6x+80, t6y-10))
    pygame.display.update()
  #repeats steps
  while startscreen and normalmode and runall and displayinstruction == 1: #creates an instruction screen where you click to move on
    #insert sprites
    for event in pygame.event.get(): #quits the game
      if event.type == pygame.QUIT:
        startscreen = False
        runall = False
      if event.type == pygame.MOUSEBUTTONDOWN: #cycles through the instructions
        instructionnumber += 1
        if instructionnumber == 2: #ends instructions when all of the pages have been shown
          startscreen = False
    
    win.fill((0,0,0))

    if instructionnumber == 1:

      text = font.render("You are a rocket in the vast space,", True, (150, 150, 50))
      win.blit(text, (t1x-40, t1y))
      text = font.render("Your job is to save Earth", True, (150, 150, 50))
      win.blit(text, (t2x+30, t2y))
      text = font.render("Use the left arrow key to go left.", True, (150, 150, 50))
      win.blit(text, (t3x-13, t3y))
      text = font.render("Use the right arrow key to go right.", True, (150, 150, 50))
      win.blit(text, (t4x-27, t4y))
      text = font.render("Press the spacebar to shoot the comets.", True, (150, 150, 50))
      win.blit(text, (t5x-50, t5y))
      text = font.render("Good luck!", True, (150, 150, 50))
      win.blit(text, (t6x+90, t6y-10))
    pygame.display.update()
  #repeats steps
  clock = pygame.time.Clock() #creates a clock variable
  run = True #variable that is true if the main game is running
  shooting = 1 #variable that controls the gap between when bullets are shot
  bullets = [] #array of all of the bullets
  while run and runall: #defines what happens when the game is run

    if shooting > 0: 
      shooting += 1
    if shooting > 4:
      shooting = 1
    #resets shooting after the loop runs a number of times, in this case, 3. It is basically a cooldown checker, change the value thet shooting is > up to increase cooldown and down to decrease the cooldown time
    for event in pygame.event.get(): #defines what happens if the game is quit
      if event.type == pygame.QUIT:
        run = False

    for bullet in bullets:
      #this for loop checks whether any bullets hits the comets and then removes them from the bullet list to make them disappear and also reset the comet position if they are hit
      if upshoot:
        if bullet.y > 0 and bullet.y < screenheight:
          bullet.y -= bullet.vel
        else:
          bullets.pop(bullets.index(bullet))

      if bullet.y - bullet.radius < cometbox[1] + cometbox[3] and bullet.y > cometbox[1]:
        if bullet.x + bullet.radius > cometbox[0] and bullet.x < cometbox[0] + cometbox[2]:
          bullets.pop(bullets.index(bullet))
          cometx = random.randint(50,750)
          comety = random.randint(-300,-100)
          cometvel = random.randint(1,3)
          score += 1
          
      if bullet.y - bullet.radius < cometbox1[1] + cometbox1[3] and bullet.y > cometbox1[1]:
        if bullet.x + bullet.radius > cometbox1[0] and bullet.x < cometbox1[0] + cometbox1[2]:
          bullets.pop(bullets.index(bullet))
          cometx1 = random.randint(50,750)
          comety1 = random.randint(-300,-100)
          cometvel1 = random.randint(1,3)
          score += 1

      if bullet.y - bullet.radius < cometbox2[1] + cometbox2[3] and bullet.y > cometbox2[1]:
        if bullet.x + bullet.radius > cometbox2[0] and bullet.x < cometbox2[0] + cometbox2[2]:
          bullets.pop(bullets.index(bullet))
          cometx2 = random.randint(50,750)
          comety2 = random.randint(-300,-100)
          cometvel2 = random.randint(1,3)
          score += 1
    
      if bullet.y - bullet.radius < cometbox3[1] + cometbox3[3] and bullet.y > cometbox3[1]:
        if bullet.x + bullet.radius > cometbox3[0] and bullet.x < cometbox3[0] + cometbox3[2]:
          bullets.pop(bullets.index(bullet))
          cometx3 = random.randint(50,750)
          comety3 = random.randint(-300,-100)
          cometvel3 = random.randint(1,3)
          score += 1

      if bullet.y - bullet.radius < cometbox4[1] + cometbox4[3] and bullet.y > cometbox4[1]:
        if bullet.x + bullet.radius > cometbox4[0] and bullet.x < cometbox4[0] + cometbox4[2]:
          bullets.pop(bullets.index(bullet))
          cometx4 = random.randint(50,750)
          comety4 = random.randint(-300,-100)
          cometvel4 = random.randint(1,3)
          score += 1
    '''
    if y > comety and y + 50 < comety + 50:
      if x > cometx and x + 50 < cometx + 50:
        run = False
    if y > comety1 and y + 50 < comety1 + 50:
      if x > cometx1 and x + 50 < cometx1 + 50:
        run = False
    if y > comety2 and y + 50 < comety2 + 50:
      if x > cometx2 and x + 50 < cometx2 + 50:
        run = False
    if y > comety3 and y + 50 < comety3 + 50:
      if x > cometx3 and x + 50 < cometx3 + 50:
        run = False
    if y > comety4 and y + 50 < comety4 + 50:
      if x > cometx4 and x + 50 < cometx4 + 50:
        run = False
    '''
    #makes the comets move down the screen:
    comety += cometvel
    comety1 += cometvel1
    comety2 += cometvel2
    comety3 += cometvel3
    comety4 += cometvel4

    #stops the game when a comet hits the bottom of the screen
    if comety > (screenheight - height - vel):
      run = False
    if comety1 > (screenheight - height - vel):
      run = False
    if comety2 > (screenheight - height - vel):
      run = False
    if comety3 > (screenheight - height - vel):
      run = False
    if comety4 > (screenheight - height - vel):
      run = False

    keys = pygame.key.get_pressed() #creating a list of all of the keys that can be pressed
    #when the cooldown is complete and the user presses space, a bullet shoots upwards
    if keys[pygame.K_SPACE] and shooting == 1:
      facing = 0 #direction of the bullet/ where it is facing
      upshoot = True
      if len(bullets) < 5: #limits the number of bullets
        bullets.append(projectile(round(x + width // 2), round(y + height // 2), 6, (0,255,0), facing))
    
    if keys[pygame.K_LEFT]: #character goes left if left arrow is pressed
      #if the character goes off the screen they go to the other side
      if x < 0:
        x = screenwidth
      else:
        x -= vel
        up = True
  #x < (screenwidth - width)
  #x > vel
    if keys[pygame.K_RIGHT]: #character goes right if right arrow is pressed
      #if the character goes off the screen they go to the other side
      if x > (screenwidth):
        x = 0
      else:
        x += vel
        up = True

  #  if keys[pygame.K_UP] and y > vel: #character goes up if up arrow is pressed
  #    y -= vel
  #    left = False
  #    right = False
  #    up = True

  #  if keys[pygame.K_DOWN] and y < (screenheight - height - vel): #character goes down if down arrow is pressed
  #    y += vel
  #    left = False
  #    right = False
  #    up = True

    redrawbg(bg1, rocketup) #draws the sprite, background and comets by calling the function
    pygame.display.update() #refreshes the display
    clock.tick(25) #how fast the screen refreshes

pygame.quit() #quits the game

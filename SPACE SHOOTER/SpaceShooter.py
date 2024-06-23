# imports go at the top 
import pygame #allows acccesss to the pygame module...alows for the grabation of methods already made 
import os #operating system -- grab info about the system of itself 

pygame.font.init() # initialize the font to access the module 

#variables 
WINDOW = pygame.display.set_mode((1000,800))             #why caps? to represent constants(not going to change) #in paranthese(width and height ) #alllows to access pygame window
RED = (255, 0, 0) #Constant RED is equal to the RGB color of Yellow
YELLOW = (255, 255, 0) #Constant Yellow is equal to the RBG color of Yellow

MYCOLOR = (0, 0, 0)# Constant MYCOLOR is equal to the RGB value of violet-blue 

SPACE_IMAGE = pygame.image.load(os.path.join('assets','space.png')) #brings the space image from the assets to the background + import os will allow us to get the file location and bring it + path is where it is located in computer + join makes it lot easier to bring the file in -- load an image in the game 
SPACE = pygame.transform.scale(SPACE_IMAGE, (1000,800))
# space will make sure it is scaled down so the image is not blurry -- transformed version of our image 



R_IMAGE = pygame.image.load(os.path.join('assets', 'red.jpg'))
R = pygame.transform.scale(R_IMAGE, (1000,800))
YELLOW_IMAGE = pygame.image.load(os.path.join('assets', 'yellow-screen.jpeg'))










YELLOW_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.image.load(os.path.join('assets','spaceship_yellow.png')), 180) # brings the yellowspaceship from the assests to the background of the window 
YELLOW_SPACESHIP= pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (50,50)) # transforms the size of the spaceship so it is not too large or small


RED_SPACESHIP_IMAGE =pygame.image.load(os.path.join('assets','spaceship_red.png')) # brings the redspaceship from the assests to the background of the window + rotates the image to a 180
RED_SPACESHIP= pygame.transform.scale(RED_SPACESHIP_IMAGE, (50,50)) # transforms the size of the spaceship so it is not too large or small

VEL = 2 # this is to make sure the spaceship won't go off the speed 

BULLET_VEL = 7 # the bullet velocity
MAX_BULLETS = 5 # the number of bullets for one color 

GAME_FONT = pygame.font.Font('assets/Montserrat-Regular.ttf', 36)  # this makes a varaible for the font of the game and the way you bring in the custom font + the number you see is the font size 


# allow us to check and make sure when we hit our oppnent it registers 
RED_HIT = pygame.USEREVENT + 1 # +1 makes sure the events are the same
YELLOW_HIT = pygame.USEREVENT + 2 # 2 different events so they can act independent from each other 





#methods 

    # checking mechanism to have it stop half way

def drawWindow(red,yellow, yellow_bullets, red_bullets, red_health, yellow_health, red_var, yellow_var ):  #be called ever single time a loop runs and this is how we redraw our window each time -- red(allows for image and rectange to move as one otherwise the image will be stuck and the rectange will be used freely )  
    if red_var == True:
        red_won = GAME_FONT.render("Red Won!", 1, MYCOLOR)
        WINDOW.blit(R, (0,0))
        WINDOW.blit(red_won, (10, 750))
    elif yellow_var == True:
        yellow_won = GAME_FONT.render("Yellow Won!", 1, MYCOLOR)
        WINDOW.blit(YELLOW_IMAGE, (0,0))
        WINDOW.blit(yellow_won, (10, 750))
    else:
        WINDOW.blit(SPACE,(0,0))  #surface - image + dest: coordinate   ---- blit : takes in surface objet and returns a rect object --- draws the image 
        WINDOW.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y)) # prints the yellow spaceship on the window with the coordinates that are given
        WINDOW.blit(RED_SPACESHIP,(red.x,red.y)) # prints the red spaceship on the window with the coordinates that are written down  -- x and y are the coordinates that are being changed with the key hits  # this line will redraw the thing everytime the loop runs 
    
        yellow_health_text = GAME_FONT.render('HEALTH: ' + str(yellow_health), 1, YELLOW) # this makes sure that the text appears 
        WINDOW.blit(yellow_health_text, (10, 750)) # draws the image of the font on the screen 



        red_health_text = GAME_FONT.render('HEALTH: ' + str(red_health), 1, RED) # this makes sure that the text appears 
        WINDOW.blit(red_health_text, (10, 10)) # draws the image of the font on the screen 

        # modification on the code: whenever the players have x amount of healths, there will be a message representing the health they are in 
        if yellow_health == 1:
            yellow_1 = GAME_FONT.render('ABOUT TO LOSE :(', 1, YELLOW)
            WINDOW.blit(yellow_1, (500,750))
        if red_health == 1:
            red_1 = GAME_FONT.render('ABOUT TO LOSE :(', 1, RED)
            WINDOW.blit(red_1, (500,10))

        if yellow_health == 3:
            yellow_3 = GAME_FONT.render('You have to win!!!!', 1, YELLOW)
            WINDOW.blit(yellow_3, (500,750))
        if red_health == 3:
            red_3 = GAME_FONT.render('You have to win!!!!', 1, RED)
            WINDOW.blit(red_3, (500,10))

        if yellow_health == 5:
            motivation_yellow = GAME_FONT.render('HALF WAY ><', 1, YELLOW)
            WINDOW.blit(motivation_yellow, (500,750))
        if red_health == 5:
            motivation_red = GAME_FONT.render('HALF WAY ><', 1, RED)
            WINDOW.blit(motivation_red, (500,10))

        if yellow_health == 7:
            yellow_7 = GAME_FONT.render('STILL HAVE TIME', 1, YELLOW)
            WINDOW.blit(yellow_7, (500,750))
        if red_health == 7:
            red_7 = GAME_FONT.render('STILL HAVE TIME', 1, RED)
            WINDOW.blit(red_7, (500,10))

        if yellow_health == 9:
            yellow_9 = GAME_FONT.render('BE CAREFUL', 1, YELLOW)
            WINDOW.blit(yellow_9, (500,750))
        if red_health == 9:
            red_9 = GAME_FONT.render('BE CAREFUL', 1, RED)
            WINDOW.blit(red_9, (500,10))
        for bullet in yellow_bullets: # this will actually draw the rectangle on the game 
            pygame.draw.rect(WINDOW, YELLOW, bullet) # this shows the of the bullet that is going to shoot 
        for bullet in red_bullets:
            pygame.draw.rect(WINDOW, RED, bullet )
    
    
    
def redMovement(keysPressed, red): # this method will make the spaceship move 
    #arrow keys 
    # all the words after the "and" for each sentence will make sure that the spaceships stay in the boundaries for the red spaceship
    if keysPressed[pygame.K_UP] and red.y - VEL > 0: # this will register the up arrow key and whenver pressed it will print an up
        red.y -= VEL
    elif keysPressed[pygame.K_DOWN] and red.y + VEL + 50 < WINDOW.get_height() // 2: # give the height of the full screen/ 2 + stop at the halfway point----- #this will register the down arrow key and whenever the down key is pressed, it will move down 
        red.y += VEL
    elif keysPressed[pygame.K_RIGHT]  and red.x + VEL + 50 < WINDOW.get_width(): #this will register the right arrow key and whenever pressd, it will move right
        red.x += VEL
    elif keysPressed[pygame.K_LEFT] and red.x -VEL > 0 : #this will register the left arrow key and whenever pressd, it will move left
        red.x -=VEL

def yellowMovement(keysPressed, yellow): #this method will make the yellow spaceship move 
    # WASD keys 
    # all the words after the "and" for each sentence will make sure that the spaceships stay in the boundaries for the yellow spaceship
    if keysPressed[pygame.K_w] and yellow.y - VEL > WINDOW.get_height() // 2 :# give heigth of the full screen + stop at the half-way point : #this will register the w and whenever pressed, the spaceship will go up
        yellow.y -= VEL
    elif keysPressed[pygame.K_s] and yellow.y + VEL < WINDOW.get_height()- 50: #this will register the s and whenever pressed, the spaceship will go down
        yellow.y += VEL
    elif keysPressed[pygame.K_d]  and yellow.x + VEL + 50 < WINDOW.get_width(): #this will register the d and whenever pressed, the spaceship will go right
        yellow.x += VEL
    elif keysPressed[pygame.K_a] and yellow.x - VEL > 0: #this will register the a and whenever pressed, the spaceship will go left 
        yellow.x -= VEL




def bulletMovement(red_bullets, yellow_bullets, red, yellow): # control both the red and yellow bullet movements -- input 4 arguments 
    for bullet in yellow_bullets: # for 1 amount bullets, it will run once and continues running if it is called 
        bullet.y = bullet.y - BULLET_VEL # makes the bullets go up


        if red.colliderect(bullet): # amkes sure when the red is collided, the yellow bullets are removed 
            pygame.event.post(pygame.event.Event(RED_HIT)) # registers an event  to the event list and that event list runs through the loop in the game loop
            yellow_bullets.remove(bullet)

        
        if bullet.y < 0: # the top of the platform is 0 so once the bullets pass 
            yellow_bullets.remove(bullet) #this constantly removes the bullet from the list so the list has enough space to fill in more bullets 





    for bullet in red_bullets: # for 1 amount bullets, it will run once and continues running if it is called 
        bullet.y = bullet.y + BULLET_VEL # makes the bullets go down

        if yellow.colliderect(bullet): # amkes sure when the yellow is collided, the red bullets are removed
            pygame.event.post(pygame.event.Event(YELLOW_HIT)) # registers an event  to the event list and that event list runs through the loop in the game loop
            red_bullets.remove(bullet)

        if bullet.y + bullet.height> WINDOW.get_height(): # since the bottom of the screen is get height, it will make sure that once the bullet enters the end of the screen, the if statement will start working after 5 is shot 
            red_bullets.remove(bullet) #this constantly removes the bullet from the list so the list has enough space to fill in more bullets 



    



def game():
    yellow = pygame.Rect(100,550,50,50)  #attched to the image to give some boundaries -- constructor of an object -- windth, height, size, size # only runs once 
    red = pygame.Rect(100,0,50,50)   #attched to the image to give some boundaries -- constructor of an object -- windth, height, size, size # only runs once 
    #makes it always run -- global variables -- variables that cna be always run -- local variables--only good for the methpds you write 
    running = True #local variable 
    red_var = False
    yellow_var = False
    #they both hold the value for the arguments 
    red_bullets= [] 
    yellow_bullets = []


    # makes sure that both the soaceships have 10 lives saved into this local variable 
    red_health = 10
    yellow_health = 10




    clock = pygame.time.Clock() #local variable to slow down our game--module is time and already located in pygame --- frames/sec 





    while running: #wanting the window to always open 
        clock.tick(250) # makes sure the clock works for 60 milliseconds -- 60 frames per second
        # events  (interact with the window/game--alreadybuiltin the pygame )-- loop control variable 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #will stop if it is a quit event -- all caps means event
                running = False #this will end the program because in the beginning running is ste to true, but setting it to false will make the programmer exit the game 
            # print(event) #displays all the events that can happen 


            if event.type == pygame.KEYDOWN: #this is for shooting the bullets (only makes the bullet )
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS: #this calles for the right shift key for the bullets + it won't let more than 5 bullets shoot from the spaceshooter since MAX_BULLETS is set to 5
                    bullet = pygame.Rect(yellow.x + yellow.width//2 , yellow.y, 5,10) # this is to create the retangle shape for the bullets -- 5 and 10 is the bullet height and width 
                    yellow_bullets.append(bullet) # will append the bullets from the lists 
                    print(len(yellow_bullets)) # will show how mant bullets have been shot 

            if event.type == pygame.KEYDOWN: #this is for shooting the bullets (only makes the bullet )
                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS: #this calles for the right shift key for the bullets  + it won't let more than 5 bullets shoot from the spaceshooter since MAX_BULLETS is set to 5 
                    bullet = pygame.Rect(red.x + red.width//2, red.y, 5,10) # this is to create the retangle shape for the bullets -- 5 and 10 is the bullet height and width  + # the red.width creates for the bullet to come from the center
                    red_bullets.append(bullet) # will append the bullets from the lists 
                    print(len(red_bullets)) # will show how mant bullets have been shot 
            
            if event.type == RED_HIT: # amkes sure these values are equal to each other + if red gets hit 
                red_health -= 1 # this will make the 10 decerase every time it gets hit 
                print('RH', red_health) # prints out our health 

            if red_health == 0:
                yellow_var = True
                print(yellow_var)
                drawWindow(red,yellow, yellow_bullets, red_bullets, red_health, yellow_health, red_var, yellow_var) #call draw window here to make the space background to appear in our game  -- have to pass red as there is a connection b/t the image being drawn and the x and y coordinates 
                pygame.display.update()
                pygame.time.wait(5000)
                running = False
            if yellow_health == 0:
                red_var = True
                print(red_var)
                drawWindow(red,yellow, yellow_bullets, red_bullets, red_health, yellow_health, red_var, yellow_var) #call draw window here to make the space background to appear in our game  -- have to pass red as there is a connection b/t the image being drawn and the x and y coordinates 
                pygame.display.update()
                pygame.time.wait(5000)
                running = False

            if event.type == YELLOW_HIT:
                yellow_health -= 1 
                print('YH', yellow_health)



        keysPressed = pygame.key.get_pressed() #holds all of the keypressed events and find the arrowkeys(local variable) -- list of all the keys pressed in an event on the window
        
        yellowMovement(keysPressed, yellow)
        redMovement(keysPressed, red)   #red object is the way we do collision---rectange with the same size and location with the image, calling the redmovement to work with the keyspressed 
        
        bulletMovement(red_bullets, yellow_bullets, red, yellow) # calling the function; bullets movement 
        
        
        drawWindow(red,yellow, yellow_bullets, red_bullets, red_health, yellow_health, red_var, yellow_var) #call draw window here to make the space background to appear in our game  -- have to pass red as there is a connection b/t the image being drawn and the x and y coordinates 
        pygame.display.update() # displays the window, the program will show # updates windoow appearance 



#main method 
if __name__ == '__main__': #will run with being on the file -- if space shooter is equal to space shooter, it will run, so as long as it is in the file, it will run 
    pygame.init() #initializes all python modules 
    game()#game method -- call the game--loop that continues the game 
    pygame.quit() #quit method -- ends the game






# 2 things to get a 100 

# you have to mod your game 
# you need to tell me who wins 
import pygame as pg
import time


pg.init()

gameExit = False


display_width = 800
display_height = 600

screen = pg.display.set_mode((display_width,display_height))
pg.display.set_caption('Machine Learning')


black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)

car_width = 73


clock = pg.time.Clock()
crashed = False
carImg = pg.image.load('racecar.png')

COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')
FONT = pg.font.Font(None, 32)


class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)

def car(x,y):
    screen.blit(carImg, (x,y))
    
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pg.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    screen.blit(TextSurf, TextRect)
    
    pg.display.flip()
    
    time.sleep(2)
    
    game_loop()
    
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pg.draw.rect(screen, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
            clock.tick(15)         
    else:
        pg.draw.rect(screen, ic,(x,y,w,h))

    smallText = pg.font.SysFont("comicsansms",50)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)
class DisplayManager:
    def __init__(self):
        self.text = "Machine learning german"
        self.array = ["Victor", "espabila", "que", "no", "vas", "a", "Munich"]
        self.i = 0
        self.size = 55
    def change_text(self):

        self.text = self.array[self.i]
        self.i += 1  

    
    def game_intro(self):
        box = InputBox(100, 100, 140, 32)
        intro = True

            # Create TextInput-object
        textinput = pygame_textinput.TextInput()

        screen = pygame.display.set_mode((1000, 200))
        clock = pygame.time.Clock()

        screen.fill((225, 225, 225))

    

    pygame.display.update()
    clock.tick(30)

        while intro:
            for event in pg.event.get():
                print(event)
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type==pg.KEYDOWN:
                    if event.key==pg.K_RETURN:
                        print("enter")
                        self.change_text()
                box.handle_event(event)
                textinput.update(events)


            screen.fill(white)
            largeText = pg.font.Font('freesansbold.ttf',self.size)
            TextSurf, TextRect = text_objects(self.text, largeText)
            TextRect.center = ((display_width/2),(display_height/2))
            screen.blit(TextSurf, TextRect)

            # Feed it with events every frame
            
            # Blit its surface onto the screen
            screen.blit(textinput.get_surface(), (10, 10))

            box.update()

          
            box.draw(screen)

             # Feed it with events every frame
            textinput.update(events)
            # Blit its surface onto the screen
            screen.blit(textinput.get_surface(), (10, 10))


            button("GO!",150,450,100,50,green,bright_green,self.change_text)
            button("Quit",550,450,100,50,red,bright_red,quitgame)

            pg.display.flip()
            clock.tick(30)

def new_screen(text, size, next_screen):
    intro = True

    while intro:
        for event in pg.event.get():
            print(event)
            if event.type == pg.QUIT:
                pg.quit()
                quit()
                
        screen.fill(white)
        largeText = pg.font.Font('freesansbold.ttf',size)
        TextSurf, TextRect = text_objects(text, largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        screen.blit(TextSurf, TextRect)
        
        button("GO!",400,450,100,50,green,bright_green,next_screen)
        

        pg.display.flip()
        clock.tick(15)
    
    
def crash():
    message_display('You crashed!')
    
def quitgame():
    pg.quit()
    

def game_loop():
    x =  (display_width * 0.45)
    y = (display_height * 0.8)
    
    x_change = 0
    car_speed = 0

    while not gameExit:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                crashed = True

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    x_change = -5
                elif event.key == pg.K_RIGHT:
                    x_change = 5
            if event.type == pg.KEYUP:
                if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                    x_change = 0

        x += x_change


        screen.fill(white)
        car(x,y)


        if x > display_width - car_width or x < 0:
            crash()

        pg.display.flip()
        clock.tick(60)
men = DisplayManager()
men.game_intro()
game_loop()
pg.quit()
quit()
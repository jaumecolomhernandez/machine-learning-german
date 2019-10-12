import pygame as pg
import time
import text_input


pg.init()

gameExit = False


display_width = 800
display_height = 600

screen = pg.display.set_mode((display_width,display_height))
pg.display.set_caption('Machine Learning German')
clock = pg.time.Clock()

# Colours
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)




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
    

    
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()
    
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
        
        intro = True

        # Create TextInput-object
        textinput = text_input.TextInput(font_size=65)

        clock = pg.time.Clock()

        screen.fill((225, 225, 225))


        while intro:
            events = pg.event.get()
            for event in events:
                #print(event)
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type==pg.KEYDOWN:
                    if event.key==pg.K_RETURN:
                        self.change_text()
                        print(textinput.get_text())
                        textinput.clear_text()
                #box.handle_event(event)

            screen.fill(white)
            largeText = pg.font.Font('freesansbold.ttf',self.size)
            TextSurf, TextRect = text_objects(self.text, largeText)
            TextRect.center = ((display_width/2),(display_height/2))
            screen.blit(TextSurf, TextRect)
            
             # Feed it with events every frame
            textinput.update(events)
            # Blit its surface onto the screen
            screen.blit(textinput.get_surface(), (200, 350))


            button("GO!",150,450,100,50,green,bright_green,self.change_text)
            button("Quit",550,450,100,50,red,bright_red,quitgame)

            pg.display.flip()
            clock.tick(30)

def new_screen(text, size, next_screen):
    intro = True

    while intro:
        for event in pg.event.get():
            #print(event)
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



men = DisplayManager()
men.game_intro()

quit()
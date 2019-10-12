import pygame as pg
import text_input
import colours
import button
import time

display_width = 800
display_height = 600

class Screen:
    def __init__(self,screen):
        self.screen = screen


class QuestionScreen(Screen):
    """ Screen that asks a question"""
    def __init__(self, screen, text):
        self.text = text
        
        self.i = 0
        self.size = 55
        self.intro = True
        super().__init__(screen)
    
    def text_objects(self, text, font):
        textSurface = font.render(text, True, colours.black)
        return textSurface, textSurface.get_rect()

    def message_display(self, text):
        largeText = pg.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = self.text_objects(text, largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        self.screen.blit(TextSurf, TextRect)
        
        pg.display.flip()
        
        time.sleep(2)

    def change_text(self):
        self.text = self.array[self.i]
        self.i += 1  

        if self.i == len(self.array):
            self.i = 0
            self.intro = False

    
    def render(self):
        

        # Create TextInput-object
        textinput = text_input.TextInput(font_size=65)

        clock = pg.time.Clock()

        self.screen.fill((225, 225, 225))


        def print_on_press():
            print('button pressed')
            
        settings = {
            "clicked_font_color" : (0,0,0),
            "hover_font_color"   : (205,195, 100),
            'font'               : pg.font.Font(None,16),
            'font_color'         : (255,255,255),
            'border_color'       : (0,0,0),
        }
        

        btn = button.Button(rect=(10,10,105,25), command=print_on_press, text='Statistics', **settings)

        while self.intro:

            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    # Catach quit flag
                    pg.quit()
                    quit()
                if event.type==pg.KEYDOWN:
                    if event.key==pg.K_RETURN:
                        # If user presses enter catch the word and send it
                        # to manager
                        # self.change_text()
                        
                        self.intro = False
                        result = textinput.get_text()
                        
                        textinput.clear_text()
                btn.get_event(event)
            
            

            self.screen.fill(colours.white)

            # GERMAN WORD
            largeText = pg.font.Font('freesansbold.ttf',self.size)
            TextSurf, TextRect = self.text_objects(self.text, largeText)
            TextRect.center = ((display_width/2),(250))
            self.screen.blit(TextSurf, TextRect)
            
            # INPUT WORD
             # Feed it with events every frame
            textinput.update(events)
            inputSurf = textinput.get_surface()  
            inputRect = inputSurf.get_rect()
            inputRect.center = ((display_width/2),(350))
            # Blit its surface onto the screen
            self.screen.blit(textinput.get_surface(), inputRect)

            # BUTTONS
            btn.draw(self.screen)
        
            # COSAS PYGAME
            pg.display.flip()
            clock.tick(30)

        return result

         

            
            
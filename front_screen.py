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


class FrontScreen(Screen):
    """ Screen that asks a question"""
    def __init__(self, screen):
        super().__init__(screen)
        self.text = "Machine learning german"
        self.intro = True
        
    
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

    def finish(self):
        self.intro = False

    
    def render(self):

        clock = pg.time.Clock()

        self.screen.fill((225, 225, 225))
            
        settings = {
            "clicked_font_color" : (0,0,0),
            "hover_font_color"   : (205,195, 100),
            'font'               : pg.font.Font(None,36),
            'font_color'         : (255,255,255),
            'border_color'       : (0,0,0),
        }
        

        btn = button.Button(rect=(350,350,100,50), command=self.finish, text='START!', **settings)

        while self.intro:
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    # Catach quit flag
                    pg.quit()
                    quit()
                btn.get_event(event)
            
            self.screen.fill(colours.white)

            # GERMAN WORD
            largeText = pg.font.Font('freesansbold.ttf',55)
            TextSurf, TextRect = self.text_objects("Machine Learning German", largeText)
            TextRect.center = ((display_width/2),(250))
            self.screen.blit(TextSurf, TextRect)

            # BUTTONS
            btn.draw(self.screen)
        
            # COSAS PYGAME
            pg.display.flip()
            clock.tick(30)

        


         

            
            
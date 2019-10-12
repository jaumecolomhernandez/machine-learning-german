import question_screen
import front_screen
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

if __name__ == "__main__":
    man = question_screen.QuestionScreen(screen, ["Risco", "paraula1", "paraula2", "paraula3", "paraula4"])
    scren = front_screen.FrontScreen(screen)

    scren.render()
    for pal in ["Risco", "paraula1", "paraula2", "paraula3", "paraula4"]:
        man = question_screen.QuestionScreen(screen, pal)
        result = man.render()
        print(result)
    

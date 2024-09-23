from pico2d import *
import math

open_canvas()

# fill here

grass = load_image('grass.png')
character = load_image('character.png')


x = 400
y = 90

angle = 0

while(True):


    while(x < 800):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x += 2
        delay(0.02)

    while(x>400):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x -= 2
        y += 2
        delay(0.02)


    
        

    #while(angle < 90):
     #   clear_canvas_now()
      #  grass.draw_now(400, 30)
       # character.draw_now(x, y)
        #y = 400 * math.cos((angle+270)/360*2*math.pi)
        #x = 400 + 200 * math.cos((angle+270)/360*2*math.pi)
        #angle+=2
        #delay(0.02)


close_canvas()

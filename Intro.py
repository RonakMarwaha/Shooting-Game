import pgzrun
import random
WIDTH=500
HEIGHT=600 
TITLE='Basic Shapes'
message=''
aien=Actor('aien')
def draw():
    screen.clear()
    screen.fill('blue') 
    aien.draw()
    screen.draw.text(message,center=(250,10))


def placealien():
    aien.x=random.randint(50,WIDTH-75)
    aien.y=random.randint(50,WIDTH-75)

def on_mouse_down(pos):
    global message
    if aien.collidepoint(pos): 
        message='Good Shot'
        placealien()
    else:
        message='You Missed!'
pgzrun.go()
import utilities
from tkinter import Canvas, Tk
import helpers
import helpers
import time

def make_grid(canvas, w, h):
    interval = 100

    # Delete old grid if it exists:
    canvas.delete('grid_line')
    # Creates all vertical lines at intevals of 100
    for i in range(0, w, interval):
        canvas.create_line(i, 0, i, h, tag='grid_line')

    # Creates all horizontal lines at intevals of 100
    for i in range(0, h, interval):
        canvas.create_line(0, i, w, i, tag='grid_line')

    # Creates axis labels
    offset = 2
    for y in range(0, h, interval):
        for x in range(0, w, interval):
            canvas.create_oval(
                x - offset, 
                y - offset, 
                x + offset,  
                y + offset, 
                fill='black'
            )
            canvas.create_text(
                x + offset, 
                y + offset, 
                text="({0}, {1})".format(x, y),
                anchor="nw", 
                font=("Purisa", 8)
            )
    

def make_landscape_object(canvas, position, size=100):
    # your code to create your creature goes here:
    # replace the code below...
    print('make_landscape_object...')
    print('size:', size, 'center:', position)

# drink options
passionfruit_tea = '#fadadd'
matcha_latte = '#a0ce9d'
milk_tea = '#f6f5e1'
peach_tea = '#f6c737'
thai_tea = '#ff8b4c'

# toppings
boba = 'black'
popping_boba = '#FFFF00'
red_bean = '#672422'


#  sizes
small = 75
regular = 105
large = 150


def make_oval(canvas, center: tuple, width: int, height: int, fill='hotpink', tag=()):
    top_left = (center[0] - width, center[1] - height)
    bottom_right = (center[0] + width, center[1] + height)
    canvas.create_oval([top_left, bottom_right], fill=fill, tag=tag)
    tag=tag


def make_circle(canvas, center: tuple, radius: int, fill='hotpink', tag=()):
    make_oval(canvas, center, radius, radius, fill=fill, tag=tag)



###################
## boba creature ##
###################


def make_cup(canvas, center, size, primary_color, tag=()):
    canvas.create_polygon(
    [
        (center[0]-50*size/150, center[1]-100*size/150),
        (center[0]-100*size/150, center[1]-100*size/150),
        (center[0]-85*size/150, center[1]+50*size/150),
        (center[0], center[1]+75*size/150),
        (center[0]+85*size/150, center[1]+50*size/150),
        (center[0]+100*size/150, center[1]-100*size/150),
        (center[0]+50*size/150, center[1]-100*size/150)

    ], 
    splinesteps=20,
    width=10,
    fill = primary_color, #ffffee
    smooth=True,
    tag=tag
    )

def make_tea(canvas, center, size, drink, tag=()):
    canvas.create_polygon(
    [

        (center[0]-85*size/150, center[1]-65*size/150),
        (center[0]-50*size/150, center[1]+45*size/150),
        (center[0], center[1]+60*size/150),
        (center[0]+50*size/150, center[1]+45*size/150),
        (center[0]+85*size/150, center[1]-65*size/150),
        (center[0]+50*size/150, center[1]-60*size/150),
        (center[0], center[1]-55*size/150),
        (center[0]-50*size/150, center[1]-60*size/150),
        (center[0]-85*size/150, center[1]-65*size/150)

    ], 
    splinesteps=20,
    width=10,
    fill = drink,
    smooth=True,
    tag=tag
    )

def make_cup_outline(canvas, center, size, secondary_color, tag=()):
    canvas.create_line(
    [
        (center[0]-100*size/150, center[1]-100*size/150),
        (center[0]-85*size/150, center[1]+50*size/150),
        (center[0], center[1]+75*size/150),
        (center[0]+85*size/150, center[1]+50*size/150),
        (center[0]+100*size/150, center[1]-100*size/150)

    
        
    ], 
    splinesteps=20,
    width=10*size/150,
    fill = secondary_color, #ffd0a1
    smooth=True,
    tag=tag
    )
    
def make_lid(canvas, center, size, primary_color, tag=()):
    [make_oval(canvas, (center[0], center[1]-100*size/150), 115 * size/150, 30 * size/150, primary_color, tag=tag)] #ffffee



    
def make_lid_outline(canvas, center, size, secondary_color, tag=()):
    canvas.create_line(
    [
        (center[0]-150*size/150, center[1]-100*size/150),
        (center[0], center[1]-60*size/150),
        (center[0]+150*size/150, center[1]-100*size/150),
        (center[0], center[1]-140*size/150),
        (center[0]-150*size/150, center[1]-100*size/150)
 
    ], 
    splinesteps=20,
    width=10*size/150,
    fill = secondary_color, #ffd0a1
    smooth=True,
    tag=tag
    )
    
def make_straw_hole(canvas, center, size, secondary_color, tag=()):
    canvas.create_line(
    [
        (center[0]-13*size/150, center[1]-100*size/150),
        (center[0]-10*size/150, center[1]-95*size/150),
        (center[0], center[1]-90*size/150),
        (center[0]+10*size/150, center[1]-95*size/150),
        (center[0]+13*size/150, center[1]-100*size/150),
        (center[0]+11*size/150, center[1]-102*size/150),
        (center[0]-2*size/150, center[1]-104*size/150),
        (center[0]-13*size/150, center[1]-100*size/150)

    ], 
    splinesteps=20,
    width=5*size/150,
    fill = secondary_color, #ffd0a1
    smooth=True,
    tag=tag
    )

def make_straw(canvas, center, size, straw_color, tag=()):
    canvas.create_polygon(
    [
        
        (center[0]-10*size/150, center[1]-200*size/150),
        (center[0]-10*size/150, center[1]-100*size/150),
        (center[0], center[1]-95*size/150),
        (center[0]+10*size/150, center[1]-100*size/150),
        (center[0]+10*size/150, center[1]-200*size/150),
        (center[0], center[1]-205*size/150)

    ], 
    splinesteps=20,
    width=5,
    fill = straw_color, 
    smooth=True,
    tag=tag
    )

def make_topping(canvas, center, size, type_of_topping, tag=()):
    make_circle(canvas, (center[0], center[1]+45*size/150), 5*size/150, fill = type_of_topping, tag=tag),
    make_circle(canvas, (center[0]-15*size/150, center[1]+45*size/150), 5*size/150, fill = type_of_topping, tag=tag),
    make_circle(canvas, (center[0]+15*size/150, center[1]+45*size/150), 5*size/150, fill = type_of_topping, tag=tag),
    make_circle(canvas, (center[0]+30*size/150, center[1]+40*size/150), 5*size/150, fill = type_of_topping, tag=tag),
    make_circle(canvas, (center[0]-30*size/150, center[1]+40*size/150), 5*size/150, fill = type_of_topping, tag=tag),
    
    make_circle(canvas, (center[0]-40*size/150, center[1]+28*size/150), 5*size/150, fill = type_of_topping, tag=tag),
    make_circle(canvas, (center[0]+40*size/150, center[1]+28*size/150), 5*size/150, fill = type_of_topping, tag=tag),
    make_circle(canvas, (center[0], center[1]+30*size/150), 5*size/150, fill = type_of_topping, tag=tag),
    make_circle(canvas, (center[0]-20*size/150, center[1]+30*size/150), 5*size/150, fill = type_of_topping, tag=tag),
    make_circle(canvas, (center[0]+20*size/150, center[1]+30*size/150), 5*size/150, fill = type_of_topping, tag=tag),
    

def make_face(canvas, center, size, tag=()):
    # eyes
    make_circle(canvas, (center[0]-25*size/150, center[1]-35*size/150), 13*size/150, fill = 'black', tag=tag),
    make_circle(canvas, (center[0]+25*size/150, center[1]-35*size/150), 13*size/150, fill = 'black', tag=tag),
    make_circle(canvas, (center[0]+27*size/150, center[1]-37*size/150), 5*size/150, fill = 'white', tag=tag),
    make_circle(canvas, (center[0]-23*size/150, center[1]-37*size/150), 5*size/150, fill = 'white', tag=tag),

    # nose
    canvas.create_line(
    [
        (center[0], center[1]-15*size/150),
        (center[0]+10*size/150, center[1]),
        (center[0], center[1])
        
    ], 
    splinesteps=20,
    width=5*size/150,
    fill = 'black',
    smooth=True,
    tag=tag
    )

def make_creature(canvas, center, size, primary_color='#ffffee', secondary_color='#ffd0a1', drink=milk_tea, type_of_topping=red_bean, straw_color='black', trash=False, tag=()):
    make_cup(canvas, center, size, primary_color, tag=tag)
    make_tea(canvas, center, size, drink, tag=tag)
    make_cup_outline(canvas, center, size, secondary_color, tag=tag)
    make_lid(canvas, center, size, primary_color, tag=tag)
    make_lid_outline(canvas, center, size, secondary_color, tag=tag)
    make_straw_hole(canvas, center, size, secondary_color, tag=tag)
    if trash == False:
        make_straw(canvas, center, size, straw_color, tag=tag)
        make_topping(canvas, center, size, type_of_topping, tag=tag)
        make_face(canvas, center, size, tag=tag)



#################
#### dumpster ###
#################

def make_landscape_object(canvas, center, size=10, fill_color="#3D9970", tag=()):
    [
    #trash can main body
    canvas.create_rectangle(
        [ (center[0] - 25*size, center[1] - 15*size),
          (center[0] + 25*size, center[1] + 15*size) ],
        fill=fill_color,
        tag=tag),

    # trash can lid
    canvas.create_rectangle(
        [ (center[0] - 26*size, center[1] - 15*size),
          (center[0] + 26*size, center[1] - 17*size) ],
        fill='black',
        tag=tag),

    canvas.create_rectangle(
        [ (center[0] - 25*size, center[1] - 17*size),
          (center[0] + 25*size, center[1] - 18.5*size) ],
        fill='black',
        tag=tag),

    #side dents??

    canvas.create_line(
        [
            (center[0] - 24*size, center[1] - 15*size),
            (center[0] - 24*size, center[1] + 15*size)
        ],
        width=0.3*size,
        tag=tag),

    canvas.create_line(
        [
            (center[0] + 24*size, center[1] - 15*size),
            (center[0] + 24*size, center[1] +15*size)
        ], 
        splinesteps=20,
        width=0.3*size,
        tag=tag),

    # fill of small squares
    canvas.create_rectangle(
        [ (center[0] - 25*size, center[1] - 7.5*size),
          (center[0] - 22*size, center[1] - 2.5*size) ],
        fill=fill_color,
        tag=tag),

    canvas.create_rectangle(
        [ (center[0] + 22*size, center[1] - 7.5*size),
          (center[0] + 25*size, center[1] - 2.5*size) ],
        fill=fill_color,
        tag=tag),

    #outline
    canvas.create_line(
        [ (center[0] - 25*size, center[1] - 15*size),
          (center[0] - 25*size, center[1] + 15*size),
          (center[0] + 25*size, center[1] + 15*size),
          (center[0] + 25*size, center[1] - 15*size),
          (center[0] - 25*size, center[1] - 15*size) ],
        width=0.5*size,
        tag=tag),


    #outline of small squares
    canvas.create_line(
        [ (center[0] - 25*size, center[1] - 7.5*size),
          (center[0] - 22*size, center[1] - 7.5*size),
          (center[0] - 22*size, center[1] - 2.5*size),
          (center[0] - 25*size, center[1] - 2.5*size)],
        width=0.3*size,
        tag=tag),

    canvas.create_line(
        [ (center[0] + 25*size, center[1] - 7.5*size),
          (center[0] + 22*size, center[1] - 7.5*size),
          (center[0] + 22*size, center[1] - 2.5*size),
          (center[0] + 25*size, center[1] - 2.5*size)],
        width=0.3*size,
        tag=tag),

    # dents in can

    canvas.create_line(
        [
            (center[0] - 22*size, center[1] - 5.5*size),
            (center[0] + 22*size, center[1] - 5.5*size),
            (center[0] + 22*size, center[1] - 4.5*size),
            (center[0] - 22*size, center[1] - 4.5*size)
        ],
        width=0.3*size,
        tag=tag),

    canvas.create_line(
        [
            (center[0] - 25*size, center[1] + 4.5*size),
            (center[0] + 25*size, center[1] + 4.5*size),
            (center[0] + 25*size, center[1] + 5.5*size),
            (center[0] - 25*size, center[1] + 5.5*size)
        ],
        width=0.3*size,
        tag=tag),

    # lid outline
    canvas.create_line(
        [
            (center[0] - 26*size, center[1] - 15*size),
            (center[0] + 26*size, center[1] - 15*size),
            (center[0] + 26*size, center[1] - 17*size),
            (center[0] - 26*size, center[1] - 17*size),
            (center[0] - 26*size, center[1] - 15*size)
        ],
        width=0.3*size,
        tag=tag,
        fill='grey') ]

    canvas.create_line(
        [
            (center[0] - 25*size, center[1] - 17*size),
            (center[0] - 25*size, center[1] - 18.5*size),
            (center[0] + 25*size, center[1] - 18.5*size),
            (center[0] + 25*size, center[1] - 17*size),
            (center[0] - 25*size, center[1] - 17*size)
        ],
        width=0.3*size,
        fill='grey',
        tag=tag),


################
####cockroach###
################

def make_cockroach(canvas, center, size=10, fill='#9f6934', tag=()):
    # main body = same coord at outline   
    canvas.create_polygon(
        [ (center[0] - 2*size, center[1] + size),
          (center[0] - 1.75*size, center[1]),
          (center[0] - size, center[1] - 0.5*size),
          (center[0], center[1] - 0.75*size),
          (center[0] + size, center[1] - 0.5*size),
          (center[0] + 1.75*size, center[1]),
          (center[0] + 2*size, center[1] + size)], 
        width=2,
        fill=fill,
        smooth=True,
        tag=tag)

    # body outline
    canvas.create_line(
        [ (center[0] - 2*size, center[1] + size),
          (center[0] - 1.75*size, center[1]),
          (center[0] - size, center[1] - 0.5*size),
          (center[0], center[1] - 0.75*size),
          (center[0] + size, center[1] - 0.5*size),
          (center[0] + 1.75*size, center[1]),
          (center[0] + 2*size, center[1] + size),
          (center[0] - 2*size, center[1] + size)
        ], 
        splinesteps=20,
        width=size/10,
        fill='black',
        smooth=True,
        tag=tag)

    ### head ##

    #face line
    canvas.create_line(
        [ (center[0] - size, center[1] - 0.47*size),
          (center[0] - 0.65*size, center[1] + 0.5*size),
          (center[0] - 0.85*size, center[1] + 0.95*size)
        ], 
        splinesteps=20,
        width=size/10,
        fill='black', #654321
        smooth=True,
        tag=tag)

    # eye
    canvas.create_oval(
        [ (center[0] - 1.35*size, center[1]),
          (center[0] - 1.17*size, center[1] + 0.28*size) ], # top left x-y, bottom right x-y
        fill='black',
        width=0,
        tag=tag)

    #legs
    canvas.create_line(
        [ (center[0] - 0.85*size, center[1] + size),
          (center[0] - 0.85*size, center[1] + 1.5*size)
        ], 
        splinesteps=20,
        width=size/10,
        fill='black',
        tag=tag)

    canvas.create_line(
        [ (center[0] - 0.5*size, center[1] + size),
          (center[0] - 0.5*size, center[1] + 1.3*size)
        ], 
        splinesteps=20,
        width=size/10,
        fill='black',
        tag=tag)

    canvas.create_line(
        [ (center[0] + 0.5*size, center[1] + size),
          (center[0] + 0.5*size, center[1] + 1.3*size)
        ], 
        splinesteps=20,
        width=size/10,
        fill='black',
        tag=tag)

    canvas.create_line(
        [ (center[0] + 0.85*size, center[1] + size),
          (center[0] + 0.85*size, center[1] + 1.5*size)
        ], 
        splinesteps=20,
        width=size/10,
        fill='black',
        tag=tag)

    # pinchers
    canvas.create_line(
        [ (center[0] - 1.45*size, center[1] - 0.17*size),
          (center[0] - 1.55*size, center[1] - 0.6*size),
          (center[0] - 0.25*size, center[1] - 1.5*size)
        ], 
        splinesteps=20,
        width=size/10,
        fill='black',
        tag=tag)

    canvas.create_line(
        [ (center[0] - 1.2*size, center[1] - 0.12*size),
          (center[0] - 1.3*size, center[1] - 0.55*size),
          (center[0], center[1] - 1.45*size)
        ], 
        splinesteps=20,
        width=size/10,
        fill='black',
        tag=tag)





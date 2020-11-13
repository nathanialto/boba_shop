from tkinter import Canvas, Tk
import helpers
import utilities
import helpers
import time

gui = Tk()
gui.title('My Terrarium')

# initialize canvas:
window_width = gui.winfo_screenwidth()
window_height = gui.winfo_screenheight()
canvas = Canvas(gui, width=window_width, height=window_height, background='white')
canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################
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
'''
# make a label:
canvas.create_text(
    (210, 210), 
    text="Hello world!", 
    font=("Purisa", 32),
    anchor='nw'  # align to "northwest" corner
)

# make an oval:
canvas.create_oval(
    [ (50, 150),  (150, 250) ], # top left x-y, bottom right x-y
    fill='#FF4136',
    width=5
)

# make a polygon
canvas.create_polygon(
    [ (370, 150),  (630, 150), (500, 350) ],  # list of x-y pairs
    width=2,
    fill='#BCD39C',
    smooth=True)  #make smooth false for angular polygon

# make a line:
canvas.create_line(
    [ (10, 0),  (210, 100),  (420, 0),  (630, 100) ],  # list of x-y pairs
    width=3)

# make a dashed line: 
canvas.create_line(
    [ (10, 100),  (210, 0),  (420, 100),  (630, 10) ], 
    fill="#3D9970", 
    dash=(4, 4), 
    width=3)

# make a curvy line:
canvas.create_line(
    [
        (0,   100), 
        (50,  150), 
        (100, 100), 
        (150, 150), 
        (200, 100), 
        (250, 150), 
        (300, 100), 
        (350, 150), 
        (400, 100)
    ], 
    splinesteps=20,
    width=3, 
    smooth=True)

# make a rectangle
canvas.create_rectangle(
    [ (500, 25), (650, 75) ],  #  coords: top-left, bottom-right
    fill="#3D9970")

'''



############
###########

'''
(950, 350)

canvas.create_rectangle(
    [ (700, 200), (1200, 500) ],
    fill="#3D9970")

# trash can lid
canvas.create_rectangle(
    [ (690, 200), (1210, 180) ],
    fill="#3D9970")

canvas.create_rectangle(
    [ (700, 180), (1200, 165) ],
    fill="black")

canvas.create_polygon(
    [ (700, 165),  (1200, 165), (1133, 133), (733, 133), (700, 165) ], 
    width=2,
    fill='black')

#side dents??

canvas.create_line(
    [
        (710, 200),
        (710, 500)
    ],
    width=3)

canvas.create_line(
    [
        (1190, 200),
        (1190, 500)
    ], 
    splinesteps=20,
    width=3)

# fill of small squares
canvas.create_rectangle(
    [ (700, 275), (730, 325) ],
    fill="#3D9970")

canvas.create_rectangle(
    [ (1170, 275), (1200, 325) ],
    fill="#3D9970")

#outline
canvas.create_line(
    [ (700, 200),  (700, 500),  (1200, 500),  (1200, 200), (700, 200) ],
    width=5)


#outline of small squares
canvas.create_line(
    [ (700, 275),  (730, 275),  (730, 325),  (700, 325)],
    width=3)

canvas.create_line(
    [ (1200, 275),  (1170, 275),  (1170, 325),  (1200, 325)],
    width=3)

# dents in can

canvas.create_line(
    [
        (730, 295),
        (1170, 295),
        (1170, 305),
        (730, 305)
    ],
    width=3)

canvas.create_line(
    [
        (700, 395),
        (1200, 395),
        (1200, 405),
        (700, 405)
    ],
    width=3)

# lid outline
canvas.create_line(
    [
        (690, 200),
        (1210, 200),
        (1210, 180),
        (690, 180),
        (690, 200)
    ],
    width=3)

canvas.create_line(
    [
        (700, 180),
        (700, 165),
        (1200, 165),
        (1200, 180),
        (700, 180)
    ],
    width=3,
    fill='grey')

canvas.create_line(
    [
        (700, 165),
        (1200, 165),
        (1133, 133),
        (733, 133),
        (700, 165) 
    ], 
    splinesteps=20,
    width=3,
    fill='grey')

#################
#####cockroach###
#################

center = (500, 400)
size = 100
    
canvas.create_polygon(
    [ (center[0] - 2*size, center[1] + size),
      (center[0] - 1.75*size, center[1]),
      (center[0] - size, center[1] - 0.5*size),
      (center[0], center[1] - 0.75*size),
      (center[0] + size, center[1] - 0.5*size),
      (center[0] + 1.75*size, center[1]),
      (center[0] + 2*size, center[1] + size)], 
    width=2,
    fill='#9f6934',
    smooth=True)

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
    width=7,
    fill='black',
    smooth=True)

### head ##

#face line
canvas.create_line(
    [ (center[0] - size, center[1] - 0.47*size),
      (center[0] - 0.65*size, center[1] +450),
      (415, 495)
    ], 
    splinesteps=20,
    width=7,
    fill='black', #654321
    smooth=True)

# eye
canvas.create_oval(
    [ (365, 400),  (383, 428) ], # top left x-y, bottom right x-y
    fill='black',
    width=0)

#legs
canvas.create_line(
    [ (415, 500),
      (415, 550)
    ], 
    splinesteps=20,
    width=7,
    fill='black')

canvas.create_line(
    [ (450, 500),
      (450, 530)
    ], 
    splinesteps=20,
    width=7,
    fill='black')

canvas.create_line(
    [ (550, 500),
      (550, 530)
    ], 
    splinesteps=20,
    width=7,
    fill='black')

canvas.create_line(
    [ (585, 500),
      (585, 550)
    ], 
    splinesteps=20,
    width=7,
    fill='black')

# pinchers
canvas.create_line(
    [ (355, 383),
      (345, 340),
      (475, 250)
    ], 
    splinesteps=20,
    width=7,
    fill='black')

canvas.create_line(
    [ (380, 388),
      (370, 345),
      (500, 255)
    ], 
    splinesteps=20,
    width=7,
    fill='black')

'''




########################## YOUR CODE ABOVE THIS LINE ############################## 

# makes sure the canvas keeps running:
canvas.mainloop()

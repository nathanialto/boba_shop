from tkinter import Canvas, Tk
import helpers
import utilities
import helpers
import time
import random
import math
import keycodes

gui = Tk()
gui.title('My Terrarium')

# initialize canvas:
window_width = gui.winfo_screenwidth()
window_height = gui.winfo_screenheight()
canvas = Canvas(gui, width=window_width, height=window_height, background='white')
canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################

#################
## boba extras ##
#################

# drink options
passionfruit_tea = '#fadadd'
matcha_latte = '#a0ce9d'
milk_tea = '#f6f5e1'
peach_tea = '#f6c737'
thai_tea = '#ff8b4c'

drink_options = (passionfruit_tea, matcha_latte, milk_tea, peach_tea, thai_tea)

# toppings
boba = 'black'
popping_boba = '#FFFF00'
red_bean = '#672422'
toppings_options = (boba, popping_boba, red_bean)



#  sizes
small = 75
regular = 105
large = 150

################
## background ##
################



## ground
canvas.create_polygon(
    [
        (0, 350),
        (200, 600),
        (1500, 600),
        (1500, 800),
        (0, 800),
        (0, 350)
        
    ],
    width=2,
    fill='grey',
    tag='ground')

canvas.create_polygon(
    [
        (100, 0),
        (0, 0),
        (0, 350),
        (200, 600),
        (1500, 600),
        (1500, 500),
        (500, 500),
        (100, 0)
        
    ],
    width=2,
    fill='#d3d3d3',
    tag='ground')

canvas.create_polygon(
    [
        (760, 800),
        (624, 600),
        (650, 600),
        (786, 800)
    ],
    width=2,
    fill='white',
    tag='ground')

canvas.create_polygon(
    [
        (1360, 800),
        (1224, 600),
        (1250, 600),
        (1386, 800)
    ],
    width=2,
    fill='white',
    tag='ground')

# highlight on sidewalk
canvas.create_polygon(
    [   (125, 31.25),
        (65, 200),
        (200, 200),
        (200, 125)
    ], 
    width=2,
    fill='wheat2',
    tag='sidewalk')

canvas.create_polygon(
    [   (300, 250),
        (100, 250),
        (200, 437),
        (450, 437)
        ], 
    width=2,
    fill='wheat2',
    tag='sidewalk')

canvas.create_polygon(
    [   (150, 437),
        (109.6, 437),
        (0, 300),
        (0, 250),
        (50, 250)
        ], 
    width=2,
    fill='wheat2',
    tag='sidewalk')

canvas.create_polygon(
    [   (109.6, 437),
        (109.6, 437),
        (109.6, 485),
        (0, 350),
        (0, 300),
        ], 
    width=2,
    fill='wheat2',
    tag='sidewalk')

canvas.create_polygon(
    [
        (109.6, 485),
        (0, 485),
        (0, 350),
        ], 
    width=2,
    fill='wheat4',
    tag='ground')

##############
## building ##
##############

# main building fill
canvas.create_polygon(
    [ (500, 500),  (500, 0), (1500, 0), (1500, 500) ],
    width=2,
    fill='gray26',
    tag='building')

# rightmost bar?
canvas.create_polygon(
    [   (500, 500),
        (450, 437.5),
        (450, 0),
        (500, 0) ], 
    width=2,
    fill='gray26',
    tag='building')

# leftmost bar
canvas.create_polygon(
    [   (250, 0),
        (250, 187.5),
        (300, 250),
        (300, 0)], 
    width=2,
    fill='gray26',
    tag='building')

canvas.create_polygon(
    [   (250, 0),
        (250, 187.5),
        (200, 125),
        (200, 0)
        ], 
    width=2,
    fill='gray26',
    tag='building')

# window
canvas.create_polygon(
    [   (450, 437.5),
        (300, 250),
        (300, 0),
        (450, 0)], 
    width=2,
    fill='DarkGoldenrod1',
    tag='building')

#center bar
canvas.create_polygon(
    [   (450, 200),
        (250, 0),
        (300, 0),
        (450, 150),
        (450, 200)], 
    width=2,
    fill='gray26',
    tag='building')

#main frame
canvas.create_line(
    [
        (100, 0),
        (500, 500),
        (500, 0)
    ], 
    width=5,
    fill='black',
    tag='building')

canvas.create_line(
    [
        (500, 500),
        (1500, 500)
        
    ], 
    width=5,
    fill='black',
    tag='building')

# rightmost bar outline
canvas.create_line(
    [
        (450, 437.5),
        (450, 0)
    ], 
    width=3,
    fill='black',
    tag='building')

# center bar outline
canvas.create_line(
    [
        (450, 200),
        (250, 0),
        (300, 0),
        (450, 150),
        (450, 200)
    ], 
    width=3,
    fill='black',
    tag='building')

# leftmost bar
canvas.create_line(
    [
        (250, 0),
        (250, 187.5),
        (300, 250),
        (300, 50)
        
    ], 
    width=3,
    fill='black',
    tag='building')

canvas.create_line(
    [
        (250, 0),
        (250, 187.5),
        (200, 125),
        (200, 0)
        
    ], 
    width=3,
    fill='black',
    tag='building')


# inside
canvas.create_polygon(
    [   (125, 0),
        (125, 31.25),
        (200, 125),
        (200, 0)], 
    width=2,
    fill='gold',
    tag='building')

# door
canvas.create_polygon(
    [   (85, 0),
        (85, 100),
        (100, 100),
        (100, 0),
        (85, 0)], 
    width=2,
    fill='gray26',
    tag='building')

canvas.create_polygon(
    [   (100, 100),
        (125, 31.25),
        (125, 0),
        (100, 0)], 
    width=2,
    fill='ivory3',
    tag='building')

canvas.create_line(
    [
        (85, 0),
        (85, 100),
        (100, 100),
        (100, 0),
        (85, 0)
        
    ], 
    width=3,
    fill='black',
    tag='building')

canvas.create_line(
    [
        (100, 100),
        (125, 31.25),
        (125, 0)
        
    ], 
    width=3,
    fill='black',
    tag='building')



##############
## sidewalk ##
##############

canvas.create_line(
    [
        (1500, 550),
        (200, 550),
        (0, 300)
    ], width=5,
    tag='sidewalk')

canvas.create_line(
    [
        (1500, 600),
        (200, 600),
        (0, 350)
    ], width=5,
    tag='sidewalk')

canvas.create_line(
    [
        (200, 550),
        (200, 600)
    ], width=5,
    tag='sidewalk')

# poster 1
canvas.create_polygon(
    [ (530, 50),  (660, 50), (660, 250), (530, 250) ], 
    width=2,
    fill='white',
    tag='poster1')

canvas.create_line(
    [(530, 50),  (660, 50), (660, 250), (530, 250), (530, 50)],
    width=3,
    tag='poster1')

canvas.create_text(
    (540, 65), 
    text="Dumpster Sale", 
    font=("Times", 18, 'bold'),
    anchor='nw',  # align to "northwest" corner
    tag='poster1'
)

# poster 2
canvas.create_polygon(
    [ (530, 270),  (660, 270), (660, 450), (530, 450) ], 
    width=2,
    fill='pink',
    tag='poster2')

canvas.create_line(
    [(530, 270),  (660, 270), (660, 450), (530, 450), (530, 270)],
    width=3, tag='poster2')

canvas.create_text(
    (540, 280), 
    text="Matcha Latte", 
    font=("Century Gothic", 18, 'bold'),
    anchor='nw',  # align to "northwest" corner
    tag='poster2'
    )

canvas.create_text(
    (550, 420), 
    text="Sold Here", 
    font=("Century Gothic", 20, 'bold italic'),
    anchor='nw',  # align to "northwest" corner
    tag='poster2'
)


helpers.make_creature(canvas, (595, 380), 57, drink=matcha_latte, type_of_topping=boba, straw_color='LightGoldenrod1', tag = 'poster2')

# trash cans
helpers.make_landscape_object(canvas, (950, 370), size=10, tag='main_can')
helpers.make_landscape_object(canvas, (1485, 370), size=10, tag='side_can')

# cans on posters
helpers.make_landscape_object(canvas, (595, 150), size=1.9, fill_color='pink', tag='poster_can_1')
helpers.make_landscape_object(canvas, (565, 220), size=1, fill_color='LightGoldenrod1', tag='poster_can_1')
helpers.make_landscape_object(canvas, (630, 220), size=1, fill_color='SkyBlue1', tag='poster_can_1')

   

#####################
## click functions ##
#####################

MOUSE_CLICK = '<Button-1>'
RIGHT_CLICK = '<Button-2>'
MOUSE_DRAG = '<B1-Motion>'
KEY_PRESS = '<Key>'


###########################
## generates cockroaches ##
###########################

cockroaches = []
number_of_cockroaches = 5
counter = 1
boba_counter = 1
active_tag = None
dumpster_tag: utilities.get_tag_from_x_y_coordinate(canvas, 950, 350)


while True:
    
## deletes boba over dumpster
    canvas.addtag_enclosed('tag', 750, 200, 1150, 500)
    canvas.delete('tag')
    
## selects + moves boba 
    def select_boba(event):
        global active_tag
        # if something is already active, deactivate it:
        if active_tag:
            active_tag = None
        # get new active tag:
        active_tag = utilities.get_tag_from_x_y_coordinate(canvas, event.x, event.y)
    canvas.bind(MOUSE_CLICK, select_boba)
    
    def move_boba(event):
        if 'boba_' in active_tag:
            # calculate the current position of the current shape:
            width = utilities.get_width(canvas, active_tag)
            height = utilities.get_height(canvas, active_tag)
            left = utilities.get_left(canvas, active_tag) 
            top = utilities.get_top(canvas, active_tag) 
            current_x = left + (width / 2)
            current_y = top + (height / 2)

            # calculate the delta of the current shape:
            delta_x = -1 * (current_x - event.x)
            delta_y = -1 * (current_y - event.y)

            # move the shape:
            utilities.update_position_by_tag(canvas, active_tag, x=delta_x, y=delta_y)   
    canvas.bind(MOUSE_DRAG, move_boba)

## controls boba w/ keys
    def control_boba(event):
        distance = 10
        if 'boba_' in active_tag:
            if event.keycode == keycodes.get_up_keycode():
                utilities.update_position_by_tag(canvas, tag=active_tag, x=0, y=-distance)
            elif event.keycode == keycodes.get_down_keycode():
                utilities.update_position_by_tag(canvas, tag=active_tag, x=0, y=distance)
            elif event.keycode == keycodes.get_left_keycode():
                utilities.update_position_by_tag(canvas, tag=active_tag, x=-distance, y=0)
            elif event.keycode == keycodes.get_right_keycode():
                utilities.update_position_by_tag(canvas, tag=active_tag, x=distance, y=0)
    canvas.bind(KEY_PRESS, control_boba)

## makes boba 
    def make_boba(event):
        global boba_counter
        size = random.uniform(10, 100)
        helpers.make_creature(canvas,
            (event.x, event.y),
            size,
            drink=random.choice(drink_options),
            type_of_topping=random.choice(toppings_options),
            tag = 'boba_' + str(boba_counter))
        boba_counter += 1
        canvas.focus_set()
    canvas.bind(RIGHT_CLICK, make_boba)
    
## makes cockroaches
    if counter < 20:
        x = random.randint(0, window_width)
        y = random.randint(600, 770)
        tag_name = 'cockroach_' + str(counter)
        cockroaches.append({
            'tag':tag_name,
            'speed': math.sin(random.uniform(1, 3)),
            })
        helpers.make_cockroach(canvas, (x, y), size=random.randint(5, 30), tag=tag_name)
        counter += 1
        time.sleep(0.001)
        gui.update()
        
## animates cockroaches    
    if counter >= 20:
        for info in cockroaches:
            utilities.update_position_by_tag(canvas, info['tag'], -10*info['speed'])
            gui.update()
            if utilities.get_right(canvas, info['tag']) < 0:
                utilities.update_position_by_tag(canvas, info['tag'], 1600)
            
        
        

## what else: click to kill cockroach(7), night to day, ,
## 

## (1) animate creatures that reappear on the other side, animate creatures so thay have slightly diff motion (4) ??, 
## right click to create boba (random)(3), drag to dumpster to get rid of boba (9),
## situational delete of creature (if i carry boba to dumpster it deletes) (7?)

## goal: game control selected boba (5) and delete cockroaches when boba comes in contact (8), if i cant work the first ones ,change night to day (11) 


  
helpers.make_grid(canvas, window_width, window_height)

########################## YOUR CODE ABOVE THIS LINE ############################## 

# makes sure the canvas keeps running:
canvas.mainloop()


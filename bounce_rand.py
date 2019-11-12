import pygame as pg
import math
import random

# Pygame initialization
pg.init()
screen = pg.display.set_mode((800, 800))

# Attributes for the ball. Self-explanatory. Both x and y are constrained to the size of the 500x500 box.
# You can mess with these attributes if you'd like, and put a single angle or x and/or y coordinate to make it start
# in a certain place. I left a margin outside of the box. I think it increases the effectiveness of the illusion of
# the "bounce." It was also for debugging purposes, as the ball would often pass through the box while coding this!
size = 10
speed = .1
angle = random.uniform(-math.pi, math.pi)
x_start = random.randint(151, 649)
y_start = random.randint(151, 649)

# These are multipliers, for both x and y. They can each either be 1, for forwards, or -1 for backwards. You can also
# change these yourself to decide the direction of the initial ball shot.
x_reflect = random.choice([-1, 1])
y_reflect = random.choice([-1, 1])

# Simple initialization of important variables. "t" is used for "time." I'm not sure if there is a more efficient
# way to do this.
t = 0
x = x_start
y = y_start

# The while loop to run the display. The first five lines are to give the display the functionality to quit by clicking
# the X in the top right of the display. Then screen.fill and pg.draw basically "color" the screen and "draw" the
# objects. The  2 if statements basically handle the "bounce." If you look on the second line down from the if
# statements, you'll see the declaration of x and y coordinates being given as two equations... I don't want to
# give a lesson on parameterization of lines, but you can google it if you need to brush up on your Calculus.
# Basically, the if statements change the multiplier to -1 or 1 depending on which wall it bounces on, then resets
# x_start and y_start to where it hit the wall. This simplified a lot of things. Finally, the pg.draw and pg.display
# are for drawing and displaying the circle. I also added a coordinate tracker for debugging purposes.
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill((0, 0, 0))
    pg.draw.rect(screen, (255, 255, 255), (150, 150, 500, 500), 1)
    if y <= 150 or y >= 650:
        y_reflect *= -1
        y_start = y - (t * math.tan(angle) * y_reflect)
    if x <= 150 or x >= 650:
        x_reflect *= -1
        x_start = x - (t * x_reflect)
    t += speed
    x, y = x_start + (t * x_reflect), y_start + (t * math.tan(angle) * y_reflect)
    pg.draw.circle(screen, (255, 255, 255), (round(x), round(y)), size, size)
    pg.display.flip()
    track = "x: {},     y: {},      t: {}".format(round(x, 3), round(y, 3), round(t, 3))
    print(track)


from OpenGL.GL import * 
from OpenGL.GLUT import * 
from OpenGL.GLU import *

pos_x_min = 0
pos_x_max = 39
pos_y_min = -400
pos_y_max = -352

pos_x_change = 0
pos_y_change = 0


def tank():
    global pos_x_min, pos_x_max, pos_y_min, pos_y_max, pos_x_change, pos_y_change
    glPushMatrix()
    glTranslate(pos_x_change, pos_y_change, 0)
    glColor3f(1,1,0)
    glBegin(GL_POLYGON)
    glVertex2f(9,-400)
    glVertex2f(0,-400)
    glVertex2f(0,-364)
    glVertex2f(9,-364)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(9, -397)
    glVertex2f(15, -397)
    glVertex2f(15, -367)
    glVertex2f(9, -367)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(15,-397)
    glVertex2f(24,-397)
    glVertex2f(24,-364)
    glVertex2f(15,-364)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(24,-397)
    glVertex2f(30,-397)
    glVertex2f(30,-367)
    glVertex2f(24,-367)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(30,-400)
    glVertex2f(39,-400)
    glVertex2f(39,-364)
    glVertex2f(30,-364)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(18,-364)
    glVertex2f(21,-364)
    glVertex2f(21,-352)
    glVertex2f(18,-352)
    glEnd()
    #### Hiasan ####
    glColor3f(0,0,0)
    glBegin(GL_LINES)
    glVertex2f(9,-400)
    glVertex2f(9,-364)
    glVertex2f(30,-400)
    glVertex2f(30,-364)
    glVertex2f(15,-385)
    glVertex2f(24,-385)
    glVertex2f(24,-385)
    glVertex2f(24,-376)
    glVertex2f(24,-376)
    glVertex2f(15,-376)
    glVertex2f(15,-376)
    glVertex2f(15,-385) 
    glEnd()
    if pos_x_max > 300:
        pos_x_change = 260
        pos_x_min = 261
        pos_x_max = 300
    elif pos_x_min < -450:
        pos_x_change = -450
        pos_x_min = -450
        pos_x_max = -402
    # elif pos_y_min < -400:
    #     pos_y_change = 0
    #     pos_y_min = -400
    #     pos_y_max = -361
    # elif pos_y_max > 400:
    #     pos_y_change = 751
    #     pos_y_min = 361
    #     pos_y_max = 400
    glPopMatrix()

pos_y_change_bullet = 0
def bullet(bul_x, bul_y):
    global pos_y_change_bullet
    glPushMatrix()
    pos_y_change_bullet += 5
    glTranslate(15, -352, 0)
    glTranslate(bul_x, bul_y, 0)
    glTranslated(0, pos_y_change_bullet, 0,)
    glColor3f(1,1,0)
    glBegin(GL_QUADS)
    glVertex2f(0, 0)
    glVertex2f(6, 0)
    glVertex2f(6, 6)
    glVertex2f(0, 6)
    glEnd()
    glPopMatrix()

def keyboard(key,x,y):
    global pos_x_change, pos_y_change, pos_x_min, pos_x_max, pos_y_min, pos_y_max, bul
    if key == b'a' or key == GLUT_KEY_LEFT:
        pos_x_change -= 20
        pos_x_min -= 20
        pos_x_max -= 20
    elif key == b'd' or key == GLUT_KEY_RIGHT:
        pos_x_change += 20
        pos_x_min += 20
        pos_x_max += 20
    # elif key == b'w':
    #     pos_y_change += 20
    #     pos_y_min += 20
    #     pos_y_max += 20
    # elif key == b's':
    #     pos_y_change -= 20
    #     pos_y_min -= 20
    #     pos_y_max -= 20

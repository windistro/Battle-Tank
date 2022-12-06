from OpenGL.GL import * 
from OpenGL.GLUT import * 
from OpenGL.GLU import *
from main import *

pos_x_min = -100
pos_x_max = -61
pos_y_min = -400
pos_y_max = -352

pos_x_change = 0
pos_y_change = 0

class Tank():
    def __init__(self,pos_x, pos_y):
        self._pos_x = pos_x
        self._pos_y = pos_y

    def player(self):
        glColor3f(1,1,0)
        glBegin(GL_POLYGON)
        glVertex(self._pos_x + 9, self._pos_y)
        glVertex(self._pos_x, self._pos_y)
        glVertex(self._pos_x, self._pos_y + 36)
        glVertex(self._pos_x + 9, self._pos_y + 36)
        glEnd()


def tank():
    global pos_x_min, pos_x_max,pos_y_min,pos_y_max, pos_x_change, pos_y_change
    glPushMatrix()
    glTranslate(-300, -500,0)
    glTranslate(pos_x_change, pos_y_change, 0)
    glColor3f(1,1,0)
    glBegin(GL_POLYGON)
    glVertex2f(209,100)
    glVertex2f(200,100)
    glVertex2f(200,136)
    glVertex2f(209,136)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(209,103)
    glVertex2f(215,103)
    glVertex2f(215,133)
    glVertex2f(209,133)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(215,103)
    glVertex2f(224,103)
    glVertex2f(224,136)
    glVertex2f(215,136)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(224,103)
    glVertex2f(230,103)
    glVertex2f(230,133)
    glVertex2f(224,133)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(230,100)
    glVertex2f(239,100)
    glVertex2f(239,136)
    glVertex2f(230,136)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(218,136)
    glVertex2f(221,136)
    glVertex2f(221,148)
    glVertex2f(218,148)
    glEnd()
    #### Hiasan ####
    glColor3f(0,0,0)
    glBegin(GL_LINES)
    glVertex2f(209,100)
    glVertex2f(209,136)
    glVertex2f(230,100)
    glVertex2f(230,136)
    glVertex2f(215,115)
    glVertex2f(224,115)
    glVertex2f(224,115)
    glVertex2f(224,124)
    glVertex2f(224,124)
    glVertex2f(215,124)
    glVertex2f(215,124)
    glVertex2f(215,115) 
    glEnd()
    print(pos_x_min, pos_y_min)
    if pos_x_max > 300:
        pos_x_change = 360
        pos_x_min = 252
        pos_x_max = 300
    elif pos_y_min < -400:
        pos_y_change = 0
        pos_y_min = -400
        pos_y_max = -361
    elif pos_x_min < -450:
        pos_x_change = -350
        pos_x_min = -450
        pos_x_max = -402
    elif pos_y_max > 400:
        pos_y_change = 751
        pos_y_min = 361
        pos_y_max = 400
    glPopMatrix()

def bullet(pos_x, pos_y):
    glColor3f(1,1,0)
    glBegin(GL_QUADS)
    glVertex2f(pos_x + 15, pos_y + 3)
    glVertex2f(pos_x + 21, pos_y + 3)
    glVertex2f(pos_x + 21, pos_y + 9)
    glVertex2f(pos_x + 15, pos_y + 9)
    glEnd()
    pos_x += 10

def keyboard(key,x,y):
    global pos_x_change, pos_y_change, pos_x_min, pos_x_max, pos_y_min, pos_y_max
    if key == b'a':
        pos_x_change -= 10
        pos_x_min -= 10
        pos_x_max -= 10
    elif key == b'd':
        pos_x_change += 10
        pos_x_min += 10
        pos_x_max += 10
    elif key == b'w':
        pos_y_change += 10
        pos_y_min += 10
        pos_y_max += 10
    elif key == b's':
        pos_y_change -= 10
        pos_y_min -= 10
        pos_y_max -= 10
    elif key == b' ':
        bullet(pos_x_min, pos_y_max)
    # elif ord(key) == 27:
    #     glutDestroyWindow()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
    glLoadIdentity()
    glViewport(0, 0, 900, 800) 
    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity()
    glOrtho(-450, 450, -400, 400, 0.0, 1.0) 
    glMatrixMode (GL_MODELVIEW) 
    glLoadIdentity()

glutInit()
glutInitDisplayMode(GLUT_RGBA) 
glutDisplayFunc(display)
glutKeyboardFunc(keyboard)
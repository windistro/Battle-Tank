from OpenGL.GL import * 
from OpenGL.GLUT import * 
from OpenGL.GLU import *
from main import *

pos_x_min = 200
pos_x_max = 239
pos_y_min = 100
pos_y_max = 148

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

def bullet():
    glColor3f(1,1,0)
    glBegin(GL_QUADS)
    glVertex2f()
    glEnd()


def tank():
    glPushMatrix()
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
    glPopMatrix()
    print(pos_x_max)

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
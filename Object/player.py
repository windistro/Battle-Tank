from OpenGL.GL import * 
from OpenGL.GLUT import * 
from OpenGL.GLU import *

pos_x = 215
pos_y = 118

class Tank():
    def __init__(self,pos_x, pos_y):
        self._pos_x = pos_x
        self._pos_y = pos_y

    def player(self):
        glColor3f(1,1,0)
        glBegin(GL_POLYGON)
        glVertex2f(self._pos_x + 60, self._pos_y)
        glEnd()

    def bullet(self):
        glColor3f(1,1,0)
        glBegin(GL_QUADS)
        glVertex2f()
        glEnd()


def tank():
    global pos_x, pos_y
    glScaled(4,4,1)
    glTranslatef(-500, -200, 0)
    glTranslatef(pos_x, pos_y, 0)
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

def keyboard(key,x,y):
    global pos_x, pos_y
    if key == b'a':
        pos_x -= 10
    elif key == b'd':
        pos_x += 10
    elif key == b'w':
        pos_y += 10
    elif key == b's':
        pos_y -= 10

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
glutDisplayFunc(display)
glutKeyboardFunc(keyboard)
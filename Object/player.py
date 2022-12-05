from OpenGL.GL import * 
from OpenGL.GLUT import * 
from OpenGL.GLU import *
from main import keyboard

class Tank():
    def __init__(self,x_min, x_max, y_min, y_max) -> None:
        self._x_min = x_min
        self._x_max = x_max
        self._y_min = y_min
        self._y_max = y_max

    def player(self):
        glColor3f(1,1,0)
        glBegin(GL_POLYGON)
        glVertex2f()
        glEnd()

    def bullet(self):
        glColor3f(1,1,0)
        glBegin(GL_QUADS)
        glVertex2f()
        glEnd()

pos_x = 215
pos_y = 118

def tank():
    global pos_x, pos_y
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

glutInit()
glutInitDisplayMode(GLUT_RGBA) 
glutKeyboardFunc(keyboard)
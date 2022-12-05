from OpenGL.GL import * 
from OpenGL.GLUT import * 
from OpenGL.GLU import *

def hp():
    glColor3f(1,0,0.2)
    glBegin(GL_POLYGON)
    glVertex2f(700, 615)
    glVertex2f(665, 665)
    glVertex2f(665, 675)
    glVertex2f(675, 700)
    glVertex2f(690, 700)
    glVertex2f(700, 675)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(700, 615)
    glVertex2f(735, 665)
    glVertex2f(735, 675)
    glVertex2f(725, 700)
    glVertex2f(710, 700)
    glVertex2f(700, 675)
    glEnd()

def wall():
    glColor3f(0.5,0.5,0.5)
    glBegin(GL_QUADS)
    glVertex2f(350,400)
    glVertex2f(450,400)
    glVertex2f(450,-400)
    glVertex2f(350,-400)
    glEnd()

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

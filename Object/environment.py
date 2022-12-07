from OpenGL.GL import * 
from OpenGL.GLUT import * 
from OpenGL.GLU import *
from main import drawText

score = 0

def hp():
    glPushMatrix()
    glColor3f(1,0,0.2)
    glBegin(GL_POLYGON)     # 900 x 800 > 450 x 400
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
    glPopMatrix()

def wall():
    global score
    glPushMatrix()
    glColor3f(0.5,0.5,0.5)
    glBegin(GL_QUADS)
    glVertex2f(300,400)
    glVertex2f(450,400)
    glVertex2f(450,-400)
    glVertex2f(300,-400)
    glEnd()
    drawText("Score :", 325, 0, 255, 255, 255)
    drawText(str(score),350, -25, 255, 255, 255)
    glPopMatrix()

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

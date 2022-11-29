from OpenGL.GL import * 
from OpenGL.GLUT import * 
from OpenGL.GLU import *

def iterate():
    glViewport(0, 0, 900, 800) 
    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity()
    glOrtho(0.0, 900, 0.0, 800, 0.0, 1.0) 
    glMatrixMode (GL_MODELVIEW) 
    glLoadIdentity()

def hp():
    glColor3f(1,0,0.2)
    glTranslatef(150,0,0)
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
    glVertex2f(800,800)
    glVertex2f(900,800)
    glVertex2f(900,0)
    glVertex2f(800,0)
    glEnd()

def update(value):
    glutPostRedisplay()
    glutTimerFunc(10,update,0)

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
    glLoadIdentity()
    iterate()
    wall()
    hp()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA) 
glutInitWindowSize(900, 800) 
glutInitWindowPosition(500, 100)

wind = glutCreateWindow("BattleCity") 
glutDisplayFunc(showScreen)
glutTimerFunc(1,update,0)
glutIdleFunc(showScreen)
# glutKeyboardFunc(controller)
glutMainLoop()
from OpenGL.GL import * 
from OpenGL.GLUT import * 
from OpenGL.GLU import *
from Object.environment import *
from Object.player import *
from Object.enemy import *
import random as rd
import ctypes

w,h = 900, 800
w_win,h_win = ctypes.windll.user32.GetSystemMetrics(0)/2, ctypes.windll.user32.GetSystemMetrics(1)/2
start = False

def comet(x,y):
    glColor3f(1,1,0)
    glTranslatef(10,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(x,y+4)
    glVertex2f(x+2.33,y+4)
    glVertex2f(x+3,y+6)
    glVertex2f(x+3.66,y+4)
    glVertex2f(x+6,y+4)
    glVertex2f(x+4.15,y+2.52)
    glVertex2f(x+5,y)
    glVertex2f(x+3,y+1.6)
    glVertex2f(x+1,y)
    glVertex2f(x+1.82,y+2.52)
    glEnd()

def initial():
    drawBigText("Battle Tank", -80, 50, 255, 255, 255)
    drawText("Press Space to Play", -110 , 0, 255, 255, 255)
    for i in range(100):
        comet(-w/2,rd.randint(-h,h))

def iterate():
    glViewport(0, 0, 900, 800) 
    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity()
    glOrtho(-450, 450, -400, 400, 0.0, 1.0) 
    glMatrixMode (GL_MODELVIEW) 
    glLoadIdentity()

def drawText(text,xpos,ypos,r,g,b):
    color = (r,g,b)
    font_style = GLUT_BITMAP_9_BY_15
    glColor3ub(color[0],color[1],color[2])
    line=0
    glRasterPos2f (xpos, ypos)
    for i in text:
       if  i=='\n':
          line=line+1
          glRasterPos2f (xpos, ypos*line)
       else:
          glutBitmapCharacter(font_style, ord(i))    

def drawBigText(text,xpos,ypos,r,g,b):
    glPushMatrix()
    color = (r,g,b)
    font_style = GLUT_BITMAP_HELVETICA_18
    glScale(1,1,0)
    glColor3ub(color[0],color[1],color[2])
    line=0
    glRasterPos2f (xpos, ypos)
    for i in text:
       if  i=='\n':
          line=line+1
          glRasterPos2f (xpos, ypos*line)
       else:
          glutBitmapCharacter(font_style, ord(i))     
    glPopMatrix()

def update(value):
    glutPostRedisplay()
    glutTimerFunc(1,update,0)

def key_init(key,x,y):
    global start
    if key== b' ':
        start = True
        glutKeyboardFunc(keyboard)

# def keyboard(key,x,y):
#     global pos_x, pos_y
#     if key == b'a':
#         pos_x -= 50
#     elif key == b'd':
#         pos_x += 50
#     elif key == b'w':
#         pos_y += 50
#     elif key == b's':
#         pos_y -= 50
    # elif key == b' ':
    #     bullet()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
    glLoadIdentity()
    iterate()
    if start:
        wall() 
        hp()
        tank()
        alien() 
    else:
        initial()
    glFlush()
    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA) 
    glutInitWindowSize(w, h) 
    glutInitWindowPosition(int(w_win)-int((w/2)), int(h_win)-int((h/2)))

    wind = glutCreateWindow("BattleCity") 
    glutDisplayFunc(showScreen)
    glutTimerFunc(1,update,0)
    glutIdleFunc(showScreen)
    glutKeyboardFunc(key_init)
    glutMainLoop()

if __name__ == '__main__':
    main()
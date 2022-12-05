from OpenGL.GL import * 
from OpenGL.GLUT import * 
from OpenGL.GLU import *
from menu import *
import ctypes

pos_x = 0
pos_y = 0

w,h = 900, 800
w_win,h_win = ctypes.windll.user32.GetSystemMetrics(0)/2, ctypes.windll.user32.GetSystemMetrics(1)/2
start = False

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
 
# def drawTextBold(ch,xpos,ypos):
#     glPushMatrix()
#     color = (0,0,0)
#     font_style = GLUT.GLUT_BITMAP_HELVETICA_18
#     glColor3ub(color[0],color[1],color[2])
#     line=0
#     glRasterPos2f (xpos, ypos)
#     for i in ch:
#        if  i=='\n':
#           line=line+1
#           glRasterPos2f (xpos, ypos*line)
#        else:
#           glutBitmapCharacter(font_style, ord(i))  
#     glPopMatrix()  
       
# def drawTextNum(skor,xpos,ypos,r,b,g):
#     color = (r, b, g)
#     font_style = GLUT.GLUT_BITMAP_8_BY_13
#     glColor3ub(color[0],color[1],color[2])
#     line=0
#     glRasterPos2f (xpos, ypos)
#     for i in str(skor):
#        if  i=='\n':
#           line=line+1
#           glRasterPos2f (xpos, ypos*line)
#        else:
#           glutBitmapCharacter(font_style, ord(i))

def mainmenu():
    if start:
        tank()
    else:
        initial()

def update(value):
    glutPostRedisplay()
    glutTimerFunc(1000,update,0)

def key_init(key,x,y):
    global start
    if key== b' ':
        start = True
        glutKeyboardFunc(keyboard)

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
    # elif key == b' ':
        # bullet()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
    glLoadIdentity()
    iterate()
    mainmenu()
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

if __name__ == "__main__":
    main()
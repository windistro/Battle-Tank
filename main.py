from OpenGL.GL import * 
from OpenGL.GLUT import * 
from OpenGL.GLU import *
from object import *

pos_x = 0
pos_y = 0
pos_x_min_gun = 218
pos_x_max_gun = 221

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
    glOrtho(0.0, 900, 0.0, 800, 0.0, 1.0) 
    glMatrixMode (GL_MODELVIEW) 
    glLoadIdentity()

def drawText(ch,xpos,ypos,r,b,g):
    color = (r, b, g)
    font_style = GLUT.GLUT_BITMAP_8_BY_13
    glColor3ub(color[0],color[1],color[2])
    line=0
    glRasterPos2f (xpos, ypos)
    for i in ch:
       if  i=='\n':
          line=line+1
          glRasterPos2f (xpos, ypos*line)
       else:
          glutBitmapCharacter(font_style, ord(i))    
 
def drawTextBold(ch,xpos,ypos):
    glPushMatrix()
    color = (0,0,0)
    font_style = GLUT.GLUT_BITMAP_HELVETICA_18
    glColor3ub(color[0],color[1],color[2])
    line=0
    glRasterPos2f (xpos, ypos)
    for i in ch:
       if  i=='\n':
          line=line+1
          glRasterPos2f (xpos, ypos*line)
       else:
          glutBitmapCharacter(font_style, ord(i))  
    glPopMatrix()  

def bg_text(x,y):
    glColor3ub(0, 255, 255)     
    glBegin(GL_QUADS)
    glVertex2f(285+x,230+y)
    glVertex2f(495+x,230+y)
    glVertex2f(495+x,280+y)
    glVertex2f(285+x,280+y)
    glEnd()
       
def drawTextNum(skor,xpos,ypos,r,b,g):
    color = (r, b, g)
    font_style = GLUT.GLUT_BITMAP_8_BY_13
    glColor3ub(color[0],color[1],color[2])
    line=0
    glRasterPos2f (xpos, ypos)
    for i in str(skor):
       if  i=='\n':
          line=line+1
          glRasterPos2f (xpos, ypos*line)
       else:
          glutBitmapCharacter(font_style, ord(i))

def mainmenu():
    glColor3f(1,1,1)
    

def bullet(pos):
    glColor3f(1,1,0)
    glBegin(GL_QUADS)
    glVertex2f(pos_x_min_gun, )

def update(value):
    glutPostRedisplay()
    glutTimerFunc(10,update,0)

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
    elif key == b' ':
        bullet()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
    glLoadIdentity()
    iterate()
    wall()
    hp()
    tank()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA) 
glutInitWindowSize(900, 800) 
glutInitWindowPosition(500, 100)

wind = glutCreateWindow("BattleCity") 
glutDisplayFunc(showScreen)
glutTimerFunc(1,update,0)
glutIdleFunc(showScreen)
glutKeyboardFunc(keyboard)
glutMainLoop()
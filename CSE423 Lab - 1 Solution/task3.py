from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

id = input()
digit = int(id[-1])

def DDA_for_xcord(x1, y1, x2, y2):
    glPointSize(2)
    glBegin(GL_POINTS)
    while x1 < x2:
        glVertex2f(x1, y1)
        x1 = x1 + 1
    glEnd()


def DDA_for_ycord(x1, y1, x2, y2):
    glPointSize(2)
    glBegin(GL_POINTS)
    while y1 < y2:
        glVertex2f(x1, y1)
        y1 = y1 + 1
    glEnd()

def DDA_for_dashed_line_x(x1, y1, x2, y2):
    glPointSize(2)
    glBegin(GL_POINTS)
    while x1 <= x2:
        glVertex2f(x1, y1)
        x1 = x1 + 5
    glEnd()

def DDA_for_dashed_line_y(x1, y1, x2, y2):
    glPointSize(2)
    glBegin(GL_POINTS)
    while y1 <= y2:
        glVertex2f(x1, y1)
        y1 = y1 + 5
    glEnd()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0)

    if (digit % 2) == 0:
        DDA_for_ycord(250, 150, 250, 450)
        DDA_for_dashed_line_x(100, 450, 400, 450)
    else:
        DDA_for_ycord(400, 150, 400, 450)
        DDA_for_xcord(100, 300, 400, 300)
        DDA_for_dashed_line_y(100, 150, 100, 450)

    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(720, 640)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Lab1 - Task3")
glutDisplayFunc(showScreen)

glutMainLoop()
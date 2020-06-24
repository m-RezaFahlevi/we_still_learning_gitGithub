#include <windows.h>
#include <stdlib.h>
#include <bits/stdc++.h>
#include <GL/glut.h>
using namespace std;

float fx = 10.0, fy = 2.0, fz = 8.0; //location point of view
float tx = 0, ty = 7.0, tz = 0;   //location destination point of view
float yp = 0;

void LV()
{
    gluLookAt(fx, fy, fz,
        tx, ty, tz,
        0, 1, 0);

    GLfloat light_position[] = {0, 50, 100, 0.0}; //location of source of light
    glLightfv(GL_LIGHT0, GL_POSITION, light_position);
    glBlendFunc(GL_SRC_ALPHA, GL_ONE);

    glEnable(GL_LIGHTING); // light
    glEnable(GL_LIGHT0);
    glEnable(GL_DEPTH_TEST); // 3d effect
    glEnable(GL_COLOR_MATERIAL); //coloring things
}


void Gambar()
{
	
	//begin3DLineCoordinate()
	glLineWidth(2);
	glBegin(GL_LINES);
		glColor3ub(123, 43, 65);
		
		//x-coordinate
		glVertex3f(0.0, 0.0, 0.0); glVertex3f(5.0, 0.0, 0.0);
		glVertex3f(0.0, 0.0, 0.0); glVertex3f(-5.0, 0.0, 0.0);
		//y-coordinate
		glVertex3f(0.0, 0.0, 0.0); glVertex3f(0.0, 15.0, 0.0);
		glVertex3f(0.0, 0.0, 0.0); glVertex3f(0.0, -15.0, 0.0);
		//z-coordinate
		glVertex3f(0.0, 0.0, 0.0); glVertex3f(0.0, 0.0, 5.0);
		glVertex3f(0.0, 0.0, 0.0); glVertex3f(0.0, 0.0, -5.0);
		
		//lines
		glVertex3f(0.0, 0.0, 0.0); glVertex3f(0.0, 2.0, 0.0);
	glEnd();
	//end3DLineCoordinate()
	
	glPointSize(10);
	glBegin(GL_POINTS);
		glColor3ub(123, 32, 87);
		glVertex3f(0.0, 0.0, 0.0);
	glEnd();
	
	glPointSize(10);
	glBegin(GL_POINTS);
		glColor3ub(123, 32, 87);
		glVertex3f(0.0, 2.0, -0.0);
	glEnd();
	
	glBegin(GL_POLYGON);    // square 1
        glColor3ub(250, 99, 71);
        glVertex3f(-1.0, 0.0, -1.0); glVertex3f(1.0, 0.0, -1.0);
		glVertex3f(-1.0, 0.0, 1.0); glVertex3f(1.0, 0.0, 1.0);
		glVertex3f(1.0, 0.0, -1.0);
    glEnd();
	
	glBegin(GL_POLYGON);    // square 2
        glColor3ub(123, 86, 71);
        glVertex3f(-3.0, 2.0, -3.0); glVertex3f(3.0, 2.0, -3.0);
		glVertex3f(-3.0, 2.0, 3.0); glVertex3f(3.0, 2.0, 3.0);
		glVertex3f(3.0, 2.0, -3.0);
    glEnd();
	
	glBegin(GL_POLYGON);    // square 3
        glColor3ub(200, 89, 71);
        glVertex3f(-1.0, 0.0, -1.0);; glVertex3f(-1.0, 0.0, 1.0);
		glVertex3f(-3.0, 2.0, 3.0); glVertex3f(-3.0, 2.0, -3.0);
		glVertex3f(-1.0, 0.0, -1.0);
    glEnd();
	
	glBegin(GL_POLYGON);    // square 4
        glColor3ub(195, 29, 71);
        glVertex3f(-1.0, 0.0, -1.0);; glVertex3f(-3.0, 2.0, -3.0);
		glVertex3f(3.0, 2.0, -3.0); glVertex3f(1.0, 0.0, -1.0);
		glVertex3f(-1.0, 0.0, -1.0);
    glEnd();
	
	glBegin(GL_POLYGON);    // square 5
        glColor3ub(182, 29, 71);
        glVertex3f(1.0, 0.0, -1.0); glVertex3f(3.0, 2.0, -3.0);
		glVertex3f(3.0, 2.0, 3.0); glVertex3f(1.0, 0.0, 1.0);
		glVertex3f(1.0, 0.0, -1.0);
    glEnd();
	
	glBegin(GL_POLYGON);    // square 6
        glColor3ub(122, 99, 71);
        glVertex3f(1.0, 0.0, 1.0); glVertex3f(3.0, 2.0, 3.0);
		glVertex3f(-3.0, 2.0, 3.0); glVertex3f(-1.0, 0.0, 1.0);
		glVertex3f(1.0, 0.0, 1.0);
    glEnd();
	
	glBegin(GL_POLYGON);    // square 7 up
        glColor3ub(250, 99, 71);
        glVertex3f(-1.0, 5.0, -1.0); glVertex3f(1.0, 5.0, -1.0);
		glVertex3f(-1.0, 5.0, 1.0); glVertex3f(1.0, 5.0, 1.0);
		glVertex3f(1.0, 5.0, -1.0);
    glEnd();
	
	glBegin(GL_POLYGON);    // square 8 up
        glColor3ub(250, 99, 71);
        glVertex3f(-1.5, 7.0, -2.0); glVertex3f(1.5, 7.0, -1.5);
		glVertex3f(-1.5, 7.0, 1.5); glVertex3f(1.5, 7.0, 1.5);
		glVertex3f(1.5, 7.0, -1.5);
    glEnd();
	
	glBegin(GL_POLYGON);    // square 9 up
        glColor3ub(250, 99, 23);
        glVertex3f(-1.0, 5.0, -1.0); glVertex3f(-1.5, 7.0, -1.5);
		glVertex3f(1.5, 7.0, -1.5); glVertex3f(1.0, 5.0, -1.0);
		glVertex3f(-1.0, 5.0, -1.0);
    glEnd();
	
	glBegin(GL_POLYGON);    // square 10 up
        glColor3ub(250, 29, 13);
        glVertex3f(1.0, 5.0, -1.0); glVertex3f(1.5, 7.0, -1.5);
		glVertex3f(1.5, 7.0, 1.5); glVertex3f(1.0, 5.0, 1.0);
		glVertex3f(-1.0, 5.0, -1.0);
    glEnd();
	
	glBegin(GL_POLYGON);    // square 11 up
        glColor3ub(250, 19, 98);
        glVertex3f(1.0, 5.0, 1.0); glVertex3f(1.5, 7.0, 1.5);
		glVertex3f(-1.5, 7.0, 1.5); glVertex3f(-1.0, 5.0, 1.0);
		glVertex3f(1.0, 5.0, 1.0);
    glEnd();
	
	glBegin(GL_POLYGON);    // square 12 stick
        glColor3ub(12, 99, 99);
        glVertex3f(-1.0, 2.0, 1.0); glVertex3f(-1.0, 5.0, 1.0);
		glVertex3f(1.0, 5.0, 1.0); glVertex3f(1.0, 2.0, 1.0);
		glVertex3f(-1.0, 5.0, 1.0);
    glEnd();
	
	glBegin(GL_POLYGON);    // square 13 stick
        glColor3ub(12, 99, 99);
        glVertex3f(1.0, 2.0, 1.0); glVertex3f(1.0, 5.0, 1.0);
		glVertex3f(1.0, 5.0, -1.0); glVertex3f(1.0, 2.0, -1.0);
		glVertex3f(1.0, 5.0, 1.0);
    glEnd();
	
	glBegin(GL_POLYGON);    // square 14 stick
        glColor3ub(12, 99, 99);
        glVertex3f(1.0, 2.0, -1.0); glVertex3f(1.0, 5.0, -1.0);
		glVertex3f(-1.0, 5.0, -1.0); glVertex3f(-1.0, 2.0, -1.0);
		glVertex3f(1.0, 5.0, -1.0);
    glEnd();
	
	glBegin(GL_POLYGON);    // square 15 stick
        glColor3ub(12, 99, 99);
        glVertex3f(-1.0, 2.0, -1.0); glVertex3f(-1.0, 5.0, -1.0);
		glVertex3f(-1.0, 5.0, 1.0); glVertex3f(-1.0, 2.0, 1.0);
		glVertex3f(-1.0, 2.0, -1.0);
    glEnd();
	
	glBegin(GL_POLYGON);    // triangle 1
        glColor3ub(250, 99, 71);
        glVertex3f(-1.0, 7.0, 1.0); glVertex3f(1.0, 7.0, 1.0);
		glVertex3f(0.0, 10.0, 0.0);
    glEnd();
	
	glBegin(GL_POLYGON);    // triangle 2
        glColor3ub(250, 99, 71);
        glVertex3f(1.0, 7.0, 1.0); glVertex3f(1.0, 7.0, -1.0);
		glVertex3f(0.0, 10.0, 0.0);
    glEnd();
	
	glBegin(GL_POLYGON);    // triangle 3
        glColor3ub(250, 99, 71);
        glVertex3f(1.0, 7.0, -1.0); glVertex3f(-1.0, 7.0, -1.0);
		glVertex3f(0.0, 10.0, 0.0);
    glEnd();
	
	glBegin(GL_POLYGON);    // triangle 4
        glColor3ub(250, 99, 71);
        glVertex3f(-1.0, 7.0, -1.0); glVertex3f(-1.0, 7.0, 1.0);
		glVertex3f(0.0, 10.0, 0.0);
    glEnd();
	
	//beginCreate(plane_as_a_floor);
	glBegin(GL_POLYGON);    // square 1
        glColor3ub(122, 98, 89);
        glVertex3f(-20.0, 0.0, 20.0); glVertex3f(20.0, 0.0, 20.0);
		glVertex3f(20.0, 0.0, -20.0); glVertex3f(-20.0, 0.0, -20.0);
		glVertex3f(-20.0, 0.0, 20.0);
    glEnd();
	//endCreate();
}

void tampil()
{
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glLoadIdentity();
    LV();
    Gambar();
    glutSwapBuffers();
}

void reshape(int w, int h)
{
    glViewport(0, 0, (GLsizei)w, (GLsizei)h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(75, (GLsizei)w/(GLsizei)h, 1, 300);
    glMatrixMode(GL_MODELVIEW);
}

void timer(int value)
{
    yp += 10;
    if(yp >= 360)
    {
        yp = 0;
    }

    glutPostRedisplay();
    glutTimerFunc(100, timer, 0);
}

void keyboard1(unsigned char key, int x, int y)
{
    switch(key)
    {
        case 'w':
            fy += 2;
            break;
        case 's':
            fy -= 2;
            break;
        case 'a':
            fx -= 2;
            break;
        case 'd':
            fx += 2;
            break;
        case 'o':
            fz -= 2;
            break;
        case '1':
            fz += 2;
            break;
        case 27:
            exit(0);
            break;
    }
}

void keyboard2(int key, int x, int y)
{
    switch(key)
    {
        case GLUT_KEY_PAGE_UP:
            tz -= 2;
            break;
        case GLUT_KEY_PAGE_DOWN:
            tz += 2;
            break;
        case GLUT_KEY_RIGHT:
            tx += 2;
            break;
        case GLUT_KEY_LEFT:
            tx -= 2;
            break;
        case GLUT_KEY_UP:
            ty += 2;
            break;
        case GLUT_KEY_DOWN:
            ty -= 2;
            break;

    }
}

int main(int argc, char * argv[])
{
    glutInit(&__argc, __argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
    glutInitWindowPosition(50, 10);
    glutInitWindowSize(500, 500);
    glutCreateWindow("3D || KGV");
    glClearColor(1, 1, 1, 1);
    glOrtho(-2, 2, -2, 2, -2, 2);
    glutDisplayFunc(tampil);
    glutReshapeFunc(reshape);
    glutKeyboardFunc(keyboard1);
    glutSpecialFunc(keyboard2);
    glutTimerFunc(1, timer, 0);
    glutMainLoop();
}
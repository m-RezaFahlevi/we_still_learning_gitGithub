#include <bits/stdc++.h>
#include <stdlib.h>
#include <GL/freeglut.h>
using namespace std;

float xp = 0, yp = 0, r = 25, n = 1000, a, x, y;

/*
 *Note:
 *xp and yp = center coordinate of cartesian
 *r = radius
 *n = n of side
 */

void Circle() {
	glColor3ub(20, 210, 190);
	glBegin(GL_POLYGON);
		a = 6.28 / n;	// a = 6.28 is divide it by n of side;
		for (int i = 0; i < n; i++) {
			x = xp + r * cos(i * a);
			y = yp + r * sin(i * a);
			glVertex2f(x,y);
		}
	glEnd();

	glFlush();
}

void display() {
	glClear(GL_COLOR_BUFFER_BIT);
	Circle();
	glutSwapBuffers();
}


int main(int argc, char** argv) {
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB);
	glutInitWindowPosition(25, 25);
	glutInitWindowSize(640, 480);
	glutCreateWindow("Lingkaran");
	glClearColor(1, 1, 1, 1);
	gluOrtho2D(-160, 160, -120, 120);
	glutIdleFunc(display);
	glutDisplayFunc(display);
	glutMainLoop();
}


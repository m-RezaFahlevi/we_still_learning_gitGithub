#include <bits/stdc++.h>
#include <GL/freeglut.h>
using namespace std;

void tampil() {
	glClear(GL_COLOR_BUFFER_BIT);

	glPointSize(10);
	glEnable(GL_POINTS);
	glBegin(GL_POINTS);
		glVertex2i(75, -75);
		glVertex2i(75,75);
		glVertex2i(-75,75);
		glVertex2i(-75,-75);
	glEnd();

	glLineWidth(2);
	glEnable(GL_LINES);
	glBegin(GL_LINES);
		glVertex2i(75,-75);
		glVertex2i(75,75);
		glVertex2i(75,75);
		glVertex2i(-75,75);
		glVertex2i(-75,75);
		glVertex2i(-75,-75);
	glEnd();

	glFlush();
}

int main(int argc, char** argv) {
	glutInit(&argc, argv);
	glutInitWindowSize(320, 240);
	glutInitWindowPosition(0,0);
	glutCreateWindow("Primitive Drawing");
	gluOrtho2D(-320, 320, -240, 240);
	glutDisplayFunc(tampil);
	glutMainLoop();
}

#include <bits/stdc++.h>
#include <GL/freeglut.h>
using namespace std;

void display() {
	glClear(GL_COLOR_BUFFER_BIT);
	glColor3f(0,0,0);
	glEnable(GL_LINE_STIPPLE);
	glLineStipple(3, 0x1111); //create a point
	glBegin(GL_LINE_LOOP);
		glVertex2f(-0.8, 0);
		glVertex2f(-0.4, 0.4);
		glVertex2f(0, 0);
		glVertex2f(0.4, 0.4);
		glVertex2f(0.4, 0.4);
		glVertex2f(0.8, 0);
		glVertex2f(0, -0.8);
	glEnd();
	glutSwapBuffers();
}
int main(int argc, char** argv) {
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
	glutInitWindowPosition(100,100);
	glutInitWindowSize(500,500);
	glutCreateWindow("Line Stipple");
	glClearColor(1.0, 1.0, 1.0, 1.0);
	gluOrtho2D(-1, 1, -1, 1);
	glutIdleFunc(display);
	glutDisplayFunc(display);
	glutMainLoop();
}

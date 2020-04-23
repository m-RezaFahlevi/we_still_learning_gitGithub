#include <bits/stdc++.h>
#include <GL/freeglut.h>
using namespace std;

void userdraw() {
	glBegin(GL_QUADS);
		glColor3ub(255,0,0);
		glVertex2f(-100,100);
		glVertex2f(100,100);
		glColor3f(0.5,1,0.5);
		glVertex2f(100,-100);
		glVertex2f(-100,-100);
	glEnd();
}

void display() {
	glClear(GL_COLOR_BUFFER_BIT);
	userdraw();
	glutSwapBuffers();
}

int main(int argc, char** argv) {
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
	glutInitWindowPosition(100,100);
	glutInitWindowSize(640,480);
	glutCreateWindow("Project Perta KGV");
	glClearColor(0.0,0.0,0.0,0.0);
	gluOrtho2D(-320,320,-240,240);
	glutIdleFunc(display);
	glutDisplayFunc(display);
	glutMainLoop();
}

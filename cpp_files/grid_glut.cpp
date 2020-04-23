#include <bits/stdc++.h>
#include <GL/freeglut.h>
using namespace std;

void display() {
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	glLineWidth(1); //manage the size of pixel (point)

	for (float i = -1.0; i < 1.0; i += 0.1) {
		glBegin(GL_LINES); //function to create a line;
			glVertex2f(i, -1.0);
			glVertex2f(i, 1.0);
		glEnd();
	}

	for (float i = -1.0; i < 1.0; i += 0.1) {
		glBegin(GL_LINES);	//function to create a line
			glVertex2f(-1.0, i);
			glVertex2f(1.0, i);
		glEnd();
	}

	glutSwapBuffers();
}

int main(int argc, char** argv) {
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA);
	glutInitWindowPosition(50,0);
	glutInitWindowSize(500,500);
	glutCreateWindow("Create a Grid");
	glClearColor(0.0, 0.0, 0.0, 0.0);
	gluOrtho2D(-1, 1, -1, 1);
	glutIdleFunc(display);
	glutDisplayFunc(display);
	glutMainLoop();
}


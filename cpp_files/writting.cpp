#include <bits/stdc++.h>
#include <GL/freeglut.h>
using namespace std;

void write(float x, float y, float z, void *font, const char * string) {
	const char *c;
	glRasterPos3f(x, y, z);
	for (c = string; *c != '\0'; c++) {
		glutBitmapCharacter(font, *c);
	}
}

void display() {
	glClear(GL_COLOR_BUFFER_BIT);
	glColor3ub(200, 120, 100);
	write(0.2, 0.2, 0, GLUT_BITMAP_HELVETICA_18, "IKLC");
	write(-0.8, -0.5, 0, GLUT_BITMAP_HELVETICA_18, "Ilmu Komputer Laboratory Center");
	glEnd();
	glFlush();
	glutSwapBuffers();
}

int main(int argc, char** argv) {
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB);
	glutInitWindowPosition(25,25);
	glutInitWindowSize(640,640);
	glutCreateWindow("Create a letter");
	glClearColor(1, 1, 1, 1);
	gluOrtho2D(-1.0, 1.0, -1.0, 1.0);
	glutDisplayFunc(display);
	glutMainLoop();
}

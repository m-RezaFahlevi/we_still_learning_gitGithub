#include <bits/stdc++.h>
using namespace std;

class Node {
public:
	int the_data;
	Node *next_node;
};

void insert_the_data(Node *st_node) {
	Node *temp = NULL;
	temp = new Node();
	temp = st_node;
	while (temp != NULL) {
		cout << "Enter the data : "; cin >> temp -> the_data;
		temp = temp->next_node;
	}
}

void display_the_data(Node *st_node) {
	Node *temp = NULL;
	temp = new Node();
	temp = st_node;

	while(temp != NULL) {
		cout << temp -> the_data << " --> ";
		temp = temp -> next_node;
	}

	cout << "NULL\n";
}

void display_the_address(Node *st_node) {
	Node *temp = NULL;
	temp = new Node();
	temp = st_node;

	while(temp != NULL) {
		cout << temp << " --> ";
		temp = temp -> next_node;
	}

	cout << temp << endl;
}

int main(void) {
	Node *head = NULL;
	Node *second = NULL;
	Node *third = NULL;

	// allocate 3 nodes in random memory
	head = new Node();
	second = new Node();
	third = new Node();

	//assign the value;
	head -> next_node = second;
	second -> next_node = third;
	third -> next_node = NULL;

	insert_the_data(head);
	display_the_data(head);
	display_the_address(head);
}

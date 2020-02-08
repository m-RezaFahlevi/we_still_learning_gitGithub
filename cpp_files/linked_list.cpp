#include <bits/stdc++.h>
using namespace std;

class Node {
public:
	int the_data;
	Node *next_node;
	Node *previous_node;
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

void display_the_data_forwards(Node *st_node) {
	Node *temp = NULL;
	temp = new Node();
	temp = st_node;

	while(temp != NULL) {
		cout << temp -> the_data << " --> ";
		temp = temp -> next_node;
	}

	cout << "NULL\n";
}

void display_the_data_backwards(Node *thrd_node) {
	Node *temp = NULL;
	temp = new Node();
	temp = thrd_node;

	while(temp != NULL) {
		cout << temp -> the_data << " --> ";
		temp = temp -> previous_node;
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
	head -> previous_node = NULL;
	head -> next_node = second;
	second -> previous_node = head;
	second -> next_node = third;
	third -> previous_node = second;
	third -> next_node = NULL;

	insert_the_data(head);
	display_the_data_forwards(head);
	display_the_data_backwards(third);
	display_the_address(head);

	//Create a new node
	Node *new_node = NULL;
	new_node = new Node(); // allocate the new_node;

	new_node -> the_data = 7;
	new_node -> previous_node = second;
	new_node -> next_node = third;

	second -> next_node = new_node;
	third -> previous_node = new_node;

	display_the_data_forwards(head);
	display_the_data_backwards(third);

}

import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;

class LinkedList {
	Node head;

	static class Node {
		int data;
		Node next;
		
		//create the constructor here;
		Node(int theData) {
			data = theData;
			next = null;
		}
	}

	public static void main(String[] args) {
		BufferedReader scan = new BufferedReader(new InputStreamReader(System.in));
		try {
			LinkedList linkedList = new LinkedList();	//create the object named linkedList;
			linkedList.head = new Node(1);
			Node second = new Node(2);
			Node third = new Node(3);

			//linked the data
			linkedList.head.next = second;
			second.next = third;
			third.next = null;

			//Display the data;
			System.out.println(linkedList.head.data + " --> " + second.data + " --> " + third.data);

			//Display the address of each node;
			System.out.println(linkedList.head + " --> " + linkedList.head.next + " --> " + second.next + " --> " + third.next);
		} catch(Throwable exc) {
			System.out.println(exc);
		}
	}
}

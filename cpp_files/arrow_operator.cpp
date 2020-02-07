#include <bits/stdc++.h>
using namespace std;

class cpp_class {
public:
    int the_data;
    bool truth_value;
    
    cpp_class() {
        the_data = 0;
        truth_value = false;
    }
};

int main(void) {
    cpp_class my_cpp_class; //This is not pointer;
    cpp_class *pointer_cpp_class; //we defined some pointer
    pointer_cpp_class = new cpp_class(); //allocate the pointer to some memory
    
    //Accessing the class attribute
    pointer_cpp_class -> the_data = 10;
    pointer_cpp_class -> truth_value = true;
    
    if (pointer_cpp_class -> truth_value)
        cout << "The data : " << pointer_cpp_class << endl;
}

// Using vectors
//Includes 2 ways to initialize them
//use of size() front() back() to get current size, first element and last element of vector
//use of begin() and end() to get pointer to first and last+1 element of vector
//use of erase and insert function which is linear in time
//using iterator whhich are pointer-like objects that can be used to traverse a sequence of objects here(vectors)


#include <iostream>
#include <vector>
using namespace std;

int main() {
	// from initializer list (C++11)
	cout << "vector from initializer list (C++11): " << endl;
	vector<int> vi1 = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
	cout << "size: "  <<   vi1.size()    << endl;
	cout << "begin: " <<  *(vi1.begin()) <<endl;
	cout << "end: "   <<  *(--vi1.end()) <<endl;
	cout << "front: " <<   vi1.front()   << endl;
	cout << "back: "  <<   vi1.back()    << endl<<endl;
	
	cout << "insert 42 at begin + 5: " << endl;
	vi1.insert(vi1.begin() + 5, 42);
	cout << "size: " << vi1.size() << endl;
	cout << "vi1[5]: " << vi1[5] << endl;
	cout << "erase at begin + 5: " << endl;
	vi1.erase(vi1.begin() + 5);
	cout << "size: " << vi1.size() << endl;
	cout << "vi1[5]: " << vi1[5] << endl<<endl;

	cout << "push_back 47: " << endl;
	vi1.push_back(47);
	cout << "size: " << vi1.size() << endl;
	cout << "vi1.back() " << vi1.back() << endl<<endl;

	// range-based iterator (C++11)
	cout << "range-based iterator (C++11): " << endl;
	for(int & v : vi1) {
		cout << v << " ";
	}
    cout << endl<<endl;
    
    
	// from C-array
	const static int size = 10;
	cout << "vector from C-array: " << endl;
	int ia[size] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
	vector<int> vi2(ia, ia + size);
	cout << "printing using loop" << endl;
	for(int i = 0; i < size; i++) {
		cout << vi2[i] << " ";
	}
	
	//using iterator
	cout << endl <<endl<<"printing using iterator"<<endl;
	for(vector<int>::iterator i = vi2.begin();i<vi2.end();i++)
	cout << *i<< " ";
		return 0;
}

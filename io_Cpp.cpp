#include <iostream>
#include <fstream>

using namespace std;

int main() {
//    std::cout << "Hello, World!" << std::endl;
//    ofstream out;
//    out.open("file");
//    out<<"Hello";
//    out.close();

    string string1;
    ifstream in;
    in.open("file");
    while (getline(in,string1))
    {
        cout << string1 << endl;
    }
    in.close();

    return 0;
}

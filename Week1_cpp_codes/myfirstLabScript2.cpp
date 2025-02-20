#include <iostream>
using namespace std;

int main(){
    cout << "Enter a number: ";
    int var1;
    cin >> var1;
    cout << "Enter another number: ";
    int var2;
    cin >> var2;

    int sum = var1 + var2;
    int diff = var1 - var2;
    int prod = var1 * var2;

    cout << "The sum is " << sum << endl;
    cout << "The difference is " << diff << endl;
    cout << "The production is " << prod << endl;

}
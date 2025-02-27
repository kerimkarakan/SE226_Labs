#include <iostream>
using namespace std;

int main(){
    cout << "Enter a number between 3 and 9 (inclusive): ";
    int user_num;
    cin >> user_num;

    if(user_num <= 9 && user_num >= 3){
        for(int i = 1; i <= user_num; i++){
            for(int j = 0; j < i; j++){
                cout << "*";
            }
            cout << endl;
        }

        for(int j = user_num - 1; 0 < j; j--){
            for(int k = 0; k < j; k++){
                cout << "*";
            }
            cout << endl;
        }
    }
    else{
        cout << "Enter a valid number!" << endl;
    }
}
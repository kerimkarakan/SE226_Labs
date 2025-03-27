#include <iostream>
using namespace std;


double func(int n){

    if(n <= 0){
        return 0;
    }

    return (1.0/n) + func(n-1);
}

double func(){
    cout << "Please enter a number: ";
    int n;
    cin >> n;

    double sum = 0;

    for(int i = 1; i <= n; i++){
        sum += 1.0/i;
    }

    return sum;
}
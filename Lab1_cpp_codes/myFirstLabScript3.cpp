#include <iostream>
using namespace std;

int main(){
    cout << "Name: ";
    string name;
    cin >> name;

    cout << "Lab: ";
    int lab_grade;
    cin >> lab_grade;

    cout << "Midterm: ";
    int midterm_grade;
    cin >> midterm_grade;

    cout << "Final: ";
    int final_grade;
    cin >> final_grade;

    double calculated_lab_grade = lab_grade * 0.25;
    double calculated_midterm_grade = midterm_grade * 0.35;
    double calculated_final_grade = final_grade * 0.40;
    
    cout << "Last Score: " << calculated_lab_grade + calculated_midterm_grade + calculated_final_grade << endl;
}
#include <iostream>
using namespace std;


class Queue{
    private:
    class Node{
        public:
        int data;
        Node *next;
        Node(int x, Node *n)   {data=x; next=n;}
    };

    Node *frontPtr;
    Node *backPtr;
    int count;

    public:
    Queue(){
        frontPtr = nullptr;
        backPtr = nullptr;
        count = 0;
    }

    bool isEmpty(){
        return frontPtr == nullptr;
    }

    void enqueue(int value){
        Node *newNode = new Node(value, nullptr);

        if(isEmpty()){
            frontPtr = newNode;
            backPtr = newNode;
        } 
        else{
            backPtr->next = newNode;
            backPtr = newNode;
        };
        count++;
    }

    void dequeue(){
        if(isEmpty()){
            cout << "Queue is empty!"<< endl;
            return;
        }

        Node *temp = frontPtr;
        frontPtr = frontPtr->next;

        if(frontPtr == nullptr){
            backPtr = nullptr;
        }

        delete temp;
        count--;
    }

    int top(){
        if(isEmpty()){
            cout << "Queue is empty!"<< endl;
            return 0;
        }
        else{
            return frontPtr->data;
        }
    }

    int size(){
        return count;
    }

};
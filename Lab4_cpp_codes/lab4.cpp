#include <iostream>
#include <new>
using namespace std;

class Node {
public:
    int data;
    Node* next;
};

class Stack {
private:
    Node *head;
    int num;
    int capacity;

public:
    Stack(int initialCapacity) {
        head = nullptr;
        num = -1;
        capacity = initialCapacity;
    }

    void push(int x) {
        Node *newNode = new Node;
        newNode->data = x;
        newNode->next = head;
        head = newNode;
        num++;
    }

    int pop() {
        if(isEmpty()){
            cout << "The stack is empty!" << endl;
            return 0;
        }
        else{
            int topEl = head->data;
            Node *temp = head;
            head = head->next;
            delete temp;
            num--;
            return topEl;
        }
    }
    int peek() {
        if(isEmpty()){
            cout << "The stack is empty!" << endl;
            return 0;
        }
        else{
            return head->data;
        }
    }

    bool isEmpty() {
        return num < 0;
    }

    void increaseCapacity() {
        if(num >= capacity){
            capacity = capacity * 2;
        }
    }

    bool deleteElement(int val) {
        if(isEmpty()){
            return false;
        }

        if(head->data == val){
            Node *temp = head;
            head = head->next;
            delete temp;
            num--;
            return true;
        }

        Node *prev = head;
        
        for(Node *current = head->next; current != nullptr; current = current->next){
            if(current->data == val){
                prev->next = current->next;
                delete current;
                num--;
                return true;
            }
            prev = current;
        }

        return false;
    }
};
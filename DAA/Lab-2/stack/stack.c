#include<stdio.h>
#define SIZE 100
int stack[SIZE];
int top = -1;


void push(int n) {
    if(top >= SIZE-1) {
        printf("Not valid");
    }
    else {
        stack[++top] = n;
        printf("Number is pushed\n");
    }
}

void pop() {
    if(top < 0) {
        printf("Stack Underflow\n");
    }
    else {
        printf("Popped element: %d \n", stack[top--]);
    }
}

void peep() {
    if(top < 0) {
        printf("Stack is empty");
    }
    else {
        printf("Top element: %d", stack[top]);
    }
}

void display() {
    if(top < 0) {
        printf("Stack is empty\n");
    } else {
        printf("Stack elements: ");
        for(int i = top; i >= 0; i--) {
            printf("%d ", stack[i]);
        }
        printf("\n");
    }
}

void change(int index, int value) {
    if(index < 0 || index > top) {
        printf("Invalid index\n");
    } else {
        stack[index] = value;
        printf("Value changed at index %d \n", index);
    }
}

int main() {
    push(20);
    push(30);
    push(10);
    pop();
    change(0,100);
    display();
	return 0;
}
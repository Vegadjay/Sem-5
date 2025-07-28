#include<stdio.h>
#define SIZE 100
int queue[SIZE];
int top = -1;

int front = -1, rear = -1;

void enqueue(int value) {
    if (rear == SIZE - 1) {
        printf("Queue Overflow\n");
        return;
    }
    
    if (front == -1){
        front = 0;
    }

    rear++;
    queue[rear] = value;
    printf("%d enqueued to queue\n", value);
}

int dequeue() {
    if (front == -1 || front > rear) {
        printf("Queue Underflow\n");
        return -1;
    }
    int value = queue[front];
    front++;
    if (front > rear) {
        front = rear = -1;
    }
    printf("%d dequeued from queue\n", value);
    return value;
}

void display() {
    if (front == -1) {
        printf("Queue is empty\n");
        return;
    }
    printf("Queue elements: ");
    for (int i = front; i <= rear; i++) {
        printf("%d ", queue[i]);
    }
    printf("\n");
}

void main() {
    enqueue(20);
    enqueue(30);
    enqueue(10);
    enqueue(260);
    dequeue();
    display();
}
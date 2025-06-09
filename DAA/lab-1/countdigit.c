#include<stdio.h>

int main() {
    int number, cnt = 0;
    printf("Enter a number:- ");
    scanf("%d", &number);
    while(number != 0) {
        number % 10;
        cnt++;
        number /= 10;
    }
    printf("%d", cnt);
}
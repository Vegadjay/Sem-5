#include <stdio.h>

int sumofn(int n) {
    if(n == 1) {
        return 1;
    }
    return n + sumofn(n-1);
}

int main() {
    

    int number;
    printf("Enter a number:- ");
    scanf("%d", &number);
    printf("%d",sumofn(3));

    return 0;
}
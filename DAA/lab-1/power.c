#include <stdio.h>

void main() {
    int number = 1, pow = 1;
    printf("Enter a number:- ");
    scanf("%d", &number);
    printf("Enter a pow:- ");
    scanf("%d", &pow);
    int ans = 1;
    for(int i = 1; i<=pow; i++) {
        ans *= number;
    }
    printf("%d", ans);
}
#include<stdio.h>

int power(int number, int pow) {
    if(pow < 1) {
        return 1;
    }
    return number * power(number, pow-1);
}

int main() {
    int number = 1, pow = 1;
    printf("Enter a number:- ");
    scanf("%d",&number);
    printf("Enter power:- ");
    scanf("%d", &pow);
    printf("%d",power(number, pow));
    return 0;
}
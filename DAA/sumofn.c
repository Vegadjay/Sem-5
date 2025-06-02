#include <stdio.h>

int main() {
    int n, sum = 0, i, num;

    printf("Enter the number of elements: ");
    scanf("%d", &n);

    printf("Enter %d numbers:\n", n);
    for(i = 0; i < n; i++) {
        scanf("%d", &num);
        sum += num;
    }

    printf("Sum of %d numbers is: %d\n", n, sum);
    return 0;
}
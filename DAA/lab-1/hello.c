#include <stdio.h>

int main() {

    int ans = 1, number;
    scanf("%d", &number);
    for(int i = 1; i <= number; i++) {
        ans *= i;
    }
    printf("%d", ans);
}

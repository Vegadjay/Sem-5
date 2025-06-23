#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int selectionSort(int arr[], int n) {
    int i, j, temp;
    clock_t start, end;

    start = clock();

    for(i = 0; i < n - 1; i++) {
        int minIndex = i;
        for(j = i + 1; j < n; j++) {
            if(arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
        if(minIndex != i) {
            temp = arr[i];
            arr[i] = arr[minIndex];
            arr[minIndex] = temp;
        }
    }
    end = clock();
    double time_taken = (double)(end - start) / CLOCKS_PER_SEC;
    printf("Time taken for selection sort: %f seconds\n", time_taken);
    return 0;
}

void main() {
    int arr[] = {64, 25, 12, 22, 11};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    selectionSort(arr, n);
    
    printf("Sorted array: \n");
    for(int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}
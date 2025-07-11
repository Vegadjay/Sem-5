#include<stdio.h>

int pivot(int arr[], int i, int j) {
    int p = arr[i];
    int k = i;
    int l = j + 1;
    do {
        k++;
    } while(arr[k] < p && k <= j);
    do {
        l--;
    } while(arr[l] > p);
    while(k < l) {
        int temp = arr[k];
        arr[k] = arr[l];
        arr[l] = temp;

        do {
            k++;
        } while (arr[k] < p && k <= j);

        do {
            l--;
        } while (arr[l] > p);
    }
    int temp = arr[i];
    arr[i] = arr[l];
    arr[l] = temp;
    return l;
}

void quick_sort(int arr[], int low, int high) {
    if (low < high) {
        int pi = pivot(arr, low, high);
        quick_sort(arr, low, pi - 1);
        quick_sort(arr, pi + 1, high);
    }
}

void print_array(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    int arr[] = {4,3,2,111,2,3,444,32,4444,2};
    int n = sizeof(arr) / sizeof(arr[0]);
        
    quick_sort(arr, 0, n - 1);
    print_array(arr, n);
    return 0;
}
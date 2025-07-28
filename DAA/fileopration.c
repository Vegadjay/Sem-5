#include<stdio.h>
#include<stdlib.h>

int main(){
    FILE *file;

    file = fopen("best.txt","w");
    for(int i=0 ; i< 100000 ; i++){
        fprintf(file , "%d " , i);
    }
    fclose(file);

    file = fopen("worst.txt","w");
    for(int i=100000 ; i> 0 ; i--){
        fprintf(file , "%d " , i);
    }
    fclose(file);

    file = fopen("average.txt","w");
    for(int i=100000 ; i> 0 ; i--){
        fprintf(file , "%d " , rand()%100000);
    }
    fclose(file);
    return 0;
}
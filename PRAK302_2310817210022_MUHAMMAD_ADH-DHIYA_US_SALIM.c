#include <stdio.h>
int main() {
    int nilai;
    for(int i=0;i<5;i++){
    scanf("%d", &nilai);
    if(nilai >= 80){printf("A\n");}
    else if(nilai >= 70){printf("B\n");}
    else if(nilai >= 60){printf("C\n");}
    else if(nilai >= 50){printf("D\n");}
    else if(nilai <= 50){printf("E\n");}
    }
    return 0;
}
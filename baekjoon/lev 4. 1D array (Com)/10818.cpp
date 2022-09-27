#include <stdio.h>
int main(){
    int min,max;
    min = 1000000;
    max = -1000000;
    int n;
    scanf("%d",&n);
    int a;
    for(int i =0;i<n;i++){
        scanf("%d",&a);
        if(a<min)
            min = a;
        if(a>max)
            max = a;
    }
    printf("%d %d",min,max);
}
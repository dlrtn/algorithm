#include <stdio.h>
int main(){
    int a,b;
    scanf("%d %d",&a,&b);
    if(a==0 && b<45)
        a=24;
    if(b<45)
        printf("%d %d",a-1,b+60-45);
    else
        printf("%d %d",a,b-45);
}
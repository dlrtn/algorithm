#include <stdio.h>
int main(){
    int a,b,c[10000],n;
    int cnt = 0;
    scanf("%d %d",&a,&b);
    for(int i=0;i<a;i++){
        scanf("%d",&n);
        if(n<b){
            c[cnt]=n;
            cnt++;
        }

    }
    for(int i=0;i<cnt;i++){
        printf("%d ",c[i]);
    }
}
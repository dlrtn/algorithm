#include <stdio.h>
int main(){
    int n, goal;
    int a[101];
    scanf("%d %d",&n,&goal);
    for(int i = 0;i <n;i++)
        scanf("%d",&a[i]);
    int temp;
    int max =0;
    for(int i=0;i<n;i++){
        for(int j=i+1;j<n;j++){
            for(int k=j+1;k<n;k++){
                temp = a[i]+a[j]+a[k];
                if(temp <= goal && max < temp)
                    max = temp;
            }
        }
    }
    printf("%d",max);
}
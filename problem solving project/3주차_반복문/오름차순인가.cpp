#include <stdio.h>
#include <iostream>
#include <string>

using namespace std;

bool isOrdered(int data[], int n){
	for(int i = 0; i < n-1; i++){ //마지막 인덱스는 비교하면 큰일남
		if(data[i] > data[i+1]){ //오름차순인지는 i인덱스 기준 i+1인덱스와 비교해서 구할 수 있음
			return false; //오름차순이 아닐 경우 바로 false 리턴
		}
	}
	return true; // 위 검사문을 잘 마치고 나오면 true 리턴
}

int main(){
	int n;
	int *data;
	
	scanf("%d", &n);
	data = new int[n];
	
	for (int i =0; i < n; i++) {
		scanf("%d", &data[i]);		
	}
	
	bool result = isOrdered(data, n);
	
	if(result){
		printf("YES");
	}
	else{
		printf("NO");
	}
	
	delete[] data;
	return 0;
}
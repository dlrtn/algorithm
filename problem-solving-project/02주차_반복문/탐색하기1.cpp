#include <stdio.h>
#include <iostream>
#include <string>

using namespace std;

int findIndex(int data[], int n, int m){
	for(int i = 0; i < n; i++)	{ //데이터 사이즈만큼의 검사를 위한 반복문
		if(data[i] == m) //찾는 값과 일치하는 data의 인덱스를 반환
			return i;
	}
	return -1; //찾지 못할경우 -1 반환
}

int main(){
	int n, m;
	int *data;
	
	scanf("%d %d", &n, &m);
	data = new int[n];
	for (int i =0; i < n; i++) {
		scanf("%d", &data[i]);		
	}
	
	int answer = findIndex(data, n, m);
	
	printf("%d\n", answer);
	delete[] data;
	return 0;
}
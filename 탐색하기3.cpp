#include <cstdio>
#include <cmath>
#include <iostream>

using namespace std;

int findIndex(int data[], int n){
	int min = 10000, a, sum = 0; //sum은 평균을 구하기 위한 변수, min은 평균과 각 data값의 차이중 가장 작은 값
	for (int i = 0; i < n; i++){ //data값의 총합을 구하는 for문
		sum += data[i];		
	} 
	for (int i = 0; i < n; i++){
		if (min > abs((sum / n) - data[i])){ //cmath 라이브러리에서 절대값을 구해주는 abs라는 함수를 사용하였습니다. 
			a = i; 
			min = abs((sum / n) - data[i]); //min에 평균값과의 차를 저장합니다
		}			
	}
	
	return a; //출력부분에서 인덱스에만 +1을 해주기로 하였습니다.
}
int main(){
	int n;
	int* data;
	
	scanf("%d", &n);
	data = new int[n];
	
	for (int i = 0; i < n; i++){
		scanf("%d", &data[i]);		
	}
	
	int answer = findIndex(data, n);
	printf("%d %d\n", answer+1, data[answer]);
	
	delete[] data;
	return 0;
	
}
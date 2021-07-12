#include <cstdio>
#include <iostream>

using namespace std;

int getMinIndexInRange(int data[], int n, int begin, int end){
	int min = 65535;
	int min_index = 0;
	for (int i = begin; i <= end; i++){ //begin~ end 사이의 값에서 검색
		if (data[i] < min){ //i번째 data가 min보다 작을 경우 실행
			min = data[i];	//min 값에 최소값 삽입 (추후 if문 비교를 위해)
			min_index = i;  //min_index에는 그 값의 인덱스를 삽입
		}
	}
	return min_index;	
}

void selectionSort(int data[], int n){
	int temp; //swap시 임시로 사용할 변수
	for (int i = 0; i < n; i++){ 
		int minIndex = getMinIndexInRange(data, n, i, n-1); //최소값을 찾음
		temp = *(&data[i]); // 바꿀 값을 임시변수에 저장
		*(&data[i]) = data[minIndex]; // 바꿔야하는 값에 i~n 인덱스 사이의 최소값 저장
		*(&data[minIndex]) = temp; // 원래 있던 최소값의 인덱스에 임시변수 저장
	}	
}

int main(){
	int n;
	int* data;
	
	scanf("%d", &n);
	data = new int[n];
	
	for (int i = 0; i < n; i++){
		scanf("%d", &data[i]);
	}
	
	selectionSort(data, n);
	
	for (int i =0;i < n; i++){
		if (i > 0){
			printf(" ");
		}
		printf("%d", data[i]);
	}
	
	delete[] data;
	return 0;
}
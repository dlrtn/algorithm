#include <stdio.h>
#include <iostream>
#include <string>

using namespace std;

int getElementTypeCount(int* data, int n){
	int countType = 0;
	
	for (int i =0; i < n-1; i++){//마지막 인덱스는 제외
		for (int j = i+1; j<n; j++){//마지막 인덱스까지 현재 인덱스의 숫자와 중복이 있는지 검사함
			if(data[i] == data[j]){ //중복이 있을경우 ++ 해줌
				countType++;
				break; //중복을 하나 발견하면 바로 다음 인덱스로 넘어감
				// 중복을 하나의 인덱스에서 두개 이상 발견할 경우 값에 오류가 생김
			}			
		}
	}
	countType = n - countType; //n의 값에서 중복 값을 빼줌
	return countType;
}

int main(){
	int n; //n의 값을 저장할 변수 size
	int *data; // 배열을 저장할 변수, 동적임
	
	scanf("%d", &n); 
	data = new int[n];
	
	for (int i =0; i < n; i++) { // n개만큼 배열에 저장받음
		scanf("%d", &data[i]);		
	}
	
	int answer = getElementTypeCount(data, n); //data와 n을 매개변수로 하여 답을 구해냄.
	
	printf("%d\n", answer);
	
	delete[] data; //동적할당된 메모리 해제
	return 0;
}
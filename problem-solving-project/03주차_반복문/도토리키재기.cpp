#include <iostream>
#include <stdio.h>

using namespace std;

int getMaximumHeiht(int height[], int month[], int n, int m) {
	int max = -1; //최댓값을 비교할 변수인 max 선언, -1인 이유는 m값이 비정상적일 경우 -1을 리턴해야되기 때문
	for (int i = 0; i < n; i++){
		if(month[i] == m)//태어난 달이 m과 같을시에만 동작
			if(max < height[i])//i번째 인덱스의 사람이 태어난 달이 같을 경우 키가 가장 큰지 아닌지를 판별해줌
				max = height[i];//i번째 인덱스의 도토리가 0~i번째중에 가장 크다면 그 키를 대입해줌
	}
	
	return max; //최댓값 리턴
}
int main() {
	int n,m; //m은 달의 변수, n은 총 인원
	int* height; //키 배열 
	int* month; //생일 배열
	
	scanf("%d", &n); //총 인원을 입력받음
	height = new int[n]; //총 인원만큼의 키 배열
	month = new int[n]; //총 인원만큼의 태어난 달 배열
	
	for (int i = 0; i < n; i++){ //키 배열 초기화
		scanf("%d", &height[i]);		
	}

	for (int i = 0; i < n; i++){ //생일 배열 초기화
		scanf("%d", &month[i]);		
	}
	
	scanf("%d", &m); //비교하기 위해 생일이 있는 달을 입력받음
	
	int answer = getMaximumHeiht(height, month, n, m); // getMaximuHeight 함수에서 return값을 answer 변수에 저장함
	
	printf("%d\n", answer); //answer를 출력함
	
	delete[] height; //동적할당 해제 
	delete[] month;//동적할당 해제
	return 0;
}

#include<cstdio>
#include<iostream>

using namespace std;


void bubbleSort(int data[], int n) {
	int temp; //값 swqp시 임시로 저장해놓을 변수
	for (int i = n - 1; i > 0; i--) { //마지막 인덱스부터 차례대로 시작 i번째 인덱스에는 0~i번째 인덱스 사이에서 최댓값이 와야하기 때문
		for (int j = 0; j < i; j++) { //j는 0부터 i까지
			if (data[j] > data[j + 1]) { //만약 j가 j+1인덱스보다 큰경우
			    temp = data[j]; //swap 진행
				data[j] = data[j + 1];
				data[j + 1] = temp;
			}
		}
	}
}

int main() {
	int n;//몇 사이즈의 배열을 정렬할지 저장할 변수
	int* data;//정렬할 배열

	scanf("%d", &n); //사이즈 입력받음
	data = new int[n]; //동적할당

	for (int i = 0; i < n; i++) { //배열의 사이즈만큼 입력받음
		scanf("%d", &data[i]);
	}

	bubbleSort(data, n); //버블정렬진행

	for (int i = 0; i < n; i++) {//정렬결과 출력해주는 함수
		if (i > 0) { //처음 실행할땐 공백이 필요 없으므로
			printf(" ");
		}
		printf("%d", data[i]); //배열 출력
	}

	delete[] data; //메모리할당 해제
	return 0; //종료
}
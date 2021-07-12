#include<cstdio>
#include<iostream>

using namespace std;

bool isConsecutive(int data[], int n) { //"연속"되는 수열인지에 대해 검사하는 함수 연속이므로 1씩 증가하거나 감소하여아함
	int max_data = data[0]; //초기값을 0번째 인덱스로 설정
	int min_data = data[0]; //초기값을 0번째 인덱스로 설정

	for (int i = 0; i < n; i++) { //인덱스는 마지막 인덱스까지 방문
		if (max_data < data[i]) //max_data보다 data[i]가 크면
			max_data = data[i];	//max_data에 data[i] 삽입
		if (min_data > data[i]) //min_data보다 data[i]가 작으면
			min_data = data[i];	//min_data에 data[i] 삽입
	}

	if (max_data - min_data + 1 == n) //max값에서 min값을 빼면 즉 입력이 1,2,3,4,5일 경우 4가 되는데 이에 +1을 해주면 사이즈와 같아지므로 수열이 성립하고
									  //입력이 1,2,3,4,6인 경우 5(max-min) + 1 = 6 != n이 되므로 수열이 성립하지 않음을 알 수 있다.
		return true;	
	else  //수열이 성립하지 않을경우 false return
		return false;
}

int main() {
	int n; ;//몇 사이즈의 배열을 입력받을지 저장할 변수
	int* data; //입력된 배열을 저장할 변수

	scanf("%d", &n); //사이즈 입력
	data = new int[n]; //n만큼 동적할당
	for (int i = 0; i < n; i++) { //n만큼 실행해서 배열 입력받음
		scanf("%d", &data[i]);
	}

	bool result = isConsecutive(data, n); //입력된 배열이 정수 수열로 표현될 수 있는지를 검출하는 함수 실행


	if (result) { //가능하면 YES출력
		printf("YES");
	}
	else { //가능하지 않으면 NO 출력
		printf("NO");
	}

	delete[] data; //메모리할당 해제
	return 0; //종료
}
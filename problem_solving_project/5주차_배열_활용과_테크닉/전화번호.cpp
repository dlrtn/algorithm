#include<cstdio>

using namespace std;

const int MAX_TABLE_LENGTH = 10000; //전화번호 뒷자리는 4자리이므로 최대 9999까지 저장가능

void fillFrequencyTable(int data[], int n, int table[]) { //
	for (int i = 0; i < MAX_TABLE_LENGTH; i++) { //변수가 선언만 됐지 초기화는 되어있지 않으므로 초기화시켜주는 포문
		table[i] = 0;
	}
	for (int i = 0; i < n; i++) { 
		int number = data[i]; //number라는 함수에 입력된 전화번호 값을 n개만큼 넣고 
		table[number]++;      //해당 인덱스 table의 값을 1씩 올려줌 
	}
}

int getFrequentNumber(int data[], int n) {
	int frequent_number = 0; //빈도수는 당연히 0으로 초기화되어야함

	int table[MAX_TABLE_LENGTH]; //변수 초기화를 꼭 해야되므로 유의해야함
	fillFrequencyTable(data, n, table); //뒷자리번호마다 나오는 빈도수를 구해주는 함수임


	for (int i = 0; i < MAX_TABLE_LENGTH; i++) { //0~9999까지 돌면서
		if (table[i] > table[frequent_number]) { //가장 많이 나온 인덱스의 번호를 저장함
			frequent_number = i;
		}
	}
	return frequent_number; //그리고 그 인덱스의 값을 리턴해줌
}

int main() {
	int n; //n개를 저장하겠다는 변수

	scanf("%d", &n); //n을 입력받음
	int* data = new int[n]; //포인터 변수 data를 선언하자마자 sizeof(int)*n의 크기만큼 동적할당시켜줌

	for (int i = 0; i < n; ++i) {
		scanf("%d", &data[i]); //뒷자리 번호 배열을 입력받음
	}

	int answer = getFrequentNumber(data, n); //frequent_number값을 answer에 저장함

	printf("%04d", answer); //answer를 출력함, 0이 출력되더라도 앞 04d의 형식이므로  0000으로 출력값이 변함

	delete[] data; //동적할당 해제
	return 0; //끝
}
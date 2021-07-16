#include<stdio.h>
#include<map>
using namespace std;

int main() {
	
	int N; 
	scanf("%d", &N); //CaseSize를 입력받음

	map<int, int> frequencyMap; //빈도수 Map 변수 선언, 

	for (int i = 0; i < N; i++) {
		int X; //입력을 저장할 변수
		scanf("%d", &X); 
		frequencyMap[X]++; //등장한 수의 값을 ++시킴
		printf("%d %d\n", frequencyMap.size(), frequencyMap[X]);//현재 저장된 변수의 종류는 size를 통해서 쉽게 구할 수 있고, 입력된 X에 ++하여 빈도수를 저장하였으므로 이를 출력하면 빈도수를 쉽게 구할 수 있다.
	}

	return 0;
}
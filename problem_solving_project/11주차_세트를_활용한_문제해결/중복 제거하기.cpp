#include <iostream>
#include <set>

using namespace std;

int main() {
	int N;
	cin >> N;

	set<int>integers;
	for (int i = 0; i < N; i++) { //N개만큼 검사할 것이므로
		int X; //각 0~N번의 검사시 사용할 변수
		cin >> X;

		if (integers.find(X) != integers.end()) { //찾는 수가 있다면 해당 iterator를 반환
			printf("DUPLICATED\n");
		}
		else { //찾는 수가 없다면 end() iterator를 반환
			integers.insert(X); //set에 수를 등록한다.
			printf("OK\n");
		}
	}
	return 0;
}
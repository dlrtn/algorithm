#include <cstdio>
#include <vector>

using namespace std;

const int MAX_N = 1000000;
vector<int> FIBONACCI_TABLE;

vector<int> makeFibonacciTable(int n) { //피보나치 수열의 1~n번째 항을 배열에 저장하여 반환해주는 함수
	const int MOD = 100000000; //8자리만 남기기 위한 상수임

	vector<int> ret(n + 1); // 피보나치 배열을 미리 선언해준다.	
	ret[1] = 0; // 첫 번재 항은 0이다.
	ret[2] = 1; // 두 번째 항은 1이다.

	for (int i = 3; i <= n; ++i) { // 세 번째 항부터는 피보나치의 정의를 이용해 계산 == f(n) = f(n - 1) + f(n - 2)
		ret[i] = ret[i - 1] + ret[i - 2];

		// 피보나치를 구할 때 모듈러 값을 이용해 뒤에 8자리만 남기도록 해줌
		// ((A % MOD) + (B % MOD)) % MOD == (A + B) % MOD임
		// 위 식이 성립하기 때문에 피보나치의 값이 잘못될 일은 없음
		ret[i] %= MOD;
	}

	return ret;
}

int getFibo(int n) {	
	int answer = FIBONACCI_TABLE[n]; // 피보나치의 값을 미리 계산해 뒀기 때문에 그 값을 반환
	return answer; //정답 리턴
}

int main() {
	FIBONACCI_TABLE = makeFibonacciTable(MAX_N); //피보나치테이블이라는 전역변수 벡터를 초기화시킴

	int caseSize;
	scanf("%d", &caseSize); //케이즈 사이즈를 입력받음

	for (int caseIndex = 1; caseIndex <= caseSize; ++caseIndex) { //caseindex마다 출력할 피보나치를 입력받ㄷ아 처리함
		int n;
		scanf("%d", &n);

		// 피보나치 수열의 n번째 항을 계산하여 출력한다.
		int answer = getFibo(n);
		printf("%d\n", answer);
	}

	// 불필요한 배열은 가능하면 할당 해제해주는 버릇을 들이자.
	FIBONACCI_TABLE.clear();

	return 0;
}
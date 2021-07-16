#include <cstdio>
#include <vector>

using namespace std;

vector<long long> factorize(long long n) { //자연수 N을 구성하는 모든 소인수를 반환하는 함수
	vector<long long> factors; //최대 10억이하의 자연수이므로 다음과 같은 long long 벡터로 선언

	for (long long div = 2; div * div <= n; div += 1) { // sqrt(N)이하의 자연수 div에 대해서
		while (n % div == 0) { //div이 N의 약수라면 이 때, div보다 작은 약수는 모두 처리되었으므로 div은 소인수임이 보장된다		
			factors.push_back(div); // 소인수 목록에 div을 추가한다.

			// N에서 div을 소거해준다. 
			// 그러므로 이후에는 div을 제외한 소인수를 찾게 된다.
			n /= div;
		}
	}
	if (n > 1) // 소인수를 찾지 못하고 남아있는 N이 존재한다면, 소수일 수 밖에 없다. 이를 소인수에 추가한다.
		factors.push_back(n); //push_back 함수는 Probing에서 설명했듯이 괄호 안의 값을 벡터에 삽입하는 함수임
	
	return factors; //총 저장된 소인수 벡터들을 반환함
}

void process(int caseIndex) { //caseIndex만큼 동작하는 변수
	long long n; //10억 이하의 자연수를 받으므로 그 크기만큼 선언
	scanf("%lld", &n); //n을 입력받음

	vector<long long> factors = factorize(n); //소인수를 구하는 함수를 통해 모든 n에 대한 소인수를 벡터로 저장하여 반환함

	printf("#%d:\n", caseIndex); //caseindex를 출력함 인덱스는 1부터 시작함
	for (int i = 0; i < factors.size(); i++) { //size만큼 실행함
		if (i > 0) 
			printf(" "); //i가 0보다 커지면 공백으로 구분해줌
		printf("%lld", factors[i]); //출력함
	}
	printf("\n"); //끝나면 줄바꿈
}

int main() {
	int caseSize; //case갯수를 저장할 변수
	scanf("%d", &caseSize); //입력받음

	for (int caseIndex = 1; caseIndex <= caseSize; caseIndex++) //case인덱스만큼 수행함 1부터 시작
		process(caseIndex);
	
}
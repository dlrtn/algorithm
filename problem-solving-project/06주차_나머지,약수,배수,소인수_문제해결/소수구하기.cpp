#include <cstdio>
#include <vector>

using namespace std;

class Sieve {
public:
	int maximumValue;     // 에라토스테네스의 체에서 다룰 가장 큰 범위의 값
	vector<bool> isPrime; // 각 숫자별 소수 여부
	Sieve(int maximumValue) { //초기화 시켜주는 생성자
		this->maximumValue = maximumValue;
		this->isPrime.assign(maximumValue + 1, false); //isPrime 변수를 모두 false로 선언함
		this->fillSieve(); //fillSieve 함수를 작동시킴
	}

	bool isPrimeNumber(int num) const { //'num'이 소수라면 true, 그렇지 않으면 false 리턴
		return this->isPrime[num];
	}

	void fillSieve() {
		isPrime.assign(this->maximumValue, true); // 처음에는 모두 소수라고 저장한다.
		isPrime[0] = isPrime[1] = false;    // 0과 1은 소수가 아니므로 미리 처리한다.

		for (int num = 2; num <= maximumValue; num += 1) {			
			if (isPrime[num] == false) { // [2, N] 사이의 모든 자연수 num에 대해
				// 이미 소수가 아니라고 체크되었다면 건너 뛴다.
				continue;
			}

			// 이 때 num은 소수임
			// 그러므로 num의 모든 배수를 소수가 아니라고 체크함
			// num보다 작은 k에 대해 mul=num*num으로 표현되는 모든 자연수는 이미 처리되었음
			// 그러므로 mul = num * num 부터만 처리하면 됨
			for (long long mul = (long long)num * num; mul <= maximumValue; mul += num) {
				// 이 때 mul에 대해서, mul을 나누는 '최초의 소인수 num'이 등장
				// 이 정보를 저장해두면 소인수 분해를 할 때 유용함
				int index = (int)mul; //index에는 mul를 정수화한 인덱스를 false라고 선언함
				isPrime[index] = false;
			}
		}
	}
};

vector<int> getAllPrimeNumbers(int from, int to, const Sieve& sieve) {
	vector<int> primes; //

	for (int num = from; num <= to; num += 1) {//L부터 R까지 모든 정수에 대해서
		if (sieve.isPrimeNumber(num)) { //num이 소수인지를 검사하여
			primes.push_back(num); //primes라는 정수형 벡터에 추가함
		}
	}

	return primes; //그리고 그 정수형 벡터를 반환함
}

void process(int caseIndex, const Sieve& sieve) {
	int L, R; //L이상 R이하의 범위의 소수를 구하기 위한 정수형 변수 L,R
	scanf("%d%d", &L, &R); //L과 R을 입력받음

	vector<int> allPrimeNumbers = getAllPrimeNumbers(L, R, sieve); //모든 

	printf("Case #%d:\n", caseIndex);
	printf("%d\n", (int)allPrimeNumbers.size()); //해당 백터의 사이즈를 정수형으로 반환함
}

int main() {
	const int MAX_VALUE = 1000000; //최대 100만을 입력하므로 최대로 설정함
	Sieve sieve = Sieve(MAX_VALUE); //sieve라는 클래스 변수를 최대로 설정함

	int caseSize;
	scanf("%d", &caseSize); //size를 입력받음

	for (int caseIndex = 1; caseIndex <= caseSize; ++caseIndex) {//size만큼 실행함.
		process(caseIndex, sieve);
	}
}
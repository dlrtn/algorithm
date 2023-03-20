#include <cstdio>
#include <vector>

using namespace std;

class Sieve {
public:
	int maximumValue;     // �����佺�׳׽��� ü���� �ٷ� ���� ū ������ ��
	vector<bool> isPrime; // �� ���ں� �Ҽ� ����
	Sieve(int maximumValue) { //�ʱ�ȭ �����ִ� ������
		this->maximumValue = maximumValue;
		this->isPrime.assign(maximumValue + 1, false); //isPrime ������ ��� false�� ������
		this->fillSieve(); //fillSieve �Լ��� �۵���Ŵ
	}

	bool isPrimeNumber(int num) const { //'num'�� �Ҽ���� true, �׷��� ������ false ����
		return this->isPrime[num];
	}

	void fillSieve() {
		isPrime.assign(this->maximumValue, true); // ó������ ��� �Ҽ���� �����Ѵ�.
		isPrime[0] = isPrime[1] = false;    // 0�� 1�� �Ҽ��� �ƴϹǷ� �̸� ó���Ѵ�.

		for (int num = 2; num <= maximumValue; num += 1) {			
			if (isPrime[num] == false) { // [2, N] ������ ��� �ڿ��� num�� ����
				// �̹� �Ҽ��� �ƴ϶�� üũ�Ǿ��ٸ� �ǳ� �ڴ�.
				continue;
			}

			// �� �� num�� �Ҽ���
			// �׷��Ƿ� num�� ��� ����� �Ҽ��� �ƴ϶�� üũ��
			// num���� ���� k�� ���� mul=num*num���� ǥ���Ǵ� ��� �ڿ����� �̹� ó���Ǿ���
			// �׷��Ƿ� mul = num * num ���͸� ó���ϸ� ��
			for (long long mul = (long long)num * num; mul <= maximumValue; mul += num) {
				// �� �� mul�� ���ؼ�, mul�� ������ '������ ���μ� num'�� ����
				// �� ������ �����صθ� ���μ� ���ظ� �� �� ������
				int index = (int)mul; //index���� mul�� ����ȭ�� �ε����� false��� ������
				isPrime[index] = false;
			}
		}
	}
};

vector<int> getAllPrimeNumbers(int from, int to, const Sieve& sieve) {
	vector<int> primes; //

	for (int num = from; num <= to; num += 1) {//L���� R���� ��� ������ ���ؼ�
		if (sieve.isPrimeNumber(num)) { //num�� �Ҽ������� �˻��Ͽ�
			primes.push_back(num); //primes��� ������ ���Ϳ� �߰���
		}
	}

	return primes; //�׸��� �� ������ ���͸� ��ȯ��
}

void process(int caseIndex, const Sieve& sieve) {
	int L, R; //L�̻� R������ ������ �Ҽ��� ���ϱ� ���� ������ ���� L,R
	scanf("%d%d", &L, &R); //L�� R�� �Է¹���

	vector<int> allPrimeNumbers = getAllPrimeNumbers(L, R, sieve); //��� 

	printf("Case #%d:\n", caseIndex);
	printf("%d\n", (int)allPrimeNumbers.size()); //�ش� ������ ����� ���������� ��ȯ��
}

int main() {
	const int MAX_VALUE = 1000000; //�ִ� 100���� �Է��ϹǷ� �ִ�� ������
	Sieve sieve = Sieve(MAX_VALUE); //sieve��� Ŭ���� ������ �ִ�� ������

	int caseSize;
	scanf("%d", &caseSize); //size�� �Է¹���

	for (int caseIndex = 1; caseIndex <= caseSize; ++caseIndex) {//size��ŭ ������.
		process(caseIndex, sieve);
	}
}
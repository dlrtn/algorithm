#include <cstdio>
#include <vector>

using namespace std;

const int MAX_N = 1000000;
vector<int> FIBONACCI_TABLE;

vector<int> makeFibonacciTable(int n) { //�Ǻ���ġ ������ 1~n��° ���� �迭�� �����Ͽ� ��ȯ���ִ� �Լ�
	const int MOD = 100000000; //8�ڸ��� ����� ���� �����

	vector<int> ret(n + 1); // �Ǻ���ġ �迭�� �̸� �������ش�.	
	ret[1] = 0; // ù ���� ���� 0�̴�.
	ret[2] = 1; // �� ��° ���� 1�̴�.

	for (int i = 3; i <= n; ++i) { // �� ��° �׺��ʹ� �Ǻ���ġ�� ���Ǹ� �̿��� ��� == f(n) = f(n - 1) + f(n - 2)
		ret[i] = ret[i - 1] + ret[i - 2];

		// �Ǻ���ġ�� ���� �� ��ⷯ ���� �̿��� �ڿ� 8�ڸ��� ���⵵�� ����
		// ((A % MOD) + (B % MOD)) % MOD == (A + B) % MOD��
		// �� ���� �����ϱ� ������ �Ǻ���ġ�� ���� �߸��� ���� ����
		ret[i] %= MOD;
	}

	return ret;
}

int getFibo(int n) {	
	int answer = FIBONACCI_TABLE[n]; // �Ǻ���ġ�� ���� �̸� ����� �ױ� ������ �� ���� ��ȯ
	return answer; //���� ����
}

int main() {
	FIBONACCI_TABLE = makeFibonacciTable(MAX_N); //�Ǻ���ġ���̺��̶�� �������� ���͸� �ʱ�ȭ��Ŵ

	int caseSize;
	scanf("%d", &caseSize); //������ ����� �Է¹���

	for (int caseIndex = 1; caseIndex <= caseSize; ++caseIndex) { //caseindex���� ����� �Ǻ���ġ�� �Է¹ޤ��� ó����
		int n;
		scanf("%d", &n);

		// �Ǻ���ġ ������ n��° ���� ����Ͽ� ����Ѵ�.
		int answer = getFibo(n);
		printf("%d\n", answer);
	}

	// ���ʿ��� �迭�� �����ϸ� �Ҵ� �������ִ� ������ ������.
	FIBONACCI_TABLE.clear();

	return 0;
}
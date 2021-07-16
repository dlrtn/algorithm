#include <cstdio>
#include <vector>

using namespace std;

vector<long long> factorize(long long n) { //�ڿ��� N�� �����ϴ� ��� ���μ��� ��ȯ�ϴ� �Լ�
	vector<long long> factors; //�ִ� 10�������� �ڿ����̹Ƿ� ������ ���� long long ���ͷ� ����

	for (long long div = 2; div * div <= n; div += 1) { // sqrt(N)������ �ڿ��� div�� ���ؼ�
		while (n % div == 0) { //div�� N�� ������ �� ��, div���� ���� ����� ��� ó���Ǿ����Ƿ� div�� ���μ����� ����ȴ�		
			factors.push_back(div); // ���μ� ��Ͽ� div�� �߰��Ѵ�.

			// N���� div�� �Ұ����ش�. 
			// �׷��Ƿ� ���Ŀ��� div�� ������ ���μ��� ã�� �ȴ�.
			n /= div;
		}
	}
	if (n > 1) // ���μ��� ã�� ���ϰ� �����ִ� N�� �����Ѵٸ�, �Ҽ��� �� �ۿ� ����. �̸� ���μ��� �߰��Ѵ�.
		factors.push_back(n); //push_back �Լ��� Probing���� �����ߵ��� ��ȣ ���� ���� ���Ϳ� �����ϴ� �Լ���
	
	return factors; //�� ����� ���μ� ���͵��� ��ȯ��
}

void process(int caseIndex) { //caseIndex��ŭ �����ϴ� ����
	long long n; //10�� ������ �ڿ����� �����Ƿ� �� ũ�⸸ŭ ����
	scanf("%lld", &n); //n�� �Է¹���

	vector<long long> factors = factorize(n); //���μ��� ���ϴ� �Լ��� ���� ��� n�� ���� ���μ��� ���ͷ� �����Ͽ� ��ȯ��

	printf("#%d:\n", caseIndex); //caseindex�� ����� �ε����� 1���� ������
	for (int i = 0; i < factors.size(); i++) { //size��ŭ ������
		if (i > 0) 
			printf(" "); //i�� 0���� Ŀ���� �������� ��������
		printf("%lld", factors[i]); //�����
	}
	printf("\n"); //������ �ٹٲ�
}

int main() {
	int caseSize; //case������ ������ ����
	scanf("%d", &caseSize); //�Է¹���

	for (int caseIndex = 1; caseIndex <= caseSize; caseIndex++) //case�ε�����ŭ ������ 1���� ����
		process(caseIndex);
	
}
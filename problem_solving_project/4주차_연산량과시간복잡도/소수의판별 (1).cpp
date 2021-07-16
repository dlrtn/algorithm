#include <iostream>
#include <math.h>

//2���̳��� ����ؾ��Ѵٴ� ������ �־����Ƿ� ����ð��� ���̴� ����� �ʿ�

bool isPrime(int N) { //�Ϲ����� 2~N���� ����� �ִ��� ���ϴ� ����� �ԷµǴ� N�� Ŀ������ ����ð��� ���ظ� ���⶧���� math��������� sqrt�Լ� Ȱ��
	int sq; // N�� �������� ����� ����

	if (N == 1) //���� N�� 1�� ��� �ٷ� �Ҽ��� �ƴϴٰ� return
		return false;
	
	sq = (int)sqrt(N); //N�� ������ ���� sqrt�� ����

	for (int i = 2; i <= sq; i++) { //�� for���� 2���� ������ n�� ������ �����Ű�Ƿ� ���� ������� �ξ� ���� ����ð� �ʿ�
		if (N % i == 0) //���� ����� ���� ��� �ٷ� false return
			return false;
	}

	return true; //�׿ܿ��� ����� ���� ����̹Ƿ� true return
}

void testcase(int caseIndex) {
	int n; //�Ҽ����� �Ǻ��� ����
	scanf("%d", &n);// ������ �Է¹���

	bool result = isPrime(n); //isPrime�̶�� �Լ��� n�� ���� �Ҽ����� �Ǻ��ϴ� return���� ����

	printf("Case #%d\n", caseIndex); //���° ����Ǵ� �Լ������� ǥ���ϴ� ����Ʈ��
	if (result) //isPrime ���������� true�� ��� = �Ҽ��ΰ��
	{
		printf("YES\n"); // YES ���
	}
	else { //isPrime ���������� false�� ��� = �Ҽ��� �ƴѰ��
		printf("NO\n"); // NO ���
	}
}

int main() {
	int caseSize; //������ ���̽��� ������� �����ϴ� ����
	scanf("%d", &caseSize); //�Էµ� ���̽� ������ �Է¹޴� �Լ�
	for (int caseIndex = 1; caseIndex <= caseSize; caseIndex += 1) //testcase��� �Լ��� caseSize����ŭ ��������ִ� �Լ� 
	{
		testcase(caseIndex); //caseIndex�� �Ű������� �����Ű�� �Լ�
	}
	return 0;
}

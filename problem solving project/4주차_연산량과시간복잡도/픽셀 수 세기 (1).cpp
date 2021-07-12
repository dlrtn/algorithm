#include<cstdio>
#include<iostream>

using namespace std;

bool isInside(long long x, long long y, long long R) {
	long long sqd = x * x + y * y; //�Ÿ��� ����
	if (sqd < R * R)  //�������� ����
	{   
		return true;//�������� �Ÿ��� ���������� �۴ٸ�, �� �ȿ� �����Ƿ� true
	}
	return false;//�ƴϸ� false
}

void testcase(int caseIndex) {
	long long R; //�������� �� long long�̶�� �ڷ����� ����ߴ����� �𸣰ڽ��ϴ�.
	scanf("%lld", &R);

	long long sum = 0; //1��и鿡 �����ϴ� �� �ȼ��� ��
	long long y = R; //���������� �������Ƿ� R���� ����
	for (long x = 0; x <= R; x++) { // x�� 0���� ���������� ���ؾ���.
		long long height = 0; //�ʱ� ���̴� 0
		for (; y >= 0; y--) {//���� y�� �̹� �ʱⰪ�� �������־����Ƿ� ����, �������Ƿ�
			if (isInside(x, y, R)) {// ���������� �������ٰ� ���ʷ� �� �ȿ� ���Ե� ��ǥ x, y
				height = (y + 1); //����� ���̴� y+1�� �ֳ� �� ���� 1�̹Ƿ� ��
				break;
			}
		}

		sum += height; //�ʺ�� 1�̹Ƿ�
	}


	printf("#%d\n", caseIndex);
	printf("%lld\n", sum * 4); //��� ��и��� �ȼ� ��
}

int main() {
	int caseSize; //case ������ ����޴� ����
	scanf("%d", &caseSize); //�Է�
	for (int caseIndex = 1; caseIndex <= caseSize; caseIndex += 1) //caseSize��ŭ ����
	{
		testcase(caseIndex);//testcase�� index�� ���� ����
	}
	return 0;
}
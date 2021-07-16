#include <algorithm>
#include <iostream>
#include <cmath>
#include <time.h>

using namespace std;

#define MIN(x,y) (x)<(y)?(x):(y)
#define GET_MIN(x,y,z) (MIN(x, y))<(z)?(MIN(x, y)):(z)

int main() {
	int y, x;
	cin >> y >> x;
	int min = 2147483647;
	time_t start, end;
	double result;
	int** a = new int* [y]; //�̹��� B1 (����)
	int** b = new int* [y]; //�̹��� B2 (������)
	int** c = new int* [y]; //DP�� ����� Ǯ�� ���� �迭 ������� x, y�� B1, B2�� ����

	for (int i = 0; i < y; i++) //�̹��� B1�� ��⸦ a��� 2���� �迭�� �����ϱ����� �����Ҵ�
		a[i] = new int[x];
	for (int i = 0; i < y; i++) //�̹��� B2�� ��⸦ b��� 2���� �迭�� �����ϱ����� �����Ҵ�
		b[i] = new int[x];
	for (int i = 0; i < y; i++) //�̹��� (B1-B2)^2�� ���� c��� 2���� �迭�� �����ϱ����� �����Ҵ�
		c[i] = new int[x];

	for (int i = 0; i < y; i++) { //B1 �̹����� ��⸦ �޾� �ʱ�ȭ
		for (int j = 0; j < x; j++)
			cin >> a[i][j];
	}
	for (int i = 0; i < y; i++) { //B2 �̹����� ��⸦ �޾� �ʱ�ȭ
		for (int j = 0; j < x; j++)
			cin >> b[i][j];
	}
	start = time(NULL);
	//DP�� ����Ͽ� Ǯ��� �Ͽ���.
	for (int i = 0; i < y; i++) {
		for (int j = 0; j < x; j++)
			c[i][j] = (a[i][j] - b[i][j]) * (a[i][j] - b[i][j]); // a�� b�� �� ��ҿ��� ���� �����Ͽ� c�迭�� ����		
	}

	for (int i = 1; i < y; i++) { //���� Ǯ�̴� �ι�° �ٺ��� �����ϹǷ� ���� �ε����� 1�� ����
		for (int j = 0; j < x; j++) { //0���� ������ ������ ����
			if (j == 0) //���� �ȼ��� ��ġ�� ���� ������ ���, -1ĭ ���̳��� �ȼ��� ������� ����
				c[i][j] += MIN(c[i - 1][j + 1], c[i - 1][j]);
			else if ((j + 1) == x) //���� �ȼ��� ��ġ�� ���� �������� ��� +1ĭ ���̳��� �ȼ��� ������� ����
				c[i][j] += MIN(c[i - 1][j - 1], c[i - 1][j]);
			else  //������ ��쿡�� -1,0,+1 ��� ��밡����
				c[i][j] += GET_MIN(c[i - 1][j + 1], c[i - 1][j - 1], c[i - 1][j]);
		}
	}

	for (int i = 0; i < x; i++) { //���� �������ٿ��� �ּڰ��� ����ϰ� ������ ������
		if (min > c[y - 1][i])
			min = c[y - 1][i];
	}
	end = time(NULL);
	printf("%d\n", min);
	result = (double)(end - start);
	printf("����ð� : %f��", result / CLOCKS_PER_SEC);
}
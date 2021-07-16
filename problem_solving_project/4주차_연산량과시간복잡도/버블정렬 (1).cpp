#include<cstdio>
#include<iostream>

using namespace std;


void bubbleSort(int data[], int n) {
	int temp; //�� swqp�� �ӽ÷� �����س��� ����
	for (int i = n - 1; i > 0; i--) { //������ �ε������� ���ʴ�� ���� i��° �ε������� 0~i��° �ε��� ���̿��� �ִ��� �;��ϱ� ����
		for (int j = 0; j < i; j++) { //j�� 0���� i����
			if (data[j] > data[j + 1]) { //���� j�� j+1�ε������� ū���
			    temp = data[j]; //swap ����
				data[j] = data[j + 1];
				data[j + 1] = temp;
			}
		}
	}
}

int main() {
	int n;//�� �������� �迭�� �������� ������ ����
	int* data;//������ �迭

	scanf("%d", &n); //������ �Է¹���
	data = new int[n]; //�����Ҵ�

	for (int i = 0; i < n; i++) { //�迭�� �����ŭ �Է¹���
		scanf("%d", &data[i]);
	}

	bubbleSort(data, n); //������������

	for (int i = 0; i < n; i++) {//���İ�� ������ִ� �Լ�
		if (i > 0) { //ó�� �����Ҷ� ������ �ʿ� �����Ƿ�
			printf(" ");
		}
		printf("%d", data[i]); //�迭 ���
	}

	delete[] data; //�޸��Ҵ� ����
	return 0; //����
}
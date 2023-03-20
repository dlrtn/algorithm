#include<cstdio>

using namespace std;

const int MAX_TABLE_LENGTH = 10000; //��ȭ��ȣ ���ڸ��� 4�ڸ��̹Ƿ� �ִ� 9999���� ���尡��

void fillFrequencyTable(int data[], int n, int table[]) { //
	for (int i = 0; i < MAX_TABLE_LENGTH; i++) { //������ ���� ���� �ʱ�ȭ�� �Ǿ����� �����Ƿ� �ʱ�ȭ�����ִ� ����
		table[i] = 0;
	}
	for (int i = 0; i < n; i++) { 
		int number = data[i]; //number��� �Լ��� �Էµ� ��ȭ��ȣ ���� n����ŭ �ְ� 
		table[number]++;      //�ش� �ε��� table�� ���� 1�� �÷��� 
	}
}

int getFrequentNumber(int data[], int n) {
	int frequent_number = 0; //�󵵼��� �翬�� 0���� �ʱ�ȭ�Ǿ����

	int table[MAX_TABLE_LENGTH]; //���� �ʱ�ȭ�� �� �ؾߵǹǷ� �����ؾ���
	fillFrequencyTable(data, n, table); //���ڸ���ȣ���� ������ �󵵼��� �����ִ� �Լ���


	for (int i = 0; i < MAX_TABLE_LENGTH; i++) { //0~9999���� ���鼭
		if (table[i] > table[frequent_number]) { //���� ���� ���� �ε����� ��ȣ�� ������
			frequent_number = i;
		}
	}
	return frequent_number; //�׸��� �� �ε����� ���� ��������
}

int main() {
	int n; //n���� �����ϰڴٴ� ����

	scanf("%d", &n); //n�� �Է¹���
	int* data = new int[n]; //������ ���� data�� �������ڸ��� sizeof(int)*n�� ũ�⸸ŭ �����Ҵ������

	for (int i = 0; i < n; ++i) {
		scanf("%d", &data[i]); //���ڸ� ��ȣ �迭�� �Է¹���
	}

	int answer = getFrequentNumber(data, n); //frequent_number���� answer�� ������

	printf("%04d", answer); //answer�� �����, 0�� ��µǴ��� �� 04d�� �����̹Ƿ�  0000���� ��°��� ����

	delete[] data; //�����Ҵ� ����
	return 0; //��
}
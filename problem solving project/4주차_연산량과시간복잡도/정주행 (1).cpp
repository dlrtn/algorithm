#include<cstdio>
#include<iostream>

using namespace std;

bool isConsecutive(int data[], int n) { //"����"�Ǵ� ���������� ���� �˻��ϴ� �Լ� �����̹Ƿ� 1�� �����ϰų� �����Ͽ�����
	int max_data = data[0]; //�ʱⰪ�� 0��° �ε����� ����
	int min_data = data[0]; //�ʱⰪ�� 0��° �ε����� ����

	for (int i = 0; i < n; i++) { //�ε����� ������ �ε������� �湮
		if (max_data < data[i]) //max_data���� data[i]�� ũ��
			max_data = data[i];	//max_data�� data[i] ����
		if (min_data > data[i]) //min_data���� data[i]�� ������
			min_data = data[i];	//min_data�� data[i] ����
	}

	if (max_data - min_data + 1 == n) //max������ min���� ���� �� �Է��� 1,2,3,4,5�� ��� 4�� �Ǵµ� �̿� +1�� ���ָ� ������� �������Ƿ� ������ �����ϰ�
									  //�Է��� 1,2,3,4,6�� ��� 5(max-min) + 1 = 6 != n�� �ǹǷ� ������ �������� ������ �� �� �ִ�.
		return true;	
	else  //������ �������� ������� false return
		return false;
}

int main() {
	int n; ;//�� �������� �迭�� �Է¹����� ������ ����
	int* data; //�Էµ� �迭�� ������ ����

	scanf("%d", &n); //������ �Է�
	data = new int[n]; //n��ŭ �����Ҵ�
	for (int i = 0; i < n; i++) { //n��ŭ �����ؼ� �迭 �Է¹���
		scanf("%d", &data[i]);
	}

	bool result = isConsecutive(data, n); //�Էµ� �迭�� ���� ������ ǥ���� �� �ִ����� �����ϴ� �Լ� ����


	if (result) { //�����ϸ� YES���
		printf("YES");
	}
	else { //�������� ������ NO ���
		printf("NO");
	}

	delete[] data; //�޸��Ҵ� ����
	return 0; //����
}
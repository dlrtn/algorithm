#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

const int MAX_SERIAL_NUMBER = 100000;

void fillFrequencyTable(const vector<int>& data, int n, vector<int>& table) {//data[0] ~data[n - 1]�� ������ �ø��� ��ȣ�鿡 ���� �󵵼� ���̺��� ä��� �Լ�
	table.clear(); //���� �ʱ�ȭ
	table.resize(MAX_SERIAL_NUMBER + 1, 0); //��ĭ �� ũ�� ����� ������ �׸��� 0���� ä��

	for (int i = 0; i < n; ++i) { //�ش� ��ȣ�� �����ϸ� ���̺��� �� �ε����� ���� ++����
		int serial = data[i];
		table[serial]++;
	}
}

vector<int> getUniqueElements(const vector<int>& data, int n) {	//data[0] ~data[n - 1]���� �ߺ��� �������� �ʴ� ���ҵ��� ��ȯ
	vector<int> ret; //������ ���ҵ� �迭
	
	vector<int> table; //���̺� ���͸� �����ϰ�
	fillFrequencyTable(data, n, table); //data�� ���� �󵵼� ���̺��� �����

	for (int number = 1; number <= MAX_SERIAL_NUMBER; number += 1) { //������ �� �ִ� ��� �ø��� �ѹ��� ���� ���ʷ� ��ȸ
		if (table[number] == 1) { //��ü �����Ϳ��� �� ���� ������ number�� ���ʷ� ���� ����Ʈ�� �߰�
			ret.push_back(number);
		}
	}

	//�������� ������ �߰��߱� ������ ret�� ���� ������ ���ʿ��ϴ�.
	return ret;
}

int main() {
	int n;
	scanf("%d", &n); //��� �Է¹��� �� �����ϴ� ����

	vector<int> data = vector<int>(n); //���͸� �����ѵ� �̸� n�� ����� ���� int�ڷ��� �迭�� �ʱ�ȭ������
	for (int i = 0; i < n; ++i) {
		scanf("%d", &data[i]);
	}

	const vector<int> answer = getUniqueElements(data, n); //������� answer ���Ϳ� ������

	// �� ���ҵ��� ����Ѵ�.
	for (int i = 0; i < answer.size(); ++i) {
		if (i > 0) { //ù ��° ���Ұ� �ƴ϶�� �տ� ������ �ϳ� �߰��Ѵ�.
			printf(" ");
		}
		printf("%d", answer[i]);
	}

	return 0;
}
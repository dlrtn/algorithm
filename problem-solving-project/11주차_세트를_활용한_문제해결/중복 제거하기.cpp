#include <iostream>
#include <set>

using namespace std;

int main() {
	int N;
	cin >> N;

	set<int>integers;
	for (int i = 0; i < N; i++) { //N����ŭ �˻��� ���̹Ƿ�
		int X; //�� 0~N���� �˻�� ����� ����
		cin >> X;

		if (integers.find(X) != integers.end()) { //ã�� ���� �ִٸ� �ش� iterator�� ��ȯ
			printf("DUPLICATED\n");
		}
		else { //ã�� ���� ���ٸ� end() iterator�� ��ȯ
			integers.insert(X); //set�� ���� ����Ѵ�.
			printf("OK\n");
		}
	}
	return 0;
}
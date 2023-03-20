#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> getPossibleTargets(int n, int m, int* cards, int* targets) {
	vector<int> possibleTargets; // ���� �� �ִ� ��÷ ��ȣ���� �ϴ� ������

	sort(cards, cards + n); // ��� ī�带 ������������ �����Ѵ�
	

	for (int i = 0; i < m; ++i) {
		int k = targets[i]; // ��� Ÿ�� k�� ���Ͽ� ����
		bool possible = false; //�ϴ� �Ұ������� �ʱ�ȭ

		for (int j = 0; j < n; ++j) {
			int x = cards[j];  // ��� ī�� �� �ϳ��� x�� ���Ͽ�
			for (int p = 0; p <= j; p += 1) {
				int y = cards[p]; // ī�� �� �ϳ� y�� �����Ѵ�
				int z = k - (x + y); // k = (x +  y )+ z �� �Ǵ� z�� ����Ѵ�
								
				if (binary_search(cards, cards + n, z) == true) { // z�� cards[]�� �����Ѵٸ�?
					// k = x + y + z �� ������ <x, y, z>�� �����Ѵ�.
					possible = true;
					break;
				}
			}
			if (possible)// �̹� ã�Ҵٸ� Ż���Ѵ�    
				break;
			

		}

		if (possible)// �� ī���� ������ k�� ���� �� �ִٸ�, �߰��Ѵ�.
			possibleTargets.push_back(k);		
	}

	sort(possibleTargets.begin(), possibleTargets.end()); //�������ذ��� �����ϱ� ���� ����
	return possibleTargets;
}

int main() {
	int n;    // ī���� ��
	int m;    // �˻� �� �ĺ� ��÷��ȣ�� ��
	scanf("%d %d", &n, &m); 

	int* cards = new int[n]; //�����Ҵ���
	int* targets = new int[m]; //���� ����

	
	for (int i = 0; i < n; i++) { // �� ī�� ������ �Է¹޴´�
		scanf("%d", &cards[i]);
	}
		
	for (int i = 0; i < m; i++) { // �� �ĺ� ��÷��ȣ�� �Է¹޴´�
		scanf("%d", &targets[i]);
	}

	vector<int> answers = getPossibleTargets(n, m, cards, targets);

	if (answers.size() == 0) {    // ������ ��÷��ȣ�� ���ٸ� NO�� ����Ѵ�
		printf("NO");
	}
	else { //������ ��÷��ȣ�� �����Ѵٸ� �� ����� ����Ѵ�.
		for (int i = 0; i < answers.size(); i++) {
			if (i > 0) {
				printf(" ");
			}
			printf("%d", answers[i]);
		}
	}

	delete[] cards;
	delete[] targets;

	return 0;
}
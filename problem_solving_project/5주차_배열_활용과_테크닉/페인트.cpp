#include <cstdio>
#include <vector>

using namespace std;

const int MAX_SEAT_NUMBER = 1000;
const int MAX_COLOR_NUMBER = 100;

//�¼����� �� �� ��ĥ�ϴ� �̺�Ʈ�� ���� ����
class Painting {
public:
	int left;
	int right;
	int color;

	Painting() {}

	Painting(int left, int right, int color) { //�¼��� ���� ��ĥ�� ������ ��(��) ��ĥ�� ������(��)�� �����ϴ� ������ �ʱ�ȭ��Ű�� �Լ�
		this->left = left; 
		this->right = right;
		this->color = color;
	}
};

void fillFrequencyTable(int data[], int n, int table[]) {
	for (int i = 0; i < MAX_COLOR_NUMBER; ++i) { //0���� �������� �÷� ��ȣ��ŭ ���̺��� �ʱ�ȭ��Ŵ
		table[i] = 0;
	}
	for (int i = 0; i < n; ++i) { //data�� i��° �ε����� ������ ���� �ش� ���� ĥ���� �󵵸� ����
		int color = data[i];
		table[color]++;
	}
}

void solve(int n, int m, const Painting* paintings) {
	int* seats = new int[n];
	for (int i = 0; i < n; i++) {    // ó�� �¼��� ���� 0�� ������ ĥ���� ����
		seats[i] = 0;
	}
		
	for (int i = 0; i < m; ++i) { //��ĥ �������� �־��� ������� �� �¼��� ��ĥ��
		const Painting& p = paintings[i]; //��� ��ĥ ���� p�� ���Ͽ� ���ʷ� ó��
				
		for (int j = p.left; j <= p.right; ++j) { // �� ������ �������� �¼��� ���� ������Ʈ ����
			seats[j] = p.color;
		}
	}
	int* table = new int[MAX_COLOR_NUMBER]; //��� ��ĥ�� �Ϸ��� ������ ���� ������ ����Ͽ�
	fillFrequencyTable(seats, n, table);    //��� ���� ���� �󵵼� ���̺��� �����

	int minColor = seats[0]; //���� ���� ������ ����
	int maxColor = seats[0]; //���� ���� ������ ����

	for (int color = 0; color <= 99; color += 1) { //0���� 99������ ������
		if (table[color] == 0) { //�� �� �̻� ������ ��� ���� color�� ���Ͽ�
			continue;
		}
		
		if (table[minColor] > table[color]) { //���� ���� ������ ���� ���� ���ų�, color�� �� ���� ������ ���
			minColor = color;
		}
		if (table[maxColor] < table[color]) { //���� ���� ������ ���� ���� ���ų�, color�� �� ���� ������ ���
			maxColor = color;
		}
	}

	printf("%d\n", maxColor); //���� ���� �����ѻ� ���
	printf("%d\n", minColor); //���� ���� �����ѻ� ���

	delete[] table; //�����Ҵ�����
}

int main() {
	int n, m; //n�� �¼��� ��, m�� ��ĥ�� ������ ���
	scanf("%d %d", &n, &m);

	// paintings[i] := i��°�� �Ͼ ��ĥ �̺�Ʈ�� ����
	Painting* paintings = new Painting[n];

	for (int i = 0; i < m; ++i) {
		scanf("%d", &paintings[i].left); //�ʱ�ȭ��Ű�� ���� ������ �Է¹���
		scanf("%d", &paintings[i].right);
		scanf("%d", &paintings[i].color);

		// �¼��� ��ȣ�� 1������ �����ϹǷ�, 0 ~ (n-1)������ ���߱� ���Ͽ� 1�� ���ش�
		paintings[i].left -= 1;
		paintings[i].right -= 1;
	}

	// ������ ������ ���Ѵ�
	solve(n, m, paintings);

	return 0;
}
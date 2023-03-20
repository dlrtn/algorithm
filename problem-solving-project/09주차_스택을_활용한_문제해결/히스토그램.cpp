#include <iostream>
#include <vector>
#include <stack>
#include <cmath>
#include <algorithm>

using namespace std;

class Histogram {
public:
	int height;    // ������׷��� ����
	int leftX;     // �ε��� Ȥ�� ������׷��� ���� ���� x ��ǥ
	int rightX;    // ������׷��� ������ ���� x��ǥ

	Histogram() { } //������ 1

	Histogram(int index, int height) { //������ 2
		this->leftX = index; 
		this->rightX = this->leftX + 1;   // �� ������׷��� �ʺ� 1�̹Ƿ�
		this->height = height;
	}

};

long long getLargestRectangleArea(const vector<Histogram>& histograms) {
	long long answer = 0;    // �ִ� ���簢���� ����

	stack<Histogram> continuedHistograms; // ���� �������� Ȯ�� ���ɼ��� �ִ� ������׷���

	
	continuedHistograms.push(Histogram(-1, 0)); // ������ ���Ǹ� ���� ���� ���ʿ� ���� 0���� ������ ������׷� �߰�
	for (int i = 0; i < histograms.size() + 1; i++) { // ���ʺ��� ������ ������׷����� ���ʷ�
		Histogram h;
		if (i < histograms.size()) {
			h = histograms[i];
		}
		else {
			// if ( i == n )
			// ������ ���Ǹ� ���� ���� �����ʿ� ���� 0���� ������ ������׷� �߰�
			h = Histogram(histograms.size(), 0);
		}

		// ������ Ȯ�����̴� ������׷��� ��, h���� ���̰� ���� ������׷����� �� �̻� Ȯ��� �� ���� => �ִ� ���̰� ����
		while (continuedHistograms.size() > 1
			&& continuedHistograms.top().height >= h.height) {
			// Ȯ�����̴� ������׷�
			Histogram lh = continuedHistograms.top();
			continuedHistograms.pop();

			// �� ������ ������׷� (���� Ȯ���� ��)
			Histogram bh = continuedHistograms.top();

			// ���� �߰��� h�� �ٷ� ���ʱ��� Ȯ��
			long long width = abs(h.leftX - bh.rightX);
			long long height = lh.height;
			long long area = width * height;

			// �ִ� �� ����
			answer = max(answer, area);
		}

		// h�� ������ �߰�
		continuedHistograms.push(h);
	}

	return answer; //answer ��ȯ
}

void process(int caseIndex) {
	int n;
	cin >> n; //n�� �Է¹���

	vector<Histogram> histograms;
	for (int i = 0; i < n; i++) { //n����ŭ �����ϰ�
		int height;
		cin >> height; //�� i���� ���̸� �Է¹޾�
		histograms.push_back(Histogram(i, height)); //�����ڷ� �����Ͽ� ���͹迭�� �־���
	}

	long long answer = getLargestRectangleArea(histograms); //���͹迭�� ������ ���� ����ؼ�
	cout << answer << endl; //������ְ� ����
}

int main() {
	int caseSize;
	cin >> caseSize; //caseSize�� �Է¹ް�

	for (int caseIndex = 1; caseIndex <= caseSize; caseIndex += 1) {
		process(caseIndex); //caseSize��ŭ �����ϰ� ������
	}
}
#include <iostream>
#include <queue>
#include <vector>
#include <functional>
#include <algorithm>

using namespace std;

class City {
public:
	int index;     // ������ �ε���
	int income;    // �ش� ������ �ҵ�

	City(int index, int income) { //������
		this->index = index;
		this->income = income;
	}

	bool operator < (const City& o) const { //Ŭ���� ���� ���Լ�
		return this->income < o.income;
	}
	bool operator > (const City& o) const { //Ŭ���� ���� ���Լ�
		return this->income > o.income;
	}
};

int getMaximumRangeDifference(int n, int k, const vector<City>& cities) {
	int answer = 0;
	
	priority_queue<City, vector<City>, greater<City>> rangeMinimum; // �ҵ��� ���� ���� ���ú��� pop�Ǵ� �켱���� ť
		
	priority_queue<City> rangeMaximum; // �ҵ��� ���� ���� ���ú��� pop�Ǵ� �켱���� ť

	for (int i = 0; i < k - 1; i++) { //���� �켱���� ���� ť�� ������� ����
		rangeMaximum.push(cities[i]); //k = 3�ϰ�� 2������ �Է�
		rangeMinimum.push(cities[i]); 
	}
	for (int i = k - 1; i < n; i++) { //k-1 �ε������� ���� ����
		rangeMaximum.push(cities[i]); //�� ���� �߰��Ͽ� �� ������ k�� ���� �� �۾� ����
		rangeMinimum.push(cities[i]); 
		while (rangeMaximum.top().index < i - k + 1) rangeMaximum.pop(); //������ K���� �����ֱ� ���� pop�ϴ� ����
		while (rangeMinimum.top().index < i - k + 1) rangeMinimum.pop(); //
		answer = max(answer, rangeMaximum.top().income - rangeMinimum.top().income); //���� �ȿ��� �ִ� �ҵ�� �ּ� �ҵ��� ����, answer�� �������� ���ؼ� �� Ŭ��� ����
	}

	return answer;
}

void process(int caseIndex) {
	int n, k;
	cin >> n >> k; //n, k�� �Է¹ް�
	vector<City> cities; //���͸� ������ ��

	for (int i = 0; i < n; i += 1) { //�� ���ø��� �ҵ������ �Է¹��� 
		int income;
		cin >> income;
		cities.push_back(City(i, income));
	}

	int answer = getMaximumRangeDifference(n, k, cities);  //

	cout << answer << endl; //���� ����ϰ� �ٹٲ�
}

int main() {
	int caseSize;
	cin >> caseSize;

	for (int caseIndex = 1; caseIndex <= caseSize; caseIndex += 1) { //�Էµ� ���̽�������ŭ �����ϰ� ����
		process(caseIndex);
	}
}
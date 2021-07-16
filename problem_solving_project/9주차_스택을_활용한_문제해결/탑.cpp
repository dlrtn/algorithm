#include <iostream>
#include <vector>
#include <stack>

using namespace std;

class Tower {
public:
	int index; // Ÿ���� �ε���
	int height; // Ÿ���� ����
	int targetTowerIndex;  // �� Ÿ���� �������� �����ϴ� ��� Ÿ��

	Tower(int index, int height) { //������ �Լ�
		this->index = index;
		this->height = height;
		this->targetTowerIndex = 0;
	}

	void setTargetTowerIndex(int targetTowerIndex) { //targetTowerIndex �ʱ�ȭ �Լ�
		this->targetTowerIndex = targetTowerIndex;
	}

	int getTargetTowerIndex() { //targetTowerIndex�� �����ϴ� �Լ��Ͽ� ��ȯ���ִ� �Լ�
		return this->targetTowerIndex;
	}
};

void findTargetTowers(vector<Tower>& towers) {
	
	stack<Tower> touchableTowers; // ���� �ٸ� Ÿ���� ��ȣ�� ������ ���ɼ��� �ִ� Ÿ����


	for (int i = 0; i < towers.size(); i++) {
		Tower& t = towers[i];    // �� Ÿ�� t�� ���� ���ʷ� ���
		int targetTowerIndex = 0;   // Ÿ�� t�� ��ȣ�� ������ �ĺ� ( �ʱⰪ null )

		while (touchableTowers.empty() == false	&& touchableTowers.top().height < t.height) { // t���� ���̰� ���� Ÿ������ ���Ŀ��� ���� ���ɼ��� �����Ƿ� ����
			
			touchableTowers.pop();
		}

		
		if (touchableTowers.size() > 0) { // t �̻��� ���̸� ���� Ÿ���� �����ִ� ��� 	 
			targetTowerIndex = touchableTowers.top().index; // t�� �ش� Ÿ���� Ÿ������ ����	
		}
		
		t.setTargetTowerIndex(targetTowerIndex); // ����� Ÿ�� ������ ����

		touchableTowers.push(t); // t�� �������� ���������Ƿ� �ٸ� Ÿ���� ��ȣ�� ������ �� �����Ƿ� �������
	}
}

int main() {
	int n;
	cin >> n;

	vector<Tower> towers; //Tower ���͹迭�� ������� ����
	for (int i = 0; i < n; ++i) {
		int hi;
		cin >> hi;
		towers.push_back(Tower(i + 1, hi)); // �ε��� 1���� ����
	}

	
	findTargetTowers(towers); // �� Ÿ���� �۽��ϴ� �������� ���� Ÿ���� ��� ���

	for (int i = 0; i < n; i++) { //������ְ� ������
		if (i > 0) {
			cout << " "; //���⸦ ����
		}

		Tower t = towers[i];
		int targetIndex = t.getTargetTowerIndex();
		cout << targetIndex;
	}
}
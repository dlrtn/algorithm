#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int main() {
	int N;
	cin >> N;
	
	vector<string> curMaxFreqName; // ������� �ִٵ�ǥ�� �ĺ����� ���
	map<string, int> frequencyMap; // �� �ĺ� �̸��� ��ǥ ���� �����ϴ� key-value Map

	int maxFrequency = 0; // ���� ���� ��ǥ��

  
  
	for (int i = 0; i < N; i++) { //�� �̸����ϳ��߰��ɶ����� ��������� �ִ� Ưǥ �� ����, �ִ� ��ǥ �ĺ� ����Ʈ�� ����, vector�� clear�޼ҵ�� O(1)��
		string st;
		cin >> st; //�ĺ��� �̸��� �Է¹ް�
		frequencyMap[st]++; //�ĺ��� �̸����� �� Ű ����� ++
		int k = frequencyMap[st]; //k���� �ش� Ű ������� �־ �ִ����� �ƴ����� ���ϴ� �κ�
		if (k > maxFrequency) { //���� ���� ������ ��쿡��
			maxFrequency = k; //�ִٺ󵵼��� ���Ž����ְ�
			curMaxFreqName.clear(); //�ִٵ����� �ĺ��� �̸�ĭ�� �ʱ�ȭ�����ص�
			curMaxFreqName.push_back(st); //���� �Է¹��� �ĺ��� �̸��� �־���
		}
		else if (k == maxFrequency)  //�ִ� �󵵼��� ������ ��쿡��
			curMaxFreqName.push_back(st); //�ʱ�ȭ���� �ʰ� �־���
		
	}
		
	cout << maxFrequency << endl; // �ִ� ��ǥ �ĺ� ���� ���

	sort(curMaxFreqName.begin(), curMaxFreqName.end());// �ִ� ��ǥ���� ���� �ĺ��� �̸��� ���������� ���
	bool first = true;
	for (auto i : curMaxFreqName) {
		if (first == false) {
			cout << ' ';
		}
		first = false;
		cout << i;
	}
}
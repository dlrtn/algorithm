#include<stdio.h>
#include<map>
using namespace std;

int main() {
	
	int N; 
	scanf("%d", &N); //CaseSize�� �Է¹���

	map<int, int> frequencyMap; //�󵵼� Map ���� ����, 

	for (int i = 0; i < N; i++) {
		int X; //�Է��� ������ ����
		scanf("%d", &X); 
		frequencyMap[X]++; //������ ���� ���� ++��Ŵ
		printf("%d %d\n", frequencyMap.size(), frequencyMap[X]);//���� ����� ������ ������ size�� ���ؼ� ���� ���� �� �ְ�, �Էµ� X�� ++�Ͽ� �󵵼��� �����Ͽ����Ƿ� �̸� ����ϸ� �󵵼��� ���� ���� �� �ִ�.
	}

	return 0;
}
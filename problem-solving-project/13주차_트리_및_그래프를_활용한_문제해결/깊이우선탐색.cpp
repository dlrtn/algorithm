#include <iostream>

using namespace std;

int maps[10][10];
int visited[10] = { 0 };
int num;
void init() { //���� ���� �ʱ�ȭ�����ִ� �Լ�
	for (int i = 0; i < 10; i++) 
		for (int j = 0; j < 10; j++)
			maps[i][j] = 0; //0���� �ʱ�ȭ
}

void dfs(int v)
{
	cout << v << endl;
	visited[v] = 0; //�湮�� ���� 0���� �ʱ�ȭ
	for (int i = 0; i <= num; i++) { //�׸��� �湮���� ���������� ���ʴ�� dfs ����Լ�
		if (maps[v][i] && visited[i])
			dfs(i);
	}
}

int main(void) {
	int v1, v2; 
	init();
	cin >> num; //������ ������ �Է¹���
	for (int i = 0; i < num; i++) { //������ ������ŭ �Է¹ް�
		cin >> v1 >> v2; //�� ������ ������ ������ �Է�
		maps[v1][v2] = maps[v2][v1] = 1; //�ΰ��� ���� �ʱ�ȭ�����־���� ����Ǿ��ִٰ� ��Ÿ���Բ�
		visited[v1] = visited[v2] = 1; //�湮�ؾ��ϴ� ���� 1�� �ʱ�ȭ
	}
	dfs(1);//�������� 1�� dfs ����

	return 0;
}
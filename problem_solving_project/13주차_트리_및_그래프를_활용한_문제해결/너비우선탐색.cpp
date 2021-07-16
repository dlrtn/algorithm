#include <iostream>
#include <queue>
using namespace std;

int map[10][10];
int visit[10] = { 0 };
queue<int> q;
int num, edge_num;

void bfs(int v)
{
	cout << v << '\n';
	q.push(v);
	while (!q.empty()) { //q�� ������ ������쿡 ����
		int node = q.front();//node�� ���� �տ� �ִ� q�� ��尪�� �־��ְ�
		q.pop(); //�� q���� �� ��带 ����
		for (int i = 0; i < num; i++) { //���� ������ŭ ���ƾ��ϹǷ�
			if (map[node][i] == 1 && visit[i] == 0) { //���� ���� 0~num-1��带 ��ȸ�ϸ鼭 �湮���� ���� ���� ã��
				visit[node] = 1; //�湮�ϰ�
				cout << i << '\n'; //�湮�ߴٴ� ǥ��
				q.push(i); //�׸��� �� �湮�� ��带 ť�� �־���
			}
		}
	}
}

int main(void) {
	cin >> num >> edge_num; // ����� ������ ������ ���� �Է¹���
	for (int i = 0; i < edge_num; i++) { //������ ������ŭ �Է¹��� 
		int v1, v2; //����, ����
		cin >> v1 >> v2; //�Է�
		map[v1][v2] = map[v2][v1] = 1; //����Ǿ����� �˷��ְԲ� 1�� ǥ��
		
	}
	bfs(1); //�������� 1�� bfs ����
	return 0;
}
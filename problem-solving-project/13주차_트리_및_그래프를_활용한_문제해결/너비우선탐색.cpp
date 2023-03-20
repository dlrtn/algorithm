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
	while (!q.empty()) { //q에 남은게 있을경우에 진행
		int node = q.front();//node에 가장 앞에 있는 q의 노드값을 넣어주고
		q.pop(); //그 q에서 그 노드를 빼줌
		for (int i = 0; i < num; i++) { //간선 갯수만큼 돌아야하므로
			if (map[node][i] == 1 && visit[i] == 0) { //현재 노드와 0~num-1노드를 순회하면서 방문하지 않은 곳을 찾아
				visit[node] = 1; //방문하고
				cout << i << '\n'; //방문했다는 표시
				q.push(i); //그리고 그 방문한 노드를 큐에 넣어줌
			}
		}
	}
}

int main(void) {
	cin >> num >> edge_num; // 노드의 갯수와 간선의 갯수 입력받음
	for (int i = 0; i < edge_num; i++) { //간선의 갯수만큼 입력받음 
		int v1, v2; //시작, 종점
		cin >> v1 >> v2; //입력
		map[v1][v2] = map[v2][v1] = 1; //연결되었음을 알려주게끔 1로 표시
		
	}
	bfs(1); //시작점이 1로 bfs 시작
	return 0;
}
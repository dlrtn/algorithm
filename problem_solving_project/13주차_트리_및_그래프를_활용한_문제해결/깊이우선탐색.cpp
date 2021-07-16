#include <iostream>

using namespace std;

int maps[10][10];
int visited[10] = { 0 };
int num;
void init() { //기존 맵을 초기화시켜주는 함수
	for (int i = 0; i < 10; i++) 
		for (int j = 0; j < 10; j++)
			maps[i][j] = 0; //0으로 초기화
}

void dfs(int v)
{
	cout << v << endl;
	visited[v] = 0; //방문한 곳은 0으로 초기화
	for (int i = 0; i <= num; i++) { //그리고 방문하지 않은곳부터 차례대로 dfs 재귀함수
		if (maps[v][i] && visited[i])
			dfs(i);
	}
}

int main(void) {
	int v1, v2; 
	init();
	cin >> num; //간선의 갯수를 입력받음
	for (int i = 0; i < num; i++) { //간선의 갯수만큼 입력받고
		cin >> v1 >> v2; //각 간선의 시작점 종점을 입력
		maps[v1][v2] = maps[v2][v1] = 1; //두가지 맵을 초기화시켜주어야함 연결되어있다고 나타나게끔
		visited[v1] = visited[v2] = 1; //방문해야하는 곳은 1로 초기화
	}
	dfs(1);//시작점이 1인 dfs 시작

	return 0;
}
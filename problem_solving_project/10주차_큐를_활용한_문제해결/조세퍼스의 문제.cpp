#include <cstdio>
#include <iostream>
#include <vector>
#include <queue>

using namespace std;


class Player { //Player라는 클래스 생성 내부변수는 index만
public:
	int index;

	Player(int index = 0) { //초기화 시킬때 사용하는 함수
		this->index = index;
	}
};

vector<Player> getDeadPlayersList(int n, int m, const vector<Player>& players) {
	
	vector<Player> deadPlayers; // 현재 게임에서 제외된 플레이어들의 리스트
		
	queue<Player> playerQueue; // 아직 게임에서 제외되지 않는 플레이어들의 리스트

	for (int i = 0; i < n; i += 1) { //각 플레이어들을 playerQueue에 삽입함
		playerQueue.push(players[i]);
	}

	for (int i = 0; i < n; i++) {
		int jump = 1 + (m - 1) % playerQueue.size();  // (m-1)명의 사람을 건너뛴다.		
		for (int j = 0; j < jump - 1; j += 1) {
			Player p = playerQueue.front();
			playerQueue.pop();
			playerQueue.push(p);
		}
				
		Player dead = playerQueue.front(); // m번째 사람은 게임에서 제외한다.
		playerQueue.pop();
		deadPlayers.push_back(dead); // 제외 리스트에 추가한다.
	}


	return deadPlayers;
}

void testcase(int caseIndex) {
	int n, m;
	scanf("%d %d", &n, &m);

	vector<Player> players;
	for (int i = 0; i < n; i++) {
		players.push_back(Player(i + 1));//players라는 player클랙스 벡터에 각각 플레이어들의 인덱스를 넣어줌.
	}

	vector<Player> deadPlayers = getDeadPlayersList(n, m, players); //함수를 작동시켜 제외된 순서대로 저장함.

	for (int i = 0; i < n; i++) {
		if (i > 0) {
			printf(" "); //출력 시 공백을 위해
		}

		Player p = deadPlayers[i]; //i번째로 제외된 플레이어를 p에 저장하고
		printf("%d", p.index); //해당 p의 인덱스를 출력해줌
	}
	printf("\n"); //작동이 끝나면 종료함.
}

int main() {
	int caseSize;
	scanf("%d", &caseSize);

	for (int caseIndex = 1; caseIndex <= caseSize; caseIndex += 1) {
		testcase(caseIndex); //각 케이스마다 역할 수행
	}

	return 0;
}
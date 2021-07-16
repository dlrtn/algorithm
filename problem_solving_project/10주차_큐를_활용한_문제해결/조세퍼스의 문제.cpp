#include <cstdio>
#include <iostream>
#include <vector>
#include <queue>

using namespace std;


class Player { //Player��� Ŭ���� ���� ���κ����� index��
public:
	int index;

	Player(int index = 0) { //�ʱ�ȭ ��ų�� ����ϴ� �Լ�
		this->index = index;
	}
};

vector<Player> getDeadPlayersList(int n, int m, const vector<Player>& players) {
	
	vector<Player> deadPlayers; // ���� ���ӿ��� ���ܵ� �÷��̾���� ����Ʈ
		
	queue<Player> playerQueue; // ���� ���ӿ��� ���ܵ��� �ʴ� �÷��̾���� ����Ʈ

	for (int i = 0; i < n; i += 1) { //�� �÷��̾���� playerQueue�� ������
		playerQueue.push(players[i]);
	}

	for (int i = 0; i < n; i++) {
		int jump = 1 + (m - 1) % playerQueue.size();  // (m-1)���� ����� �ǳʶڴ�.		
		for (int j = 0; j < jump - 1; j += 1) {
			Player p = playerQueue.front();
			playerQueue.pop();
			playerQueue.push(p);
		}
				
		Player dead = playerQueue.front(); // m��° ����� ���ӿ��� �����Ѵ�.
		playerQueue.pop();
		deadPlayers.push_back(dead); // ���� ����Ʈ�� �߰��Ѵ�.
	}


	return deadPlayers;
}

void testcase(int caseIndex) {
	int n, m;
	scanf("%d %d", &n, &m);

	vector<Player> players;
	for (int i = 0; i < n; i++) {
		players.push_back(Player(i + 1));//players��� playerŬ���� ���Ϳ� ���� �÷��̾���� �ε����� �־���.
	}

	vector<Player> deadPlayers = getDeadPlayersList(n, m, players); //�Լ��� �۵����� ���ܵ� ������� ������.

	for (int i = 0; i < n; i++) {
		if (i > 0) {
			printf(" "); //��� �� ������ ����
		}

		Player p = deadPlayers[i]; //i��°�� ���ܵ� �÷��̾ p�� �����ϰ�
		printf("%d", p.index); //�ش� p�� �ε����� �������
	}
	printf("\n"); //�۵��� ������ ������.
}

int main() {
	int caseSize;
	scanf("%d", &caseSize);

	for (int caseIndex = 1; caseIndex <= caseSize; caseIndex += 1) {
		testcase(caseIndex); //�� ���̽����� ���� ����
	}

	return 0;
}
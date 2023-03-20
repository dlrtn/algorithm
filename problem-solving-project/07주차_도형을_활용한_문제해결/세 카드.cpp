#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> getPossibleTargets(int n, int m, int* cards, int* targets) {
	vector<int> possibleTargets; // 만들 수 있는 당첨 번호들을 일단 선언함

	sort(cards, cards + n); // 모든 카드를 오름차순으로 정렬한다
	

	for (int i = 0; i < m; ++i) {
		int k = targets[i]; // 모든 타겟 k에 대하여 실행
		bool possible = false; //일단 불가능으로 초기화

		for (int j = 0; j < n; ++j) {
			int x = cards[j];  // 모든 카드 중 하나인 x에 대하여
			for (int p = 0; p <= j; p += 1) {
				int y = cards[p]; // 카드 중 하나 y를 선택한다
				int z = k - (x + y); // k = (x +  y )+ z 가 되는 z를 계산한다
								
				if (binary_search(cards, cards + n, z) == true) { // z가 cards[]에 존재한다면?
					// k = x + y + z 가 가능한 <x, y, z>가 존재한다.
					possible = true;
					break;
				}
			}
			if (possible)// 이미 찾았다면 탈출한다    
				break;
			

		}

		if (possible)// 세 카드의 합으로 k를 만들 수 있다면, 추가한다.
			possibleTargets.push_back(k);		
	}

	sort(possibleTargets.begin(), possibleTargets.end()); //정렬해준것을 리턴하기 위해 정렬
	return possibleTargets;
}

int main() {
	int n;    // 카드의 수
	int m;    // 검사 할 후보 당첨번호의 수
	scanf("%d %d", &n, &m); 

	int* cards = new int[n]; //동적할당함
	int* targets = new int[m]; //위와 동일

	
	for (int i = 0; i < n; i++) { // 각 카드 정보를 입력받는다
		scanf("%d", &cards[i]);
	}
		
	for (int i = 0; i < m; i++) { // 각 후보 당첨번호를 입력받는다
		scanf("%d", &targets[i]);
	}

	vector<int> answers = getPossibleTargets(n, m, cards, targets);

	if (answers.size() == 0) {    // 가능한 당첨번호가 없다면 NO를 출력한다
		printf("NO");
	}
	else { //가능한 당첨번호가 존재한다면 그 목록을 출력한다.
		for (int i = 0; i < answers.size(); i++) {
			if (i > 0) {
				printf(" ");
			}
			printf("%d", answers[i]);
		}
	}

	delete[] cards;
	delete[] targets;

	return 0;
}
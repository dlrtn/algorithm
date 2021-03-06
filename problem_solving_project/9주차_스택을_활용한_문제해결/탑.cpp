#include <iostream>
#include <vector>
#include <stack>

using namespace std;

class Tower {
public:
	int index; // 타워의 인덱스
	int height; // 타워의 높이
	int targetTowerIndex;  // 이 타워의 레이저를 수신하는 대상 타워

	Tower(int index, int height) { //생성자 함수
		this->index = index;
		this->height = height;
		this->targetTowerIndex = 0;
	}

	void setTargetTowerIndex(int targetTowerIndex) { //targetTowerIndex 초기화 함수
		this->targetTowerIndex = targetTowerIndex;
	}

	int getTargetTowerIndex() { //targetTowerIndex에 접근하는 함수하여 반환해주는 함수
		return this->targetTowerIndex;
	}
};

void findTargetTowers(vector<Tower>& towers) {
	
	stack<Tower> touchableTowers; // 현재 다른 타워의 신호를 수신할 가능성이 있는 타워들


	for (int i = 0; i < towers.size(); i++) {
		Tower& t = towers[i];    // 각 타워 t에 대해 차례로 고려
		int targetTowerIndex = 0;   // 타워 t의 신호를 수신할 후보 ( 초기값 null )

		while (touchableTowers.empty() == false	&& touchableTowers.top().height < t.height) { // t보다 높이가 낮은 타워들은 이후에도 수신 가능성이 없으므로 제거
			
			touchableTowers.pop();
		}

		
		if (touchableTowers.size() > 0) { // t 이상의 높이를 가진 타워가 남아있는 경우 	 
			targetTowerIndex = touchableTowers.top().index; // t는 해당 타워를 타겟으로 정함	
		}
		
		t.setTargetTowerIndex(targetTowerIndex); // 계산한 타겟 정보를 저장

		touchableTowers.push(t); // t는 마지막에 등장했으므로 다른 타워의 신호를 수신할 수 있으므로 등록해줌
	}
}

int main() {
	int n;
	cin >> n;

	vector<Tower> towers; //Tower 벡터배열을 저장받을 변수
	for (int i = 0; i < n; ++i) {
		int hi;
		cin >> hi;
		towers.push_back(Tower(i + 1, hi)); // 인덱스 1부터 저장
	}

	
	findTargetTowers(towers); // 각 타워가 송신하는 레이저에 대해 타겟을 모두 계산

	for (int i = 0; i < n; i++) { //출력해주고 종료함
		if (i > 0) {
			cout << " "; //띄어쓰기를 위해
		}

		Tower t = towers[i];
		int targetIndex = t.getTargetTowerIndex();
		cout << targetIndex;
	}
}
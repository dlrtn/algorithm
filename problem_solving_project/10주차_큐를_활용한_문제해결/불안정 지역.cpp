#include <iostream>
#include <queue>
#include <vector>
#include <functional>
#include <algorithm>

using namespace std;

class City {
public:
	int index;     // 도시의 인덱스
	int income;    // 해당 도시의 소득

	City(int index, int income) { //생성자
		this->index = index;
		this->income = income;
	}

	bool operator < (const City& o) const { //클래스 내의 비교함수
		return this->income < o.income;
	}
	bool operator > (const City& o) const { //클래스 내의 비교함수
		return this->income > o.income;
	}
};

int getMaximumRangeDifference(int n, int k, const vector<City>& cities) {
	int answer = 0;
	
	priority_queue<City, vector<City>, greater<City>> rangeMinimum; // 소득이 가장 작은 도시부터 pop되는 우선순위 큐
		
	priority_queue<City> rangeMaximum; // 소득이 가장 높은 도시부터 pop되는 우선순위 큐

	for (int i = 0; i < k - 1; i++) { //각각 우선순위 들의 큐에 순서대로 삽입
		rangeMaximum.push(cities[i]); //k = 3일경우 2개까지 입력
		rangeMinimum.push(cities[i]); 
	}
	for (int i = k - 1; i < n; i++) { //k-1 인덱스부터 실행 시작
		rangeMaximum.push(cities[i]); //한 개씩 추가하여 총 갯수를 k를 만든 후 작업 수행
		rangeMinimum.push(cities[i]); 
		while (rangeMaximum.top().index < i - k + 1) rangeMaximum.pop(); //범위를 K개로 맞춰주기 위해 pop하는 과정
		while (rangeMinimum.top().index < i - k + 1) rangeMinimum.pop(); //
		answer = max(answer, rangeMaximum.top().income - rangeMinimum.top().income); //범위 안에서 최대 소득과 최소 소득을 빼줌, answer의 기존값과 비교해서 더 클경우 저장
	}

	return answer;
}

void process(int caseIndex) {
	int n, k;
	cin >> n >> k; //n, k를 입력받고
	vector<City> cities; //벡터를 선언한 뒤

	for (int i = 0; i < n; i += 1) { //각 도시마다 소득수준을 입력받음 
		int income;
		cin >> income;
		cities.push_back(City(i, income));
	}

	int answer = getMaximumRangeDifference(n, k, cities);  //

	cout << answer << endl; //답을 출력하고 줄바꿈
}

int main() {
	int caseSize;
	cin >> caseSize;

	for (int caseIndex = 1; caseIndex <= caseSize; caseIndex += 1) { //입력된 케이스갯수만큼 실행하고 종료
		process(caseIndex);
	}
}
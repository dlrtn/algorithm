#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int main() {
	int N;
	cin >> N;
	
	vector<string> curMaxFreqName; // 현재까지 최다득표한 후보들의 목록
	map<string, int> frequencyMap; // 각 후보 이름과 득표 수를 저장하는 key-value Map

	int maxFrequency = 0; // 가장 많은 득표수

  
  
	for (int i = 0; i < N; i++) { //각 이름이하나추가될때마다 현재까지의 최다 특표 값 갱신, 최다 득표 후보 리스트를 갱신, vector의 clear메소드는 O(1)임
		string st;
		cin >> st; //후보의 이름을 입력받고
		frequencyMap[st]++; //후보의 이름으로 된 키 밸류를 ++
		int k = frequencyMap[st]; //k에는 해당 키 밸류값을 넣어서 최다인지 아닌지를 비교하는 부분
		if (k > maxFrequency) { //가장 많이 나왔을 경우에는
			maxFrequency = k; //최다빈도수를 갱신시켜주고
			curMaxFreqName.clear(); //최다등장한 후보의 이름칸을 초기화시켜준뒤
			curMaxFreqName.push_back(st); //현재 입력받은 후보의 이름을 넣어줌
		}
		else if (k == maxFrequency)  //최다 빈도수와 동일할 경우에는
			curMaxFreqName.push_back(st); //초기화하지 않고 넣어줌
		
	}
		
	cout << maxFrequency << endl; // 최대 득표 후보 수를 출력

	sort(curMaxFreqName.begin(), curMaxFreqName.end());// 최대 득표를한 동점 후보들 이름을 사전순으로 출력
	bool first = true;
	for (auto i : curMaxFreqName) {
		if (first == false) {
			cout << ' ';
		}
		first = false;
		cout << i;
	}
}
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

const int MAX_SERIAL_NUMBER = 100000;

void fillFrequencyTable(const vector<int>& data, int n, vector<int>& table) {//data[0] ~data[n - 1]에 등장한 시리얼 번호들에 대한 빈도수 테이블을 채우는 함수
	table.clear(); //벡터 초기화
	table.resize(MAX_SERIAL_NUMBER + 1, 0); //한칸 더 크게 사이즈를 조정함 그리고 0으로 채움

	for (int i = 0; i < n; ++i) { //해당 번호가 등장하면 테이블의 그 인덱스의 값을 ++해줌
		int serial = data[i];
		table[serial]++;
	}
}

vector<int> getUniqueElements(const vector<int>& data, int n) {	//data[0] ~data[n - 1]에서 중복이 존재하지 않는 원소들을 반환
	vector<int> ret; //유일한 원소들 배열
	
	vector<int> table; //테이블 벡터를 생성하고
	fillFrequencyTable(data, n, table); //data에 대한 빈도수 테이블을 계산함

	for (int number = 1; number <= MAX_SERIAL_NUMBER; number += 1) { //존재할 수 있는 모든 시리얼 넘버에 대해 차례로 조회
		if (table[number] == 1) { //전체 데이터에서 한 번만 등장한 number를 차례로 정답 리스트에 추가
			ret.push_back(number);
		}
	}

	//오름차순 순서로 추가했기 때문에 ret에 대한 정렬은 불필요하다.
	return ret;
}

int main() {
	int n;
	scanf("%d", &n); //몇개를 입력받을 지 저장하는 변수

	vector<int> data = vector<int>(n); //벡터를 선언한뒤 이를 n의 사이즈를 가진 int자료형 배열로 초기화시켜줌
	for (int i = 0; i < n; ++i) {
		scanf("%d", &data[i]);
	}

	const vector<int> answer = getUniqueElements(data, n); //결과값을 answer 벡터에 저장함

	// 각 원소들을 출력한다.
	for (int i = 0; i < answer.size(); ++i) {
		if (i > 0) { //첫 번째 원소가 아니라면 앞에 공백을 하나 추가한다.
			printf(" ");
		}
		printf("%d", answer[i]);
	}

	return 0;
}
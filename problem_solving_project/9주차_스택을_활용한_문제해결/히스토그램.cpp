#include <iostream>
#include <vector>
#include <stack>
#include <cmath>
#include <algorithm>

using namespace std;

class Histogram {
public:
	int height;    // 히스토그램의 높이
	int leftX;     // 인덱스 혹은 히스토그램의 왼쪽 변의 x 좌표
	int rightX;    // 히스토그램의 오른쪽 변의 x좌표

	Histogram() { } //생성자 1

	Histogram(int index, int height) { //생성자 2
		this->leftX = index; 
		this->rightX = this->leftX + 1;   // 각 히스토그램은 너비가 1이므로
		this->height = height;
	}

};

long long getLargestRectangleArea(const vector<Histogram>& histograms) {
	long long answer = 0;    // 최대 직사각형의 넓이

	stack<Histogram> continuedHistograms; // 현재 우측으로 확장 가능성이 있는 히스토그램들

	
	continuedHistograms.push(Histogram(-1, 0)); // 구현상 편의를 위해 가장 왼쪽에 높이 0까지 가상의 히스토그램 추가
	for (int i = 0; i < histograms.size() + 1; i++) { // 왼쪽부터 오른쪽 히스토그램까지 차례로
		Histogram h;
		if (i < histograms.size()) {
			h = histograms[i];
		}
		else {
			// if ( i == n )
			// 구현상 편의를 위해 가장 오른쪽에 높이 0까지 가상의 히스토그램 추가
			h = Histogram(histograms.size(), 0);
		}

		// 이전에 확장중이던 히스토그램들 중, h보다 높이가 높은 히스토그램들은 더 이상 확장될 수 없다 => 최대 넓이가 결정
		while (continuedHistograms.size() > 1
			&& continuedHistograms.top().height >= h.height) {
			// 확장중이던 히스토그램
			Histogram lh = continuedHistograms.top();
			continuedHistograms.pop();

			// 그 이전의 히스토그램 (왼쪽 확장의 끝)
			Histogram bh = continuedHistograms.top();

			// 현재 추가된 h의 바로 왼쪽까지 확장
			long long width = abs(h.leftX - bh.rightX);
			long long height = lh.height;
			long long area = width * height;

			// 최대 값 갱신
			answer = max(answer, area);
		}

		// h를 새로이 추가
		continuedHistograms.push(h);
	}

	return answer; //answer 반환
}

void process(int caseIndex) {
	int n;
	cin >> n; //n을 입력받음

	vector<Histogram> histograms;
	for (int i = 0; i < n; i++) { //n번만큼 수행하고
		int height;
		cin >> height; //각 i마다 높이를 입력받아
		histograms.push_back(Histogram(i, height)); //생성자로 생성하여 벡터배열에 넣어줌
	}

	long long answer = getLargestRectangleArea(histograms); //벡터배열을 가지고 답을 계산해서
	cout << answer << endl; //출력해주고 끝냄
}

int main() {
	int caseSize;
	cin >> caseSize; //caseSize를 입력받고

	for (int caseIndex = 1; caseIndex <= caseSize; caseIndex += 1) {
		process(caseIndex); //caseSize만큼 실행하고 종료함
	}
}
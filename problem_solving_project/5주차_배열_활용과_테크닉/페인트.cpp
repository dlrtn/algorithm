#include <cstdio>
#include <vector>

using namespace std;

const int MAX_SEAT_NUMBER = 1000;
const int MAX_COLOR_NUMBER = 100;

//좌석들을 한 번 색칠하는 이벤트에 대한 정보
class Painting {
public:
	int left;
	int right;
	int color;

	Painting() {}

	Painting(int left, int right, int color) { //좌석의 색과 색칠을 시작할 곳(좌) 색칠이 끝날곳(우)를 저장하는 변수를 초기화시키는 함수
		this->left = left; 
		this->right = right;
		this->color = color;
	}
};

void fillFrequencyTable(int data[], int n, int table[]) {
	for (int i = 0; i < MAX_COLOR_NUMBER; ++i) { //0부터 끝까지의 컬러 번호만큼 테이블을 초기화시킴
		table[i] = 0;
	}
	for (int i = 0; i < n; ++i) { //data의 i번째 인덱스의 색깔값을 토대로 해당 색이 칠해진 빈도를 구함
		int color = data[i];
		table[color]++;
	}
}

void solve(int n, int m, const Painting* paintings) {
	int* seats = new int[n];
	for (int i = 0; i < n; i++) {    // 처음 좌석은 전부 0번 색으로 칠해져 있음
		seats[i] = 0;
	}
		
	for (int i = 0; i < m; ++i) { //색칠 정보들이 주어진 순서대로 각 좌석을 색칠함
		const Painting& p = paintings[i]; //모든 색칠 정보 p에 대하여 차례로 처리
				
		for (int j = p.left; j <= p.right; ++j) { // 각 페인팅 정보마다 좌석의 색을 업데이트 해줌
			seats[j] = p.color;
		}
	}
	int* table = new int[MAX_COLOR_NUMBER]; //모든 색칠을 완료한 이후의 색상 정보를 사용하여
	fillFrequencyTable(seats, n, table);    //모든 색상에 대한 빈도수 테이블을 계산함

	int minColor = seats[0]; //가장 적게 등장한 색상
	int maxColor = seats[0]; //가장 많이 등장한 색상

	for (int color = 0; color <= 99; color += 1) { //0부터 99까지의 색깔중
		if (table[color] == 0) { //한 번 이상 등장한 모든 색깔 color에 대하여
			continue;
		}
		
		if (table[minColor] > table[color]) { //가장 적게 등장한 색이 아직 없거나, color가 더 적게 등장한 경우
			minColor = color;
		}
		if (table[maxColor] < table[color]) { //가장 많이 등장한 색이 아직 없거나, color가 더 많이 등장한 경우
			maxColor = color;
		}
	}

	printf("%d\n", maxColor); //가장 많이 등장한색 출력
	printf("%d\n", minColor); //가장 적게 등장한색 출력

	delete[] table; //동적할당해제
}

int main() {
	int n, m; //n은 좌석의 수, m은 색칠을 진행할 방법
	scanf("%d %d", &n, &m);

	// paintings[i] := i번째에 일어난 색칠 이벤트의 정보
	Painting* paintings = new Painting[n];

	for (int i = 0; i < m; ++i) {
		scanf("%d", &paintings[i].left); //초기화시키기 위한 변수를 입력받음
		scanf("%d", &paintings[i].right);
		scanf("%d", &paintings[i].color);

		// 좌석의 번호는 1번부터 시작하므로, 0 ~ (n-1)범위로 맞추기 위하여 1씩 빼준다
		paintings[i].left -= 1;
		paintings[i].right -= 1;
	}

	// 문제의 정답을 구한다
	solve(n, m, paintings);

	return 0;
}
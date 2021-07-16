#include <cstdio>

using namespace std;

const int MAX_ROW = 9;
const int MAX_COL = 9;


class SudokuBoard {
public:	
	int getRowByIndex(int index) { // 칸의 번호로 행의 번호를 계산하는 메소드
		// 칸의 번호에 대해 마디를 가지고 증가하므로 몫으로 계산할 수 있다
		return (index - 1) / 9 + 1;
	}
		
	int getColByIndex(int index) { // 칸의 번호로 열의 번호를 계산하는 메소드
		// 칸의 번호에 대해 규칙적으로 순환하므로 나머지로 계산할 수 있다
		return (index - 1) % 9 + 1;
	}

	int getGroupByIndex(int index) { // 칸의 번호로 그룹 번호를 계산하는 메소드
		int r = getRowByIndex(index); //r에는 Row의 약자이므로 Row의 index를 계산한 값을 넣어줌
		int c = getColByIndex(index); //c에는 Colum의 약자이므로 Colum의 index를 계산한 값을 넣어줌
		return getGroupByPosition(r, c); //getGroup에 r,c의 좌표를 넘겨줌
	}
		
	int getGroupByPosition(int row, int column) { // 칸의 위치 (행, 열)로 그룹 번호를 계산하는 메소드, ex) (8,1)일 경우		
		int left = ((row - 1) / 3) * 3 + 1; // 행의 번호를 통해, 해당 행에 존재하는 그룹들 중 가장 왼쪽 그룹의 번호를 알 수 있다, 8번 열일 경우 (7/3)*3+1은 7이다.
		int offset = ((column - 1) / 3); // ex 1번 열일 경우 8번이었던 7과 함께 (1-1)/3이므로 0이 나오니 
		return left + offset; //7+0을 리턴함
	}
		
	int getIndexByPosition(int row, int column) { // 칸의 위치 (행, 열)로 칸의 번호를 계산하는 메소드
		return (row - 1) * 9 + (column - 1) % 9 + 1; // 행과 열 번호를 알면 반대로 인덱스도 쉽게 계산할 수 있다.
	}
};


void process(int caseIndex) {
	int index;
	scanf("%d", &index); //칸의 번호는 1~81임

	SudokuBoard board = SudokuBoard(); //기본 생성자를 통해 생성

	// 칸의 번호로 행, 열, 그룹 번호를 계산한다
	int row = board.getRowByIndex(index); //index를 가지고 검사해야함!!
	int col = board.getColByIndex(index);
	int group = board.getGroupByIndex(index);

	printf("Case #%d:\n", caseIndex); //몇번째 케이스인지
	printf("%d %d %d\n", row, col, group); //row, col과 속한 그룹번호를 출력
}

int main() {
	int caseSize; //caseSize를 입력받는 변수
	scanf("%d", &caseSize); //입력받음

	for (int i = 1; i <= caseSize; i++) {
		process(i);
	}
}
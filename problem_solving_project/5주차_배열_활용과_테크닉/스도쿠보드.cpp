#include <cstdio>

using namespace std;

const int MAX_ROW = 9;
const int MAX_COL = 9;


class SudokuBoard {
public:	
	int getRowByIndex(int index) { // ĭ�� ��ȣ�� ���� ��ȣ�� ����ϴ� �޼ҵ�
		// ĭ�� ��ȣ�� ���� ���� ������ �����ϹǷ� ������ ����� �� �ִ�
		return (index - 1) / 9 + 1;
	}
		
	int getColByIndex(int index) { // ĭ�� ��ȣ�� ���� ��ȣ�� ����ϴ� �޼ҵ�
		// ĭ�� ��ȣ�� ���� ��Ģ������ ��ȯ�ϹǷ� �������� ����� �� �ִ�
		return (index - 1) % 9 + 1;
	}

	int getGroupByIndex(int index) { // ĭ�� ��ȣ�� �׷� ��ȣ�� ����ϴ� �޼ҵ�
		int r = getRowByIndex(index); //r���� Row�� �����̹Ƿ� Row�� index�� ����� ���� �־���
		int c = getColByIndex(index); //c���� Colum�� �����̹Ƿ� Colum�� index�� ����� ���� �־���
		return getGroupByPosition(r, c); //getGroup�� r,c�� ��ǥ�� �Ѱ���
	}
		
	int getGroupByPosition(int row, int column) { // ĭ�� ��ġ (��, ��)�� �׷� ��ȣ�� ����ϴ� �޼ҵ�, ex) (8,1)�� ���		
		int left = ((row - 1) / 3) * 3 + 1; // ���� ��ȣ�� ����, �ش� �࿡ �����ϴ� �׷�� �� ���� ���� �׷��� ��ȣ�� �� �� �ִ�, 8�� ���� ��� (7/3)*3+1�� 7�̴�.
		int offset = ((column - 1) / 3); // ex 1�� ���� ��� 8���̾��� 7�� �Բ� (1-1)/3�̹Ƿ� 0�� ������ 
		return left + offset; //7+0�� ������
	}
		
	int getIndexByPosition(int row, int column) { // ĭ�� ��ġ (��, ��)�� ĭ�� ��ȣ�� ����ϴ� �޼ҵ�
		return (row - 1) * 9 + (column - 1) % 9 + 1; // ��� �� ��ȣ�� �˸� �ݴ�� �ε����� ���� ����� �� �ִ�.
	}
};


void process(int caseIndex) {
	int index;
	scanf("%d", &index); //ĭ�� ��ȣ�� 1~81��

	SudokuBoard board = SudokuBoard(); //�⺻ �����ڸ� ���� ����

	// ĭ�� ��ȣ�� ��, ��, �׷� ��ȣ�� ����Ѵ�
	int row = board.getRowByIndex(index); //index�� ������ �˻��ؾ���!!
	int col = board.getColByIndex(index);
	int group = board.getGroupByIndex(index);

	printf("Case #%d:\n", caseIndex); //���° ���̽�����
	printf("%d %d %d\n", row, col, group); //row, col�� ���� �׷��ȣ�� ���
}

int main() {
	int caseSize; //caseSize�� �Է¹޴� ����
	scanf("%d", &caseSize); //�Է¹���

	for (int i = 1; i <= caseSize; i++) {
		process(i);
	}
}
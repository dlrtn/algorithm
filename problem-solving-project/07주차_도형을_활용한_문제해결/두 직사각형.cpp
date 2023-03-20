#include <iostream>
#include <cstdio>

using namespace std;

int get_area(int la, int ra, int ta, int ba, int lb, int rb, int tb, int bb) {
	int l, r, t, b; //�������� �簢��

	l = max(la, lb); //�������� ��ǥ�� ������ �׸��󿡼� �� ������ �ִ� ���簢���� ��ǥ�̹Ƿ�
	r = min(ra, rb); //�������� ��ǥ�� �������� �׸��󿡼� �� ������ �ִ� ���簢���� ��ǥ�̹Ƿ�
	t = min(ta, tb); //�������� ��ǥ�� ������ �׸��󿡼� �� ���� ��ġ�� �ִ� ���簢���� ��ǥ�̹Ƿ�
	b = max(ba, bb); //�������� ��ǥ�� �Ʒ����� �׸��󿡼� �� ���� ��ġ�� �ִ� ���簢���� ��ǥ�̹Ƿ�

	if (l <= r && b <= t) //������ ������ �ɼ��������� ������ ���� �ʱ��ϱ� ����
		return ((r - l) * (t - b));

	return 0;
}

void test_case() {
	int ax, ay, bx, by; //���簢�� A
	int px, py, qx, qy;
	scanf("%d %d %d %d", &ax, &ay, &bx, &by);
	scanf("%d %d %d %d", &px, &py, &qx, &qy);

	int la, ra, ba, ta;//���簢�� A
	la = min(ax, bx);//���� ��ǥ
	ra = max(ax, bx);//������ ��ǥ
	ta = max(ay, by);//���� ��ǥ
	ba = min(ay, by);//�Ʒ� ��ǥ

	int lb, rb, bb, tb;//���簢�� B
	lb = min(px, qx);//���� ��ǥ
	rb = max(px, qx);//������ ��ǥ
	tb = max(py, qy);//�� ��ǥ
	bb = min(py, qy);//�Ʒ� ��ǥ

	int answer = get_area(la, ra, ta, ba, lb, rb, tb, bb); //�������� ������ ���ؼ� �����ϴ� �Լ�

	printf("%d\n", answer);
}
int main() {
	int t;
	scanf("%d", &t); //�׽�Ʈ���̽� ������ �Է¹޴� ����

	for (int i = 0; i < t; i++)
		test_case();//�׽�Ʈ���̽� ������ŭ ����

	return 0;
}
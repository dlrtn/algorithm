#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int p[1025][1025]; //�ִ��� 1024�̹Ƿ�
int n, ans; //nxn���� size�� �Է¹��� ������ ������ ������ ����

//�� ��°�� ū ���� ��ȯ�ϴ� �Լ�
int Pulling(int x, int y) //
{
    vector <int > a; //a�� 2x2 �����̴�.
    for (int i = x; i < x + 2; i++)
        for (int j = y; j < y + 2; j++)
            a.push_back(p[i][j]);
    sort(a.begin(), a.end()); //a���͸� �����Ͽ� 3��° �ε����� ��ȯ��.
    return a[2];
}

int main() {
    time_t start, end;
    double result;
    cin >> n;
    for (int i = 0; i < n; i++)  {
        for (int j = 0; j < n; j++)
            cin >> p[i][j];        
    }
    start = time(NULL); //�Է³� �������
    while (n > 1) //n�� ���������� 1�� �ɶ�����
    {
        for (int i = 0; i < n; i += 2)
            for (int j = 0; j < n; j += 2)
                p[i / 2][j / 2] = Pulling(i, j); //���� ���� 2ĭ�� �����̸� p����
        n /= 2; //n�� ����� �������� ����
    }
    end = time(NULL); // ��������
    cout << p[0][0] << '\n';//���� �������� �����ִ� n�� ���� �����.
    result = (double)(end - start);
    printf("����ð� : %f��", result / CLOCKS_PER_SEC);
}
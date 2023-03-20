#include <iostream>
#include <map>
#include <algorithm>
#include <time.h>

using namespace std;

int main()
{
    int size1, size2, ans = 65536; //size1�� size2�� ���� arr1, 2�� ������, ans�� ��� ���������� ������ ��ī�� ���絵�� ���Ͽ� ������ ��
    double all = 0, dup = 0, result; //all�� �������� ����, dup�� �������� ����, result�� ����ð� ��� �� ����� ����
    string arr1, arr2; //�� ���ڿ��� �Է¹��� ����
    map<string, int> map1; //�Է¹��� ���ڿ��� �� ���� ��� �˻��� ��, Ȱ���� map����
    time_t start, end;

    cin >> arr1 ;
    cin >> arr2 ;

    start = time(NULL); //�Է��� �������Ƿ� �����ġ ��ŸƮ

    transform(arr1.begin(), arr1.end(), arr1.begin(), ::tolower); //�� arr�� ������ ��꿡 �����ϱ� ���� ��� �ҹ��ڷ� ��ȯ������
    transform(arr2.begin(), arr2.end(), arr2.begin(), ::tolower); 

    size1 = arr1.size(); //size���� �����Ͽ� ����
    size2 = arr2.size();

    for (int i = 0; i < size1 - 1; i++) //���� �˻�� i+1�� ���� �˻��ϹǷ� n-1������ �ݺ����� ����ϸ� ��. �α��ھ� ��� ���������� ����Ƿ�
    {
        if (arr1[i] < 97 || arr1[i] > 122) //���� ���ڰ� �ҹ��ڰ� �ƴ� ��쿡�� �Ѿ���� ��, �տ��� ��� �빮�ڸ� �ҹ��ڷ� �ٲ��־����Ƿ� Ư������������ �˻��ϴ� ���ǹ�
            continue;
        if (arr1[i + 1] < 97 || arr1[i + 1] > 122) //���� ab+���� b+�� ��쿡�� �Ѿ���� �ϱ� ���Ͽ� ���� ���ڸ� �˻�
            continue;

        string arr;
        arr = arr1[i]; //���ڿ��� ����� ���ڸ� ������. 
        arr += arr1[i + 1]; //���� ������ ���� ���ڵ� ����
        all++; //�������� ����ϴ� �뵵

        if (map1.count(arr))    map1[arr]++; //map1���� ���� �α��ھ� ��� ������� �迭�� key������ ����ϴ� ������ �ִٸ� ++
        else    map1[arr] = 1; //�ƴ� ��쿡�� ���� ������ ���̹Ƿ� 1�� ����
    }

    for (int i = 0; i < size2 - 1; i++)
    {
        if (arr2[i] < 97 || arr2[i] > 122) continue; //�� �ݺ��������� ���ǹ��� ����
        if (arr2[i + 1] < 97 || arr2[i + 1] > 122) continue;

        string arr; //������
        arr = arr2[i];
        arr += arr2[i + 1];

        if (map1.count(arr)) //arr�� Ű������ ���� ������ �̹� �����ϴ� ���
        {
            if (map1[arr] > 0) //�� ���� 0���� Ŭ ��쿡�� �� �������� 2�� �̻��� ���� �������� �����ϴ� ���
            {
                map1[arr]--; //�� ���� ���ְ�
                dup++; //������ ++
            }
            else    all++;// ������ ��쿡�� �������� ++���ش�. �̹� �������� �ʴ� ����̹Ƿ�
        }
        else
            all++; //�̿��� ��쿡�� ��� �������� �ƴ� ����̹Ƿ� �������� ++ ����
    }

    if (all != 0) //�������� 0�� �ƴѰ�� 0�� ��쿡�� 1�� ���
        ans = (int)((double)ans * (dup / all)); //������ / ������ * 65536�� ����Ͽ� ����, �̶� ans�� int���̹Ƿ� int����ȯ�� ����
    cout << ans;

    end = time(NULL);
    result = (double)(end - start);
    printf("����ð� : %f��", result / CLOCKS_PER_SEC);

    return 0;
}
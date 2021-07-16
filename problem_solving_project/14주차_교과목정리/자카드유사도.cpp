#include <iostream>
#include <map>
#include <algorithm>
#include <time.h>

using namespace std;

int main()
{
    int size1, size2, ans = 65536; //size1과 size2는 각각 arr1, 2의 사이즈, ans의 경우 최종적으로 구해진 자카드 유사도를 곱하여 제출할 값
    double all = 0, dup = 0, result; //all은 합집합의 갯수, dup은 교집합의 갯수, result는 실행시간 출력 시 사용할 변수
    string arr1, arr2; //각 문자열을 입력받을 변수
    map<string, int> map1; //입력받은 문자열을 두 개씩 끊어서 검사할 때, 활용할 map변수
    time_t start, end;

    cin >> arr1 ;
    cin >> arr2 ;

    start = time(NULL); //입력이 끝났으므로 스톱워치 스타트

    transform(arr1.begin(), arr1.end(), arr1.begin(), ::tolower); //각 arr의 값들을 계산에 용이하기 위해 모두 소문자로 변환시켜줌
    transform(arr2.begin(), arr2.end(), arr2.begin(), ::tolower); 

    size1 = arr1.size(); //size값을 리턴하여 저장
    size2 = arr2.size();

    for (int i = 0; i < size1 - 1; i++) //문자 검사시 i+1의 값도 검사하므로 n-1까지만 반복문을 사용하면 됨. 두글자씩 끊어서 다중집합을 만드므로
    {
        if (arr1[i] < 97 || arr1[i] > 122) //현재 문자가 소문자가 아닌 경우에는 넘어가도록 함, 앞에서 모든 대문자를 소문자로 바꿔주었으므로 특수문자인지를 검사하는 조건문
            continue;
        if (arr1[i + 1] < 97 || arr1[i + 1] > 122) //또한 ab+에서 b+의 경우에는 넘어가도록 하기 위하여 다음 문자를 검사
            continue;

        string arr;
        arr = arr1[i]; //문자열에 통과한 문자를 삽입함. 
        arr += arr1[i + 1]; //현재 문자의 다음 문자도 삽입
        all++; //합집합을 계산하는 용도

        if (map1.count(arr))    map1[arr]++; //map1에서 현재 두글자씩 끊어서 만들어진 배열을 key값으로 사용하는 변수가 있다면 ++
        else    map1[arr] = 1; //아닌 경우에는 새로 등장한 것이므로 1을 삽입
    }

    for (int i = 0; i < size2 - 1; i++)
    {
        if (arr2[i] < 97 || arr2[i] > 122) continue; //위 반복문에서의 조건문과 동일
        if (arr2[i + 1] < 97 || arr2[i + 1] > 122) continue;

        string arr; //동일함
        arr = arr2[i];
        arr += arr2[i + 1];

        if (map1.count(arr)) //arr을 키값으로 가진 변수가 이미 존재하는 경우
        {
            if (map1[arr] > 0) //그 값이 0보다 클 경우에는 즉 교집합이 2개 이상인 경우와 교집합이 존재하는 경우
            {
                map1[arr]--; //그 값을 빼주고
                dup++; //교집합 ++
            }
            else    all++;// 나머지 경우에는 합집합을 ++해준다. 이미 존재하지 않는 경우이므로
        }
        else
            all++; //이외의 경우에도 모두 교집합이 아닌 경우이므로 합집합을 ++ 해줌
    }

    if (all != 0) //합집합이 0이 아닌경우 0인 경우에는 1로 계산
        ans = (int)((double)ans * (dup / all)); //교집합 / 합집합 * 65536을 계산하여 대입, 이때 ans는 int형이므로 int형변환후 삽입
    cout << ans;

    end = time(NULL);
    result = (double)(end - start);
    printf("실행시간 : %f초", result / CLOCKS_PER_SEC);

    return 0;
}
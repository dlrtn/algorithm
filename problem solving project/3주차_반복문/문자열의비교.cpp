#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

const int MAX_LENGTH = 100000; //길이의 최대는 십만

class MyString{
private: //접근 제한
	char *charaters; //문장을 저장할 배열
	int length; //문장의 길이 변수

public:
	MyString(const char * str){
		this->length = strnlen(str, MAX_LENGTH); //입력된 문장의 길이를 클래스 내부의 변수로 초기화
		this->charaters = new char[this->length]; //동적할당을 해줌
		for (int i =0; i < this->length; i++){ //문장을 넣어줌
			this->charaters[i] = str[i];
		}
	}
	
	MyString(const string & original){ 
		this->length = original.length();  //클래스 내부의 변수를 초기화
		this->charaters = new char[this->length]; //동적할당을 해줌
		for (int i =0; i < this->length; i++){  //문장을 넣어줌
			this->charaters[i] = original[i];
		}
	}
	~MyString(){ //동적할당된 메모리를 해제해주는 부분
		delete[] charaters;
	}
	
	bool operator < (const MyString & o) const{
		int n = min(this->length, o.length); //크기가 작은 것을 반환, app과 apple같은 경우 apple이 사전순으로 더 뒤에 오기때문에 비교가 무의미하므로 더 작은 것의 사이즈만큼만 비교
		
		for(int i = 0; i < n; i++){
			if(this->charaters[i] < o.charaters[i]) //mys1이 mys2보다 더 작으면 사전순으로 앞에 있는 것이 정상이므로 true를 반환
				return true;
			else if(this->charaters[i] > o.charaters[i]) //mys1이 mys2보다 더 클경우는 사전순으로 뒤로 가야하므로 false를 반환
				return false;
		}
		if(this->length < o.length) // 더 작은 사이즈만큼의 비교가 끝나고 mys1의 길이가 mys2보다 짧을경우에는 사전순으로 앞으로 와야하므로 true를 반환
				return true;
			else 
				return false;
	}
	
	bool operator > (const MyString & o) const{
		int n = min(this->length, o.length); //길이가 더 짧은 부분을 변수 n에 저장
		
		for(int i = 0; i < n; i++){
			if(this->charaters[i] > o.charaters[i]) //위 내용과 반대되는 내용 사전순으로 뒤에 와야되는 것이 맞다면 true
				return true;
			else if(this->charaters[i] < o.charaters[i]) //앞에 와야된다면 true
				return false;
		}
		if(this->length > o.length) // 더 작은 사이즈만큼의 비교가 끝나고 mys1의 길이가 mys2보다 길경우에는 사전순으로 뒤로 가야하므로 true를 반환
				return true;
			else 
				return false;
	}
	
	bool operator == (const MyString & o) const{
		int n = min(this->length, o.length); //길이가 더 짧은 부분을 변수 n에 저장
		
		for(int i = 0; i < n; i++){ //같은지를 비교하는 부분으로 다를경우 false를 리턴
			if(this->charaters[i] != o.charaters[i])
				return false;
		}
		
		return true;
			
	}
};

int main(){
	string s1; //s1, s2라는 스트링 변수 생성
	string s2;
	cin >> s1 >> s2; // 입력받음
	
	MyString mys1(s1); //mys1이라는 변수에 s1으로 초기화시켜줌
	MyString mys2(s2); //mys2라는 변수에 s2로 초기화 시켜줌
	
	if (mys1 < mys2) //만약 mys1가 mys2보다 사전순으로 빠르면 -1
		printf("-1");
	else if (mys1 > mys2) // 느리면 1
		printf("1");
	else // 같다면 0
		printf("0");
	
	return 0;
}

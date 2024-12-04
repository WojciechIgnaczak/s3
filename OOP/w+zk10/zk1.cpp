#include<iostream>
#include <algorithm>
#include <cctype>
#include<unordered_map>
#include<set>
#include<array>
using namespace std;
// ANAGRAM
bool anagram(string &str1, string &str2){
    if(str1.size()!=str2.size()){return 0;}
    std::unordered_map<char,int> charCount;
    for(char ch: str1){
        charCount[tolower(ch)]++;
    }
    for(char ch: str2){
        char lowerChar=tolower(ch);
        if( charCount.find(lowerChar)==charCount.end()|| charCount[lowerChar]==0)
        {
            return false;
        }
        charCount[lowerChar]--;
    }
    return true;

}

set<string> podciag(string &str)
{
set<string>substring;
for(int i=0;i<=str.length();i++)
{
    for(int j=i;j<=str.length();j++)
    {
        substring.insert(str.substr(i,j));
        
    }
}
return substring;
}


template<typename T,size_t n>
void babelsort(array<T, n> &arr)
{
    for(int i=0;i<n-1;i++)
    {
        for(int j=0;j<n-i-1;j++)
        {
            if(arr[j]>arr[j+1])
            {
                swap(arr[j],arr[j+1]);
            }
        }
    }
}

int main()
{
    cout<<"ZAD1\n";
    string a="aaabbbwccc";
    string b="cccbbbasaa";
    cout<<anagram(a,b)<<endl;
    

    cout<<"ZAD2\n";
    string input="abc";
    set<string> s=podciag(input);

    for(const auto &sub: s)
    {
        cout<<sub<<endl;
    }
    


    cout<<"ZAD3\n";
    array<int,5> arr ={2,5,1,5,3};

    for(const int &el: arr)
    {
        cout<<el<<" "<<endl;
    }

    babelsort(arr);

    cout<<"Po sortowaniu\n";

    for(auto &el: arr)
    {
        cout<<el<<" "<<endl;
    }
    return 0;
}


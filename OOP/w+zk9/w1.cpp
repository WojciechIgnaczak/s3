#include <iostream>
#include <cstdlib>
#include <vector>
#include <map>
using namespace std;

template <typename T>
pair<T, unsigned int> findMostOccurences(const vector<T> &v)
{
    if (v.empty()){
        throw length_error("Vector is empty");
    }
    map<T,size_t>map;
    for(const auto &value:v)
    {
        map[value]+=1;

    }
    map[v[0]]=1;
    pair<int,unsigned int>result;
    result.second=0;
    for (const auto &value: map)
    {   if(value.second> result.second)
        {
            result.first=value.first;
            result.second=value.second;
        }
        cout<<value.first<<" "<<value.second<<endl;
    }
    return result;
}


int main()
{
    vector<int>numbers={1,2,3,4,5,6,7,8,9,0,64,45,3,4,6,4,5,4,5,4,6,3,7,90};
    pair<int,unsigned int>result=findMostOccurences(numbers);
    cout<<"Najczesciej wystepuje liczba: "<<result.first<<", występuje "<<result.second<<" razy"<<endl;
    return 0;
}
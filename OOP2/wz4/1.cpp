#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <stdexcept>
using namespace std;
class TextLines
{
    public:
        virtual ~TextLines() = default;
        virtual int get_number_of_lines()=0;
        virtual string read_line(int line_number)=0;
        virtual void delete_line(int line_number)=0;
        virtual void write_line(string text)=0; // at end
        virtual void write_line(string text, int line_number)=0;// at index
    
};

class TextLinesInMemory:public TextLines
{
    public:

        
        virtual int get_number_of_lines()override
        {
            return lines.size();
        }
        
        
        virtual string read_line(int line_number) override
        {
            if (get_number_of_lines()>=line_number && line_number >=0)
            {
                return lines[line_number];
            }
            else
            {
             throw out_of_range("index out of range");
            }
        }
        
        
        virtual void delete_line(int line_number) override
        {
            if (get_number_of_lines()>=line_number && line_number >=0)
            {
                lines[line_number]="";
            }
            else
            {
                throw out_of_range("index out of range");
            }
        }
        
        
        
        virtual void write_line(string text) override // at end
        {
            cout<<"D";
        }
        
        
        virtual void write_line(string text, int line_number) override // at index
        {
            cout<<"D";

        }
        
        
    private:
        vector<string> lines;
};
int main()
{
    TextLinesInMemory t;
    cout<<t.get_number_of_lines();
    return 0;
}
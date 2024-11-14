#include<iostream>
#include<cstdlib>
#include<cstring>
using namespace std;

class TimeLength{
public:
    TimeLength(const char *_seconds){
        copy=strdup(_seconds);
        unsigned long value =strtoul(copy,NULL,10);
        hours=value/3600;
        minutes=(value-hours*3600)/60;
        seconds=value-hours*3600-minutes*60;
    };

    ~TimeLength(){};

    TimeLength(const TimeLength& source){
        copy=strdup(source.copy);
        hours=source.hours;
        minutes=source.minutes;
        seconds=source.seconds;
    };

    friend ostream& operator<<(ostream& os, const TimeLength& source);
    
    const string getString() const
    {
        return copy;
    }

    static TimeLength createZeroLenght(){
        static TimeLength zerowa("0");
        return zerowa;
    }
    
private:
    char *copy;
    unsigned long  hours;
    unsigned long  minutes;
    unsigned long  seconds;
};
ostream& operator<<(ostream& os, const TimeLength& source)
{
    os<<source.hours<<"h "<<source.minutes<<"min "<<source.seconds<<"sec"<<endl;
    return os;
}

int main()
{
    TimeLength uptime("19592");
    // Konstruktor i przeciążenie operatora <<
    cout<<"b) Konstruktor i przeciążenie operatora <<\n";
    cout<<uptime<<endl;

    // Konstruktor kopiujący c)
    TimeLength kopia(uptime);
    cout<<"c) Konstruktor kopiujący\n";
    cout<<kopia<<endl;

    // d) Metoda getString
    cout<<"d) getString\n";
    cout<<uptime.getString()<<endl;

    // e) Metoda statyczna
    cout<<"e) Metoda statyczna\n";
    cout<<TimeLength::createZeroLenght()<<endl;
    return 0;
}
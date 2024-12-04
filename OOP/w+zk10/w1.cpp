#include<iostream>
#include<iomanip>
using namespace std;

class Logger{
public:
    enum LogLevel{Debug, Info, Warning, Error};
    static Logger& getInstance(){
        static Logger instance;
        return instance;
    } 

    void setVerbosity(LogLevel level)
    {
        this->verbosity=level;
    }
    void log(LogLevel level,const string &message)
    {
        if(level<this->verbosity){
            return;
        }
        time_t time=std::time(nullptr);

        cerr<<put_time(localtime(&time),"%F %T%z")<<" ";
        switch(level)
        {
            case Debug: cerr<<"[DEBUG]";break;
            case Info: cerr<<"[INFO]";break;
            case Warning: cerr<<"[WARN]";break;
            case Error: cerr<<"[ERR]";break;

        }
        cerr<<" "<< message<<endl;
    }
private:
    Logger(): verbosity(Debug){};
    LogLevel verbosity;
};
int main(){
    Logger logger=Logger::getInstance();
    logger.setVerbosity(Logger::Info);
    logger.log(Logger::Debug, "test debug");
    logger.log(Logger::Info, "test info");

    return 0;
}
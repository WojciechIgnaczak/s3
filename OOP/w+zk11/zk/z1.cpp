#include <iostream>
#include <unordered_map>
#include <fstream>

class Config
{
public:
	/* Kasujemy domyślny konstruktor kopiujący */
	Config(const Config &other) = delete;
	/* Kasujemy domyślny operator przypisania */
    Config& operator=(const Config &other) = delete;

    ~Config()
        {
            // stringi
        std::ofstream file_str("value_string.txt");
        for (const auto& pair : v_string) {
            file_str << pair.first << ":" << pair.second << "\n";
        }
        file_str.close();
        std::cout << "Plik został zapisany." << std::endl;
            // inty
        std::ofstream file_int("value_int.txt");
        for (const auto& pair : v_int) {
            file_int << pair.first << ":" << pair.second << "\n";
        }
        file_int.close();
        std::cout << "Plik został zapisany." << std::endl;
    }
    
    void set(const std::string &key, const std::string &value){
        v_string[key]=value;
    }
    void set(const std::string &key, const int value){
        v_int[key]=value;
    }
    std::string getString(const std::string &key){
        return v_string[key];
    }
    int getInt(const std::string &key){
        return v_int[key];
    }
    static Config& getInstance() {
        static Config instance;
        return instance;
    }
private:
    Config(){

        // stringi
        std::ifstream file_str(path_string);
        std::string line_str;
        while (std::getline(file_str, line_str)) {
            size_t delimiterPos = line_str.find(':');
            if (delimiterPos != std::string::npos) {
                std::string key = line_str.substr(0, delimiterPos);
                std::string value = line_str.substr(delimiterPos + 1);
                v_string[key] = value;
            }
        }
        file_str.close();
        for (const auto& pair : v_string) {
        std::cout << "Klucz: " << pair.first << ", Wartość: " << pair.second << std::endl;
        }
        //inty
        std::ifstream file_int(path_int);
        std::string line_int;
        while (std::getline(file_int, line_int)) {
            size_t delimiterPos = line_int.find(':');
            if (delimiterPos != std::string::npos) {
                std::string key = line_int.substr(0, delimiterPos);
                int value = stoi(line_int.substr(delimiterPos + 1));
                v_int[key] = value;
            }
        }
        file_int.close();
        for (const auto& pair : v_int) {
        std::cout << "Klucz: " << pair.first << ", Wartość: " << pair.second << std::endl;
        }
    }
    std::string path_string="value_string.txt";
    std::string path_int="value_int.txt";
    std::unordered_map<std::string, std::string> v_string;
    std::unordered_map<std::string, int> v_int;
};

int main()
{   
    //Config k;
    Config &k = Config::getInstance();
    k.set("d",4);
    k.set("d","dd");
    k.set("aa",2);
    k.set("aaa","fff");
    int k1=k.getInt("aa");
    std::cout<<"getint "<<k1<<std::endl;
    std::string k2=k.getString("d");
    std::cout<<"getstring "<<k2<<std::endl;

    return 0;
}
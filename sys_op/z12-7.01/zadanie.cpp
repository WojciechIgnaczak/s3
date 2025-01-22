#include <iostream>
#include <fstream>
#include <vector>
#include <thread>
#include <mutex>
#include <cstring>

#define TAB_LENGTH 10

struct Shared {
    int tab[TAB_LENGTH];
    std::mutex mtx;
};

void count_digits(const char* content, size_t start, size_t end, Shared& shared) {
    int local_count[TAB_LENGTH] = {0};

    for (size_t i = start; i < end; ++i) {
        if (content[i] >= '0' && content[i] <= '9') {
            local_count[content[i] - '0']++;
        }
    }

    std::lock_guard<std::mutex> lock(shared.mtx);
    for (int i = 0; i < TAB_LENGTH; ++i) {
        shared.tab[i] += local_count[i];
    }
}

int main(int argc, char* argv[]) {
    if (argc != 3) {
        std::cout << "BŁĘDNA ILOŚĆ ARGUMENTÓW" << std::endl;
        return -1;
    }

    int number_of_threads = std::stoi(argv[2]);
    if (number_of_threads <= 0) {
        std::cout << "ZA MAŁO WĄTKÓW" << std::endl;
        return -1;
    }

    std::ifstream file(argv[1], std::ios::binary | std::ios::ate); // muszą być flagi bo inaczej '0'
    if (!file.is_open()) {
        std::cout << "BŁĄD OTWIERANIA PLIKU" << std::endl;
        return -1;
    }

    size_t file_size = file.tellg(); // sprawdzanie rozmiaru pliku
    file.seekg(0, std::ios::beg);

    std::vector<char> content(file_size);
    if (!file.read(content.data(), file_size)) {
        std::cerr << "BŁĄD ODCZYTU PLIKU" << std::endl;
        return -1;
    }

    Shared shared = {};
    std::vector<std::thread> threads;
    size_t segment_size = file_size / number_of_threads;

    for (int i = 0; i < number_of_threads; ++i) {
        size_t start = i * segment_size;
        size_t end = (i == number_of_threads - 1) ? file_size : start + segment_size;

        threads.emplace_back(count_digits, content.data(), start, end, std::ref(shared));
    }

    for (auto& thread : threads) {
        thread.join();
    }

    for (int i = 0; i < TAB_LENGTH; ++i) {
        std::cout << i << " = " << shared.tab[i] << std::endl;
    }

    return 0;
}

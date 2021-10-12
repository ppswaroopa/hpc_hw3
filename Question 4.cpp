#include <iostream>
#include <vector>

using namespace std;

bool distinct(std::string str, int a, int b){
    vector<bool> visited (26);

    for (int k = a; k<=b; k++){
        if (visited[str[k] - 'a'])
            return false;
        visited[str[k] - 'a'] = true;
    }
    return true;
}

int uniqueSubString(std::string str){
    int size = str.size();
    int result = 0;

    for (int i=0; i<size; i++){
        for (int j=0; j<size; j++){
            if (distinct(str, i, j))
                result = max(result, j-i+1);
        }
    }
    return result;
}

int main() {
    string word;
    std::cout << "Enter word to check for longest substring without repeating character" << std::endl;
    std::cin >> word;
    int length = uniqueSubString(word);
    std::cout << "Length of the longest substring without repeating character is:" << length;
    return 0;
}

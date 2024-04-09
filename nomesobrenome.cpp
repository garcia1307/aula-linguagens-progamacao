#include <iostream>
#include <string>

using namespace std;

int main() {
    string nome;
    string sobrenome;
    int tamanho;

    cin >> nome;
    cin >> sobrenome;

    tamanho = nome.size() - 1;

    cout << sobrenome << "," << nome[0] << nome[tamanho] << endl;
}

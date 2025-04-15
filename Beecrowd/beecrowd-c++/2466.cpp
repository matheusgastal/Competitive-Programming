#include <stdio.h>
#include <iostream>
using namespace std;
int main() {
    int n;
    cin >> n;
    int vet[n];
    int aux[n-1];
    int tam = n;
    for(int i = 0; i<n ; i++){ 
        cin >> vet[i];
    }

    for(int i = 0; i<n-1; i++){
         if(i % 2 == 0){
            for(int j = 0; j < tam-1; j++){
                if(vet[j] == vet[j + 1]){
                    aux[j] = 1;
                }
                else{
                    aux[j] = -1;
                }
                tam --;
            }
            for(int x = 0; x<tam-1; x++){
                cout << aux[x];
                cout << "\n";
            }
        }
        else{
            for(int j = 0; j<tam-1; j++){
                if(aux[j] == aux[j + 1]){
                    vet[j] = 1;
                }
                else{
                    vet[j] = -1;
                }
                tam--;
        }
        for(int x = 0; x<tam-1; x++){
            cout << vet[x];
            cout << "\n";
        }
    }
}
        if(n % 2 == 1){
            if(vet[0] == -1){
                cout << "branca" << endl;
            }
            else{
                cout << "preta" << endl;
            }
        }
        else{
            if(aux[0] == -1){
                cout << "branca" << endl;
            }
            else{
                cout << "preta" << endl;
            }
        }
        return 0;
    }

#include <stdio.h>
#include <iostream>
using namespace std;

int main() {
 
    int vet[5];
    int cresc = 1;
    int decresc = 1;

    for(int i = 0; i<5; i++){
        cin >> vet[i];
    }
    for(int i = 0; i<4; i++){
        if (vet[i] > vet[i+1]){
            cresc = 0;
        }
    }
    for(int i = 1; i<5; i++){
        if(vet[i] > vet[i-1]){
            decresc = 0;
        }
    }

    if(cresc){
        cout << "C" << endl;
    }
    else if(decresc){
        cout << "D" << endl;
    }
    else{
        cout << "N" << endl;
    }
    return 0;
}
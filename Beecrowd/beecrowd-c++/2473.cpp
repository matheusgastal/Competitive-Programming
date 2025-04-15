#include <stdio.h>
#include <bits/stdc++.h>
using namespace std;
#include <map>

int main(){
    map <int,int> numbers;
    int n, total;
    total = 0; 
    for(int i = 0; i<6; i++){
        cin >> n;
        numbers[n] = 1;
    }
    for(int i = 0; i<6; i++){
        cin >> n;
        if(numbers[n] == 1){
            total ++;
        }
    }
    if(total == 6){
        cout << "sena" << endl;
    }
    else if(total == 5){
        cout << "quina" << endl;
    }
    else if(total == 4){
        cout << "quadra" << endl;
    }
    else if(total == 3){
        cout << "terno" << endl;
    }
    else{
        cout << "azar" << endl;
    }
    return 0;
}
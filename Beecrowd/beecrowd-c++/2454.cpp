#include <stdio.h>
#include <iostream>
using namespace std;
 int main(){
    int p,r;
    cin >> p;
    cin >> r;
    if(p == 0){
        cout << "C" << endl;
    }
    else{
        if (r == 1){
        cout << "A" << endl;
        }
        else{
            cout << "B" << endl;
        }
    }
    return 0;
 }
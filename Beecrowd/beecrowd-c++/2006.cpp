#include <stdio.h>
#include <bits/stdc++.h>
using namespace std;

int main() {
    int correct,type,count;
    cin >> correct;
    count = 0;
    for(int i = 0; i<5; i++){
        cin >> type;
        if(type == correct){
            count ++;
        }
    }
    cout << count << endl;
    return 0;
}
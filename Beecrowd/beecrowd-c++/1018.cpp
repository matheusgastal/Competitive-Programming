#include <stdio.h>
#include <iostream>
using namespace std;

int main() {
    int val,hundred,fifty,twenty,ten,five,two,one;
    hundred = 0;
    fifty = 0;
    twenty = 0;
    ten = 0;
    five = 0;
    two = 0;
    one = 0;

    cin >> val;
    cout << val << endl;
        if(val / 100 >= 1){
            hundred = val / 100;
            val -= 100 * hundred;
        }
        if(val / 50 >= 1){
            fifty = val / 50;
            val -= 50 * fifty;
        }
        if(val / 20 >= 1){
            twenty= val / 20;
            val -= 20 * twenty;
        }
        if(val / 10 >= 1){
            ten = val / 10;
            val -= 10 * ten;
        }
        if(val / 5 >= 1){
            five = val / 5;
            val -= 5 * five;
        }
        if(val / 2 >= 1){
            two = val / 2;
            val -= 2 * two;
        }
        one = val;
        val = 0;
        cout << hundred << " nota(s) de R$ 100,00" << endl;
        cout << fifty << " nota(s) de R$ 50,00" << endl;
        cout << twenty << " nota(s) de R$ 20,00" << endl;
        cout << ten << " nota(s) de R$ 10,00"  << endl;
        cout << five << " nota(s) de R$ 5,00"  << endl;
        cout << two << " nota(s) de R$ 2,00"  << endl;
        cout << one << " nota(s) de R$ 1,00"  << endl;
    }

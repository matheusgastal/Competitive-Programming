#include <stdio.h>
#include <iostream>
using namespace std;
int main() {
    long long int l,n;
    cin >> l;
    cin >> n;
    long long int maiorarea = (l - n + 1) * (l - n + 1) + (n - 1);
    cout << maiorarea << endl;
}
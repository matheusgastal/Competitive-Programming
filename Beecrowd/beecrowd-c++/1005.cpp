#include <iostream>
using namespace std;

int main() {
    double a,b,c;

    cin >> a;
    cin >> b;
    a = 3.5 * a;
    b = 7.5 * b;
    c = (a + b) / 11.0;
    printf("MEDIA = %.5f\n", c);
}
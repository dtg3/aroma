#include <iostream>
using namespace std;

int successor(int input, int n);

int main ()
{
   // Local variable declaration:
   int a = 10;

   successor(a + 5);
   return 0;
}

int successor(int a, int n) {
  return a + n;
}
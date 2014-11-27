#include <iostream>
using namespace std;

int successor(int input);

int main ()
{
   // Local variable declaration:
   int a = 10;

   successor(a);
   return 0;
}

int successor(int a) {
  return ++a;
}
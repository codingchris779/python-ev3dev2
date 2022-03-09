#include <iostream>
#include <vector>
#include <string>

using namespace std;
   int main() {
       int cntr = 0;
       for (int loop1 = 1; loop1 < 10; loop1 *= 2)
          for (int loop2 = 0; loop2 < 10; loop2++)
             for (int loop3 = 0; loop3 < 10; loop3++)
                cntr++;
       cout << cntr << endl;

   }




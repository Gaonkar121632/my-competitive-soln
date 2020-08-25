#include <iostream>
using namespace std;

int main()
{

    int num, reversedNumber = 0, remainder;
    cin >> num;
    int inputArray[num];
    for (size_t i = 0; i < num; i++)
    {
        cin >> inputArray[i];
    }

    for (size_t i = 0; i < num; i++)
    {
        if (inputArray[i] > 9)
        {
            int score=inputArray[i];
            while (score)
            {
                remainder =9-(score%10);
              //  cout<<9-(score%10);
                reversedNumber = reversedNumber*10 + remainder;
                score /= 10;
            }
            

            while(reversedNumber){
                 cout<<reversedNumber%10;
                 reversedNumber /= 10;
            }
            
            cout<<endl;
        }
        else
        {
            cout << 9 - inputArray[i] << endl;
        }
    }

    return 0;
}

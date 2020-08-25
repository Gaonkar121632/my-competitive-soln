//execution command
//cc <filename>.c
//./a.outv


#include <stdio.h>
#include <string.h>

char *reverse(char *stringArr, int low, int high,int* ptr)
{
   if (low >= high)
   {
      return stringArr;
   }
   else
   {

      char temp = *(stringArr + low);
      *(stringArr + low) = *(stringArr + high);
      *(stringArr + high) = temp;

      (*ptr)++;
      low++;
      high--;
      reverse(stringArr, low, high, ptr);
   }
}

void main()
{
   char input[15] = "abcdefghijk";  //do not include space in the input string
   int m = 5;
   printf("input is : %s\n", input);
   printf("M is : %d\n", m);

   int *p, count = 0;
   p = &count;

   char inputArr[15];
   char reversed[15];

   char firstHalf[10];
   char secondHalf[10];

   strcpy(inputArr, input);

   strcpy(reversed, input);
   reverse(reversed, 0, (strlen(input) - 1),p);
   // printf("%s\n", reversed);

   // strncpy(firstHalf, inputArr, m);
   // strncpy(secondHalf, input + m, (strlen(inputArr) - 1));

   for (size_t i = m, j = 0; i < strlen(input); i++, j++)
   {
      secondHalf[j] = input[i];
      if ((i + 1) == strlen(input))
      {
         secondHalf[i + 1] = '\0';
      }
   }

   for (size_t i = 0; i < m; i++)
   {
      firstHalf[i] = inputArr[i];
      if ((i + 1) == m)
      {
         firstHalf[i + 1] = '\0';
      }
   }

   printf("X1 is %s\n", firstHalf);
   reverse(firstHalf, 0, (strlen(firstHalf) - 1),p);
   printf("X1` is %s\n", firstHalf);

   printf("X2 is %s\n", secondHalf);
   reverse(secondHalf, 0, (strlen(secondHalf) - 1),p);
   printf("X2` is %s\n", secondHalf);

   strcat(secondHalf, firstHalf);

   printf("(X1X2)` is %s\n", reversed);
   printf("X2` X1` is %s\n", secondHalf);
   printf("total number of swaps %d\n", *p);

}
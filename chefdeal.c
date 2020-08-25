#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {

int random,given,out;
 
srandom(time(NULL));   // Initialization, should only be called once.
 random = rand()%3+1; 
printf("%d \n",random);
fflush(stdin);
scanf("%d",&given);
// fflush(stdin);

switch(random){
    case 1 : 
           switch (given)
           {
               case 2:
                printf("%d \n",3);
                fflush(stdin);

                break;
           
               default:
               printf("%d \n",2);
               fflush(stdin);

                   break;
           }
           break ;

    case 2 : 
           switch (given)
           {
               case 1:
                printf("%d \n",3);
                fflush(stdin);

                break;
           
               default:
               printf("%d \n",1);
               fflush(stdin);

                   break;
           }
           break ;
            
    case 3 :
           switch (given)
           {
               case 1:
                printf("%d \n",2);
                fflush(stdin);

                break;
           
               default:
               printf("%d \n",1);
               fflush(stdin);

                   break;
           }
           break ;
}

return 0;
}
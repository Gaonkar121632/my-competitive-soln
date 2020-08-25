#include <stdio.h>

int main()
{
int n,r;
int value[1000];

scanf("%d %d", &n,&r);


for (size_t i = 0; i < n; i++)
{
    int x;
    scanf("%d", &x);
    if (x) {
        value[i] = x;
    }
}


for(size_t i = 0; i < n; i++)
{
    (value[i] < r) ? printf("Bad boi\n") : printf("Good boi\n");
}
return 0;
}
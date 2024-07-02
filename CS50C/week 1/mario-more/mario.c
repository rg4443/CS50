#include <stdio.h>
#include <cs50.h>

void pyramid(int n)
{
    int spaces = n - 1;
    int hashes = 1;
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < spaces; j++)
        {
            printf(" ");
        }

        for (int j = 0; j < hashes; j++)
        {
            printf("#");
        }

        printf("  ");

        for (int j = 0; j < hashes; j++)
        {
            printf("#");
        }


        printf("\n");

        spaces --;
        hashes ++;
    }
}

int main(void)
{
    int n;
    do
    {
        n = get_int("Height: ");
        pyramid(n);
    } while (n < 1);
}




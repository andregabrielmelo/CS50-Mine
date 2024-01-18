#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n = get_int("Height: ");
    while (n < 1 || n > 8)
    {
        n = get_int("Height: ");
    }

    for (int i = 0; i < n; i++)
    {
        for (int sp = 0; sp < (n - 1 - i); sp++)
        {
            printf(" ");
        }
        for (int hs = 0; hs < (i + 1); hs++)
        {
            printf("#");
        }
        for (int sp = 0; sp < 2; sp++)
        {
            printf(" ");
        }
        for (int hs = 0; hs < (i + 1); hs++)
        {
            printf("#");
        }
        printf("\n");
    }
}
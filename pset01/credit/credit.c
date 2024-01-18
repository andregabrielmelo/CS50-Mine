#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long long CardNum;
    do
    {
        CardNum = get_long_long("Number: ");
    }
    while (CardNum < 0);

    int size = 0;
    {
        long long x = 1;
        while (x < CardNum)
        {
            x = x * 10;
            size++;
        }
    }

    long long div = 10;
    int sum = 0, order = size, t, t1, t2;
    for (int i = 0; i < size; i++, order--, div *= 10)
    {
        printf("Número #%i: %lli\n", (order), ((CardNum % div) / (div / 10)));

        if (i % 2 == 0)
        {
            sum += ((CardNum % div) / (div / 10));
        }
        else
        {
            sum += ((((CardNum % div) / (div / 10)) * 2) / 10) + (((CardNum % div) / (div / 10)) * 2) % 10;
        }

        if (order == 1)
        {
            t1 = ((CardNum % div) / (div / 10));
        }
        if (order == 2)
        {
            t2 = ((CardNum % div) / (div / 10));
        }
    }

    t = (t1 * 10) + t2;
    printf("First two digits: %i\n", t);
    printf("Size: %i\n", size);
    printf("Sum: %i\n", sum);

    if (sum % 10 == 0)
    {
        if ((t == 34 || t == 37) && size == 15)
        {
            printf("AMEX\n");
        }
        else if ((t > 50 && t < 56) && size == 16)
        {
            printf("MASTERCARD\n");
        }
        else if (t1 == 4 && size > 12 && size < 17)
        {
            printf("VISA\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }
}
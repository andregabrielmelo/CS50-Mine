#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int numBegin;
    do
    {
        numBegin = get_int("Start size: ");
    }
    while (numBegin < 9);

    // TODO: Prompt for end size
    int numEnd;
    do
    {
        numEnd = get_int("End size: ");
    }
    while (numEnd < numBegin);

    // TODO: Calculate number of years until we reach threshold
    int years = 0;
    int result = numBegin;
    while (result < numEnd)
    {
        result = result + (result / 3 - result / 4);
        years++;
    }

    // TODO: Print number of years
    printf("Years: %i\n", years);
}

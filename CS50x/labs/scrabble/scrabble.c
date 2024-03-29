#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

//
int upper_letters[] = {65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77,
                       78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90};

//
int lower_letters[] = {97,  98,  99,  100, 101, 102, 103, 104, 105, 106, 107, 108,
                       109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120};

int compute_score(string word);

int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // TODO: Print the winner
    printf("Player 1 score: %i\n", score1);
    printf("Player 2 score: %i\n", score2);

    if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    else if (score1 < score2)
    {
        printf("Player 2 wins!\n");
    }
    else if (score1 == score2 && score1 != 0)
    {
        printf("Tie!\n");
    }
    else
    {
        printf("Invalid input!\n");
    }
}

int compute_score(string word)
{
    // TODO: Compute and return score for string
    int score = 0, point;
    for (int i = 0; i < strlen(word); i++)
    {
        if (isupper(word[i]))
        {
            for (int l = 0; l < sizeof(upper_letters); l++)
            {
                if (word[i] == upper_letters[l])
                {
                    point = POINTS[l];
                    score += point;
                    if (i == (strlen(word) - 1))
                    {
                        printf("%i: %i\n", point, score);
                    }
                    else
                    {
                        printf("%i + ", point);
                    }
                }
            }
        }
        else if (islower(word[i]))
        {
            for (int l = 0; l < sizeof(lower_letters); l++)
            {
                if (word[i] == lower_letters[l])
                {
                    point = POINTS[l];
                    score += point;
                    if (i == (strlen(word) - 1))
                    {
                        printf("%i: %i\n", point, score);
                    }
                    else
                    {
                        printf("%i + ", point);
                    }
                }
            }
        }
        else
        {
        }
    }

    return score;
}

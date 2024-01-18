#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    string text = get_string("Text: ");

    // Get Number of Letters, Words and Sentences
    int letters = count_letters(text), words = count_words(text), sentences = count_sentences(text);
    // printf("%i letters\n", letters);
    // printf("%i words\n", words);
    // printf("%i sentences\n", sentences);

    // Calculate The Grade
    float L = (float) letters / (float) words * 100;
    float S = (float) sentences / (float) words * 100;
    int index = round(0.0588 * L - 0.296 * S - 15.8);

    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }
}

int count_letters(string text)
{
    int L = 0;
    for (int i = 0, text_lenght = strlen(text); i < text_lenght; i++)
    {
        if (isalpha(text[i]))
        {
            L++;
        }
    }

    return L;
}

int count_words(string text)
{
    int W = 1;
    for (int i = 0, text_lenght = strlen(text); i < text_lenght; i++)
    {
        if (text[i] == ' ')
        {
            W++;
        }
    }

    return W;
}

int count_sentences(string text)
{
    int S = 0;
    for (int i = 0, text_lenght = strlen(text); i < text_lenght; i++)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            S++;
        }
    }

    return S;
}

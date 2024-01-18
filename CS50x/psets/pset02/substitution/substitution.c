#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

const int num_alpha_letters = 26;
const string alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

int main(int argc, string argv[])
{
    char key[26];
    // Verify Input
    if (argc == 2)
    {
        for (int i = 0; i < num_alpha_letters; i++)
        {
            if (!(isalpha(argv[1][i])))
            {
                printf("Use letters only!");
                return 1;
            }

            for (int j = 0; j < i; j++)
            {
                if (argv[1][i] == argv[1][j])
                {
                    printf("Duplicated letters!");
                    return 1;
                }
            }

            key[i] = argv[1][i];
        }
    }
    else
    {
        printf("usage: ./substitution key\n");
        return 1;
    }

    // Get Text To Implement Substitution Cipher
    string plain_text = get_string("plaintext: ");
    // Make Both Equal So The Cipher Text Has As Much Memory As Plain Text
    string cipher_text = plain_text;

    // Substitution
    for (int i = 0; i < strlen(plain_text); i++)
    {
        for (int j = 0; j < num_alpha_letters; j++)
        {
            // Finding The Letter To Link The Indexes
            if (toupper(plain_text[i]) == alpha[j])
            {
                if (isupper(plain_text[i]))
                {
                    cipher_text[i] = toupper(key[j]);
                }
                else
                {
                    cipher_text[i] = tolower(key[j]);
                }
                break;
            }
        }
    }

    // Answer
    printf("ciphertext: %s\n", cipher_text);
    return 0;
}
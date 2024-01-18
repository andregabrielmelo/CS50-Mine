#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

string alphabet = "ABCDEFGHIJKLMNOPQRSTUV";

int main(int argc, string argv[])
{
    // Create Key
    char key[26];
    // One Command-line Argument
    if (argc == 2)
    {
        for (int i = 0; i < 26; i++)
        {
            key[i] = argv[1][i];

            for (int j = 0; j < i; j++)
            {
                if (toupper(key[i]) == toupper(key[j]))
                {
                    printf("Duplicate characters\n");
                    return 1;
                }
            }

            if (!(isalpha(key[i])))
            {
                printf("Key must contain 26 characters.\n");
                return 1;
            }
        }
    }
    // None or More Than One Command-line Argument
    else
    {
        printf("usage: ./substitution key\n");
        return 1;
    }

    // Get Normal Text
    string plain_text = get_string("plaintext: ");

    char cipher_text[strlen(plain_text)];
    for (int i = 0; i < strlen(plain_text); i++)
    {
        for (int j = 0; j < 26; j++)
        {
            if (toupper(plain_text[i]) == alphabet[j])
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

    printf("ciphertext: %s\n", cipher_text);
    return 0;

}
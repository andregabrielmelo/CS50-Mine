// Implements a dictionary's functionality

#include <ctype.h>
#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26 * 26 * 26; // Three first letters

// Hash table
node *table[N];

// Size of dictionary
long long int dictionary_size = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // Get hash value of the word, the bucket
    int hash_value = hash(word);

    // Point to linked list of specific bucket
    node *p = table[hash_value];

    // Loop through linked list
    while (p != NULL)
    {
        if (strcasecmp(word, p->word) == 0)
        {
            return true;
        }
        p = p->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    long long int bucket = 0; // bucket initialized to 0, AA and 0 length
    for (int i = 0, j = 2; i < 2; i++, j--)
    {
        if (isalpha(word[i]))
        {
            bucket = (toupper(word[i]) - 'A') * pow(26, j); // multiply first three characters of a word with a value to determine the hash
        }
    }
    return bucket;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // Open dictionary file
    FILE *dictionary_stream = fopen(dictionary, "r");

    // Check if there is enough memory
    if (dictionary_stream == NULL)
    {
        printf("Could not open dictionary");
        return false;
    }

    // Initialise new word array
    char next_word[LENGTH + 1];

    // Reading string
    while (fscanf(dictionary_stream, "%s", next_word) == 1)
    {
        // Create new node for each word
        node *new_node = malloc(sizeof(node)); // pointer to allocate memory
        if (new_node == NULL)                  // if it does not have memory, exit
        {
            printf("\nNot enough memory");
            unload();
            return false;
        }

        // Copy the next word into the new node
        strcpy(new_node->word, next_word);

        // Hash to obtain the hash value of the next word, number of the bucket
        int hash_value = hash(&next_word[0]);

        // Insert node at hash table
        new_node->next = table[hash_value]; // the new node points to the last node added
        table[hash_value] = new_node;       // the hash table points to the new node
        dictionary_size++;                  // Size of dictionary plus one
    }

    // Close file
    fclose(dictionary_stream);

    // Successfully loaded dictionary
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return dictionary_size;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int bucket = 0; bucket < N; bucket++)
    {
        node *p = table[bucket];

        while (p != NULL)
        {
            node *temp = p;
            p = p->next;
            free(temp);
        }
    }
    return true; // Successfully unloaded the dictionary
}

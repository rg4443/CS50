// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

// Hashes word to a number
unsigned int hash(const char *word)
{
    unsigned int hash_value = 0;
    for (int i = 0; word[i] != '\0'; i++)
    {
        hash_value = (hash_value * 31 + tolower(word[i])) % N;
    }
    return hash_value;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    FILE *dict = fopen(dictionary, "r");
    if (dict == NULL)
    {
        printf("Error: Could not open dictionary\n");
        return false;
    }

    char word[LENGTH + 1];
    while (fscanf(dict, "%s", word) != EOF)
    {
        // Convert words to lowercase of case-insensitive
        for (int i = 0; word[i] != '\0'; i++)
        {
            word[i] = tolower(word[i]);
        }


        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            fclose(dict);
            printf("Error: Could not allocate memory for new node\n");
            return false;
        }
        strcpy(n->word, word);
        int index = hash(word);
        n->next = table[index];
        table[index] = n;
    }

    fclose(dict);
    return true;
}

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // Convert words to lowercase for case-insensitive spell checking
    char lower_word[LENGTH + 1];
    strcpy(lower_word, word); // turn "lower_word" into word

    for (int i = 0; lower_word[i] != '\0'; i++)
    {
        lower_word[i] = tolower(lower_word[i]);
    }


    // Main stuff
    int index = hash(lower_word);

    node *cursor = table[index];
    while (cursor != NULL)
    {
        if (strcmp(cursor->word, lower_word) == 0)
        {
            return true; // word is found
        }
        cursor = cursor->next; // Go to next node
    }
    return false; // Word not found
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    unsigned int total_words = 0;
    for (unsigned int i = 0; i < N; i++)
    {
        node *cursor = table[i];
        while (cursor != NULL)
        {
            total_words++;
            cursor = cursor->next;
        }
    }
    return total_words;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        node *cursor = table[i];
        while (cursor != NULL)
        {
            node *tmp = cursor;
            cursor = cursor->next;
            free(tmp);
        }
    }
    return true;
}

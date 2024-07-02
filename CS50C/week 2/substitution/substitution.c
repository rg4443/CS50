#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

// function that is going to decipher whatever input is given
string cyphertext(string key, string plaintext)
{
    // create a mapping that has all of the alphabetical letters
    char mapping[26];
    for(int i = 0; i < 26; i++)
    {
        mapping[i] = 'a' + i;
    }

    // assigns key to the mapping
    for(int i = 0; i < strlen(key); i++)
    {
        int index = tolower(key[i]) - 'a';
        mapping[i] = key[i];
    }

    // create an array that will have all of the plain text then turned into cyphertext
    string cyphertext = malloc(strlen(plaintext)) + 1; // + 1 for the null terminator

    // goes through each char of the plain text and turns it into cyphered text
    for(int i = 0; i < strlen(plaintext); i++)
    {
        // get the current char in the iteration
        char current_char = plaintext[i];
        // check if it is a lowercased alphabetical letter
        if('a' <= current_char && current_char <= 'z')
        {
            int index = current_char - 'a';
            // replace the plaintext to chyphered text
            cyphertext[i] += tolower(mapping[index]);
        }
        // else if the letter is an uppercased alphabetical letter
        else if ('A' <= current_char && current_char <= 'Z')
        {
            int index = current_char - 'A';
            // replace the plaintext to chyphered text
            cyphertext[i] += toupper(mapping[index]);
        }
        else
        {
            // if the char is not an alphabetical char then leave as is
            cyphertext[i] += current_char;
        }
    }
    cyphertext[strlen(plaintext)] = '\0';
    return cyphertext;
}

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: %s key\n", argv[0]);
        return 1;
    }

    // assign argc to a variable and use it to see if it has 26 chars
    string second_arg = argv[1];
    int count = 0;
    // for every char in length of the second cmd arg update count and make sure that it is 26
    for (int i = 0; i < strlen(second_arg); i++)
    {
        count ++;
        char current_char = second_arg[i];
        // make sure that the key does not have any duplicates
        for (int j = i + 1; j < strlen(second_arg);  j++)
        {
            if (current_char == second_arg[j])
            {
                printf("Error: Key must not have duplicate chars");
                return 1;
            }
        }
        // make sure that each char in key is not a special char
        if(!isalpha(current_char) && !isdigit(current_char))
        {
            printf("Key must be alphabetical or have numbers");
            return 1;
        }
    }

    if (count != 26)
    {
        printf("Error: Key Must be 26 chars\n");
        return 1;
    }

    // MAIN PART OF FUNCTION PROMTS USER FOR PLAIN TEXT AND USES THAT PUTS IT INTO CYPHERTEXT FUNCTION
    string plaintext = get_string("Plaintext: ");
    string cypher_text = cyphertext(second_arg, plaintext);

    printf("ciphertext: %s\n", cypher_text);

    return 0;
}

#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int grade_level(string text)
{
    int text_chars = 0;
    int text_words = 1;
    int text_sentences = 0;

    int length = strlen(text);
    for (int i = 0; i < length; i++)
    {
        // for every char that is alphabetical then add it so the text_chars
        if (isalpha(text[i]))
        {
            text_chars ++;
        }

        // for every char that has a space then add it to the amount of words
        else if (isspace(text[i]))
        {
            text_words ++;
        }

        // for each . ! ? in the text.lenght add to the text_sentences
        else if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            text_sentences ++;
        }

    }
    float L = (float) text_chars / text_words * 100.0;
    float S = (float) text_sentences / text_words * 100.0;

    int coleman_liau_index = round(0.0588 * L - 0.296 * S - 15.8);

    return coleman_liau_index;

}

int main(void)
{
    string text = get_string("Text : ");
    int grade = grade_level(text);

    if (grade >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", grade);
    }
}

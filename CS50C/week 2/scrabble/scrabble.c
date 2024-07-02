#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int scrabble(string input)
{
    int w[26];
    for(int i = 0; i < w[i]; i++)
    {
        w[i] = 'a' + i;
    }
    // giving each letter the value it corresponds to
    w[0] = 1;
    w[1] = 3;
    w[2] = 3;
    w[3] = 2;
    w[4] = 1;
    w[5] = 4;
    w[6] = 2;
    w[7] = 4;
    w[8] = 1;
    w[9] = 8;
    w[10] = 5;
    w[11] = 1;
    w[12] = 3;
    w[13] = 1;
    w[14] = 1;
    w[15] = 3;
    w[16] = 10;
    w[17] = 1;
    w[18] = 1;
    w[19] = 1;
    w[20] = 1;
    w[21] = 4;
    w[22] = 4;
    w[23] = 8;
    w[24] = 4;
    w[25] = 10;

    // connect the logic that for every char update the count by its respective value
    int count = 0;
    for (int i = 0; i < strlen(input); i++)
    {
        // convert to lowercase
        char lowercased_input = tolower(input[i]);
        if (lowercased_input >= 'a' && lowercased_input <= 'z')
        {
            count += w[lowercased_input - 'a'];
        }

    }
    return count;

}

int main(void)
{
    string player_1 = get_string("Player 1: ");
    string player_2 = get_string("Player 2: ");

    // Calculate the Scrabble score for each player
    int scrabble_player_1_value = scrabble(player_1);
    int scrabble_player_2_value = scrabble(player_2);

    if (scrabble_player_1_value > scrabble_player_2_value)
    {
        printf("Player 1 wins!\n");
    }
    else if (scrabble_player_1_value < scrabble_player_2_value)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }


}

#include <stdio.h>
#include <cs50.h>

// Step 1: Get every other digit and mutiply it by 2

int credit_card(long num)
{
    int count = 0;
    int sum = 0;
    int first_two_digits = 0;
    while (num > 0)
    {
        int digit = num % 10;
        if (count % 2 == 0)
        {
            sum += digit;
        }
        else
        {
            digit *= 2;
            sum += digit % 10 + digit / 10;
        }
        if (num < 100 && num >= 10) // Check if we're at the first two digits
        {
            first_two_digits = num;
        }

        num /= 10;
        count++;
    }
    // Check if it's a Mastercard
    if ((first_two_digits == 51 || first_two_digits == 52 || first_two_digits == 53 || first_two_digits == 54 || first_two_digits == 55) && count == 16)
    {
        return 1; // Mastercard
    }
}


int main(void)
{
    long user_input = get_long("Number: ");
    int card_type = credit_card(user_input);

    if (card_type == 1)
    {

        printf("MASTERCARD\n");
    }
    else if(card_type == 2)
    {
        printf("VISA\n");
    }
    else if(card_type == 3)
    {
        printf("AMEX\n");
    }
    else
    {
        printf("INVALID\n");
    }
}

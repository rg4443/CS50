#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

// PLAN:
// Iterate until find jpeg image (bits that start with 0xff 0xd8 0xff)
// Each time ^ is found, write into file with bytes from memory card, closing once another jpeg image is found
// Read aT 512 bytes at a time into a buffer


int main(int argc, char *argv[])
{
    // Accept only one cmd arg
    if (argc != 2)
    {
        printf("Usuage: ./recover FILE\n");
        return 1;
    }

    // Open memory card
    FILE *card = fopen(argv[1], "r");

    // Make sure that the memory card was opened properly
    if (!card)
    {
        printf("Error: Memory card was not opened properly\n");
        return 1;
    }

    uint8_t buffer[512]; // create buffer of 512 bits
    FILE *img = NULL; // Pointer so that it can become a global variable
    int file_count = 0; // Keep track of file count in case we need to close

    // While there is still data left to read from the memory card
    while (fread(buffer, 1, 512, card) == 512)
    {
        // Find jpeg image
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff)
        {
            // Close previous files if any
            if (img != NULL)
            {
                fclose(img);
            }

            // Create JPEGS from data
            char filename[20];
            sprintf(filename, "%03i.jpg", file_count++);
            img = fopen(filename, "w");

            // Write data to file until finding end of file
            fwrite(buffer, 1, 512, img);
        }
        else if (img != NULL)
        {
            // If already found JPEG Continue writing
            fwrite(buffer, 1, 512, img);
        }
    }

    // Close file
    fclose(card);
    if (img != NULL)
    {
        fclose(img);
    }

    return 0; // return for successful execution
}

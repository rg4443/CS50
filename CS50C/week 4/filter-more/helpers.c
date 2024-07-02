#include "helpers.h"
#include <math.h>

// Convert image to grayscale

void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // Loop through the images pixels (height and width)
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Get the average rbg value for every pixel
            float sum = image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed;
            int average = round(sum / 3);

            // Turn the new pixel into a shade of grey
            image[i][j].rgbtRed = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtBlue = average;
        }
    }
    return;
}

// Reflect image horizontally

void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // Loop through all of the pixels
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++) // Only get half the image
        {
            RGBTRIPLE temp = image[i][j]; // Create a temporary varaible to store the pixels

            // Swap pixels
            image[i][j] = image[i][width - 1 - j];
            image[i][width - 1 - j] = temp;
        }
    }
    return;
}

// Blur image

void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Create a temporary image
    RGBTRIPLE temp[height][width];

    // Loop through every pixel in the image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Initialize values for the red, green, and blue values
            int new_red = 0;
            int new_blue = 0;
            int new_green = 0;
            int count = 0;

            // Create the 3x3 box around each pixel
            for (int k = -1; k <= 1; k++)
            {
                for (int l = -1; l <= 1; l++)
                {
                    int ik = i + k;
                    int jl = j + l;

                    // Check if the surrounding pixels are within the image's boundary
                    if (0 <= ik && ik < height && 0 <= jl && jl < width)
                    {
                        new_red += image[ik][jl].rgbtRed;
                        new_blue += image[ik][jl].rgbtBlue;
                        new_green += image[ik][jl].rgbtGreen;
                        count++;
                    }
                }
            }
            // Calculate the average RGB values and assign to the temporary image
            temp[i][j].rgbtRed = round((float)new_red / count);
            temp[i][j].rgbtBlue = round((float)new_blue / count);
            temp[i][j].rgbtGreen = round((float)new_green / count);
        }
    }
    // Copy the resulting values onto the original image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = temp[i][j];
        }
    }

    return;
}




// Detect edges

// PLAN:
// For every pixel but a 3x3 grid onto it like the blur
// Take the gx kernal and multipy the corresponding values then add the results
//

// resulting integer needs to be capped at 255 and rounded to the nearest whole integer
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    // Create a temporary image
    RGBTRIPLE temp[height][width];

    // Define gx and gy kernals from sobel operator
    int Gx_kernel[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
    int Gy_kernel[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};

    // Loop through the images pixels
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {

            // Initilize gx to store values in
            int Gx_red = 0;
            int Gx_blue = 0;
            int Gx_green = 0;

            int Gy_red = 0;
            int Gy_blue = 0;
            int Gy_green = 0;

            // Create 3x3 grid
            for (int k = -1; k <= 1; k++)
            {
                for (int l = -1; l <= 1; l++)
                {
                    // Get the pixels surrounding target pixel
                    int ik = i + k;
                    int jl = j + l;

                    if (0 <= ik && ik < height && 0 <= jl && jl < width)
                    {
                        // Apply Gx kernel
                        Gx_red += image[ik][jl].rgbtRed * Gx_kernel[k + 1][l + 1];
                        Gx_green += image[ik][jl].rgbtGreen * Gx_kernel[k + 1][l + 1];
                        Gx_blue += image[ik][jl].rgbtBlue * Gx_kernel[k + 1][l + 1];

                        // Apply Gy kernel
                        Gy_red += image[ik][jl].rgbtRed * Gy_kernel[k + 1][l + 1];
                        Gy_green += image[ik][jl].rgbtGreen * Gy_kernel[k + 1][l + 1];
                        Gy_blue += image[ik][jl].rgbtBlue * Gy_kernel[k + 1][l + 1];
                    }
                }
            }

            // Add two values together
            float gradient_mag_red = round(sqrt(Gx_red * Gx_red + Gy_red * Gy_red));
            float gradient_mag_green = round(sqrt(Gx_green * Gx_green + Gy_green * Gy_green));
            float gradient_mag_blue = round(sqrt(Gx_blue * Gx_blue + Gy_blue * Gy_blue));

            // Make sure that each value is capped at 255
            int edge_intensity_red = (int)fmin(255, fmax(0, gradient_mag_red));
            int edge_intensity_green = (int)fmin(255, fmax(0, gradient_mag_green));
            int edge_intensity_blue = (int)fmin(255, fmax(0, gradient_mag_blue));

            // Assign new pixels
            temp[i][j].rgbtRed = edge_intensity_red;
            temp[i][j].rgbtGreen = edge_intensity_green;
            temp[i][j].rgbtBlue = edge_intensity_blue;
        }
    }

    // Copy into new image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = temp[i][j];
        }
    }
}

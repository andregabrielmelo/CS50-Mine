#include <math.h>

#include "helpers.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int average_rgbt = 0;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            average_rgbt = round((image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3.0);
            image[i][j].rgbtBlue = average_rgbt;
            image[i][j].rgbtGreen = average_rgbt;
            image[i][j].rgbtRed = average_rgbt;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE swap = {0, 0, 0};
    // Loop through the matrix
    for (int i = 0; i < height; i++)
    {
        // Swap #i element with the #(width - j) element
        for (int j = 0; j < width / 2; j++)
        {
            swap = image[i][j];
            image[i][j] = image[i][width - 1 - j];
            image[i][width - 1 - j] = swap;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];

    // Creates a copy to mantain the original values of the pixels
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            temp[i][j] = image[i][j];
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int red_sum = 0;
            int green_sum = 0;
            int blue_sum = 0;
            float count = 0.0;

            // Form matrix with neighbouring pixels
            for (int x = -1; x < 2; x++)
            {
                for (int y = -1; y < 2; y++)
                {
                    // Check if neighbouring pixel is within the bounds of the matrix
                    if ((i + x) >= 0 && (i + x) < height && (j + y) >= 0 && (j + y) < width)
                    {
                        // Sum each color of the matrix
                        red_sum += temp[i + x][j + y].rgbtRed;
                        green_sum += temp[i + x][j + y].rgbtGreen;
                        blue_sum += temp[i + x][j + y].rgbtBlue;

                        count++;
                    }
                }
            }

            // Change the image matrix color values with the new values
            image[i][j].rgbtRed = round(red_sum / count);
            image[i][j].rgbtGreen = round(green_sum / count);
            image[i][j].rgbtBlue = round(blue_sum / count);
        }
    }
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];

    // Creates a copy to mantain the original values of the pixels
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            temp[i][j] = image[i][j];
        }
    }

    int gx[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
    int gy[3][3] = {{1, 2, 1}, {0, 0, 0}, {-1, -2, -1}};

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // 0 for x axis and 1 for y axis
            int red_sum[2] = {0}, green_sum[2] = {0}, blue_sum[2] = {0};

            // Form matrix with neighbouring pixels
            for (int x = -1; x < 2; x++)
            {
                for (int y = -1; y < 2; y++)
                {
                    // Check if neighbouring pixel is within the bounds of the matrix
                    if ((i + x) >= 0 && (i + x) < height && (j + y) >= 0 && (j + y) < width)
                    {
                        // Gx sum of each color
                        red_sum[0] += temp[i + x][j + y].rgbtRed * gx[x + 1][y + 1];
                        green_sum[0] += temp[i + x][j + y].rgbtGreen * gx[x + 1][y + 1];
                        blue_sum[0] += temp[i + x][j + y].rgbtBlue * gx[x + 1][y + 1];

                        // Gy sum of each color
                        red_sum[1] += temp[i + x][j + y].rgbtRed * gy[x + 1][y + 1];
                        green_sum[1] += temp[i + x][j + y].rgbtGreen * gy[x + 1][y + 1];
                        blue_sum[1] += temp[i + x][j + y].rgbtBlue * gy[x + 1][y + 1];
                    }
                }
            }

            // squareroot of (Gx^2 + Gy^2) are the new RGB
            int red = round(sqrt(pow(red_sum[0], 2) + pow(red_sum[1], 2)));
            int green = round(sqrt(pow(green_sum[0], 2) + pow(green_sum[1], 2)));
            int blue = round(sqrt(pow(blue_sum[0], 2) + pow(blue_sum[1], 2)));

            // New RGB values
            image[i][j].rgbtRed = (red > 255) ? 255 : red;
            image[i][j].rgbtGreen = (green > 255) ? 255 : green;
            image[i][j].rgbtBlue = (blue > 255) ? 255 : blue;
        }
    }
    return;
}
i, j - 1
i, j
i, j + 1
i - 1, j + 1
i + 1, j + 1
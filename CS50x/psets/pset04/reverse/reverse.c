#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "wav.h"

int check_format(WAVHEADER header);
int get_block_size(WAVHEADER header);

int main(int argc, char *argv[])
{
    int header_size = sizeof(WAVHEADER); // store the size of the header of a .wav file

    // Ensure proper usage
    if (argc != 3)
    {
        printf("usage: ./reverse input.wav wav.h");
    }

    // Open input file for reading
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    // Read header
    WAVHEADER header;                      // variable to keep the header
    fread(&header, header_size, 1, input); // read from input, one time, 44 bytes, and pass it to header variable
    if (ftell(input) != header_size)       // see if it 44 bytes
    {
        printf("Error when reading.");
    }

    // Use check_format to ensure WAV format
    int check = check_format(header);
    if (check != 0)
    {
        printf("It is not a .wav file.\n");
        return 2;
    }

    // Open output file for writing
    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    // Write header to file
    fwrite(&header, header_size, 1, output);

    // Use get_block_size to calculate size of block
    int block_size = get_block_size(header);

    // Write reversed audio to file
    BYTE block[block_size];    // array to store a block
    fseek(input, 0, SEEK_END); // move the pointer to the end of the file

    long audio_size = ftell(input) - header_size;    // get the size of the audio data
    int audio_block = (int) audio_size / block_size; // quantity of blocks in the audio data

    // Iterate through the blocks reversed
    for (int i = audio_block - 1; i >= 0; i--)
    {
        // Starting from the end of the file
        fseek(input, header_size + i * block_size, SEEK_SET); // Go to beggining of the block not yet read closest to the end of the file
        fread(block, block_size, 1, input);                  // read the block
        fwrite(block, block_size, 1, output);                // write the block
    }

    // Close files
    fclose(input);
    fclose(output);
}

int check_format(WAVHEADER header)
{
    char format[5] = "WAVE"; // Include space for the null-terminator

    char headerFormatStr[5]; // Convert the header.format array to a null-terminated string
    strncpy(headerFormatStr, (const char *) header.format, 4);
    headerFormatStr[4] = '\0'; // Null-terminate the string

    // If it matches, return true, else, return false
    return strcmp(headerFormatStr, format);
}

int get_block_size(WAVHEADER header)
{
    int block_size = header.numChannels * header.bitsPerSample / 8; // 8 bits is one byte
    return block_size;
}
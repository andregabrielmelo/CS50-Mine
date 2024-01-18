#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// Candidates have name and vote count
typedef struct
{
    string name;
    int votes;
} candidate;

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototypes
bool vote(string name);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }

    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count = get_int("Number of voters: ");

    // Loop over all voters
    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");

        // Check for invalid vote
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
    }

    // Display winner of election
    print_winner();
}

// Update vote totals given a new vote
bool vote(string name)
{
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcmp(name, candidates[i].name) == 0)
        {
            candidates[i].votes++;
            return true;
        }
    }

    printf("%s is not a candidate", name);
    return false;
}

// Print the winner (or winners) of the election
void print_winner(void)
{
    int highest_votes = candidates[0].votes, winner[candidate_count], count_winners = 0;
    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes > highest_votes)
        {
            highest_votes = candidates[i].votes;
            winner[0] = i;
            count_winners = 1;
        }
        else if (candidates[i].votes == highest_votes)
        {
            winner[count_winners] = i;
            count_winners++;
        }
        // printf("%s %i votes\n", candidates[i].name, candidates[i].votes);
    }

    // printf("Winner(s): \n");
    for (int i = 0; i < count_winners; i++)
    {
        printf("%s\n", candidates[winner[i]].name);
        // printf("%s with %i votes\n", candidates[winner[i]].name, candidates[winner[i]].votes);
    }

    return;
}
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// preferences[i][j] is number of voters who prefer i over j
int preferences[MAX][MAX];

// locked[i][j] means i is locked in over j
bool locked[MAX][MAX];

// Each pair has a winner, loser
typedef struct
{
    int winner;
    int loser;
}
pair;

// Array of candidates
string candidates[MAX];
pair pairs[MAX * (MAX - 1) / 2];

int pair_count;
int candidate_count;

// New Function
bool has_cycle(int winner, int loser);

// Function prototypes
bool vote(int rank, string name, int ranks[]);
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
void lock_pairs(void);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: tideman [candidate ...]\n");
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
        candidates[i] = argv[i + 1];
    }

    // Clear graph of locked in pairs
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            locked[i][j] = false;
        }
    }

    pair_count = 0;
    int voter_count = get_int("Number of voters: ");

    // Query for votes
    for (int i = 0; i < voter_count; i++)
    {
        // ranks[i] is voter's ith preference
        int ranks[candidate_count];

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            if (!vote(j, name, ranks))
            {
                printf("Invalid vote.\n");
                return 3;
            }
        }

        record_preferences(ranks);

        printf("\n");
    }

    add_pairs();
    sort_pairs();
    lock_pairs();
    print_winner();
    return 0;
}

// Update ranks given a new vote
bool vote(int rank, string name, int ranks[])
{
    // TODO
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcmp(name, candidates[i]) == 0)
        {
            ranks[rank] = i;
            return true;
        }
    }

    // printf("%s is not a candidate", name);
    return false;
}

// Update preferences given one voter's ranks
void record_preferences(int ranks[])
{
    // TODO
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = i + 1; j < candidate_count; j++)
        {
            preferences[ranks[i]][ranks[j]]++;
        }
    }
    /*
    printf("\nPreferences: \n");
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            printf("%i ", preferences[i][j]);
        }
        printf("\n");
    }
    */
    return;
}

// Record pairs of candidates where one is preferred over the other
void add_pairs(void)
{
    // TODO
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            if (preferences[i][j] > preferences[j][i])
            {
                pairs[pair_count].winner = i;
                pairs[pair_count].loser = j;
                pair_count++;
            }
        }
    }
    /*
    for (int i = 0; i < pair_count; i++)
    {
        printf("Pair #%i: %i(winner) and %i(loser)\n", i+1, pairs[i].winner, pairs[i].loser);
    }
    printf("Number of pairs: %i\n", pair_count);
    */
    return;
}

// Sort pairs in decreasing order by strength of victory
void sort_pairs(void)
{
    // TODO
    // printf("\nSorted pairs:\n");
    pair swap;
    for (int i = pair_count - 1; i > 0; i--)
    {
        if (pairs[i].winner - pairs[i].loser < pairs[i-1].winner - pairs[i-1].loser)
        {
            swap = pairs[i];
            pairs[i] = pairs[i-1];
            pairs[i-1] = swap;
            i = 0;
        }
    }
    return;
}

// Check if there is a cycle
bool has_cycle(int winner, int loser)
{
    for (int i = 0; i < candidate_count; i++)
    {
        if (locked[loser][i])
        {
            if (i == winner || has_cycle(winner, i))
            {
                return true;
            }
        }
    }
    return false;
}

// Lock pairs into the candidate graph in order, without creating cycles
void lock_pairs(void)
{
    // TODO
    for (int i = 0; i < pair_count; i++)
    {
        int winner = pairs[i].winner;
        int loser = pairs[i].loser;
        if (!has_cycle(winner, loser))
        {
            locked[winner][loser] = true;
            //printf("Arrow from %s to %s\n", candidates[pairs[i].winner], candidates[pairs[i].loser]);
        }
    }
    return;
}

// Print the winner of the election
void print_winner(void)
{
    // TODO
    int times_beaten = 0, least_beater = candidate_count;
    for (int i = 0; i < candidate_count; i++)
    {
        times_beaten = 0;
        for (int j = 0; j < candidate_count; j++)
        {
            if (!locked[i][j])
            {
                times_beaten++;
            }
        }

        if (times_beaten < least_beater)
        {
            least_beater = times_beaten;
        }
    }


    for (int i = 0; i < candidate_count; i++)
    {
        times_beaten = 0;
        for (int j = 0; j < candidate_count; j++)
        {
            if (!locked[i][j])
            {
                times_beaten++;
            }
        }

        if (times_beaten == least_beater)
        {
           printf("%s\n", candidates[i]);
        }
    }

    return;
}
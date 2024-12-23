#include <cs50.h>
#include <stdio.h>

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
} pair;

// Array of candidates
string candidates[MAX];
pair pairs[MAX * (MAX - 1) / 2];

int pair_count;
int candidate_count;

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
    for (int i = 0; i < candidate_count; i++)
    {
        if(name == candidates[i])
        {
            // Update ranks array
            ranks[rank] = i; // Set the rank of the candidate to the provided rank
            return true;
        }
    }
    return false;
}

// Update preferences given one voter's ranks
void record_preferences(int ranks[])
{
    // loop through the pairs and assign i over j in the preferences array
    for(int i = 0; i < candidate_count; i++)
    {
        for(int j = i + 1; j < candidate_count; j++)
        {
            if(ranks[i] < ranks[j])
            {
                preferences[i][j]++;
            }
            else
            {
                preferences[j][i]++;
            }
        }
    }
    return;
}

// Record pairs of candidates where one is preferred over the other
void add_pairs()
{
    // loop through pairs and add pairs to array
    for(int i = 0; i < candidate_count; i++)
    {
        for(int j = i + 1; j < candidate_count; j++)
        {
            if(preferences[i][j] < preferences[j][i]) // if i is prefered over j then show that i is winner
            {
               pairs[pair_count].winner = i;
               pairs[pair_count].loser = j;
               pair_count ++; // increment count for pairs
            }
            else if(preferences[i][j] > preferences[j][i]) // if j is prefeered over i then do opposite
            {
                pairs[pair_count].winner = j;
                pairs[pair_count].loser = i;
                pair_count ++; // increment count for pairs
            }
        }
    }
    return;
}


// Sort pairs in decreasing order by strength of victory
void sort_pairs(void)
{
    for (int i = 0; i < pair_count - 1; i++)
    {
        for (int j = 0; j < pair_count - i - 1; j++)
        {
            // Calculate the strength of victory for each pair
            int strength1 = preferences[pairs[j].winner][pairs[j].loser];
            int strength2 = preferences[pairs[j + 1].winner][pairs[j + 1].loser];

            // If the strength of victory for the current pair is less than the next pair, swap them
            if (strength1 < strength2)
            {
                pair temp = pairs[j];
                pairs[j] = pairs[j + 1];
                pairs[j + 1] = temp;
            }
        }
    }
}


// Helper function to perform depth-first search (DFS) to detect cycles
bool is_cycle(int end, bool visited[])
{
    // If end node is already visited, then it's a cycle
    if (visited[end])
    {
        return true;
    }

    // Mark the end node as visited
    visited[end] = true;

    // Recursively check if there is a cycle starting from end node
    for (int i = 0; i < candidate_count; i++)
    {
        if (locked[end][i] && is_cycle(i, visited))
        {
            return true;
        }
    }

    // If no cycle found starting from end node
    visited[end] = false;
    return false;
}

// Lock pairs into the candidate graph in order, without creating cycles
void lock_pairs(void)
{
    // Array to keep track of visited nodes during DFS
    bool visited[candidate_count];
    for (int i = 0; i < candidate_count; i++)
    {
        visited[i] = false;
    }

    // Iterate through sorted pairs
    for (int i = 0; i < pair_count; i++)
    {
        // Temporarily lock the current pair
        locked[pairs[i].winner][pairs[i].loser] = true;

        // Check for cycle
        if (is_cycle(pairs[i].loser, visited))
        {
            // If cycle detected, unlock the current pair
            locked[pairs[i].winner][pairs[i].loser] = false;
        }
    }
}



// Print the winner of the election
void print_winner(void)
{
    for (int i = 0; i < candidate_count; i++)
    {
        bool winner = true;

        for (int j = 0; j < candidate_count; j++)
        {
            if (locked[j][i]) // If candidate j is locked by candidate i
            {
                winner = false; // Candidate i is not the winner
                break;
            }
        }

        if (winner)
        {
            printf("%s\n", candidates[i]);
            return;
        }
    }
}


import csv
import itertools
import sys

PROBS = {

    # Unconditional probabilities for having gene
    "gene": {
        2: 0.01,
        1: 0.03,
        0: 0.96
    },

    "trait": {

        # Probability of trait given two copies of gene
        2: {
            True: 0.65,
            False: 0.35
        },

        # Probability of trait given one copy of gene
        1: {
            True: 0.56,
            False: 0.44
        },

        # Probability of trait given no gene
        0: {
            True: 0.01,
            False: 0.99
        }
    },

    # Mutation probability
    "mutation": 0.01
}


def main():

    # Check for proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python heredity.py data.csv")
    people = load_data(sys.argv[1])

    # Keep track of gene and trait probabilities for each person
    probabilities = {
        person: {
            "gene": {
                2: 0,
                1: 0,
                0: 0
            },
            "trait": {
                True: 0,
                False: 0
            }
        }
        for person in people
    }

    # Loop over all sets of people who might have the trait
    names = set(people)
    for have_trait in powerset(names):

        # Check if current set of people violates known information
        fails_evidence = any(
            (people[person]["trait"] is not None and
             people[person]["trait"] != (person in have_trait))
            for person in names
        )
        if fails_evidence:
            continue

        # Loop over all sets of people who might have the gene
        for one_gene in powerset(names):
            for two_genes in powerset(names - one_gene):

                # Update probabilities with new joint probability
                p = joint_probability(people, one_gene, two_genes, have_trait)
                update(probabilities, one_gene, two_genes, have_trait, p)

    # Ensure probabilities sum to 1
    normalize(probabilities)

    # Print results
    for person in people:
        print(f"{person}:")
        for field in probabilities[person]:
            print(f"  {field.capitalize()}:")
            for value in probabilities[person][field]:
                p = probabilities[person][field][value]
                print(f"    {value}: {p:.4f}")


def load_data(filename):
    """
    Load gene and trait data from a file into a dictionary.
    File assumed to be a CSV containing fields name, mother, father, trait.
    mother, father must both be blank, or both be valid names in the CSV.
    trait should be 0 or 1 if trait is known, blank otherwise.
    """
    data = dict()
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            data[name] = {
                "name": name,
                "mother": row["mother"] or None,
                "father": row["father"] or None,
                "trait": (True if row["trait"] == "1" else
                          False if row["trait"] == "0" else None)
            }
    return data


def powerset(s):
    """
    Return a list of all possible subsets of set s.
    """
    s = list(s)
    return [
        set(s) for s in itertools.chain.from_iterable(
            itertools.combinations(s, r) for r in range(len(s) + 1)
        )
    ]


def joint_probability(people, one_gene, two_genes, have_trait):
    """
    Compute and return a list of probabilities.

    The probabilities returned should be for each person in the family:
        * the probability that they have the trait, and
        * the probability that they do not have the trait.
    """
    prob = 1

    for person in people:
        gene_count = count_genes(person, one_gene, two_genes)
        has_trait = person in have_trait

        mother = people[person]["mother"]
        father = people[person]["father"]

        if mother is None and father is None:
            prob *= PROBS["gene"][gene_count]
        else:
            inherited_probabilities = {mother: 0, father: 0}

            for parent in inherited_probabilities:
                if parent in two_genes:
                    inherit_prob = 1 - PROBS["mutation"]
                elif parent in one_gene:
                    inherit_prob = 0.5
                else:
                    inherit_prob = PROBS["mutation"]

                inherited_probabilities[parent] = inherit_prob

            if gene_count == 2:
                prob *= inherited_probabilities[mother] * inherited_probabilities[father]

            elif gene_count == 1:
                prob *= (inherited_probabilities[mother] * (1 - inherited_probabilities[father]) +
                         inherited_probabilities[father] * (1 - inherited_probabilities[mother]))
            else:
                prob *= (1 - inherited_probabilities[father]) * (1 - inherited_probabilities[mother])

        prob *= PROBS["trait"][gene_count][has_trait]

    return prob

def update(probabilities, one_gene, two_genes, have_trait, p):
    """
    Add to `probabilities` a new joint probability `p`.
    Each person should have their "gene" and "trait" distributions updated.
    Which value for each distribution is updated depends on whether
    the person is in `have_gene` and `have_trait`, respectively.
    """
    for person in probabilities:
        gene_count = count_genes(person, one_gene, two_genes)

         # Update gene distribution
        probabilities[person]["gene"][gene_count] += p

        # Update trait distribution
        probabilities[person]["trait"][person in have_trait] += p

def count_genes(person, one_gene, two_genes):
    """
    Count the number of genes a person has based on the given sets.
    """
    if person in two_genes:
        return 2
    elif person in one_gene:
        return 1
    else:
        return 0

def normalize(probabilities):
    """
    Update `probabilities` such that each probability distribution
    is normalized (i.e., sums to 1, with relative proportions the same).
    """
    for person in probabilities:
        # Normalize gene distribution
        gene_sum = sum(probabilities[person]["gene"].values())
        for gene in probabilities[person]["gene"]:
            probabilities[person]["gene"][gene] /= gene_sum

        # Normalize trait distribution
        trait_sum = sum(probabilities[person]["trait"].values())
        for trait in probabilities[person]["trait"]:
            probabilities[person]["trait"][trait] /= trait_sum



if __name__ == "__main__":
    main()

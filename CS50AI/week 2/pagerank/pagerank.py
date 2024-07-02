import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    total_pages = len(corpus)
    distribution = {}

    # check if the page has any outgoing links
    if page in corpus and corpus[page]:
        # Calclulate the probablbity of the web surfer by doing mathamtical expression
        link_probability = damping_factor / len(corpus[page])

        # Assign probabilities to pages from the current page
        for linked_page in corpus[page]:
            distribution[linked_page] = link_probability

    # Calculate the probability of choosing a link from the corpus
    all_page_probabilities = (1 - damping_factor) / total_pages

    # Assign the probabilities to all of the pages in the corpus
    for page in corpus:
        distribution.setdefault(page, 0)
        distribution[page] += all_page_probabilities

    return distribution


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # Initilize the pagerank with 0's
    pagerank = {page: 0 for page in corpus}

    # Choose a random starting page
    current_page = random.choice(list(corpus.keys()))

    # Get the n samples
    for _ in range(n):
        # Update the Pagerank value for each page
        pagerank[current_page] += 1 / n

        # Use transition model to get to next page
        transition_probabilities = transition_model(corpus, current_page, damping_factor)
        current_page = random.choices(list(transition_probabilities.keys()), weights=list(transition_probabilities.values()))[0]

    return pagerank


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # Initilize the pagerank values
    total_pages = len(corpus)
    initial_rank = 1 / total_pages
    pagerank = {page: initial_rank for page in corpus}

    # Helper function that calculates the new rank for each page
    def calculate_new_rank(page):
        new_rank = (1 - damping_factor) / total_pages

        # Add up all of the clicks on the linked pages to the specific page that was clicked on
        for linking_page, linked_pages in corpus.items():
            if page in linked_pages:
                links = len(linked_pages) or total_pages
                new_rank += damping_factor * pagerank[linking_page] / links

        return new_rank

    # while true loop to update the rank of the pages
    while True:
        # Track the amount of changes to the rank there are, first initilizing it to 0
        rank_changes = 0

        # Update the rank
        new_pagerank = {page: calculate_new_rank(page) for page in corpus}

        # Get the maximum amount of changes that have been made to the rank
        rank_changes = max(abs(new_pagerank[page] - pagerank[page]) for page in corpus)

        # Update the rank
        pagerank = new_pagerank

        # checking for convergence
        if rank_changes < 0.001:
            break

    # Normalize the PageRank values to ensure they sum to 1
    normalization_factor = sum(pagerank.values())
    pagerank = {page: value / normalization_factor for page, value in pagerank.items()}

    return pagerank

if __name__ == "__main__":
    main()

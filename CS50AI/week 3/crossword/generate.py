import sys

from crossword import *


class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        _, _, w, h = draw.textbbox((0, 0), letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
        # Get the varaibles from the domain
        for var in self.crossword.variables:

            # Get the word from the these variables, and of they don't match remove them
            for word in self.crossword.words:
                if len(word) != var.length:
                    self.domains[var].remove(word)

    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """
        revised = False

        # Check for an overlap between variables x and y
        overlap = self.crossword.overlaps.get((x, y))

        if overlap:
            x_overlap, y_overlap = overlap
            # Loop through the values of x's domain
            for value_x in list(self.domains[x]):
                valid_match = False
                # Check if there is any valid match in y's domain
                for value_y in self.domains[y]:
                    if value_x[x_overlap] == value_y[y_overlap]:
                        valid_match = True
                        break
                # If no valid match found, remove the value from x's domain
                if not valid_match:
                    self.domains[x].remove(value_x)
                    revised = True

        return revised


    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with the initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        # Initialize the queue of arcs
        if arcs is None:
            arcs_queue = [(var_x, var_y) for var_x in self.crossword.variables for var_y in self.crossword.neighbors(var_x)]
        else:
            arcs_queue = list(arcs)

        while arcs_queue:
            # Get and remove the first arc from the queue
            (var_x, var_y) = arcs_queue.pop(0)

            # Check if the domains of var_x were revised
            if self.revise(var_x, var_y):
                # If var_x's domain is empty, return False
                if not self.domains[var_x]:
                    return False

                # Add neighbors of var_x (excluding var_y) to the queue
                neighbors_x = [neighbor_x for neighbor_x in self.crossword.neighbors(var_x) if neighbor_x != var_y]
                arcs_queue.extend([(neighbor_x, var_x) for neighbor_x in neighbors_x])

        # If all arcs are consistent and no domains are empty, return True
        return True


    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        # Check if all variables in self.crossword.variables have an assignment in the given 'assignment'
        return all(var in assignment for var in self.crossword.variables)

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """
        return self.all_distinct(assignment) and self.all_correct_length(assignment) and self.no_conflicts(assignment)

    # all functions until all_conflicts are helper functions that do a certain task in order to ensure different criteras of an assignment

    def all_distinct(self, assignment):
        """
        Check if all values in the assignment are distinct.
        """
        values_set = set(assignment.values())
        return len(values_set) == len(assignment)

    def all_correct_length(self, assignment):
        """
        Check if every value in the assignment has the correct length.
        """
        return all(var.length == len(word) for var, word in assignment.items())

    def no_conflicts(self, assignment):
        """
        Check if there are no conflicts between neighboring variables.
        """
        for var_x, word_x in assignment.items():
            for var_y, word_y in assignment.items():
                if var_x != var_y and self.crossword.overlaps.get((var_x, var_y)):
                    overlap_x, overlap_y = self.crossword.overlaps[(var_x, var_y)]
                    if word_x[overlap_x] != word_y[overlap_y]:
                        return False  # Conflict between neighboring variables
        return True


    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        if var in assignment:
            return [assignment[var]]  # Variable already assigned, return the assigned value

        # Count the number of values ruled out for each value in the domain
        ruled_out_counts = {}
        for value in self.domains[var]:
            count = 0
            for neighbor in self.crossword.neighbors(var):
                if neighbor not in assignment and value in self.domains[neighbor]:
                    count += 1
            ruled_out_counts[value] = count

        # Sort the values based on the count of ruled-out values
        ordered_values = sorted(self.domains[var], key=lambda value: ruled_out_counts[value], reverse=True)


        return ordered_values

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        unassigned_variables = [var for var in self.crossword.variables if var not in assignment]

        # If all variables are assigned, return None
        if not unassigned_variables:
            return None

        # Choose the variable with the minimum number of remaining values in its domain
        min_remaining_values = float('inf')
        selected_variable = None

        for var in unassigned_variables:
            remaining_values = len(self.domains[var])
            if remaining_values < min_remaining_values:
                min_remaining_values = remaining_values
                selected_variable = var
            elif remaining_values == min_remaining_values:
                # If there is a tie, choose the variable with the highest degree
                if self.calculate_degree(var) > self.calculate_degree(selected_variable):
                    selected_variable = var

        return selected_variable

    # helper function that calculates the degree bby using the number of neighbors
    def calculate_degree(self, variable):
        """
        Calculate the degree (number of neighbors) for a variable.
        """
        return len(self.crossword.neighbors(variable))


    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """
        # check if the assignment is complete, if so then return it
        if self.assignment_complete(assignment):
            return assignment

        # get the variable from the heurestics, as well as the list of the order of the domain values
        variable = self.select_unassigned_variable(assignment)
        variable_domain_list = self.order_domain_values(variable, assignment)

        # perform backtracking search, using all of the other functions output
        for value in variable_domain_list:
            new_assignment = assignment.copy()
            new_assignment[variable] = value
            if self.consistent(new_assignment):
                result = self.backtrack(new_assignment)
                if result is not None:
                    return result
        return None


def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()

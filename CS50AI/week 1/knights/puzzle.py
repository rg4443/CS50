from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # It is either a knight or a knave and not both
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    # If a knight and a knave is the same as a knave
    Biconditional(AKnight, And(AKnight, AKnave)),
)


# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # A is either a knight or a knave and not both
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    # B is either a knight or knave
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    # A is a knave and B is a knight because if A were to be telling the truth that would make A a knave which doesn't make sense.
    Biconditional(AKnight, And(BKnave, AKnave)),
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # A is either a knight or a knave and not both
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    # B is either a knight or knave
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    # A is knave because b refutes A's response making b a knight
    Biconditional(AKnight, And(BKnave, AKnave)),
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # A is either a knight or a knave and not both
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    # B is either a knight or knave
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    # C is either a knight or knave
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave)),
    # A is a knight
    Biconditional(AKnave, And(AKnave, AKnight)),
    # B is a knave
    Biconditional(BKnight, And(BKnight, BKnave)),
    # C is a knight
    Biconditional(CKnave, And(CKnave, CKnight)),
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3),
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()

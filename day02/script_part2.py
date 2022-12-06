
def score_rock_paper_scissors(other, me):
    score = 0
    if me == "X": # Lose
        score = 0
        if other == "A": # Rock - Scissors
            score += 3 # draw
        elif other == "B": # Paper - Rock
            score += 1 # lose
        elif other == "C": # Scissors - Paper
            score += 2 # win
        else:
            raise ValueError("Invalid input")
    elif me == "Y": # Draw
        score = 3
        if other == "A": # Rock - Rock
            score += 1 # win
        elif other == "B": # Paper - Paper
            score += 2 # draw
        elif other == "C": # Scissors - Scissors
            score += 3 # lose
        else:
            raise ValueError("Invalid input")
    elif me == "Z": # Win
        score = 6
        if other == "A": # Rock - Paper
            score += 2 # lose
        elif other == "B": # Paper - Scissors
            score += 3 # win
        elif other == "C": # Scissors - Rock
            score += 1 # draw
        else:
            raise ValueError("Invalid input")
    else:
        raise ValueError("Invalid input")
    return score

total_score = 0

with open("input.txt", "r") as f:
    for line in f:
        other, me = line.split()
        total_score += score_rock_paper_scissors(other, me)

# Part 2
print(total_score)

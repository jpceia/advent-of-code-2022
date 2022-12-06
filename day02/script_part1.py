
def score_rock_paper_scissors(other, me):
    score = 0
    if me == "X": # Rock
        score = 1
        if other == "A": # Rock
            score += 3 # draw
        elif other == "B": # Paper
            score += 0 # lose
        elif other == "C": # Scissors
            score += 6 # win
        else:
            raise ValueError("Invalid input")
    elif me == "Y": # Paper
        score = 2
        if other == "A": # Rock
            score += 6 # win
        elif other == "B": # Paper
            score += 3 # draw
        elif other == "C": # Scissors
            score += 0 # lose
        else:
            raise ValueError("Invalid input")
    elif me == "Z": # Scissors
        score = 3
        if other == "A": # Rock
            score += 0 # lose
        elif other == "B": # Paper
            score += 6 # win
        elif other == "C": # Scissors
            score += 3 # draw
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

# Part 1
print(total_score)
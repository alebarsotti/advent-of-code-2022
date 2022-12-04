from Utils.Color import print_color, Color


values = {
    "A": ("rock", 0),
    "B": ("paper", 0),
    "C": ("scissors", 0),
    "X": ("rock", 1),
    "Y": ("paper", 2),
    "Z": ("scissors", 3),
}

rules = {
    "rock": lambda other: 6 if other == "scissors" else 0,
    "paper": lambda other: 6 if other == "rock" else 0,
    "scissors": lambda other: 6 if other == "paper" else 0,
}

score = 0
with open('input.txt', 'r') as file:
    for line in file:
        opponent, ours = line.strip().split(' ')
        score += values[ours][1]
        opponent = values[opponent][0]
        ours = values[ours][0]
        if opponent == ours:
            score += 3
        else:
            score_calculator = rules[ours]
            score += score_calculator(opponent)

print(f'Total score: {print_color(score, Color.PURPLE)}.')

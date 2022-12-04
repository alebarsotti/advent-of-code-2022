from Utils.Color import print_color, Color

WIN = "Z"

DRAW = "Y"

LOSE = "X"

WINNER = "winner"

LOSER = "loser"

ROCK = "A"

PAPER = "B"

SCISSORS = "C"

element_values = {
    ROCK: 1,
    PAPER: 2,
    SCISSORS: 3,
}

result_values = {
    LOSE: 0,
    DRAW: 3,
    WIN: 6,
}

results = {
    LOSE: lambda element: get_element(element, LOSER),
    DRAW: lambda element: element,
    WIN: lambda element: get_element(element),
}


def get_element(element, search_mode=WINNER):
    return rules[element][search_mode]


rules = {
    ROCK: {
        LOSER: SCISSORS,
        WINNER: PAPER
    },
    PAPER: {
        LOSER: ROCK,
        WINNER: SCISSORS
    },
    SCISSORS: {
        LOSER: PAPER,
        WINNER: ROCK
    },
}

score = 0
with open('input.txt', 'r') as file:
    for line in file:
        opponent, result = line.strip().split(' ')
        element_calculator = results[result]
        element_to_play = element_calculator(opponent)

        score += element_values[element_to_play] + result_values[result]

print(f'Total score: {print_color(score, Color.ORANGE)}.')

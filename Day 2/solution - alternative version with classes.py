from Utils.Color import print_color, Color
from abc import ABC, abstractmethod

WIN_SCORE = 6

DRAW_SCORE = 3

LOSE_SCORE = 0


class Element(ABC):
    @staticmethod
    def build(letter):
        return elements.get(letter)

    @abstractmethod
    def wins_over(self):
        pass

    def get_match_score(self, opponent):
        return DRAW_SCORE if isinstance(opponent, type(self)) else \
            WIN_SCORE if isinstance(opponent, self.wins_over()) else LOSE_SCORE


class Rock(Element):
    value = 1

    def wins_over(self):
        return Scissors


class Paper(Element):
    value = 2

    def wins_over(self):
        return Rock


class Scissors(Element):
    value = 3

    def wins_over(self):
        return Paper


elements = {
    "A": Rock,
    "B": Paper,
    "C": Scissors,
    "X": Rock,
    "Y": Paper,
    "Z": Scissors,
}

score = 0
with open('input.txt', 'r') as file:
    for line in file:
        opponent_element, player_element = line.strip().split(' ')
        opponent_element = Element.build(opponent_element)()
        player_element = Element.build(player_element)()

        score += player_element.value + player_element.get_match_score(opponent_element)

print(f'Total score: {print_color(score, Color.PURPLE)}.')

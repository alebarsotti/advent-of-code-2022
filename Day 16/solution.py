import re
import time
from itertools import permutations, pairwise
from pprint import pprint

from simpleai.search import SearchProblem, breadth_first
from tqdm import tqdm

from Utils.Color import print_color, Color

AVAILABLE_TIME = 30
START_VALVE = 'AA'


class Valve:
    def __init__(self, name, flow, tunnels):
        self.name = name
        self.flow = int(flow)
        self.tunnels = tunnels

    def __repr__(self):
        return f'{self.name} - Flow: {self.flow} - Tunnels: {self.tunnels}'


class BFSValve(SearchProblem):

    def __init__(self, initial_state, goal):
        super().__init__(initial_state=initial_state)
        self.goal = goal

    def actions(self, state):
        if self.is_goal(state):
            return []
        else:
            return valves[state].tunnels

    def result(self, state, action):
        return action

    def is_goal(self, state):
        return state == self.goal


valves = {}
costs = {}
# Read file and create valves
with open('input.txt', 'r') as file:
    for line in file:
        n, f, *t = re.findall(r'[A-Z][A-Z]|\d+', string=line.strip())
        new_valve = Valve(n, f, t)
        valves[new_valve.name] = new_valve

# Calculate costs to move between valves. Note: Floyd-Warshall could be used (should be more efficient)
for start_valve in valves:
    costs[start_valve] = {}
    for goal_valve in valves:
        if goal_valve != start_valve:
            search_problem = BFSValve(initial_state=start_valve, goal=goal_valve)
            result = breadth_first(search_problem, graph_search=True)
            costs[start_valve][goal_valve] = len(result.path()) - 1
        else:
            # The cost for returning to the same node is 1 to exit + 1 to enter again.
            costs[start_valve][goal_valve] = 2

# Generate efficient dictionaries
# Flows (for valves with flow != 0)
flows = {valve.name: valve.flow for valve in valves.values() if valve.flow != 0}
# Binary-identified flows
indexed_flows = {valve_name: 1 << index for index, valve_name in enumerate(flows)}
# Connections between valves
tunnels = {valve.name: valve.tunnels for valve in valves.values()}


def visit_from_valve(initial_valve, remaining_time, state, released_pressure, answer):
    """
    :param initial_valve: last visited valve
    :param remaining_time: remaining current time, after visiting valves in state
    :param state: represents the visited valves with bits
    :param released_pressure: released pressure for the current state
    :param answer: dictionary of all the states and flows calculated
    :return: answer dictionary
    """
    answer[state] = max(answer.get(state, 0), released_pressure)
    for valve in flows:
        # Subtract from the remaining time the cost of moving to a new valve and open it.
        new_remaining_time = remaining_time - costs[initial_valve][valve] - 1
        # Finish path if time is over or the valve was already visited.
        if new_remaining_time <= 0 or indexed_flows[valve] & state:
            continue
        new_released_pressure = released_pressure + new_remaining_time * flows[valve]
        new_state = state | indexed_flows[valve]
        visit_from_valve(valve, new_remaining_time, new_state, new_released_pressure, answer)
    return answer


start = time.perf_counter()
result = visit_from_valve('AA', 30, 0, 0, {})
end = time.perf_counter()
print(f'La mayor cantidad posible de presión a liberar es: {print_color(max(result.values()), Color.GREEN)}')
print(f"Tiempo de ejecución: {end - start:.6f} segundos")

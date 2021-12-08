from typing import List


def read_input() -> List[int]:
    """
    Reads input
    :return: returns list of ints
    """
    with open("input.txt") as file:
        return list(map(int, file.readline().split(",")))


def min_costs(fuel: List[int]) -> int:
    """
    Task 01
    search for cheapest cost
    :param fuel: list of all fuel costs
    :return: return cheapest cost
    """
    costs: List[int] = []
    for fl in range(min(fuel), max(fuel) + 1):
        cost = 0
        for item in fuel:
            cost += abs(fl - item)
        costs.append(cost)
    return min(costs)


def min_costs_new(fuel: List[int]) -> int:
    """
    Task 02
    search for cheapest cost with new algorithmus
    :param fuel: list of all fuel costs
    :return: return cheapest cost
    """
    costs: List[int] = []
    tmp = list(range(min(fuel), max(fuel) + 1))
    for fl in range(min(fuel), max(fuel) + 1):
        cost = 0
        for item in fuel:
            cost += sum(tmp[0:abs(fl - item) + 1])
        costs.append(cost)
    return min(costs)


if __name__ == '__main__':
    print(f"Task 1: {min_costs(read_input())}")
    print(f"Task 2: {min_costs_new(read_input())}")

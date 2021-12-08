from typing import Dict, List, Tuple


def read_input() -> List[List[str]]:
    with open(file="input05.txt") as file:
        return [line.rstrip().split(" -> ") for line in file]


def create_coordinates(input: List[List[str]]) -> Tuple[int, Dict[Tuple[int, int], int]]:
    """
    Task 01
    Check for coordinates, which will used more than once
    :param input: List of vectors
    :return: Count coordinates, which will used more than once and Coordinates
    """
    coordinates: Dict[Tuple[int, int], int] = {}
    for element in input:
        start = list(map(int, element[0].split(",")))
        end = list(map(int, element[-1].split(",")))
        if start[0] == end[0]:
            cnt = 1 if start[-1] < end[-1] else -1
            for num in range(start[-1], end[-1] + cnt, cnt):
                coordinates[(start[0], num)] = coordinates.get((start[0], num), 0) + 1
        if start[-1] == end[-1]:
            cnt = 1 if start[0] < end[0] else -1
            for num in range(start[0], end[0] + cnt, cnt):
                coordinates[(num, start[-1])] = coordinates.get((num, start[-1]), 0) + 1
    return len(list(filter(lambda x: x > 1, coordinates.values()))), coordinates


def diagonal_coordinates(input: List[List[str]], coordinates: Dict[Tuple[int, int], int]) -> int:
    """
    Task 02
    Add coordinates from diagonal lines and check which coordinates are used more than once
    :param input: List of vectors
    :param coordinates: Coordinates from part 01
    :return: count coordinates which will used more than once
    """
    for element in input:
        start = list(map(int, element[0].split(",")))
        end = list(map(int, element[-1].split(",")))
        if abs(end[0] - start[0]) == abs(end[-1] - start[-1]):
            cntstart = 1 if start[0] < end[0] else -1
            cntend = 1 if start[-1] < end[-1] else -1
            for x, y in zip(range(start[0], end[0] + cntstart, cntstart), range(start[-1], end[-1] + cntend, cntend)):
                coordinates[(x, y)] = coordinates.get((x, y), 0) + 1
    return len(list(filter(lambda val: val > 1, coordinates.values())))


if __name__ == "__main__":
    answer, coordinates = create_coordinates(read_input())
    print(f"Task 01: {answer}")
    print(f"Task 02: {diagonal_coordinates(read_input(), coordinates)}")

from typing import List


def read_input():
    """
    Reads input file
    :return:
    """
    with open("input.txt") as file:
        return list(map(int, file.readline().split(",")))


def transform_list(lanternfish: List[int]) -> List[int]:
    """
    Reorganize lanternfish list
    :param lanternfish:
    :return: returns new list of lanternfish
    """
    new_list: List[int] = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for fish in lanternfish:
        new_list[fish] += 1
    return new_list


def lanternfish(days: int, fish: List[int]) -> int:
    """
    Sum up all fish after N days
    :param days: days
    :param fish: list of lanternfish
    :return: returns sum of all lanternfish
    """
    for day in range(days):
        tmp = fish[0]
        fish.pop(0)
        fish[6] += tmp
        fish.append(tmp)
    return sum(fish)


if __name__ == '__main__':
    print(f"Task 01: {lanternfish(days=80, fish=transform_list(read_input()))}")
    print(f"Task 01: {lanternfish(days=256, fish=transform_list(read_input()))}")

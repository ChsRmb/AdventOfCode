from dataclasses import dataclass
from typing import List


@dataclass
class Commands:
    command: str
    change: int

    def __init__(self, cmd: str, chg: str):
        self.command = cmd
        self.change = int(chg)


def read_input() -> List[Commands]:
    """
    Reads input.txt
    :return: List of Commands
    """
    with open("input.txt") as file:
        return [Commands(*line.rstrip().split(" ")) for line in file]


def multiply_position(cmds: List[Commands]) -> int:
    """
    Task 1:
    Sum up all up and down commands and sum all horizontal forwards
    :param cmds: List of commands
    :return: returns multiply horizontal and depth sums
    """
    horizontal: int = 0
    depth: int = 0
    for cmd in cmds:
        match cmd.command:
            case "down":
                depth += cmd.change
            case "up":
                depth -= cmd.change
            case "forward":
                horizontal += cmd.change
    return horizontal * depth


def correct_position(cmds: List[Commands]) -> int:
    """
    Task 2:
    Corrected new position with aim
    :param cmds: List of Commands
    :return: returns multiply horizontal and corrected depth sums
    """
    horizontal: int = 0
    depth: int = 0
    aim: int = 0
    for cmd in cmds:
        match cmd.command:
            case "down":
                aim += cmd.change
            case "up":
                aim -= cmd.change
            case "forward":
                if aim != 0:
                    depth += cmd.change * aim
                horizontal += cmd.change
    return horizontal * depth


if __name__ == '__main__':
    print(f"Task 1: {multiply_position(read_input())}")
    print(f"Task 2: {correct_position(read_input())}")

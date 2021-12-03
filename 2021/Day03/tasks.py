from typing import List


def read_input():
    """
    Reads input.txt
    :return: Returns List of strings (binary numbers)
    """
    with open("input.txt") as file:
        return [line.rstrip() for line in file]


def binary_diagnostic(binarys: List[str]) -> int:
    """
    Answer to Task 01

    :param binarys: List of strings(binarys)
    :return: returns the product of gamma and epsilon
    """
    gamma: str = ""
    epsilon: str = ""
    for pos in range(1, len(binarys[0])):
        cnt_one: int = 0
        cnt_zero: int = 0
        for binary in binarys:
            if binary[pos] == "1":
                cnt_one += 1
            else:
                cnt_zero += 1
        if cnt_zero > cnt_one:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"
    return int(gamma, 2) * int(epsilon, 2)


def oxygen(binarys: List[str]) -> int:
    """
    Oxygen Generator Rating

    :param binarys: List of strings (binarys)
    :return: return the rating as int
    """
    for pos in range(1, len(binarys[0])):
        list_a = []
        list_b = []
        for binary in binarys:
            if binary[pos] == "1":
                list_a.append(binary)
            else:
                list_b.append(binary)
        if len(list_a) >= len(list_b):
            binarys = list_a
        else:
            binarys = list_b
        if len(binarys) == 1:
            break
    return int(binarys[0], 2)


def scrubber(binarys: List[str]) -> int:
    """
    CO2 scrubber rating

    :param binarys: List of strings (binarys)
    :return: return the rating as int
    """
    for pos in range(1, len(binarys[0])):
        list_a = []
        list_b = []
        for binary in binarys:
            if binary[pos] == "1":
                list_a.append(binary)
            else:
                list_b.append(binary)
        if len(list_a) < len(list_b):
            binarys = list_a
        else:
            binarys = list_b
        if len(binarys) == 1:
            break
    return int(binarys[0], 2)


def life_support_rating(binarys: List[str]) -> int:
    """
    Answer to task 2

    :param binarys: List of strings (binarys)
    :return: return the product of oxygen and scrubber
    """
    oxy: List[str] = []
    scr: List[str] = []
    for bin in binarys:
        if bin.startswith("1"):
            oxy.append(bin)
        else:
            scr.append(bin)
    return oxygen(oxy) * scrubber(scr)


if __name__ == '__main__':
    print(f"Task 01: {binary_diagnostic(read_input())}")
    print(f"Task 02: {life_support_rating(read_input())}")

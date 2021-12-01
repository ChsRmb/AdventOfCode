from typing import List


def depth(depths: List[int]) -> int:
    """
    Count increased measurements
    """
    count = 0
    for num, dpth in enumerate(depths[1:]):
        if dpth > depths[num]:
            count += 1
    return count


def read_depths() -> List[int]:
    """
    Reads input.txt and returns the measurements as list
    """
    with open("input.txt") as file:
        depths = [int(line.rstrip()) for line in file]
    return depths


def sum_three_depth(depths: List[int]) -> List[int]:
    """
    Sums of a three-measurement sliding window

    returns a new list of measurements
    """
    new_depths = []
    while len(depths) >= 3:
        new_dpth = 0
        for num, dpth in enumerate(depths):
            if num > 2:
                break
            new_dpth += dpth
        new_depths.append(new_dpth)
        del depths[0]
    return new_depths


if __name__ == '__main__':
    print(f"Task 01: {depth(read_depths())}")
    print(f"Task 02: {depth(sum_three_depth(read_depths()))}")

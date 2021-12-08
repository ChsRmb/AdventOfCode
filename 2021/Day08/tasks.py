from typing import Dict, List, Set, Tuple


# First answer for Task 1
def read_input() -> List[str]:
    """
    Reads input for task 1
    :return:
    """
    with open("input.txt") as file:
        return [line.rstrip().split(" | ")[-1] for line in file]


def count_num(numberlists: List[str]) -> int:
    """
    Count if 1, 4, 7 or 8 in numbers
    :param numberlists:
    :return:
    """
    cnt_nmbs: int = 0
    for nmbs in numberlists:
        tmp: List[str] = nmbs.split(" ")
        for nmb in tmp:
            match len(nmb):
                case 2 | 3 | 4 | 7:
                    cnt_nmbs += 1
    return cnt_nmbs


# Second answer for Task 1 and 2
def read_input_complete() -> List[str]:
    """
    Read lines from input
    :return: returns List of lines
    """
    with open("input.txt") as file:
        return [line.rstrip() for line in file]


def parse_num(numbers: str) -> Dict[int, Set[int]]:
    """
    Parses segment numbers to numbers

    :param numbers: Line from input
    :return: returns Dict of sets
    """
    nmbr: Dict[int, Set[int]] = {}
    tmp = numbers.split()
    tmp.pop(10)
    twothreefive: List[Set[int]] = []
    zerosixnine: List[Set[int]] = []
    for number in tmp:
        match len(number):
            case 2:
                nmbr[1] = set([ch for ch in number])
            case 4:
                nmbr[4] = set([ch for ch in number])
            case 3:
                nmbr[7] = set([ch for ch in number])
            case 7:
                nmbr[8] = set([ch for ch in number])
            case 6:
                zerosixnine.append(set([ch for ch in number]))
            case 5:
                twothreefive.append(set([ch for ch in number]))
    twofive: List[Set[int]] = []
    for number in twothreefive:
        if nmbr[1].issubset(number):
            nmbr[3] = number
            continue
        twofive.append(number)

    for number in zerosixnine:
        if nmbr[3].issubset(number):
            nmbr[9] = number
        elif nmbr[7].issubset(number):
            nmbr[0] = number
        else:
            nmbr[6] = number

    for number in twofive:
        if len(nmbr[6].difference(number)) == 1:
            nmbr[5] = number
            continue
        nmbr[2] = number

    return nmbr


def count_all_num(numberlists: List[str]) -> Tuple(int, int):
    """
    New Answer for task 1 and 2
    :param numberlists: List of lines
    :return: returns answers
    """
    cnt_task1: int = 0
    cnt: int = 0
    for numbers in numberlists:
        parsed_numbers = parse_num(numbers)
        numbers = numbers.split(" | ")[-1].split()
        buildnmbr: str = ""
        for numb in numbers:
            numb = set([ch for ch in numb])
            match len(numb):
                case 2:
                    buildnmbr += "1"
                    cnt_task1 += 1
                case 4:
                    buildnmbr += "4"
                    cnt_task1 += 1
                case 3:
                    buildnmbr += "7"
                    cnt_task1 += 1
                case 7:
                    buildnmbr += "8"
                    cnt_task1 += 1
                case 6:
                    if len(parsed_numbers[6].difference(numb)) == 0:
                        buildnmbr += "6"
                    elif len(parsed_numbers[9].difference(numb)) == 0:
                        buildnmbr += "9"
                    else:
                        buildnmbr += "0"
                case 5:
                    if len(parsed_numbers[2].difference(numb)) == 0:
                        buildnmbr += "2"
                    elif len(parsed_numbers[3].difference(numb)) == 0:
                        buildnmbr += "3"
                    else:
                        buildnmbr += "5"
        cnt += int(buildnmbr)
    return cnt_task1, cnt


if __name__ == '__main__':
    t1, t2 = count_all_num(read_input_complete())
    print(f"Task 01: {t1}")
    print(f"Task 02: {t2}")

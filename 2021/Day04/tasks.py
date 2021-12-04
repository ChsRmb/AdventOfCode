from typing import Dict, List, Optional, Tuple


class Bingofield:
    def __init__(self, nmbrs: List[int]) -> None:
        """
        Bingofield constructor
        :param nmbrs: List of 25 numbers
        """
        self.__field: List[Dict[int, bool]] = self.__create_field(nmbrs)

    @staticmethod
    def __create_field(nmbrs: List[int]) -> List[Dict[int, bool]]:
        """
        Helper function which creates bingofield as a list of dictionary's
        :param nmbrs: list of 25 numbers
        :return: returns a list of 5 dictionary's
        """
        field: List[Dict[int, bool]] = []
        tmp: Dict[int, bool] = {}
        for nmbr in nmbrs:
            tmp[nmbr] = False
            if len(tmp) == 5:
                field.append(tmp)
                tmp = {}
        return field

    def enter_number(self, nmbr: int) -> None:
        """
        Mark a number as true if the number exists
        :param nmbr: int
        :return:
        """
        for line in self.__field:
            if nmbr in line:
                line[nmbr] = True

    def check_board(self) -> bool:
        """
        Checks if the board has a 'bingo'

        :return: returns true if the board has 'bingo'
        """
        # Check horizontal
        for line in self.__field:
            if all(line.values()):
                return True

        # Check vertical
        for pos in range(0, len(self.__field)):
            cnt: int = 0
            for line in self.__field:
                if not list(line.values())[pos]:
                    cnt = 0
                    break
                cnt += 1
                if cnt == len(self.__field):
                    return True
        return False

    def sum_unmarked(self) -> int:
        """
        sum all unmarked numbers
        :return: return sum of all unmarked numbers
        """
        ret = 0
        for line in self.__field:
            ret += sum([key for key in line.keys() if not line[key]])
        return ret


def read_input() -> Tuple[List[int], List[Bingofield]]:
    """
    Reads input.txt
    :return: returns a list of numbers and a list of bingofields
    """
    with open("input.txt") as file:
        lines = [line.rstrip() for line in file]
        numbers: List[int] = list(map(int, lines[0].split(",")))
        bingofields: List[Bingofield] = []
        tmp_bngnmbrs: List[int] = []
        for line in lines[2:]:
            if len(line) == 0:
                continue
            tmp_bngnmbrs.extend(list(map(int, line.split())))
            if len(tmp_bngnmbrs) == 25:
                bingofields.append(Bingofield(tmp_bngnmbrs))
                tmp_bngnmbrs = []
        return numbers, bingofields


def play_bingo(nmbrs: List[int], fields: List[Bingofield]) -> int:
    """
    Play classical bingo

    :param nmbrs: List of numbers
    :param fields: List of bingofields
    :return: returns product of unmarked numbers from winner bingofield and last number
    """
    for nmbr in nmbrs:
        for field in fields:
            field.enter_number(nmbr=nmbr)
            if field.check_board():
                return field.sum_unmarked() * nmbr


def find_last_bingo(nmbrs: List[int], fields: List[Bingofield]) -> int:
    """
    Find the bingofield, which get 'bingo'
    :param nmbrs: List of numbers
    :param fields: List of bingofields
    :return: return product of unmarked numbers from last bingofield and last number
    """
    tmp: List[Bingofield] = fields.copy()
    for nmbr in nmbrs:
        for field in fields:
            if field not in tmp:
                continue
            field.enter_number(nmbr=nmbr)
            if field.check_board() and len(tmp) > 1:
                tmp.remove(field)
                continue
            if field.check_board():
                return field.sum_unmarked() * nmbr


if __name__ == "__main__":
    print(f"Task 01: {play_bingo(*read_input())}")
    print(f"Task 02: {find_last_bingo(*read_input())}")

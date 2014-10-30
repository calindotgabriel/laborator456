from src.ro.ubb.calin.domain.keys import *


def get_nr(ap):
    return ap[KEY_NR]


def get_expenses(ap):
    return ap[KEY_EXPENSES]


def get_no_expenses():
    return {KEY_WATER: 0., KEY_SEWERS: 0., KEY_WARMING: 0., KEY_METHANE: 0., KEY_OTHERS: 0.}


def get_ap_by_number(bl, nr):
    """
    Find the apartment by number.
        Returns None if not found.
    :param bl: list - the block of apartments
    :param nr: int - apartment nr.
    :return: dict : the required apartment.
             none : if no apartment in list.
    """
    # for ap in bl:
    #     if get_nr(ap) == nr:
    #         return ap
    bl = [ap for ap in bl if get_nr(ap) == nr]
    return bl[0] if len(bl) > 0 else None


def get_total_sum_of_expenses(ap):
    """
    Gets the sum of all expenses.
    :param dict - ap: the apartment
    :return: int - the sum of all expenses
    """
    expenses = get_expenses(ap)
    s = 0
    for ep in expenses:
        s += expenses[ep]
    return s
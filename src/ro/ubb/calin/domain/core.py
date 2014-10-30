from src.ro.ubb.calin.domain.getters import *
from src.ro.ubb.calin.validation.validate import validate_data


def add_expenses_apartment(bl, nr, bill_type, amount):
    """
    Adds expenses to apartment, if already in list, adds just expenses
                                if not, adds the whole apartment ( nr, expenses )

    :param bl: list - the block of apartments
    :param nr: int - apartment number
    :param bill_type: int - bill type
    :param amount: float - amount to pay

    """
    validate_data(nr, bill_type, amount)

    ap = get_ap_by_number(bl, nr)

    if not ap:
        #no apartment on block, create new one and add it to the list
        ap = {KEY_NR: nr, KEY_EXPENSES: get_no_expenses()}
        bl.append(ap)

    get_expenses(ap)[bill_type] += amount

    return ap


def modify_expense(bl, nr, bill_type, new_amount):
    """
    Modifies an expense for an existing apartment.

    :param bl: list - the block of apartments
    :param nr: int - apartment number
    :param bill_type: int - expense type
    :param new_amount: float - amount to overwrite the old one
    :return: the modified apartment
    """
    validate_data(nr, bill_type, new_amount)

    ap = get_ap_by_number(bl, nr)
    get_expenses(ap)[bill_type] = new_amount
    return ap


def delete_expenses_for_ap(bl, nr):
    """
    Deletes all the expenses for a given apartment.

    :param bl: list - the block of apartments
    :param nr: int - apartment number
    :return: ap - apartment corresponding to nr but with no expenses
             none - if we have no such apartment in our list
    """
    ap = get_ap_by_number(bl, nr)

    if not ap:
        return None
    ap[KEY_EXPENSES] = get_no_expenses()
    return ap


def delete_ap_expense_seq(bl, s, f):
    """
    Deletes all the expenses for a sequence of apartments

    :param bl: list - the block of apartments
    :param s: int - start
    :param f: int - finish
    :return status: list - status with what happened during the erase process
                          =  true, successfully deleted expenses
                          = false, no apartment registered so could not delete
    """
    status = []
    # noinspection PyArgumentList
    for i in range(s, f + 1):
        ap = delete_expenses_for_ap(bl, i)
        if not ap:
            status.append(False)
        else:
            status.append(True)
    return status


def delete_expenses_by_type(bl, bill_type):
    """
    Deletes all the expenses of a given type in all apartments.


    :param bl: list - the block of apartments
    :param bill_type: int - the bill type
    """

    for ap in bl:
        get_expenses(ap)[bill_type] = 0.


def get_apartments_with_bigger_expense_than(bl, amount):
    """
    Returns all the apartments with the sum of expenses bigger than an given amount.
    :param list - bl: the list of aps
    :param int - amount: the given amount
    :return: list - list of apartments
             None - no matching apartments found.
    """
    matching_aps = []
    for ap in bl:
        if get_total_sum_of_expenses(ap) > amount:
            matching_aps.append(ap)
    return matching_aps


def get_all_apartments_expenses_of_type(bl, bill_type):
    """
    Gets expenses of given type for all the apartments
    :param bill_type: int - type of expense
    :return dict - format: { ap. number 1  : expense amount m ... ap. number n : expense amount m}
    """
    d = {}
    for ap in bl: d[get_nr(ap)] = get_expenses(ap)[bill_type]
    return d

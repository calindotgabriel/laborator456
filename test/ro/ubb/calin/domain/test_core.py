from src.ro.ubb.calin.custom.exceptions import NoExpenseFoundError, EmptyListError
from src.ro.ubb.calin.domain.core import *


def test_all(bl):
    test_add_expenses_apartment(bl)
    test_modify_expense(bl)
    test_delete_expenses_apartment(bl)
    test_delete_expenses_by_type(bl)
    test_delete_ap_expense_seq(bl)
    test_get_apartments_with_bigger_expense_than(bl)
    test_get_all_apartments_expenses_of_type(bl)
    print("All Tests ran smoothly!")


def test_add_expenses_apartment(bl):
    assert add_expenses_apartment(bl, 1, 3, 5.) == get_ap_by_number(bl, 1)
    assert add_expenses_apartment(bl, 1, 2, 7.) == get_ap_by_number(bl, 1)
    assert len(bl) == 1
    assert add_expenses_apartment(bl, 22, 5, 5.5) == get_ap_by_number(bl, 22)

    try:
        add_expenses_apartment(bl, -1, 3, 4.)
        add_expenses_apartment(bl, 1, -22, 10.)
        add_expenses_apartment(bl, 1, 23, -111.)
        add_expenses_apartment(bl, -1, 22223, -111.)
        assert False
    except ValueError:
        assert True


def test_modify_expense(bl):
    add_expenses_apartment(bl, 32, 2, 10.)
    assert modify_expense(bl, 32, 2, 19.5) == {KEY_NR: 32, KEY_EXPENSES: {KEY_WATER: 0., KEY_SEWERS: 19.5, KEY_WARMING: 0., KEY_METHANE: 0., KEY_OTHERS: 0.0}}

    try:
        modify_expense(bl, -1, 3, 4)
        assert False
    except ValueError:
        assert True

    try:
        modify_expense(bl, 222, 1, 5.)
        assert False
    except NoExpenseFoundError:
        assert True


def test_delete_expenses_apartment(bl):
    add_expenses_apartment(bl, 1, 5, 2.0)
    assert(delete_expenses_for_ap(bl, 1)) == {KEY_NR: 1, KEY_EXPENSES: get_no_expenses()}

    try:
        delete_expenses_for_ap(bl, -33)
        assert False
    except ValueError:
        assert True

    try:
        delete_expenses_for_ap(bl, 212)
        assert False
    except NoExpenseFoundError:
        assert True


def test_delete_expenses_by_type(bl):
    add_expenses_apartment(bl, 2, 4, 5.0)
    add_expenses_apartment(bl, 3, 4, 6.9)
    delete_expenses_by_type(bl, 4)
    assert get_ap_by_number(bl, 2) == {KEY_NR: 2, KEY_EXPENSES: get_no_expenses()}
    assert get_ap_by_number(bl, 3) == {KEY_NR: 3, KEY_EXPENSES: get_no_expenses()}

    try:
        delete_expenses_by_type(bl, -111)
        assert False
    except ValueError:
        assert True

    try:
        bl.clear()
        delete_expenses_by_type(bl, 1)
        assert False
    except EmptyListError:
        assert True


def test_delete_ap_expense_seq(bl):
    bl.clear()
    #TODO change 'status' logic to a exception-based one
    add_expenses_apartment(bl, 2, 4, 5.0)
    add_expenses_apartment(bl, 3, 4, 6.9)
    add_expenses_apartment(bl, 4, 4, 6.9)
    add_expenses_apartment(bl, 5, 4, 6.9)
    delete_ap_expense_seq(bl, 2, 6)
    assert get_ap_by_number(bl, 2) == {KEY_NR: 2, KEY_EXPENSES: get_no_expenses()}
    assert get_ap_by_number(bl, 3) == {KEY_NR: 3, KEY_EXPENSES: get_no_expenses()}
    assert get_ap_by_number(bl, 4) == {KEY_NR: 4, KEY_EXPENSES: get_no_expenses()}
    assert get_ap_by_number(bl, 5) == {KEY_NR: 5, KEY_EXPENSES: get_no_expenses()}


def test_get_apartments_with_bigger_expense_than(bl):
    bl.clear()
    add_expenses_apartment(bl, 5, 4, 5.0)
    add_expenses_apartment(bl, 6, 4, 10.5)
    add_expenses_apartment(bl, 7, 4, 11.9)
    assert get_apartments_with_bigger_expense_than(bl, 10) == [get_ap_by_number(bl, 6), get_ap_by_number(bl, 7)]


def test_get_all_apartments_expenses_of_type(bl):
    add_expenses_apartment(bl, 1, 1, 3.0)
    add_expenses_apartment(bl, 2, 1, 4.5)
    add_expenses_apartment(bl, 3, 1, 5.0)

    get_all_apartments_expenses_of_type(bl, 1) == {1: 3.0, 2: 4.5, 3: 5.0}


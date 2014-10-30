from src.ro.ubb.calin.custom.exceptions import NoExpenseFoundError, EmptyListError
from src.ro.ubb.calin.domain.core import *
from src.ro.ubb.calin.domain.constants import *


def print_ap_expenses_by_type(d, bill_type):
    for ap_nr in d:
        print("""Apartment {0} has the amount of {1} to pay for {2}."""
              .format(ap_nr, d[ap_nr], get_expense_map()[bill_type]))


def print_block(bl):
    if not bl:
        print("List is empty.")
        return
    for ap in bl:
        print_ap(ap)


def print_ap(ap):
    expenses = get_expenses(ap)
    print("ap nr: {0}".format(get_nr(ap)))
    for ep_key in expenses.keys():
        print(" {0}: {1}".format(expense_map[ep_key], expenses[ep_key]))


def get_bill_type_map():
    type_map = "\n"
    for ep_key in expense_map.keys():
        type_map += "{0} - {1} \n".format(ep_key, expense_map[ep_key])
    return type_map


def show_functionalities():
    print('0. Show total apartments.\n'
          '1. Add expenses for apartment.\n'
          '2. Modify expenses for apartment.\n'
          '3. Delete expense for apartment.\n'
          '4. Delete expenses for a sequence of apartments.\n'
          '5. Delete all expenses of a given type.\n'
          '6. Print all apartments with expenses bigger than an amount.\n'
          '7. Print all expenses of given type. \n'
          'Press "x" to exit')


def ui_add_expenses(bl):

    nr = int(input("Enter apartment number:"))
    bill_type = int(input("Enter bill type: " + get_bill_type_map()))
    amount = float(input("Enter the amount: "))
    add_expenses_apartment(bl, nr, bill_type, amount)


def ui_modify_expense(bl):
    nr = int(input("Enter existent apartment number:"))
    ap = get_ap_by_number(bl, nr)

    bill_type = int(input("Enter bill type: " + get_bill_type_map()))
    print("Old amount was: ", get_expenses(ap)[bill_type])
    amount = float(input("Enter the new amount: "))

    modify_expense(bl, nr, bill_type, amount)


def ui_delete_expenses_for_ap(bl):
    nr = int(input("Enter existent apartment number:"))
    delete_expenses_for_ap(bl, nr)


def ui_delete_ap_expense_seq(bl):
    s = int(input("Enter first apartment:"))
    f = int(input("Enter last apartment:"))
    status = delete_ap_expense_seq(bl, s, f)
    for i in range(len(status)):
        if not status[i]:
            print(" Could not delete expenses for ap. no ", i+1, " because it hasn't been added.")
        else:
            print(" Deleted expenses for ap no. ", i+1)


def ui_delete_expenses_by_type(bl):
    bill_type = int(input("Enter bill type:"))
    delete_expenses_by_type(bl, bill_type)


def ui_get_apartments_with_bigger_expense_than(bl):
    amount = float(input("Enter Amount: "))
    aps = get_apartments_with_bigger_expense_than(bl, amount)
    print_block(aps)


def ui_get_all_apartments_expenses_of_type(bl):
    bill_type = int(input("Enter bill type:"))
    validate_block(bl)
    d = get_all_apartments_expenses_of_type(bl, bill_type)
    print_ap_expenses_by_type(d, bill_type)


def run_ui():
    # the block of apartments
    bl = []

    options = {0: print_block, 1: ui_add_expenses, 2: ui_modify_expense, 3: ui_delete_expenses_for_ap,
               4: ui_delete_ap_expense_seq, 5: ui_delete_expenses_by_type,
               6: ui_get_apartments_with_bigger_expense_than, 7: ui_get_all_apartments_expenses_of_type}
    while True:
        show_functionalities()
        opt = input("Option=")
        if opt == 'x':
            print("Bye!")
            break
        else:
            try:
                opt = int(opt)
                options[opt](bl)
            except ValueError as ve:
                print("Invalid Input.", ve)
            except KeyError:
                print("This option is not yet implemented.")
            except NoExpenseFoundError:
                print("You must first add expenses for this apartment.")
            except EmptyListError:
                print("No Expenses.")


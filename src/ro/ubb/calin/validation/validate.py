"""
author: @motan
date: 10/24/14, 23:54
project: lab456

"""
from src.ro.ubb.calin.custom.exceptions import *


def validate_nr(nr):
    if nr < 0: raise ValueError("Incorrect apartment number.")


def validate_bill_type(bill_type):
    if bill_type < 1 or bill_type > 5: raise ValueError("Incorrect expense type.")


def validate_amount(amount):
    if amount < 0: raise ValueError("Incorrect amount.")


def validate_data(nr, bill_type, amount):
    validate_nr(nr)
    validate_bill_type(bill_type)
    validate_amount(amount)


def validate_ap(ap):
    if not ap:
        raise NoExpenseFoundError


def validate_bl(bl):
    if not bl:
        raise EmptyListError("Can't delete any expenses.")
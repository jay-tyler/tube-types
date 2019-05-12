"""
Some simple examples of how tube types can be used
"""
from .tubes import data_tube, bool_tube


@data_tube
def add_1(x):
    return x + 1


@data_tube
def multiply_3(x):
    return x * 3


@data_tube
def out_of(iterable):
    return iterable


def not_equal_to(x):
    @data_tube
    def not_equal_inner(iterable):
        a = (iter_item for iter_item in iterable
                if iter_item != x)
        return a
    return not_equal_inner


@data_tube
def random_pick(iterable):
    return random.choice(tuple(iterable))


@bool_tube
def not_even(x):
    return x % 2


def not_divisible_by(x):
    @bool_tube
    def not_divisible_by_inner(val):
        return val % x
    return not_divisible_by_inner


## examples
a = add_1 | multiply_3
b = not_equal_to(2) | random_pick
c = (not_even | not_divisible_by(3)).all
d = (not_even | not_divisible_by(3)).any
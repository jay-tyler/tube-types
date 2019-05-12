import itertools
import random

class data_pipe(object):
    def __init__(self, fcts):
        self.fcts = []
        try:
            self.fcts.extend(fcts)
        except TypeError:
            self.fcts.append(fcts)

    def __call__(self, arg):
        for fct in self.fcts:
            arg = fct(arg)
        return arg

    def __or__(self, other):
        f_self = self.fcts
        f_other = other.fcts
        return data_pipe(f_self + f_other)


class bool_pipe(object):
    def __init__(self, fcts):
        self.fcts = []
        try:
            self.fcts.extend(fcts)
        except TypeError:
            self.fcts.append(fcts)

    def __or__(self, other):
        f_self = self.fcts
        f_other = other.fcts
        return bool_pipe(f_self + f_other)

    @property
    def all(self):
        def all_inner(x):
            return all(fct(x) for fct in self.fcts)
        return bool_pipe(all_inner)

    @property
    def any(self):
        def any_inner(x):
            return any(fct(x) for fct in self.fcts)
        return bool_pipe(any_inner)

@data_pipe
def add_1(x):
    return x + 1

@data_pipe
def multiply_3(x):
    return x * 3

@data_pipe
def out_of(iterable):
    return iterable

def not_equal_to(x):
    @data_pipe
    def not_equal_inner(iterable):
        a = (iter_item for iter_item in iterable
                if iter_item != x)
        return a
    return not_equal_inner

@data_pipe
def random_pick(iterable):
    return random.choice(tuple(iterable))

@bool_pipe
def not_even(x):
    return x % 2

def not_divisible_by(x):
    @bool_pipe
    def not_divisible_by_inner(val):
        return val % x
    return not_divisible_by_inner


## examples
a = add_1 | multiply_3
b = not_equal_to(2) | random_pick
c = (not_even | not_divisible_by(3)).all
d = (not_even | not_divisible_by(3)).any
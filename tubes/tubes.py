import itertools
import random


class data_tube(object):
    """
    Use as decorator to functions that are meant to transform data
    """
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
        return data_tube(f_self + f_other)


class bool_tube(object):
    """
    Use as decorator to functions that are meant to perform boolean tests
    """
    def __init__(self, fcts):
        self.fcts = []
        try:
            self.fcts.extend(fcts)
        except TypeError:
            self.fcts.append(fcts)

    def __or__(self, other):
        f_self = self.fcts
        f_other = other.fcts
        return bool_tube(f_self + f_other)

    @property
    def all(self):
        def all_inner(x):
            return all(fct(x) for fct in self.fcts)
        return bool_tube(all_inner)

    @property
    def any(self):
        def any_inner(x):
            return any(fct(x) for fct in self.fcts)
        return bool_tube(any_inner)

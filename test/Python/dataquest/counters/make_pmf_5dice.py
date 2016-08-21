#!/usr/bin/env python


# start by making a list of Pmfs to represent the dice:
def make_die(num_sides):
    die = Pmf(range(1, num_sides+1))
    die.name = 'd%d' % num_sides
    die.normalize()
    return die


dice = [make_die(x) for x in [4, 6, 8, 12, 20]]
print(dice)

#!/usr/bin/env python


# normalize computes the total of the frequencies and divides through, 
# yielding probabilities that add to 1.
#
# __add__ enumerates all pairs of value and returns a new 
#Pmf that represents the distribution of the sum.
#
# __hash__ and __id__ make Pmfs hashable; this is not the best way to do it, 
# because they are mutable. So this implementation comes with a warning that 
# if you use a Pmf as a key, you should not modify it. 
# A better alternative would be to define a frozen Pmf.
#
# render returns the values and probabilities in a form ready for plotting
class Pmf(Counter):
    """A Counter with probabilities."""

    def normalize(self):
        """Normalizes the PMF so the probabilities add to 1."""
        total = float(sum(self.values()))
        for key in self:
            self[key] /= total

    def __add__(self, other):
        """Adds two distributions.

        The result is the distribution of sums of values from the
        two distributions.

        other: Pmf

        returns: new Pmf
        """
        pmf = Pmf()
        for key1, prob1 in self.items():
            for key2, prob2 in other.items():
                pmf[key1 + key2] += prob1 * prob2
        return pmf

    def __hash__(self):
        """Returns an integer hash value."""
        return id(self)
    
    def __eq__(self, other):
        return self is other

    def render(self):
        """Returns values and their probabilities, suitable for plotting."""
        return zip(*sorted(self.items()))


#!/usr/bin/env python


# Next I'll define DiceSuite, which inherits bayesian_update 
# from Suite and provides likelihood.

# data is the observed die roll, 6 in the example.

# hypo is the hypothetical die I might have rolled; 
# to get the likelihood of the data, I select, from the given die, 
# the probability of the given value.
class DiceSuite(Suite):
    
    def likelihood(self, data, hypo):
        """Computes the likelihood of the data under the hypothesis.

        data: result of a die roll
        hypo: Die object
        """
        return hypo[data]

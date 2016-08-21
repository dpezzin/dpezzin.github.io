#!/usr/bin/env python


# A Suite is a Pmf that represents a set of hypotheses and their probabilities; 
# it provides bayesian_update, which updates the probability of the hypotheses based on new data.

# Suite is an abstract parent class; child classes should provide a likelihood method 
# that evaluates the likelihood of the data under a given hypothesis. 
# update_bayesian loops through the hypothesis, evaluates the likelihood of the data under each hypothesis, 
# and updates the probabilities accordingly. Then it re-normalizes the PMF.
class Suite(Pmf):
    """Map from hypothesis to probability."""

    def bayesian_update(self, data):
        """Performs a Bayesian update.
        
        Note: called bayesian_update to avoid overriding dict.update

        data: result of a die roll
        """
        for hypo in self:
            like = self.likelihood(data, hypo)
            self[hypo] *= like

        self.normalize()
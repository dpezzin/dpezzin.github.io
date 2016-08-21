#!/usr/bin/env python


# A Counter is a natural representation of a multiset, 
# which is a set where the elements can appear more than once. 
# You can extend Counter with set operations like is_subset:

You could use is_subset in a game like Scrabble to see if a given set of tiles can be used to spell a given word.
class Multiset(Counter):
    """A multiset is a set where elements can appear more than once."""

    def is_subset(self, other):
        """Checks whether self is a subset of other.

        other: Multiset

        returns: boolean
        """
        for char, count in self.items():
            if other[char] < count:
                return False
        return True
    
    # map the <= operator to is_subset
    __le__ = is_subset

def can_spell(word, tiles):
    """Checks whether a set of tiles can spell a word.

    word: string
    tiles: string

    returns: boolean
    """
    return Multiset(word) <= Multiset(tiles)

print(can_spell('SYZYGY', 'AGSYYYZ'))
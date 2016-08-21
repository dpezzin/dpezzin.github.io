#!/usr/bin/env python
def is_anagram(word1, word2):
    """Checks whether the words are anagrams.

    word1: string
    word2: string

    returns: boolean
    """
    return Counter(word1) == Counter(word2)

print(is_anagram('tachymetric', 'mccarthyite'))
print(is_anagram('banana', 'peach'))
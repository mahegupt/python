# Given a sequence of words, print all anagrams together
# Q: "cat", "dog", "tac", "god", "act"
# A: "cat tac act dog god"

from collections import defaultdict


def group_anagrams(words):
    anagram_map = defaultdict(list)

    for word in words:
        # Sort characters of the word → key
        key = ''.join(sorted(word))
        anagram_map[key].append(word)

    # Print all groups
    result = []
    for group in anagram_map.values():
        result += group
    print(result)


def group_anagrams_best(words):
    anagram_map = defaultdict(list)

    for word in words:
        count_w = [0] * 26
        for c in word:
            count_w[ord(c)-ord('a')] += 1

        anagram_map[tuple(count_w)].append(word)
    result = []
    for group in anagram_map.values():
        result += group
    print(result)


# Example
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
group_anagrams(words)
group_anagrams_best(words)

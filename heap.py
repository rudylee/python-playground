#
# Pass an object to heap for custom comparison 
#
# This is useful when you need to compare two items not just based on
# one value. For example, you have a heap with a list of words and number of frequency.
# If two words have the same frequency, you need to pick the one with lower alphabetical order

import heapq

class Word:
    def __init__(self, word, frequency):
        self.word = word
        self.frequency = frequency

    def __lt__(self, other):
        if other.frequency == self.frequency:
            # If the current word is higher alphabetical then it's
            # actually lower then the other word
            return self.word > other.word

        return self.frequency < other.frequency

words = { "i" : 2, "love": 2, "coding": 3 }
heap = []
heapq.heapify(heap)

for key in words.keys():
    word = Word(key, words[key])
    heapq.heappush(heap, word)

while heap:
    # This will output `love` `i` `coding`
    # because Python is using minHeap by default
    print(heapq.heappop(heap).word)

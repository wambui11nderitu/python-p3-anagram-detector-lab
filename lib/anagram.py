class Anagram:
    '''Class Anagram in anagram.py'''

    def __init__(self, word):
        self.word = word

    def match(self, candidates):
        return [word
                for word in candidates
                if self.word.lower() != word.lower()
                and sorted(self.word.lower()) == sorted(word.lower())]
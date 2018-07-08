import typing
from typing import List, Set


class Word(typing.NamedTuple):
    """A simple abstraction over each word with the following purposes:
    - Makes the word immutable
    - Referrences to each uniuqe string (see Node class docs) will instead refer to
      objects of this type which means strings will not be copied multiple times
    """

    value: str

    def __repr__(self):
        return f'<Word {self.value}>'


class WordList(list):

    def __contains__(self, word: Word):
        return any(word.value == w.value for w in self)


class Node:

    def __init__(self, word):
        self.words = WordList()
        self.words.append(word)
        self.children = {}

    def add_child(self, word: Word, letter: str):
        if letter not in self.children:
            self.children[letter] = Node(word)
        else:
            self.children[letter].words.append(word)

    def __contains__(self, letter: str):
        return letter.lower() in self.children

    def __len__(self):
        return len(self.children)

    def __repr__(self):
        return f'<Node words: {self.words} Children: {self.children}>'


class SearchCorpus:

    def __init__(self, words: List[str]):
        self.words = words
        self.base_node: Node = None

    def create(self):
        self.make_base_node()
        self.preprocess_words()

        for word in self.words:
            current_node = self.base_node

            for letter in word.value:
                self.add_child_to_node(current_node, word, letter)
                current_node = current_node.children[letter]

    def make_base_node(self):
        self.base_node = Node(None)

    def preprocess_words(self) -> Set[Word]:
        unique_lower_case_letters = {word.lower().strip() for word in self.words}
        self.words = {Word(w) for w in unique_lower_case_letters}

    def add_child_to_node(self, current_node: Node, word: Word, letter: str):
        current_node.add_child(word, letter)

    def get_hits_for_letters(self, letters):
        letters = letters.lower().strip()
        counter = 0
        children = self.base_node.children

        try:

            while counter < len(letters):
                letter_to_look_for = letters[counter]
                node = children[letter_to_look_for]

                children = children[letter_to_look_for].children

                counter += 1

            return sorted(node.words, key=lambda word: word.value)

        except KeyError:
                return []


def make_search_corpus(words):
    search_corpus = SearchCorpus(words)
    search_corpus.create()

    return search_corpus

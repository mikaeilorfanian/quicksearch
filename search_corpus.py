import typing
from typing import List


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
        self.children[letter] = Node(word)

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
        word = self.words[0].lower()
        word = Word(word)
        self.make_base_node()

        current_node = self.base_node

        for letter in word.value:
            self.add_node(current_node, word, letter)
            current_node = current_node.children[letter]

    def make_base_node(self):
        self.base_node = Node(None)

    def add_node(self, current_node: Node, word: Word, letter: str):
        current_node.add_child(word, letter)


def make_search_corpus(words):
    search_corpus = SearchCorpus(words)
    search_corpus.create()

    return search_corpus

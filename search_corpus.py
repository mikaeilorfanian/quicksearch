class Node:

    def __init__(self, word):
        self.words = [word] if word else None
        self.children = {}

    def add_child(self, word, letter):
        self.children[letter] = Node(word)

    def __contains__(self, letter):
        return letter in self.children

    def __len__(self):
        return len(self.children)

    def __repr__(self):
        return f'<Node words: {self.words} Children: {self.children}>'


class SearchCorpus:

    def __init__(self, words):
        self.words = words
        self.base_node: Node = None

    def create(self):
        word = self.words[0].lower()
        self.make_base_node()

        current_node = self.base_node

        for letter in word:
            self.add_node(current_node, word, letter)
            current_node = current_node.children[letter]

    def make_base_node(self):
        self.base_node = Node(None)

    def add_node(self, current_node, word, letter):
        current_node.add_child(word, letter)


def make_search_corpus(words):
    search_corpus = SearchCorpus(words)
    search_corpus.create()

    return search_corpus

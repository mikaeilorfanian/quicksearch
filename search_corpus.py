class Node:

    def __init__(self, word):
        self.words = [word]
        self.children = {}

    def add_child(self, word, letter):
        self.children[letter] = Node(word)

    def __repr__(self):
        return f'<Node words: {self.words} Children: {self.children}>'


class SearchCorpus:

    def __init__(self, words):
        self.words = words
        self.nodes = {}

    def create(self):
        word = self.words[0]

        self.nodes['h'] = Node(word)
        self.nodes['h'].add_child(word, 'e')

        self.nodes['h'].children['e'].add_child(word, 'l')


def make_search_corpus(words):
    search_corpus = SearchCorpus(words)

    # previous implementation had no objects in it, so the above implementation looked like this:
    # search_corpus['h'] = {'words': [word], 'children': {'e': {'words': [word], 'children': ['l']}}}

    search_corpus.create()

    return search_corpus


class TestCorpusOfOneWord:
    WORD = 'hello'
    first_letter = WORD[0]
    second_letter = WORD[1]
    third_letter = WORD[2]

    @property
    def corpus(self):
        return make_search_corpus([self.WORD])

    def test_first_letter_of_word_has_referrence_to_word(self):
        assert self.WORD in self.corpus.nodes[self.first_letter].words

    def test_first_letter_of_word_has_referrence_to_second_letter_of_word(self):
        assert self.second_letter in self.corpus.nodes[self.first_letter].children

    def test_second_letter_is_child_of_first_letter_and_has_referrence_to_word(self):

        assert self.second_letter in self.corpus.nodes[self.first_letter].children
        assert self.WORD in self.corpus.nodes[self.first_letter].children['e'].words

    def test_third_letter_is_child_of_first_letter_and_has_referrence_to_word(self):
        assert self.third_letter in self.corpus.nodes[self.first_letter].children[self.second_letter].children

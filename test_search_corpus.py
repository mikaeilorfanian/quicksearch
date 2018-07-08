from search_corpus import make_search_corpus


class TestCorpusOfOneWord:
    WORD = 'hello'
    first_letter = WORD[0]
    second_letter = WORD[1]
    third_letter = WORD[2]
    fourth_letter = WORD[3]
    fifth_letter = WORD[4]

    @property
    def corpus(self):
        return make_search_corpus([self.WORD])

    def test_first_letter_of_word_has_referrence_to_word(self):
        assert self.WORD in self.corpus.base_node.children[self.first_letter].words

    def test_only_one_letter_is_in_base_of_corpus(self):
        assert len(self.corpus.base_node) == 1

    def test_first_letter_of_word_has_referrence_to_second_letter_of_word(self):
        assert self.second_letter in self.corpus.base_node.children[self.first_letter].children

    def test_second_letter_is_child_of_first_letter_and_has_referrence_to_word(self):

        assert self.second_letter in self.corpus.base_node.children[self.first_letter].children
        assert self.WORD in self.corpus.base_node.children[self.first_letter].children['e'].words

    def test_third_letter_is_child_of_first_letter_and_has_referrence_to_word(self):
        assert self.third_letter in self.corpus.base_node.children[self.first_letter]. \
            children[self.second_letter].children

    def test_the_staructure_of_search_corpus(self):
        """
        Here we test the following:
        - each letter is referrencing the next letter
        - number of children each letter refers to is correct
        - each letter is lower case
        """
        corpus = self.corpus

        self._assert_node_structure_is_correct(corpus.base_node, self.first_letter)

        first_letter_node = corpus.base_node.children[self.first_letter]
        self._assert_node_structure_is_correct(first_letter_node, self.second_letter)

        second_letter_node = first_letter_node.children[self.second_letter]
        self._assert_node_structure_is_correct(second_letter_node, self.third_letter)

        third_letter_node = second_letter_node.children[self.third_letter]
        self._assert_node_structure_is_correct(third_letter_node, self.fourth_letter)

        fourth_letter_node = third_letter_node.children[self.fourth_letter]
        self._assert_node_structure_is_correct(fourth_letter_node, self.fifth_letter)

        fifth_letter_node = fourth_letter_node.children[self.fifth_letter]
        self._assert_number_of_children(fifth_letter_node, 0)

    def _assert_node_structure_is_correct(self, node, letter):
        self._assert_letter_in_children(letter, node)
        self._assert_number_of_children(node, 1)
        self._assert_letters_are_lower_case(node)

    def _assert_letter_in_children(self, letter, node):
        assert letter in node.children

    def _assert_number_of_children(self, node, number_of_children):
        assert len(node.children) == number_of_children

    def _assert_letters_are_lower_case(self, node):
        white_space = ' '  # don't check if white space is lower case
        assert all(letter.islower() if letter != white_space else True for letter in node.children.keys())


class TestCorpusWithOneWordWithWhiteSpaceInWord(TestCorpusOfOneWord):
    WORD = 'hel l'
    first_letter = WORD[0]
    second_letter = WORD[1]
    third_letter = WORD[2]
    fourth_letter = WORD[3]
    fifth_letter = WORD[4]

from search_corpus import make_search_corpus, Word, WordList


class TestWordList:

    def test_word_object_found_in_word_list(self):
        word = Word('hi')
        word_list = WordList()
        word_list.append(word)

        assert word in word_list

    def test_non_existing_word_not_found_in_word_list(self):
        word = Word('hi')
        word_list = WordList()
        word_list.append(Word('his'))

        assert word not in word_list

    def test_adding_to_word_list_works(self):
        word_list = WordList()
        word_list.append(Word('hi'))
        word_list.append(Word('his'))

        assert Word('his') in word_list
        assert len(word_list) == 2


class CorpusTestUtils:

    @property
    def corpus(self):
        return make_search_corpus([self.WORD])

    def _assert_node_structure_is_correct(self, node: Node, letter: str, num_children: int):
        self._assert_letter_is_in_children(letter, node)
        self._assert_number_of_children_in_node(node, num_children)
        self._assert_letters_are_lower_case(node)

    def _assert_letter_is_in_children(self, letter: str, node: Node):
        assert letter in node.children

    def _assert_number_of_children_in_node(self, node: Node, number_of_children: int):
        assert len(node.children) == number_of_children

    def _assert_letters_are_lower_case(self, node: Node):
        white_space = ' '  # don't check if white space is lower case
        assert all(letter.islower() if letter != white_space else True for letter in node.children.keys())

    def _assert_previous_letter_has_referrence_to_next_letter(self, prev_letter: str, next_letter: str, node: Node):
        assert next_letter in node.children[prev_letter].children

    def _assert_letter_has_referrence_to_word_in_node(self, word: str, letter: str, node: Node):
        assert Word(word) in node.children[letter].words


class TestCorpusOfOneWord(CorpusTestUtils):
    WORD = 'hello'
    first_letter = WORD[0]
    second_letter = WORD[1]
    third_letter = WORD[2]
    fourth_letter = WORD[3]
    fifth_letter = WORD[4]

    def test_first_letter_of_word_has_referrence_to_word(self):
        corpus = self.corpus  # this acts as a setUp for the corpus
        assert Word(self.WORD) in corpus.base_node.children[self.first_letter].words

    def test_only_one_letter_is_in_base_of_corpus(self):
        assert len(self.corpus.base_node) == 1

    def test_first_letter_of_word_has_referrence_to_second_letter_of_word(self):
        self._assert_previous_letter_has_referrence_to_next_letter(
            self.first_letter, self.second_letter, self.corpus.base_node)

        assert self.second_letter in self.corpus.base_node.children[self.first_letter].children

    def test_second_letter_is_child_of_first_letter_and_has_referrence_to_word(self):
        self._assert_previous_letter_has_referrence_to_next_letter(
            self.first_letter, self.second_letter, self.corpus.base_node)

        self._assert_letter_has_referrence_to_word_in_node(self.WORD, 'e', self.corpus.base_node.children[self.first_letter])

    def test_third_letter_is_child_of_first_letter_and_has_referrence_to_word(self):
        self._assert_previous_letter_has_referrence_to_next_letter(
            self.second_letter, self.third_letter, self.corpus.base_node.children[self.first_letter])

    def test_the_staructure_of_search_corpus(self):
        """
        Here we test the following:
        - each letter is referrencing the next letter
        - number of children each letter refers to is correct
        - each letter is lower case
        """
        corpus = self.corpus

        self._assert_node_structure_is_correct(corpus.base_node, self.first_letter, num_children=1)

        first_letter_node = corpus.base_node.children[self.first_letter]
        self._assert_node_structure_is_correct(first_letter_node, self.second_letter, num_children=1)

        second_letter_node = first_letter_node.children[self.second_letter]
        self._assert_node_structure_is_correct(second_letter_node, self.third_letter, num_children=1)

        third_letter_node = second_letter_node.children[self.third_letter]
        self._assert_node_structure_is_correct(third_letter_node, self.fourth_letter, num_children=1)

        fourth_letter_node = third_letter_node.children[self.fourth_letter]
        self._assert_node_structure_is_correct(fourth_letter_node, self.fifth_letter, num_children=1)

        fifth_letter_node = fourth_letter_node.children[self.fifth_letter]
        self._assert_number_of_children_in_node(fifth_letter_node, 0)


class TestCorpusWithOneWordWithWhiteSpaceInWord(TestCorpusOfOneWord):
    WORD = 'hel l'
    first_letter = WORD[0]
    second_letter = WORD[1]
    third_letter = WORD[2]
    fourth_letter = WORD[3]
    fifth_letter = WORD[4]


class TestCorpusWithOneWordWithWhiteSpaceAndUpperCaseLetter(TestCorpusOfOneWord):
    WORD = 'hEl l'
    first_letter = WORD[0]
    second_letter = WORD[1].lower()
    third_letter = WORD[2]
    fourth_letter = WORD[3]
    fifth_letter = WORD[4]

    @property
    def corpus(self):
        original_word = '%s' % self.WORD
        self.WORD = self.WORD.lower()
        return make_search_corpus([original_word])


class TestCorpusOfTwoWordsThatStartWithDifferentLetters:

    def test_duplicate_words_are_removed(self):
        corpus = SearchCorpus(['hi', 'hi', 'Hi', 'HI', 'hello', 'Hello', ' heY', ' hey'])
        corpus.preprocess_words()

        assert len(corpus.words) == 3


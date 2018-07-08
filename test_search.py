from pytest import fixture

from search_corpus import make_search_corpus


FIXTURE_FILENAME = './fixture_for_testing.txt'


@fixture(scope='session')
def search_corpus():
    with open(FIXTURE_FILENAME, 'r') as test_fixture_file:
        words = test_fixture_file.readlines()

    return make_search_corpus(words)


class TestSearchQueryWithOnlyOneLetter:
    number_of_words_with_f_as_first_letter = 6
    number_of_words_with_1_as_first_letter = 1

    non_existing_first_letter = '9'

    def test_searching_for_one_letter_returns_correct_number_of_results(self, search_corpus):
        assert len(search_corpus.get_hits_for_letters('f')) == self.number_of_words_with_f_as_first_letter

        assert len(search_corpus.get_hits_for_letters('1')) == self.number_of_words_with_1_as_first_letter

    def test_searching_for_nonexisting_letter_returns_nothing(self, search_corpus):
        assert len(search_corpus.get_hits_for_letters(self.non_existing_first_letter)) == 0

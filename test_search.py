from pytest import fixture

from search_corpus import make_search_corpus


FIXTURE_FILENAME = './fixture_for_testing.txt'

@fixture(scope='session')
def search_corpus():
    with open(FIXTURE_FILENAME, 'r') as test_fixture_file:
        words = test_fixture_file.readlines()

    return make_search_corpus(words)

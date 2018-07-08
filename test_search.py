from typing import List

import pytest
from pytest import fixture

from search_corpus import make_search_corpus, SearchCorpus, Word


FIXTURE_FILENAME = './fixture_for_testing.txt'


@fixture(scope='session')
def search_corpus():
    with open(FIXTURE_FILENAME, 'r') as test_fixture_file:
        words = test_fixture_file.readlines()

    return make_search_corpus(words)


def _assert_number_of_results_for_query(corpus: SearchCorpus, query: str, expected_results: List[Word]):
        query_results = corpus.get_hits_for_letters(query)

        assert len(query_results) == len(expected_results)        
        assert [word.value for word in query_results] == expected_results


@pytest.mark.parametrize(
    'search_query,results',
    [
        (
            'f',
            ['facebook', 'facebook lite', 'facebook pages manager', 'fifa 14 international', 'flappy bird', 'fts15']
        ),
        ('1', ['1mobile market']),
        ('9', []),
        ('fa', ['facebook', 'facebook lite', 'facebook pages manager']),
        ('xm', ['xmodgames']),
        ('11', []),
        (
            'go',
            [
                'go craft 3d', 'go keyboard', 'go launcher prime', 'google contacts sync', 'google drive',
                'google duo', 'google indic keyboard', 'google now launcher', 'google play newsstand',
                'google street view', 'google talkback'
            ]
        ),
        (
            'goo',
            [
                'google contacts sync', 'google drive', 'google duo', 'google indic keyboard',
                'google now launcher', 'google play newsstand', 'google street view', 'google talkback'
            ]
        ),
        ('fac', ['facebook', 'facebook lite', 'facebook pages manager']),
        (
            'google',
            [
                'google contacts sync', 'google drive', 'google duo', 'google indic keyboard',
                'google now launcher', 'google play newsstand', 'google street view', 'google talkback'
            ]
        ),
        (
            'google ',
            [
                'google contacts sync', 'google drive', 'google duo', 'google indic keyboard',
                'google now launcher', 'google play newsstand', 'google street view', 'google talkback'
            ]
        ),
        ('Dropbox', ['dropbox']),
        ('Dropbox ', ['dropbox']),
        ('Dropbox !', []),
        ('3D', ['3d tennis']),
    ]
)
def test_searching_for_string_returns_correct_results(search_corpus, search_query, results):
    _assert_number_of_results_for_query(search_corpus, search_query, results)

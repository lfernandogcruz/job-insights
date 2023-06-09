from src.pre_built.counter import count_ocurrences
import pytest


VALID_PATH = "data/jobs.csv"
INVALID_PATH = "data/steve.csv"

FIRST_WORD_LOWERCASE = "techno"
FIRST_WORD_MIGUXOCASE = "tEcHnO"

SECOND_WORD_LOWERCASE = "company"
SECOND_WORD_MIGUXOCASE = "CoMpAnY"

NONEXISTENT_WORD = "xinforimpola"


def test_counter():
    assert count_ocurrences(VALID_PATH, FIRST_WORD_LOWERCASE) == 4863
    assert count_ocurrences(VALID_PATH, FIRST_WORD_MIGUXOCASE) == 4863

    assert count_ocurrences(VALID_PATH, SECOND_WORD_LOWERCASE) == 3130
    assert count_ocurrences(VALID_PATH, SECOND_WORD_MIGUXOCASE) == 3130

    assert count_ocurrences(VALID_PATH, NONEXISTENT_WORD) == 0


def test_counter_invalid_path_1st_word():
    with pytest.raises(FileNotFoundError):
        count_ocurrences(INVALID_PATH, FIRST_WORD_LOWERCASE)


def test_counter_invalid_path_2nd_word():
    with pytest.raises(FileNotFoundError):
        count_ocurrences(INVALID_PATH, SECOND_WORD_LOWERCASE)


def test_counter_invalid_path_x_word():
    with pytest.raises(FileNotFoundError):
        count_ocurrences(INVALID_PATH, NONEXISTENT_WORD)

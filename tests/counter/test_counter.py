from src.pre_built.counter import count_ocurrences
import pytest


VALID_PATH = "data/jobs.csv"
INVALID_PATH = "data/steve.csv"

FIRST_WORD_LOWERCASE = "python"
FIRST_WORD_MIGUXOCASE = "PyTHoN"

SECOND_WORD_LOWERCASE = "javascript"
SECOND_WORD_MIGUXOCASE = "JaVaScrIPt"

NONEXISTENT_WORD = "xinforimpola"


def test_counter():
    assert count_ocurrences(VALID_PATH, FIRST_WORD_LOWERCASE) == 1639
    assert count_ocurrences(VALID_PATH, FIRST_WORD_MIGUXOCASE) == 1639

    assert count_ocurrences(VALID_PATH, SECOND_WORD_LOWERCASE) == 122
    assert count_ocurrences(VALID_PATH, SECOND_WORD_MIGUXOCASE) == 122

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

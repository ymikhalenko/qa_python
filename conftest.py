import pytest
from main import BooksCollector
from constants import BOOK_1, BOOK_2, GENRE_1, GENRE_2

@pytest.fixture
def collector():
    collector = BooksCollector()
    return collector

@pytest.fixture
def one_book(collector):
    collector.add_new_book(BOOK_1)
    return collector

@pytest.fixture
def two_books(one_book):
    one_book.add_new_book(BOOK_2)
    return one_book

@pytest.fixture
def one_book_with_genre(one_book):
    one_book.set_book_genre(BOOK_1, GENRE_1)
    return one_book

@pytest.fixture
def two_books_with_genres(two_books):
    two_books.set_book_genre(BOOK_1, GENRE_1)
    two_books.set_book_genre(BOOK_2, GENRE_2)
    return two_books

@pytest.fixture
def one_book_with_favorite(one_book):
    one_book.add_book_in_favorites(BOOK_1)
    return one_book
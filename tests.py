import pytest
from main import BooksCollector
from constants import BOOK_1, BOOK_2, GENRE_1


class TestBooksCollector:

    def test_add_new_book_new_books_doesnt_have_genre(self, collector):
        collector.add_new_book(BOOK_1)
        assert not collector.books_genre.get(BOOK_1)
    
    def test_add_new_book_add_one_book(self, collector):
        collector.add_new_book(BOOK_1)
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_add_one_book_with_genre(self, one_book):
        one_book.set_book_genre(BOOK_1, GENRE_1)
        assert one_book.books_genre[BOOK_1] == GENRE_1

    def test_get_book_genre_horror_book_returns_genre(self, one_book_with_genre):
        assert one_book_with_genre.get_book_genre(BOOK_1) == GENRE_1

    def test_get_books_with_specific_genre_horror_genre_returns_book(self, one_book_with_genre):
        assert one_book_with_genre.get_books_with_specific_genre(GENRE_1) == [BOOK_1]

    def test_get_books_genre_returns_book(self, one_book):
            assert len(one_book.get_books_genre()) == 1

    def test_get_books_for_children_two_books_with_genres_returns_one_book(self, two_books_with_genres):
        assert two_books_with_genres.get_books_for_children() == [BOOK_2]

    def test_get_books_for_children_doesnt_return_horror(self, two_books_with_genres):
        assert BOOK_1 not in two_books_with_genres.get_books_for_children()

    def test_add_book_in_favorites_add_book(self, one_book_with_genre):
        one_book_with_genre.add_book_in_favorites(BOOK_1)
        assert one_book_with_genre.get_list_of_favorites_books() == [BOOK_1]

    def test_delete_book_from_favorites_delete_book(self, one_book_with_favorite):
        one_book_with_favorite.delete_book_from_favorites(BOOK_1)
        assert not one_book_with_favorite.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_returns_book(self, one_book_with_favorite):
        assert len(one_book_with_favorite.get_list_of_favorites_books()) == 1
from queue import Empty

import pytest
from main import BooksCollector


class TestBooksCollector:

    @pytest.fixture()
    def four_books_with_genres(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Ужас 2')
        collector.add_new_book('Комедия 2')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')
        collector.set_book_genre('Ужас 2', 'Ужасы')
        collector.set_book_genre('Комедия 2', 'Комедии')
        return collector

    @pytest.fixture()
    def four_books_with_genres_and_two_favorite_books(self, four_books_with_genres):
        four_books_with_genres.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        four_books_with_genres.add_book_in_favorites('Гордость и предубеждение и зомби')
        return four_books_with_genres

    def test_add_new_book_new_books_doesnt_have_genre(self, four_books_with_genres):
        four_books_with_genres.add_new_book('Библия')
        assert not four_books_with_genres.books_genre.get('Библия')
    
    def test_add_new_book_add_four_books(self, four_books_with_genres):
        assert len(four_books_with_genres.get_books_genre()) == 4

    def test_set_book_genre_add_four_books_with_genres(self, four_books_with_genres):
        for book in four_books_with_genres.books_genre:
            assert four_books_with_genres.books_genre[book]

    def test_get_book_genre_comedy_book_returns_comedy_genre(self, four_books_with_genres):
            assert four_books_with_genres.get_book_genre('Что делать, если ваш кот хочет вас убить') == 'Комедии'

    def test_get_books_with_specific_genre_comdey_genre_returns_two_books(self, four_books_with_genres):
        assert len(four_books_with_genres.get_books_with_specific_genre('Комедии')) == 2

    def test_get_books_for_children_returns_two_books(self, four_books_with_genres):
            assert len(four_books_with_genres.get_books_for_children()) == 2

    def test_get_books_for_children_doesnt_return_horror(self, four_books_with_genres):
            assert 'Гордость и предубеждение и зомби' not in four_books_with_genres.get_books_for_children()

    def test_add_book_in_favorites_add_two_books(self, four_books_with_genres_and_two_favorite_books):
        assert len(four_books_with_genres_and_two_favorite_books.get_list_of_favorites_books()) == 2

    def test_delete_book_from_favorites_delete_two_books(self, four_books_with_genres_and_two_favorite_books):
        four_books_with_genres_and_two_favorite_books.delete_book_from_favorites('Что делать, если ваш кот хочет вас убить')
        four_books_with_genres_and_two_favorite_books.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert not four_books_with_genres_and_two_favorite_books.get_list_of_favorites_books()
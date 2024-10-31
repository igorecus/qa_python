import pytest
from main import BooksCollector

class TestBooksCollector:

    @pytest.mark.parametrize(
        "book_name, expected_books",
        [
            ("Шекспир", {"Шекспир": ""}),
            ("", {}),
            ("A" * 41, {}),
            ("12345", {"12345": ""}),
            ("Шекспир", {"Шекспир": ""}),
        ],
    )
    def test_add_new_book(self, book_name, expected_books):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert collector.get_books_genre() == expected_books

    @pytest.mark.parametrize(
        "book_name, genre, initial_books, expected_books",
        [
            ("Шекспир", "Фантастика", {"Шекспир": ""}, {"Шекспир": "Фантастика"}),
            ("Шекспир", "Несуществующий жанр", {"Шекспир": ""}, {"Шекспир": ""}),
            ("Несуществующая книга", "Фантастика", {}, {}),
        ],
    )
    def test_set_book_genre(self, book_name, genre, initial_books, expected_books):
        collector = BooksCollector()
        collector.books_genre = initial_books
        collector.set_book_genre(book_name, genre)
        assert collector.get_books_genre() == expected_books

    @pytest.mark.parametrize(
        "book_name, initial_books, expected_genre",
        [
            ("Шекспир", {"Шекспир": "Фантастика"}, "Фантастика"),
            ("Шекспир", {"Шекспир": ""}, ""),
            ("Несуществующая книга", {}, None),
        ],
    )
    def test_get_book_genre(self, book_name, initial_books, expected_genre):
        collector = BooksCollector()
        collector.books_genre = initial_books
        assert collector.get_book_genre(book_name) == expected_genre

    @pytest.mark.parametrize(
        "genre, initial_books, expected_books",
        [
            ("Фантастика", {"Шекспир": "Фантастика"}, ["Шекспир"]),
            ("Несуществующий жанр", {"Шекспир": "Фантастика"}, []),
            ("Фантастика", {}, []),
        ],
    )
    def test_get_books_with_specific_genre(self, genre, initial_books, expected_books):
        collector = BooksCollector()
        collector.books_genre = initial_books
        assert collector.get_books_with_specific_genre(genre) == expected_books

    @pytest.mark.parametrize(
        "initial_books, expected_books",
        [
            ({"Шекспир": "Фантастика"}, ["Шекспир"]),
            ({"Ужасы": "Ужасы"}, []),
            ({}, []),
        ],
    )
    def test_get_books_for_children(self, initial_books, expected_books):
        collector = BooksCollector()
        collector.books_genre = initial_books
        assert collector.get_books_for_children() == expected_books

    @pytest.mark.parametrize(
        "book_name, initial_books, expected_favorites",
        [
            ("Шекспир", {"Шекспир": ""}, ["Шекспир"]),
            ("Несуществующая", {}, []),
        ],
    )
    def test_add_book_in_favorites(self, book_name, initial_books, expected_favorites):
        collector = BooksCollector()
        collector.books_genre = initial_books
        collector.add_book_in_favorites(book_name)
        assert collector.get_list_of_favorites_books() == expected_favorites

    @pytest.mark.parametrize(
        "book_name, initial_favorites, expected_favorites",
        [
            ("Шекспир", ["Шекспир"], []),
            ("Несуществующая", ["Шекспир"], ["Шекспир"]),
        ],
    )
    def test_delete_book_from_favorites(self, book_name, initial_favorites, expected_favorites):
        collector = BooksCollector()
        collector.favorites = initial_favorites
        collector.delete_book_from_favorites(book_name)
        assert collector.get_list_of_favorites_books() == expected_favorites

    @pytest.mark.parametrize(
        "initial_favorites, expected_favorites",
        [
            (["Шекспир"], ["Шекспир"]),
            ([], []),
        ],
    )
    def test_get_list_of_favorites_books(self, initial_favorites, expected_favorites):
        collector = BooksCollector()
        collector.favorites = initial_favorites
        assert collector.get_list_of_favorites_books() == expected_favorites

import pytest
from main import BooksCollector  # Изменено импортирование на main

@pytest.fixture
def collector():
    # Фикстура создаёт новый экземпляр класса BooksCollector перед каждым тестом
    return BooksCollector()

@pytest.mark.parametrize("book_name", ["Гарри Поттер", "Дюна", "1984"])
def test_add_new_book(collector, book_name):
    # Добавляем книгу и проверяем, что она действительно добавилась в словарь
    collector.add_new_book(book_name)
    assert book_name in collector.get_books_genre()

@pytest.mark.parametrize("book_name, genre", [("Гарри Поттер", "Фантастика"), ("Дюна", "Фантастика"), ("Шерлок Холмс", "Детективы")])
def test_set_book_genre(collector, book_name, genre):
    # Добавляем книгу, устанавливаем её жанр и проверяем корректность
    collector.add_new_book(book_name)
    collector.set_book_genre(book_name, genre)
    assert collector.get_book_genre(book_name) == genre

@pytest.mark.parametrize("book_name", ["Книга с очень длинным названием, которое превышает 40 символов"])
def test_add_new_book_too_long(collector, book_name):
    # Проверяем, что книга с названием > 40 символов не добавляется
    collector.add_new_book(book_name)
    assert book_name not in collector.get_books_genre()

def test_get_book_genre(collector):
    # Проверяем, что метод корректно возвращает жанр книги
    collector.add_new_book("Гарри Поттер")
    collector.set_book_genre("Гарри Поттер", "Фантастика")
    assert collector.get_book_genre("Гарри Поттер") == "Фантастика"

def test_set_invalid_book_genre(collector):
    # Проверяем, что невозможно установить несуществующий жанр
    collector.add_new_book("Гарри Поттер")
    collector.set_book_genre("Гарри Поттер", "Роман")  # Нет в списке доступных жанров
    assert collector.get_book_genre("Гарри Поттер") == ""

def test_get_books_with_specific_genre(collector):
    # Проверяем, что метод возвращает книги только заданного жанра
    collector.add_new_book("Гарри Поттер")
    collector.set_book_genre("Гарри Поттер", "Фантастика")
    assert collector.get_books_with_specific_genre("Фантастика") == ["Гарри Поттер"]

def test_get_books_for_children(collector):
    # Проверяем, что метод возвращает только детские книги
    collector.add_new_book("Гарри Поттер")
    collector.set_book_genre("Гарри Поттер", "Фантастика")
    collector.add_new_book("Шерлок Холмс")
    collector.set_book_genre("Шерлок Холмс", "Детективы")
    assert "Гарри Поттер" in collector.get_books_for_children()
    assert "Шерлок Холмс" not in collector.get_books_for_children()

def test_add_book_in_favorites(collector):
    # Проверяем, что книга добавляется в избранное
    collector.add_new_book("Гарри Поттер")
    collector.add_book_in_favorites("Гарри Поттер")
    assert "Гарри Поттер" in collector.get_list_of_favorites_books()

def test_add_duplicate_book_in_favorites(collector):
    # Проверяем, что нельзя добавить одну книгу в избранное дважды
    collector.add_new_book("Гарри Поттер")
    collector.add_book_in_favorites("Гарри Поттер")
    collector.add_book_in_favorites("Гарри Поттер")
    assert collector.get_list_of_favorites_books().count("Гарри Поттер") == 1

def test_delete_book_from_favorites(collector):
    # Проверяем удаление книги из избранного
    collector.add_new_book("Гарри Поттер")
    collector.add_book_in_favorites("Гарри Поттер")
    collector.delete_book_from_favorites("Гарри Поттер")
    assert "Гарри Поттер" not in collector.get_list_of_favorites_books()

def test_delete_nonexistent_book_from_favorites(collector):
    # Проверяем, что удаление несуществующей книги не вызывает ошибку
    collector.delete_book_from_favorites("Несуществующая книга")
    assert collector.get_list_of_favorites_books() == []

def test_get_list_of_favorites_books(collector):
    # Проверяем, что список избранных книг формируется корректно
    collector.add_new_book("Гарри Поттер")
    collector.add_new_book("Дюна")
    collector.add_book_in_favorites("Гарри Поттер")
    assert collector.get_list_of_favorites_books() == ["Гарри Поттер"]

def test_add_new_book_add_two_books(collector):
    # Тест добавления двух книг
    collector.add_new_book("Гордость и предубеждение и зомби")
    collector.add_new_book("Что делать, если ваш кот хочет вас убить")
    assert len(collector.get_books_genre()) == 2

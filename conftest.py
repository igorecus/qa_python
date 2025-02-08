import pytest
from main import BooksCollector  # Импортируем класс из main.py

@pytest.fixture
def collector():
    """Создаёт и возвращает новый экземпляр BooksCollector перед каждым тестом."""
    return BooksCollector()

import pytest
from main import BooksCollector

class TestBooksCollector:

    # Проверка метода add_new_book

    def test_add_new_book_add_same_book_twice(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.add_new_book('Война и мир')
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('name', ['', 'A' * 41])

    def test_add_new_book_invalid_name_not_added(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 0
    
    def test_add_new_book_valid_name_40_chars(self):
        collector = BooksCollector()
        name = 'A' * 40
        collector.add_new_book(name)
        assert name in collector.get_books_genre()

    # Проверка метода set_book_genre
    
    def test_set_book_genre_valid_book_and_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert collector.get_book_genre('Гарри Поттер') == 'Фантастика'

    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс', 'Роман')
        assert collector.get_book_genre('Шерлок Холмс') == ''

    # Проверка метода get_book_genre

    def test_get_book_genre_book_without_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга без жанра')
        assert collector.get_book_genre('Книга без жанра') == ''
    
    def test_get_book_genre_nonexistent_book(self):
        collector = BooksCollector()
        assert collector.get_book_genre('Несуществующая книга') is None

    # Проверка метода get_books_with_specific_genre

    def test_get_books_with_specific_genre_multiple_books(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.add_new_book('Книга 3')
        collector.set_book_genre('Книга 1', 'Ужасы')
        collector.set_book_genre('Книга 2', 'Комедии')
        collector.set_book_genre('Книга 3', 'Ужасы')
        
        horror_books = collector.get_books_with_specific_genre('Ужасы')
        assert len(horror_books) == 2
        assert 'Книга 1' in horror_books
        assert 'Книга 3' in horror_books

    # Проверка метода get_books_genre

    def test_get_books_genre_returns_same_dictionary(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        collector.add_new_book('Хоббит')
        collector.add_new_book('Сильмариллион')

        books_genre = collector.get_books_genre()

        assert len(books_genre) == 3
        assert 'Властелин колец' in books_genre
        assert 'Хоббит' in books_genre
        assert 'Сильмариллион' in books_genre

    # Проверка метода get_books_for_children

    def test_get_books_for_children_only_appropriate_genres(self):
        collector = BooksCollector()
        collector.add_new_book('Карлик Нос')
        collector.add_new_book('Оно')
        collector.add_new_book('Карлик')
        collector.add_new_book('Таня Гроттер')
        
        collector.set_book_genre('Карлик Нос', 'Мультфильмы')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Карлик', 'Детективы')
        collector.set_book_genre('Таня Гроттер', 'Фантастика')
        
        children_books = collector.get_books_for_children()
        assert len(children_books) == 2
        assert 'Карлик Нос' in children_books
        assert 'Таня Гроттер' in children_books
        assert 'Оно' not in children_books
        assert 'Карлик' not in children_books

    # Проверка метода add_book_in_favorites

    def test_add_book_in_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book('Маленькие трагедии')
        collector.add_book_in_favorites('Маленькие трагедии')
        assert 'Маленькие трагедии' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book('Мастер и Маргарита')
        collector.add_book_in_favorites('Мастер и Маргарита')
        collector.add_book_in_favorites('Мастер и Маргарита')
        assert len(collector.get_list_of_favorites_books()) == 1

    # Проверка метода delete_book_from_favorites

    def test_delete_book_from_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book('Дракула')
        collector.add_book_in_favorites('Дракула')
        collector.delete_book_from_favorites('Дракула')
        assert 'Дракула' not in collector.get_list_of_favorites_books()

    # Проверка метода get_list_of_favorites_books

    def test_get_list_of_favorites_books_empty(self):
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() == []
    
    def test_get_list_of_favorites_books_with_multiple_books(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 4')
        collector.add_new_book('Книга 5')
        collector.add_new_book('Книга 6')
        
        collector.add_book_in_favorites('Книга 4')
        collector.add_book_in_favorites('Книга 5')
        
        favorites = collector.get_list_of_favorites_books()
        assert len(favorites) == 2
        assert favorites == ['Книга 4', 'Книга 5']

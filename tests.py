import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:
    
    @pytest.fixture(autouse=True)
    def create_empty_collector(self):
        self.sut = BooksCollector()

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_with_empty_name(self):
        self.sut.add_new_book('')
        assert len(self.sut.get_books_genre()) == 0

    def test_set_book_genre_for_existing_book_and_legal_genre(self):
        book_name = 'Солярис'
        book_genre = self.sut.genre[0]
        self.sut.add_new_book(book_name)
        self.sut.set_book_genre(book_name, book_genre)
        assert self.sut.get_book_genre(book_name) == book_genre

    def test_get_book_genre_from_empty_collector(self):
        assert self.sut.get_book_genre('Чук и Гек') is None

    @pytest.mark.parametrize(
        'search_genre, expected_result',
        [('Ужасы', ['Книга 1', 'Книга 3']),
         ('Комедии', ['Книга 2']),
         ('Фантастика', []),
         ('Dummy12345', []), ])
    def test_get_books_with_specific_genre_all_cases(self, search_genre, expected_result):
        for name, genre in [('Книга 1', 'Ужасы'),
                            ('Книга 2', 'Комедии'),
                            ('Книга 3', 'Ужасы')]:
            self.sut.add_new_book(name)
            self.sut.set_book_genre(name, genre)
        assert self.sut.get_books_with_specific_genre(search_genre) \
               == expected_result

    def test_get_books_genre_for_empty_collector(self):
        assert self.sut.get_books_genre() == {}
        
    def test_get_books_for_children_returns_many_books(self):
        for name, genre in [('Книга 1', 'Ужасы'),
                            ('Книга 2', 'Комедии'),
                            ('Книга 3', 'Детективы'),
                            ('Книга 4', 'Фантастика')]:
            self.sut.add_new_book(name)
            self.sut.set_book_genre(name, genre)
        assert self.sut.get_books_for_children() \
               == ['Книга 2', 'Книга 4']
        
    def test_add_book_in_favorites_single_book_single_book(self):
        book_name = 'Чебурашка'
        self.sut.add_new_book(book_name)
        self.sut.add_book_in_favorites(book_name)
        assert self.sut.get_list_of_favorites_books() == [book_name]

    def test_delete_book_from_favorites_single_book_empty_list(self):
        book_name = 'Чебурашка'
        self.sut.add_new_book(book_name)
        self.sut.add_book_in_favorites(book_name)
        self.sut.delete_book_from_favorites(book_name)
        assert self.sut.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_for_empty_collector(self):
        assert self.sut.get_list_of_favorites_books() == []
        

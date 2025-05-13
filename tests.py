from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

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
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector() 
    class BooksCollector:
    def init(self):
        self.books_genre = {}
        self.favorites = []
        self.genre = ["Фантастика", "Детектив", "Роман", "Нон-фикшн"]
        self.genreagerating = {
            "Фантастика": "12+",
            "Детектив": "16+",
            "Роман": "0+",
            "Нон-фикшн": "0+",
        }

    def add_new_book(self, title):
        if len(title) > 40:
            raise Value_Error("Название книги не должно превышать 40 символов.")
        if title in self.books_genre:
            raise Value_Error("Эта книга уже добавлена.")
        self.books_genre[title] = None

    def add_specific_genre(self, title, genre):
        if genre not in self.genre:
            raise Value_Error("Этот жанр недоступен.")
        if title in self.books_genre:
            self.books_genre[title] = genre
        else:
            raise Value_Error("Сначала добавьте книгу без жанра.")

    def add_bookin_favorites(self, title):
        if title not in self.books_genre:
            raise Value_Error("Эта книга не добавлена.")
        if title in self.favorites:
            raise Value_Error("Эта книга уже в избранном.")
        self.favorites.append(title)

    def delete_book_from_favorites(self, title):
        if title in self.favorites:
            self.favorites.remove(title)
        else:
            raise Value_Error("Эта книга не найдена в избранном.")

    def get_list_of_favorites_books(self):
        return self.favorites

    def get_genres(self):
        return self.genre


import unittest


class Test_Books_Collector(unittest.TestCase):
    def setUp(self):
        self.collector = BooksCollector()

    def test_add_new_book(self):
        self.collector.add_new_book("Книга 1")
        self.assert_In("Книга 1", self.collector.books_genre)
        self.assert_Is_None(self.collector.books_genre["Книга 1"])

    def test_add_new_book too_long_title(self):
        with self.assert_Raises(Value_Error):
            self.collector.add_new_book("x" * 41)  # Название слишком длинное

    def test_add_duplicate_book(self):
        self.collector.add_new_book("Книга 1")
        with self.assert_Raises(Value_Error):
            self.collector.add_new_book("Книга 1")  # Дубликат книги

    def test_add_specific_genre(self):
        self.collector.add_new_book("Книга 1")
        self.collector.add_specific_genre("Книга 1", "Фантастика")
        self.assert_Equal(self.collector.books_genre["Книга 1"], "Фантастика")

    def test_add_specific_genreinvalid_genre(self):
        self.collector.add_new_book("Книга 1")
        with self.assert_Raises(Value_Error):
            self.collector.add_specific_genre(
                "Книга 1", "Неизвестный жанр"
            )  # Неверный жанр

    def test_add_specific_genre_without_prior_addition(self):
        with self.assert_Raises(Value_Error):
            self.collector.add_specific_genre(
                "Книга 1", "Фантастика"
            )  # Книга еще не добавлена

    def test_add_book_in_favorites(self):
        self.collector.add_new_book("Книга 1")
        self.collector.add_specific_genre("Книга 1", "Фантастика")
        self.collector.add_bookin_favorites("Книга 1")
        self.assertIn("Книга 1", self.collector.get_list_of_favorites_books())

    def test_add_book_in_favorites_not_added_book(self):
        with self.assert_Raises(Value_Error):
            self.collector.add_bookin_favorites("Книга 1")  # Книга не добавлена

    def test_add_bookin_favorites_duplicateentry(self):
        self.collector.add_new_book("Книга 1")
        self.collector.add_specific_genre("Книга 1", "Фантастика")
        self.collector.add_bookin_favorites("Книга 1")
        with self.assert_Raises(Value_Error):
            self.collector.add_bookin_favorites("Книга 1")  # Дубликат в избранном

    def test_delete_book_from_favorites(self):
        self.collector.add_new_book("Книга 1")
        self.collector.add_specific_genre("Книга 1", "Фантастика")
        self.collector.add_bookin_favorites("Книга 1")
        self.collector.delete_book_from_favorites("Книга 1")
        self.assert_Not_In("Книга 1", self.collector.get_list_of_favorites_books())

    def test_delete_book_from_favorites_not_in_favorites(self):
        with self.assert_Raises(Value_Error):
            self.collector.delete_book_from_favorites("Книга 1")  # Книга не в избранном

    def test_get_list_of_favorites_books(self):
        self.collector.add_new_book("Книга 1")
        self.collector.add_specific_genre("Книга 1", "Фантастика")
        self.collector.add_bookin_favorites("Книга 1")
        self.assert_Equal(self.collector.get_list_of_favorites_books(), ["Книга 1"])

    def test_get_genres(self):
        self.assert_Equal(
            self.collector.get_genres(),
            ["Фантастика", "Детектив", "Роман", "Нон-фикшн"],
        )
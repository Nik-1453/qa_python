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
        self.genreagerating = {"Фантастика": "12+", "Детектив": "16+", "Роман": "0+", "Нон-фикшн": "0+"}
    def addnewbook(self, title):
        if len(title) > 40:
            raise ValueError("Название книги не должно превышать 40 символов.")
        if title in self.books_genre:
            raise ValueError("Эта книга уже добавлена.")
        self.books_genre[title] = None
    def addspecificgenre(self, title, genre):
        if genre not in self.genre:
            raise ValueError("Этот жанр недоступен.")
        if title in self.books_genre:
            self.books_genre[title] = genre
        else:
            raise ValueError("Сначала добавьте книгу без жанра.")
    def addbookin_favorites(self, title):
        if title not in self.books_genre:
            raise ValueError("Эта книга не добавлена.")
        if title in self.favorites:
            raise ValueError("Эта книга уже в избранном.")
        self.favorites.append(title)
    def deletebookfrom_favorites(self, title):
        if title in self.favorites:
            self.favorites.remove(title)
        else:
            raise ValueError("Эта книга не найдена в избранном.")
    def getlistoffavoritesbooks(self):
        return self.favorites
    def get_genres(self):
        return self.genre

import unittest
class TestBooksCollector(unittest.TestCase):
    def setUp(self):
        self.collector = BooksCollector()
    def testaddnew_book(self):
        self.collector.addnewbook("Книга 1")
        self.assertIn("Книга 1", self.collector.books_genre)
        self.assertIsNone(self.collector.books_genre["Книга 1"])
    def testaddnewbooktoolongtitle(self):
        with self.assertRaises(ValueError):
            self.collector.addnewbook("x" * 41)  # Название слишком длинное
    def testaddduplicate_book(self):
        self.collector.addnewbook("Книга 1")
        with self.assertRaises(ValueError):
            self.collector.addnewbook("Книга 1")  # Дубликат книги
    def testaddspecific_genre(self):
        self.collector.addnewbook("Книга 1")
        self.collector.addspecificgenre("Книга 1", "Фантастика")
        self.assertEqual(self.collector.books_genre["Книга 1"], "Фантастика")
    def testaddspecificgenreinvalid_genre(self):
        self.collector.addnewbook("Книга 1")
        with self.assertRaises(ValueError):
            self.collector.addspecificgenre("Книга 1", "Неизвестный жанр")  # Неверный жанр
    def testaddspecificgenrewithoutprioraddition(self):
        with self.assertRaises(ValueError):
            self.collector.addspecificgenre("Книга 1", "Фантастика")  # Книга еще не добавлена
    def testaddbookinfavorites(self):
        self.collector.addnewbook("Книга 1")
        self.collector.addspecificgenre("Книга 1", "Фантастика")
        self.collector.addbookin_favorites("Книга 1")
        self.assertIn("Книга 1", self.collector.getlistoffavoritesbooks())
    def testaddbookinfavoritesnotadded_book(self):
        with self.assertRaises(ValueError):
            self.collector.addbookin_favorites("Книга 1")  # Книга не добавлена
    def testaddbookinfavoritesduplicateentry(self):
        self.collector.addnewbook("Книга 1")
        self.collector.addspecificgenre("Книга 1", "Фантастика")
        self.collector.addbookin_favorites("Книга 1")
        with self.assertRaises(ValueError):
            self.collector.addbookin_favorites("Книга 1")  # Дубликат в избранном
    def testdeletebookfromfavorites(self):
        self.collector.addnewbook("Книга 1")
        self.collector.addspecificgenre("Книга 1", "Фантастика")
        self.collector.addbookin_favorites("Книга 1")
        self.collector.deletebookfrom_favorites("Книга 1")
        self.assertNotIn("Книга 1", self.collector.getlistoffavoritesbooks())
    def testdeletebookfromfavoritesnotin_favorites(self):
        with self.assertRaises(ValueError):
            self.collector.deletebookfrom_favorites("Книга 1")  # Книга не в избранном
    def testgetlistoffavorites_books(self):
        self.collector.addnewbook("Книга 1")
        self.collector.addspecificgenre("Книга 1", "Фантастика")
        self.collector.addbookin_favorites("Книга 1")
        self.assertEqual(self.collector.getlistoffavoritesbooks(), ["Книга 1"])
    def testgetgenres(self):
        self.assertEqual(self.collector.get_genres(), ["Фантастика", "Детектив", "Роман", "Нон-фикшн"])
if name == "main":
    unittest.main()

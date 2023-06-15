import time
import unittest
from common_word import (
    find_most_common_word
)

class FileProcessingTest(unittest.TestCase):

    def test_text_1(self):
        start_time = time.time()
        file_path = 'text_1.txt'
        most_common_word, count = find_most_common_word(file_path)
        end_time = time.time()
        elapsed_time = end_time - start_time

        print("\n""Файл text_1.txt:")
        print("Найчастіше слово:", most_common_word)
        print("Кількість входжень найчастішого слова:", count)
        print("Час виконання:", elapsed_time, "секунд")

    def test_text_2(self):
        start_time = time.time()
        file_path = 'text_2.txt'
        most_common_word, count = find_most_common_word(file_path)
        end_time = time.time()
        elapsed_time = end_time - start_time

        print("\n""Файл text_2.txt:")
        print("Найчастіше слово:", most_common_word)
        print("Кількість входжень найчастішого слова:", count)
        print("Час виконання:", elapsed_time, "секунд")

    def test_text_3(self):
        start_time = time.time()
        file_path = 'text_3.txt'
        most_common_word, count = find_most_common_word(file_path)
        end_time = time.time()
        elapsed_time = end_time - start_time

        print("\n""Файл text_3.txt:")
        print("Найчастіше слово:", most_common_word)
        print("Кількість входжень найчастішого слова:", count)
        print("Час виконання:", elapsed_time, "секунд")

    def test_text_4(self):
        start_time = time.time()
        file_path = 'text_4.txt'
        most_common_word, count = find_most_common_word(file_path)
        end_time = time.time()
        elapsed_time = end_time - start_time

        print("\n""Файл text_4.txt:")
        print("Найчастіше слово:", most_common_word)
        print("Кількість входжень найчастішого слова:", count)
        print("Час виконання:", elapsed_time, "секунд")

    def test_text_5(self):
        start_time = time.time()
        file_path = 'text_5.txt'
        most_common_word, count = find_most_common_word(file_path)
        end_time = time.time()
        elapsed_time = end_time - start_time

        print("\n""Файл text_5.txt:")
        print("Найчастіше слово:", most_common_word)
        print("Кількість входжень найчастішого слова:", count)
        print("Час виконання:", elapsed_time, "секунд")


if __name__ == '__main__':
    unittest.main()

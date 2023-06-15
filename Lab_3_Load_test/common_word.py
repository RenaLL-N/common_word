import re

def find_most_common_word(file_path):
    word_count = {}

    # Відкриваємо файл для читання
    with open(file_path, 'r') as file:
        # Читаємо файл по рядках
        for line in file:
            # Розбиваємо рядок на окремі слова
            words = re.findall(r'\b\w+\b', line.lower())

            # Підраховуємо кількість входжень кожного слова
            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

    # Знаходимо найчастіше слово та його кількість входжень
    most_common_word = max(word_count, key=word_count.get)
    count = word_count[most_common_word]

    return most_common_word, count


# Приклад використання програми
file_path = 'text.txt'  # Шлях до текстового файлу
most_common_word, count = find_most_common_word(file_path)
print("Найчастіше слово:", most_common_word)
print("Кількість входжень найчастішого слова:", count)
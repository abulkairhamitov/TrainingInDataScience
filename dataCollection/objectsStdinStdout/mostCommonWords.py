import sys
from collections import Counter

# Передать число слов в качестве первого аргумента
try:
    num_words = int(sys.argv[1])
except:
    print("Ошибка")
    sys.exit(1)

counter = Counter(word.lower() # Перевести в строчные
                    for line in sys.stdin
                    for word in line.strip().split() # Разбить строку по пробелам
                    if word) # Пропустить пустые слова

for word, count in counter.most_common(num_words):
    sys.stdout.write(str(count))
    sys.stdout.write("\t")
    sys.stdout.write(word)
    sys.stdout.write("\n")
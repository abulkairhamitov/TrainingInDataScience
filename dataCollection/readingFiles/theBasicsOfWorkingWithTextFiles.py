import re
# 'r' - только для чтения
file_for_reading = open('reading_file.txt', 'r')

# 'w' пишет в файл - сотрет файл, если он уже существует!
file_for_writing = open('writing_file.txt', 'w')

# 'a' - добавляет - для добавления в конец файла
file_for_appeding = open('appending_file.txt', 'a')

# Не забыть закрыть файл в конце работы
file_for_writing.close()

# Чтобы исключать случаи, когда файлы по той или иной причине не были закрыты
# следует использовать оператор with
with open('filename.txt', 'r') as f:
    data = f # что-то сделать с данными
    # process(data)

starts_with_hash = 0

with open('inpurt.txt', 'r') as f:
    for line in f:
        if re.match("^#", line): # строки начинающиеся на '#'
            starts_with_hash += 1
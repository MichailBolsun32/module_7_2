def custom_write(file_name, strings):
    file = open(str(file_name), 'a',  encoding='utf-8')

    number_str = 1
    result = {}

    for str_ in strings:
        key = []
        key.append(number_str)
        key.append(file.tell())
        result[tuple(key)] = str_
        file.write(str_ + '\n')
        number_str += 1

    file.close()
    return result

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
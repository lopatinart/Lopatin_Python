# Из предложенного текстового файла (text18-17.txt) вывести на экран его содержимое,
# количество знаков препинания. Сформировать новый файл, в который поместить текст в
# стихотворной форме предварительно поставив последнюю строку между первой и второй

with open('text18-17.txt', encoding='utf-16') as file:
    text = file.read()
    print(text, '\n')
    chars = [',', '.', ';', ':', '...', '—', '?', '!']
    chars_count = 0
    for line in text:
        for i in line:
            if i in chars:
                chars_count += 1
    print(chars_count)

with open('text-file.txt', 'w') as file2:
    text_list = text.split('\n')
    last_str = text_list[-1]
    text_list.remove(last_str)
    text_list.insert(1, last_str)

    file2.write('\n'.join(text_list))

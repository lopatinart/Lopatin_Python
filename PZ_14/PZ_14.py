# Из исходного текстового файла (experience.txt) выбрать стаж работы. Посчитать
# количество полученных элементов.

import re

with open("experience.txt", "r", encoding="utf8") as file:
    text = file.read()
    exp = re.findall(r"\d{1,2} (?:лет|год(?:а)?)?(?: \d{1,2} месяц(?:ев)?)?", text)
    print(f"Всего: {len(exp)}")

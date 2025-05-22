#!/bin/env python3

import glob, os

# change CWD
os.chdir("..")

# generate symbols
letters = []
for i in range(32):
    letters += [chr(ord('А') + i) + ' ' + chr(ord('а') + i)]
letters = letters[:6] + ["Ё ё"] + letters[6:]
print(letters)

# list names
names = ["а", "бэ", "вэ", "гэ", "де", "е", "ё", "жэ", "зэ", "и", "и краткое", "ка", "эл", "эм", "эн", "о", "пэ", "эр", "эс", "тэ", "у", "эф", "ха", "цэ", "чэ", "ша", "ща", "твёрдый знак", "ы", "мягкий знак", "э или э оборотное", "ю", "я"]

# list illustration names
illustration_names = [
    'ананас',    # А
    'банан',     # Б
    'вишня',     # В
    'груша',     # Г
    'дом',       # Д
    'еда',       # Е
    'ёлка',      # Ё
    'жираф',     # Ж
    'зонт',      # З
    'игла',      # И
    'йогурт',    # Й
    'кот',       # К
    'лимон',     # Л
    'машина',    # М
    'нос',       # Н
    'окно',      # О
    'пёс',       # П
    'роза',      # Р
    'солнце',    # С
    'тигр',      # Т
    'утка',      # У
    'фотоаппарат', # Ф
    'хлеб',      # Х
    'цветок',    # Ц
    'часы',      # Ч
    'шар',       # Ш
    'щука',      # Щ
    'подъезд',   # Ъ
    'мышь',      # Ы
    'дверь',     # Ь
    'эскимо',    # Э
    'юла',       # Ю
    'яблоко'     # Я
]

# get letter images
letter_img = glob.glob("img/letters/*.svg")
letter_img.sort()

# get illustrations
illustration = glob.glob("img/illustrations/*.png")
illustration.sort()

if __name__ == "__main__":
    with open("alfavit.htm", "w") as f:
        f.write("<table>")
        # generate table header
        f.write("<thead><tr><th>Буква</th><th>Курсив</th><th>Почерк</th><th>Название</th><th>Иллюстрация</th><th>Слово</th></tr></thead>")
        # generate table body
        f.write("<tbody>")
        for i in range(33):
            f.write(f"<tr><td>{letters[i]}</td><td><i>{letters[i]}</i></td><td><img src=\"{letter_img[i]}\"></img></td><td>{names[i]}</td><td><img src=\"{illustration[i]}\"></img></td><td>{illustration_names[i]}</td></tr>")
        f.write("</tbody>")
        f.write("</table>")
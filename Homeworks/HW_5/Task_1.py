#  Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
#  Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


def parse_file_path(link: str):
    splited = link.split(".")
    extension = splited[1]
    without_extension = splited[0].split("\\")
    name = without_extension[-1]
    path = "\\".join(without_extension[:-1])
    return path, name, extension

link = "C:\\Users\\caelp\\Downloads\\InstrukcjaPakiet4kursow.pdf"

print(parse_file_path(link))
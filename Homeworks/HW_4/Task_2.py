# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.


def get_dict(**kwargs):
    my_dict = {}
    for key, value in kwargs.items():
        try:
            hash(value)
            my_dict.setdefault(value, key)
        except TypeError:
            my_dict.setdefault(str(value), key)
    return my_dict


print(get_dict(a=123, b=2.56, c="hello", d=(3, 6, 5), e=[34, 65, "by!"]))

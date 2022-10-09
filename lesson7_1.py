# Реализовать класс CallbackData, принимающий на вход неограниченное количество аргументов
# в виде строк, а также аргумент prefix (user) в виде строки
# 'target', 'action', 'id'
# Реализовать метод new, принимающий неограниченное количество аргументов, НО количестов должно
# совпадать с количеством на вход конструктора
# 'category', 'all', '0' и возвращать user:category:all:0
# Реализовать метод parse, принимающий строку в виде user:category:all:0 и возвращающий словарь
# {'target': 'category', 'action': 'all', 'id': 0}
# Реализовать метод filtor, принимающий строку и возвращающий True/False, если это строка данного
# объекта`

class CallbackData(object):

    def __init__(self, prefix: str, *args) -> None:
        self.prefix = prefix
        self.args = tuple(map(str, args))  # make from args a tuple of strings

    def new(self, *args) -> str:
        if len(args) != len(self.args):  # if not the same length, raise an error
            raise ValueError
        return self.prefix + ':' + ':'.join(map(str, args))

    def parse(self, callback_data: str) -> dict:
        if not self.filter(callback_data=callback_data):
            raise ValueError
        callback_data = callback_data.split(':')
        del callback_data[0]  # remove the first element (prefix)
        data = {}
        for i in range(len(self.args)):
            data[self.args[i]] = callback_data[i]
        return data

    def filter(self, callback_data: str) -> bool:
        callback_data = callback_data.split(':')
        if callback_data[0] != self.prefix:  # check if the prefix is correct
            return False
        if len(callback_data[1:]) != len(self.args):  # check if lengths are the same
            return False
        return True


user_cb = CallbackData('user', 'target', 'action', 'id')
print(user_cb.new('category', 'all', 0))
callback_data = user_cb.new('category', 'all', 0)
print(user_cb.parse(callback_data=callback_data))
print(user_cb.filter(callback_data=callback_data))
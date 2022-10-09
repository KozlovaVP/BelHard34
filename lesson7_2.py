# Реализовать класс InlineButton, принимающий атрибут text: str, callback_data: str
# реализовать метод dict() - возвращающий словарь с атрибутами и их значениями

# Реализовать класс InlineMarkup, принимающий на вход атрибут inline_keyboard
# список списков объектов InlineButton
# Реализовать метод serialize - возвращающий список списков словарей

class InlineButton(object):

    def __init__(self, text: str, callback_data: str) -> None:
        if not isinstance(text, str):
            raise TypeError('argument `text` must be a string')
        if not isinstance(callback_data, str):
            raise TypeError('argument `callback_data` must be a string')
        self.text = text
        self.callback_data = callback_data

    def dict(self) -> dict:
        data = {'text': self.text, 'callback_data': self.callback_data}
        return data


class InlineMarkup(object):

    def __init__(self, inline_keyboard: list) -> None:
        if not isinstance(inline_keyboard, list):
            raise TypeError('argument `inline_keyboard` must be a list')

        for line in inline_keyboard:
            if not isinstance(line, list):
                raise TypeError('each line must be a list')
            for button in line:
                if not isinstance(button, InlineButton):
                    raise TypeError('each button must be an InlineButton')

        self.inline_keyboard = inline_keyboard

    def dict(self) -> list[list[dict]]:
        markup = []
        for line in self.inline_keyboard:
            lst = []
            for button in line:
                lst.append(button.dict())
            markup.append(lst)
        return markup


user = InlineButton('text1', 'callback_data1')
print(user.dict())

buttons = [InlineButton(text='text', callback_data='data') for i in range(10)]
markup = InlineMarkup(inline_keyboard=[buttons, buttons])
print(markup.dict())

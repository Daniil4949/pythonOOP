class CustomButton:
    def __init__(self, text, **kwargs):
        self.text = text
        self.kwargs = kwargs
        keys = list(kwargs.keys())
        values = list(kwargs.values())
        for i in range(len(self.kwargs)):
            setattr(self, keys[i], values[i])

    def config(self, **kwargs):
        self.kwargs.update(kwargs)
        keys = list(self.kwargs.keys())
        values = list(self.kwargs.values())
        for i in range(len(self.kwargs)):
            setattr(self, keys[i], values[i])

    def click(self):
        try:
            self.command()
        except AttributeError:
            print('Кнопка не настроена')
        except TypeError:
            print('Кнопка сломалась')


def func():
    print('Оно живое')


btn = CustomButton(text='Hello', bd=20, bg='#ffaaaa')
btn.click()
btn.config(command=func)
btn.click()
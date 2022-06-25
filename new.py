class CustomLabel:
    def __init__(self, text, **kwargs):
        self.text = text
        keys = list(kwargs.keys())
        values = list(kwargs.values())
        for i in range(len(kwargs)):
            setattr(self, keys[i], values[i])

    def config(self, **kwargs):
        values = list(kwargs.values())
        keys = list(kwargs.keys())
        for i in range(len(kwargs)):
            setattr(self, keys[i], values[i])


label = CustomLabel(text="Hello", bd=20, bg='#ffaaaa')

print(label.__dict__) # {'text': 'Hello', 'bd': 20, 'bg': '#ffaaaa'}

label.config(color='red', bd=100)

print(label.__dict__) # {'text': 'Hello', 'bd': 100, 'bg': '#ffaaaa', 'color': 'red'}
class Constructor:
    def add_atribute(self, value_1, value_2):
        self.__setattr__(value_1, value_2)

    def display(self):
        print(self.__dict__)


obj1 = Constructor()
obj1.display() # печатает {}
obj1.add_atribute('color', 'red')
obj1.add_atribute('width', 20)
obj1.display() # печатает {'color': 'red', 'width': 20}

obj2 = Constructor()
obj2.display() # печатает {}
obj2.add_atribute('height', 100)
obj2.display() # печатает {'height': 100}
from abc import abstractmethod, ABC


class Profession(ABC):

    @abstractmethod
    def profession(self):
        pass


class Doctor(Profession):

    def profession(self):
        print('Я могу лечить!')


class Architect(Profession):

    def profession(self):
        print('Я могу строить здания!')

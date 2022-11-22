class Animal:

    def __init__(self, name, age, weight, colour):
        self.name = name
        self.age = age
        self.weight = weight
        self.colour = colour


    def __eq__(self, other):
        if hasattr(other, 'age'):
            return self.age == other.age
        else:
            raise TypeError()

    def __gt__(self, other):
        if hasattr(other, 'age'):
            return self.age > other.age
        else:
            raise TypeError()

    def __lt__(self, other):
        if hasattr(other, 'age'):
            return self.age < other.age
        else:
            raise TypeError()

    def __ne__(self, other):
        if hasattr(other, 'age'):
            return self.age != other.age
        else:
            raise TypeError()


class Cat(Animal):

    def __init__(self, name, age, weight, colour):
        super().__init__(name, age, weight, colour)

    def __eq__(self, other):
        if hasattr(other, 'weight'):
            return self.weight == other.weight
        else:
            raise TypeError()

    def __gt__(self, other):
        if hasattr(other, 'weight'):
            return self.weight > other.weight
        else:
            raise TypeError()

    def __lt__(self, other):
        if hasattr(other, 'weight'):
            return self.weight < other.weight
        else:
            raise TypeError()


class Dog(Animal):

    def __init__(self, name: str, age, weight, colour):
        super().__init__(name, age, weight, colour)


if __name__ == '__main__':

    murka = Cat('Murka', 19, 5, 'kalico')
    simba = Cat('Simba', 1, 2, 'brown')
    bagira = Cat('Bagira', 5, 1, 'grey')

    barbos = Dog('Barbos', 2, 10, 'black')
    tuzik = Dog('Tuzic', 13, 18, 'white')
    bobik = Dog('Bobik', 13, 10, 'ginger')
    dusya = Dog('Dusya', 8, 7, 'orange')

    print(tuzik == murka)
    print(barbos == dusya)
    print(tuzik < simba)
    print(bagira != bobik)
    print(murka > simba)
    print(bagira != murka)
    print(bagira == murka)
    print(bagira < murka)

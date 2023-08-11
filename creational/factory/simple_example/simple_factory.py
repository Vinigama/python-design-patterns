from abc import ABCMeta, abstractclassmethod

class Animal(metaclass = ABCMeta):
    @abstractclassmethod
    def faca_som(self):
        pass


class Cachorro(Animal):
    def faca_som(self):
        print("AU AU!")


class Gato(Animal):
    def faca_som(self):
        print("MIAU MIAU!")


# Definição da classe de Fábrica
class ForestFactory(object):
    def execute_som(self, object_type):
        return eval(object_type)().faca_som()

if __name__ == "__main__":
    ff = ForestFactory()
    animal = input("Qual animal deveria ser utilizado? Nome: ")
    ff.execute_som(animal)
from monostate_singleton import MonoStateSingleton

c1 = MonoStateSingleton()
c1.counter = 29
print("Classe de c1", c1)
print("Estado de c1", c1.__dict__)

c1.counter = 30
c2 = MonoStateSingleton()
print("Classe de c1", c1)
print("Classe de c2", c2)
print("Estado de c1", c1.__dict__)
print("Estado de c2", c2.__dict__)

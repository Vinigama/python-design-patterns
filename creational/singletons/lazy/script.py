from lazy_singleton import LazySingleton

c1 = LazySingleton()
print("C1 antes de getInstance()", c1)
c1 = c1.getInstance()
print("Instância gerada para C1 após getInstance()", c1)
c2 = LazySingleton()
print("C2 antes de getInstance()", c2)
c2 = c2.getInstance()
print("Instância gerada para C2 após getInstance()", c1)
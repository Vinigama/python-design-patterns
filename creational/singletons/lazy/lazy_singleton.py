class LazySingleton:
    __instance = None
    def __init__(self):
        if LazySingleton.__instance:
            print("Instância já criada:", self.getInstance())            
    
    @classmethod
    def getInstance(self):
        if not self.__instance:
            self.__instance = LazySingleton()
        return self.__instance
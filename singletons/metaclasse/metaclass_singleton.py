class MetaClassSingleton(type):
    _instances = {}
    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            self._instances[self] = super(MetaClassSingleton, self)\
                                            .__call__(*args, **kwargs)
        return self._instances[self]


class FileSingleton(metaclass=MetaClassSingleton):
    def set_file_address(self, address):
        self.file_address = address
    
    def print_address(self):
        print(self.file_address)
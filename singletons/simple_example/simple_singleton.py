class MySingleton:
    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super(MySingleton, self).__new__(self)
        return self.instance
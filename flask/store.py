class Store:
    def __init__(self):
        self.configs = {}

    def get_config(self, name):
        return self.configs[name]

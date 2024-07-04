class House:
    houses_history = []
    __instance = None
    def __new__(cls, *args):
        cls.args = args
        cls.houses_history.append(args[0])
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.houses_history

    def __del__(self):
        print(f'{self.args[0]} снесен, но он останется в истории')

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

del h2
del h3

print(House.houses_history)
class Human:
    name:str
    age: int
    weight: float
    height: float

    def __init__(self, name: str, age: int, weight: float = 100, height: float = 170):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
    
    def hello(self):
        return f'Тебя приветствует {self.name}'
    
kirill = Human('Кирилл', 38)
sveta = Human('Света', 18)

print(kirill.weight)
print(sveta.name)

print(kirill.hello())
print(sveta.hello) # неправильно
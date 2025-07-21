class Temperature():
       
    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self._name]

    def __set__(self, instance, value: int):
        if value < 0:
            raise ValueError('Temperature cannot be negative')
        instance.__dict__[self._name] = value


class Dashboard():
    temp1 = Temperature()
    temp2 = Temperature()

    def __init__(self):
        pass   
        

def main():
    print('hello')
    db = Dashboard()
    db.temp1 = 20
    db.temp2 = 4
    print(db.temp1)
    print(db.temp2)
    db.temp1 = -6

if __name__ == '__main__':
    main()
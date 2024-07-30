class Vehicle:
    __COLOR_VARIANTS = ['green', 'red', 'purple', 'black', 'white', 'blue']

    def __init__(self, owner, __model: str, __color: str, __engine_power: int):
        self.owner = owner
        self.__color = __color
        self.__model = __model
        self.__engine_power = __engine_power

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет автомобиля: {self.__color}'

    def print_info(self):
        print(self.get_model(), self.get_color(), self.get_horsepower(), self.owner, sep='\n')


    def set_color(self, new_color: str):
        for i in Vehicle.__COLOR_VARIANTS:
            if new_color.lower() in Vehicle.__COLOR_VARIANTS:
                new_color = self.__color
                return new_color
            else:
                print(f'Нельзя сменить цвет на {new_color}')
                return


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5
    pass


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()

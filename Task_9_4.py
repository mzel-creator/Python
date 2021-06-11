class Car:
    ''' Автомобиль '''

    def __init__(self, name, color, speed, isPolice=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.isPolice = isPolice
        print(f'Новое авто: {self.name} (цвет {self.color}) полицейский авто - {self.isPolice}')

    def start(self):
        print(f'{self.name}: Авто поехало.')

    def stop(self):
        print(f'{self.name}: Авто остановилось.')

    def turn(self, direction):
        print(f'{self.name}: Авто повернуло {"налево" if direction == 0 else "направо"}.')

    def show_speed(self):
        return f'{self.name}: Скорость авто: {self.speed}.'

class TownCar(Car):
    ''' Городской автомобиль '''

    def show_speed(self):
        return f'{self.name}: Скорость авто: {self.speed}. Превышение скорости!' \
            if self.speed > 60 else f"{self.name}: Скорость авто {self.speed}"

class Track(Car):
    ''' Грузовой автомобиль '''

    def show_speed(self):
        return f'{self.name}: Скорость авто: {self.speed}. Превышение скорости!' \
            if self.speed > 40 else f"{self.name}: Скорость авто {self.speed}"


class SportCar(Car):
    ''' Спортивный автомобиль '''
    
class PoliceCar(Car):
    ''' Полицейский автомобиль '''
    
    def __init__(self, name, color, speed, isPolice=True):
        super().__init__(name, color, speed, isPolice)

police_car = PoliceCar('"Полиция"', 'белый', 80)
police_car.start()
print(police_car.show_speed())
police_car.turn(0)
police_car.stop()

print()
track = Track('"Грузовик"', 'чёрный', 40)
track.start()
track.turn(1)
print(track.show_speed())
track.turn(0)
track.stop()

print()
sport_car = SportCar('"Спортивная"', 'красный', 220)
sport_car.start()
sport_car.turn(1)
print(sport_car.show_speed())
track.stop()

print()
town_car = TownCar('"Городской"', 'жёлтый', 50)
town_car.start()
town_car.turn(1)
town_car.turn(0)
print(town_car.show_speed())
town_car.stop()

print(f'\nАвтомобиль {town_car.name} (цвет {town_car.color})')
print(f'\nАвтомобиль {police_car.name} (цвет {police_car.color})')



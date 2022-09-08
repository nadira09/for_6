# task 1

from time import sleep

class TrafficLight:
    __color = {0: 'Red', 1: 'Yellow', 2: 'Green'}

    def running(self):
        for i in range(3):
            print(TrafficLight.__color[i])
            if i == 1:
                sleep(3)
            else:
                sleep(7)

tl = TrafficLight()
tl.running()

# task 2

class Road:
    def mesure(self, _length, _width):
        self._length = _length
        self._width = _width
        self.coating = 25
        self.thickness = 5
        return _length * _width * self.coating * self.thickness

a = Road()
print(a.mesure(20, 5000))

# task 3

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

a = Position('NAME', 'SURNAME', 'FIRST', 5000, 150)

print(a.get_full_name())
print(a.position)
print(a.get_total_income())

# task 4

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return

    def stop(self):
        return

    def turn(self):
        return

    def show_speed(self):
        return

class TownCar(Car):
    def towncar(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print('скорость', self.name, '=', self.speed)

        if self.speed > 60:
            print(self.name, 'скорость превышена')

class SportCar(Car):
    def sportcar(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def workcar(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print('скорость', self.name, '=', self.speed)

        if self.speed > 40:
            print(self.name, 'скорость превышена')

class PoliceCar(Car):
    def policecar(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} is from police department'
        else:
            return f'{self.name} is not from police department'

BMW = TownCar(90, 'Black', 'BMW', False)
Mers = WorkCar(39, 'White', 'Mercedes', True)

BMW.show_speed()
Mers.show_speed()

# task 5

class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Запуск отрисовки'

class Pen(Stationary):
    def draw(self):
        return self.title

class Pencil(Stationary):
    def draw(self):
        return self.title

class Handle(Stationary):
    def draw(self):
        return self.title

s = Stationary('')

pen = Pen('Ручка:')
print(pen.draw(), s.draw())

pencil = Pencil('Карандаш:')
print(pencil.draw(), s.draw())

handle = Handle('Маркер:')
print(handle.draw(), s.draw())



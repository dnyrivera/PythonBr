class Car:
    wheels = 4
    passenger = 5

    def speedUp(self):
        print("Speed Up the car....")

    def slowDown(self):
        print("Breaking the car....")

    def honkHorn(self):
        print("Honking the horn....")

# Heritage in Python
class Uno(Car):
    model = "Uno"
    brand = "Fiat"
    year = 1992


uno = Uno()
uno.speedUp()
uno.honkHorn()
print(uno.brand)

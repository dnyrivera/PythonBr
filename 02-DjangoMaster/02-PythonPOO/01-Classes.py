class Cellphone:
    brand = "Nokia"
    model = "3310"
    color = "Black"
    camera = False
    battery = 100

    def call(self):
        print("Calling...")

    def snake_game(self):
        return print("Playing snake game...")

    def alarm(self):
        print("Alarm ringing...")

    def calculator(self, v1: int, v2: int) -> int:
        return v1 + v2


apple = Cellphone()

print("Brand:", apple.brand)
print("Calculator result:", apple.calculator(10, 20))
apple.snake_game()

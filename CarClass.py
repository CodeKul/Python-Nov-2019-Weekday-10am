class Car:

    def __init__(self, color, model, make):
        self.color = color
        self.model = model
        self.make = make

    def info(self):
        print("Color:",self.color)
        print("Model:",self.model)
        print("Make:", self.make)

    def start(self):
        print("Car is starting...")
        print("Car started!")

    def stop(self):
        print("Car is stopping")
        print("Car stopped")

nano = Car("Red", "XLS", "TATA")
nano.info()
nano.start()
nano.stop()
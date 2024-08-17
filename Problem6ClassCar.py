# Hikmet Tenis
# 08/17/2024
# Problem 6: Modify the car class to include additional attributes and methods.

class Car:
    def __init__(self, model, year, color, type, manufacturer):
        self.model = model
        self.year = year
        self.color = color
        self.type = type
        self.manufacturer = manufacturer

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_color(self):
        return self.color

    def get_type(self):
        return self.type

    def get_manufacturer(self):
        return self.manufacturer

    def fullspecs(self):
        return f"{self.model} {self.year} {self.color} {self.type} {self.manufacturer}"

# Example usage
car1 = Car("Sports", 2012, "Blue", "Coupe", "Toyota")
car2 = Car("Sedan", 2020, "Black", "Saloon", "Honda")

print(car1.get_color())
print(car1.get_model())
print(car2.get_color())
print(car1.fullspecs())
print(car2.fullspecs())

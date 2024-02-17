class Car:

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odmeter_rading = 0
        
    def get_descriptive_name(self):

        long_name = f"{self.year} {self.make} {self.model}"

        return long_name.title()

    def update_odmeter(self,mileage):

        if mileage >= self.odmeter_rading:
            self.odmeter_rading = mileage
        else:
            print("You Can't Roll back an odometer!")

    def read_odometer(self):

        print(f"This car has {self.odmeter_rading} miles on it.")


class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


class Battery:
    
    def __init__(self,battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kwh battery.")

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 50:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")

my_tesla = ElectricCar('tesla','model y','2024')

print(my_tesla.get_descriptive_name())
my_tesla.update_odmeter(21521)
my_tesla.read_odometer()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
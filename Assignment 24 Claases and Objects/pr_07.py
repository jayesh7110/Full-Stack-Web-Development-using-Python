# Write a python program to create a Laptop class with 4 attributes (brand, ram, cpu,
# hdd) and 2 methods (showConfig() to print the values, __init__() to initialize the
# values).

class Laptop:
    def __init__(self, brand, ram, cpu, hdd):
        self.brand = brand
        self.ram = ram
        self.cpu = cpu
        self.hdd = hdd

    def show_config(self):
        print("Brand name: ", self.brand)
        print("RAM :", self.ram)
        print("CPU : ", self.cpu)
        print("HDD :", self.hdd)


l1 = Laptop("Dell", "8 GB", "Intel i7 10th Gen", "2 TB")
l1.show_config()
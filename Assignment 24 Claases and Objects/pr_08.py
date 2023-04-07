# WRT 7th Question, create 3 Laptop objects and add them to the list in the sorted
# order based on the ram size.

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


l1 = Laptop("Dell", 8, "Intel i7 10th Gen", "2 TB")
l2 = Laptop("Lenovo", 12, "Intel i5 12th Gen", "1 TB")
l3 = Laptop("Apple", 16, "16-core Neural Engine", "2 TB")

laptop_list = [l1, l2, l3]

sorted_laptop_list = sorted(laptop_list, key=lambda x: x.ram)

for laptop in sorted_laptop_list:
    laptop.show_config()
    print("---------------------------------------------------")

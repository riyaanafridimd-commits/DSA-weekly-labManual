'''#class and obj
class bike:
    name = ""
    gear = 0
#obj of a class
bike1 = bike()

bike1.gear = 11
bike1.name = 'mountain bike'
print(f"Name: {bike1.name} Gears:{bike1.gear}")'''



'''class Employee:
    employee_id = 0

employee1 = Employee()
employee2 = Employee()

employee1.employeeID = 1001
print(f"Employee ID: {employee1.employeeID}")
employee2.employeeID = 1002
print(f"Employee ID: {employee2.employeeID}")'''



class Room:
    length = 0.0
    breadth = 0.0
    
    def calculate_area(self):
        print("Area of Room =", self.length * self.breadth)

study_room = Room() 
study_room.length = 42.5
study_room.breadth = 30.8




















# access method inside class
study_room.calculate_area()

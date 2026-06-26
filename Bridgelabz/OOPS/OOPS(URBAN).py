#UC1 - Basic fleet setup
# class Vehicle:
#     def __init__(self, vehicle_id, model, battery_percentage):
#         self.vehicle_id = vehicle_id
#         self.model = model
#         self.battery_percentage = battery_percentage
    
#     def display_details(self):
#         print(f"Vehicle ID: {self.vehicle_id}")
#         print(f"Model: {self.model}")
#         print(f"Battery Percentage: {self.battery_percentage}%")
    
# vehicle1 = Vehicle("V001", "Model X", 85)
# vehicle2 = Vehicle("V002", "Model Y", 60)
# vehicle1.display_details()

# print("-----------------")

# vehicle2.display_details() 

#UC2 - Encapsulation and security
# UC2: Encapsulation & Security

# class Vehicle:

#     # Constructor
#     def __init__(self, vehicle_id, model, battery_percentage,
#                  maintenance_status, rental_price):

#         self.vehicle_id = vehicle_id
#         self.model = model

#         # Private attributes
#         self.__maintenance_status = maintenance_status
#         self.__rental_price = rental_price

#         # Setter method call
#         self.set_battery_percentage(battery_percentage)

#     # Setter for battery percentage
#     def set_battery_percentage(self, battery_percentage):

#         if 0 <= battery_percentage <= 100:
#             self.battery_percentage = battery_percentage
#         else:
#             print("Battery percentage must be between 0 and 100")

#     # Getter for maintenance status
#     def get_maintenance_status(self):
#         return self.__maintenance_status

#     # Setter for maintenance status
#     def set_maintenance_status(self, status):
#         self.__maintenance_status = status

#     # Getter for rental price
#     def get_rental_price(self):
#         return self.__rental_price

#     # Setter for rental price
#     def set_rental_price(self, price):
#         self.__rental_price = price

#     # Display method
#     def display_details(self):
#         print("Vehicle ID:", self.vehicle_id)
#         print("Model:", self.model)
#         print("Battery:", self.battery_percentage, "%")
#         print("Maintenance Status:",
#               self.get_maintenance_status())
#         print("Rental Price:",
#               self.get_rental_price())


# # Creating object
# vehicle1 = Vehicle(
#     "V101",
#     "Tesla Model 3",
#     90,
#     "Good",
#     500
# )

# # Display details
# vehicle1.display_details()

# print("----------------")

# # Updating private data using setter
# vehicle1.set_maintenance_status("Under Maintenance")
# vehicle1.set_rental_price(700)

# vehicle1.display_details()

#UC3 - Inheritance and Specialization 
# class Vehicle:

#     # Constructor
#     def __init__(self, vehicle_id, model,
#                  battery_percentage,
#                  maintenance_status,
#                  rental_price):

#         self.vehicle_id = vehicle_id
#         self.model = model
#         self.battery_percentage = battery_percentage

#         # Private attributes
#         self.__maintenance_status = maintenance_status
#         self.__rental_price = rental_price

#     # Getter for maintenance status
#     def get_maintenance_status(self):
#         return self.__maintenance_status

#     # Getter for rental price
#     def get_rental_price(self):
#         return self.__rental_price

#     # Display method
#     def display_details(self):
#         print("Vehicle ID:", self.vehicle_id)
#         print("Model:", self.model)
#         print("Battery:", self.battery_percentage, "%")
#         print("Maintenance Status:",
#               self.get_maintenance_status())
#         print("Rental Price:",
#               self.get_rental_price())


# # Child Class 1
# class ElectricCar(Vehicle):

#     # Constructor
#     def __init__(self, vehicle_id, model,
#                  battery_percentage,
#                  maintenance_status,
#                  rental_price,
#                  seating_capacity):

#         # Calling parent constructor
#         super().__init__(
#             vehicle_id,
#             model,
#             battery_percentage,
#             maintenance_status,
#             rental_price
#         )

#         self.seating_capacity = seating_capacity

#     def display_car_details(self):
#         self.display_details()
#         print("Seating Capacity:",
#               self.seating_capacity)


# # Child Class 2
# class ElectricScooter(Vehicle):

#     # Constructor
#     def __init__(self, vehicle_id, model,
#                  battery_percentage,
#                  maintenance_status,
#                  rental_price,
#                  max_speed_limit):

#         # Calling parent constructor
#         super().__init__(
#             vehicle_id,
#             model,
#             battery_percentage,
#             maintenance_status,
#             rental_price
#         )

#         self.max_speed_limit = max_speed_limit

#     def display_scooter_details(self):
#         self.display_details()
#         print("Max Speed Limit:",
#               self.max_speed_limit, "km/h")


# # Creating Car Object
# car1 = ElectricCar(
#     "C101",
#     "Tesla Model 3",
#     95,
#     "Good",
#     500,
#     5
# )

# # Creating Scooter Object
# scooter1 = ElectricScooter(
#     "S101",
#     "Ola S1",
#     80,
#     "Good",
#     100,
#     90
# )

# # Display Details
# print("Electric Car Details")
# car1.display_car_details()

# print("---------------------")

# print("Electric Scooter Details")
# scooter1.display_scooter_details() 

#UC4 - Abstraction
# from abc import ABC, abstractmethod


# # Parent Abstract Class
# class Vehicle(ABC): 

#     def __init__(self, vehicle_id, model,
#                  battery_percentage):

#         self.vehicle_id = vehicle_id
#         self.model = model
#         self.battery_percentage = battery_percentage

#     # Abstract Method
#     @abstractmethod
#     def calculate_trip_cost(self, distance):
#         pass


# # Child Class - Car
# class ElectricCar(Vehicle):

#     def calculate_trip_cost(self, distance):
#         return 5 + (0.5 * distance)


# # Child Class - Scooter
# class ElectricScooter(Vehicle):

#     def calculate_trip_cost(self, distance):
#         return 1 + (0.15 * distance)


# # Creating objects
# car = ElectricCar("C101",
#                   "Tesla",
#                   90)

# scooter = ElectricScooter("S101",
#                           "Ola S1",
#                           80)

# print("Car Trip Cost:",
#       car.calculate_trip_cost(10))

# print("Scooter Trip Cost:",
#       scooter.calculate_trip_cost(10)) 

#UC5 - Polyumorphism 

# from abc import ABC, abstractmethod
# class Vehicle(ABC):

#     def __init__(self,vehicle_id,model): 

#         self.vehicle_id = vehicle_id
#         self.model = model 

#     @abstractmethod
#     def calculate_trip_cost(self,
#                             distance):
#         pass


# class ElectricCar(Vehicle):

#     def calculate_trip_cost(self,
#                             distance):
#         return 5 + (0.5 * distance)


# class ElectricScooter(Vehicle):

#     def calculate_trip_cost(self,
#                             distance):
#         return 1 + (0.15 * distance)


# # Mixed object list
# vehicles = [
#     ElectricCar("C101", "Tesla"),
#     ElectricScooter("S101", "Ola"),
#     ElectricCar("C102", "BMW")
# ]

# distance = 20

# for vehicle in vehicles:

#     print(vehicle.model,
#           "Trip Cost:",
#           vehicle.calculate_trip_cost(distance)) 

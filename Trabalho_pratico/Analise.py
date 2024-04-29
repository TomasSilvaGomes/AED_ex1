import pandas as pd
import csv

# class Competition:
#
#     def __init__(self, w1, w2, w3):
#         self.w1 = w1
#         self.w2 = w2
#         self.w3 = w3
#         content = pd.read_csv('Cars_input.csv')
#         self.content = content
#         self.CAR_ID = self.content['CAR_ID']
#         self.Tire_Wear = self.content['Tire_Wear']
#         self.Fuel_Level = self.content['Fuel_Level']
#         self.Race_Position = self.content['Race_Position']
#         self.Laps_Since_Last_Pit = self.content['Laps_Since_Last_Pit']
#         self.Type = self.content['TYPE']
#         self.FUEL_LOSS = self.Fuel_Level - self.content['FUEL_LOSS']
#         self.TIRE_LOSS = self.Tire_Wear - self.content['TIRE_LOSS']
#
#     # function that calculates the priority of the object
#     def priority(self):
#         weights = (self.w1, self.w2, self.w3)
#         return (self.Tire_Wear * weights[0]) + ((1 - (self.Fuel_Level * 0.01)) * weights[1]) + (weights[2] * (self.Race_Position) / len(self.Race_Position))
#
#
#     def __repr__(self):
#         # Creation of a list of tuples containing the car ID and priority
#         car_id = self.CAR_ID
#         priority = self.priority()
#         car_priorities = list(zip(car_id, priority))
#
#         # Sort the list by priority in descending order, based on the priority of the tuple (second element)
#         car_priorities.sort(key=lambda y: y[1], reverse=True)
#
#         # Format the output as a string
#         output = ""
#         for car_id, priority in car_priorities:
#             output += f"Car ID: {car_id}, Priority: {priority:.2f}\n"
#         return output


class Competition:
    def __init__(self, w1, w2, w3):
        self.w1 = w1
        self.w2 = w2
        self.w3 = w3
        self.csv_list = []
        self.priority_list = []
        with open('Cars_input.csv', 'r') as file:
            next(file)
            csv_reader = csv.reader(file)
            self.csv_list = list(csv_reader)

    # function that calculates the priority of each car
    def priority(self):
        for row in self.csv_list:
            calculator = (row[0], (float(row[1]) * self.w1) + ((1 - (int(row[2]) * 0.01)) * self.w2) + (self.w3 * int(row[3]) / len(self.csv_list)))
            self.priority_list.append(calculator)



    def __repr__(self):
        # Sort the list by priority in descending order, based on the priority (second element)
        self.priority()
        self.priority_list.sort(key=lambda x: x[1], reverse=True)

        # Format the output as a string
        output = ""
        for car_id, priority in self.priority_list:
            output += f"Car ID: {car_id}, Priority: {priority:.2f}\n"
        print(output)

cp = Competition(0.5,0.5,0.1)
print(cp.__repr__())
# cp = Competition()
# print(cp.__repr__())

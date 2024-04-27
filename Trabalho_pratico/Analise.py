import pandas as pd


class Competition:

    def __init__(self):
        content = pd.read_csv('Cars_input.csv')
        self.CAR_ID = content['CAR_ID']
        self.Tire_Wear = content['Tire_Wear']
        self.Fuel_Level = content['Fuel_Level']
        self.Race_Position = content['Race_Position']
        self.Laps_Since_Last_Pit = content['Laps_Since_Last_Pit']
        self.Type = content['TYPE']

    # function that calculates the priority of the object
    def priority(self):
        weights = (0.5, 0.5, 0.1)
        return (self.Tire_Wear * weights[0]) + (self.Fuel_Level * weights[1]) + (self.Race_Position * weights[2])

    def __repr__(self):
        # Creation of a list of tuples containing the car ID and priority
        # print(self.CAR_ID)
        car_id = self.CAR_ID
        priority = self.priority()
        car_priorities = list(zip(car_id, priority))

        # Sort the list by priority in descending order
        car_priorities.sort(key=lambda y: y[1], reverse=True)

        # Format the output as a string
        output = ""
        for car_id, priority in car_priorities:
            output += f"Car ID: {car_id}, Priority: {priority:.2f}\n"
        return output


cp = Competition()
print(cp.__repr__())

import pandas as pd


class competition:
    

    def __init__(self):
        self.read_input()


    def read_input(self):
        '''this function reads the input of the object'''
        content = pd.read_csv('Cars_input.csv')
        self.CAR_ID = content['CAR_ID']
        self.Tire_Wear = content['Tire_Wear']
        self.Fuel_Level = content['Fuel_Level']
        self.Race_Position = content['Race_Position']
        self.Laps_Since_Last_Pit = content['Laps_Since_Last_Pit']


    def __lt__(self, other):
        '''this method is used to compare the two objects, in this case, if the priority of
        the first object is less than the priority of the second object, it returns True'''
        return self.Priority < other.Priority


    # function that calculates the priority of the object
    def priority(self):
        return self.Tire_Wear + self.Fuel_Level + self.Race_Position

    #function that shows the priority of the object
    def __repr__(self):
        return f'Car {self.CAR_ID} - Priority: {self.priority()}'

cp = competition()
print(cp.__repr__())


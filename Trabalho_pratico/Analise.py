import csv


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
            if row[5].startswith('FULL'):
                # the cars that had a full accident will be considered as priority 3 because the higher priority is
                # 2.55 and full accident needs to have the highest of them all
                calculator = (row[0], 3)

            else:
                calculator = (row[0], (float(row[1]) * self.w1) + ((1 - (int(row[2]) * 0.01)) * self.w2) + (
                        self.w3 * ((len(self.csv_list) + 1) - int(row[3]))))
            self.priority_list.append(calculator)

    def __repr__(self):
        # Sort the list by priority in descending order, based on the priority (second element)
        self.priority()
        self.priority_list.sort(key=lambda x: x[1], reverse=True)

        # Format the output as a string
        output = ""
        for car_id, priority in self.priority_list:
            output += f"Car ID: {car_id}, Priority: {priority:.2f}\n"
        return output


cp = Competition(0.5, 0.5, 0.1)
print(cp.__repr__())
